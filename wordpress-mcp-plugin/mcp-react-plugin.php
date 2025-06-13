<?php
/*
Plugin Name: MCP ReactPHP Plugin
Description: Example plugin that runs a ReactPHP HTTP server and communicates with the php-mcp server.
Version: 0.1
Author: Codex
*/

use React\EventLoop\Loop;
use React\Http\HttpServer;
use React\Socket\SocketServer;
use React\Http\Browser;

if (!class_exists('MCP_ReactPHP_Plugin')) {
    class MCP_ReactPHP_Plugin
    {
        private static $serverProcess = null;

        public static function init()
        {
            add_shortcode('mcp_test', [__CLASS__, 'handle_shortcode']);
            register_activation_hook(__FILE__, [__CLASS__, 'start_server']);
            register_deactivation_hook(__FILE__, [__CLASS__, 'stop_server']);
        }

        public static function start_server()
        {
            if (self::$serverProcess) {
                return;
            }
            $cmd = PHP_BINARY . ' ' . __DIR__ . '/server.php > /dev/null 2>&1 & echo $!';
            $output = shell_exec($cmd);
            if ($output) {
                file_put_contents(__DIR__ . '/server.pid', trim($output));
            }
        }

        public static function stop_server()
        {
            $pidFile = __DIR__ . '/server.pid';
            if (file_exists($pidFile)) {
                $pid = trim(file_get_contents($pidFile));
                if ($pid) {
                    posix_kill((int)$pid, 9);
                }
                unlink($pidFile);
            }
        }

        public static function handle_shortcode()
        {
            $loop = Loop::get();
            $browser = new Browser($loop);
            $responseBody = '';

            $browser->post('http://localhost:8080/endpoint', [
                'Content-Type' => 'application/json'
            ], json_encode(['message' => 'Hello MCP']))
                ->then(function (Psr\Http\Message\ResponseInterface $response) use (&$responseBody) {
                    $responseBody = (string)$response->getBody();
                }, function (Exception $e) use (&$responseBody) {
                    $responseBody = $e->getMessage();
                });

            $loop->run();
            return 'MCP Response: ' . esc_html($responseBody);
        }
    }

    MCP_ReactPHP_Plugin::init();
}

?>
