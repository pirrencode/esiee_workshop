<?php
require __DIR__ . '/vendor/autoload.php';

use React\EventLoop\Loop;
use React\Http\HttpServer;
use React\Socket\SocketServer;
use Psr\Http\Message\ServerRequestInterface;

$loop = Loop::get();

$server = new HttpServer(function (ServerRequestInterface $request) {
    $data = [
        'method' => $request->getMethod(),
        'path' => $request->getUri()->getPath(),
        'query' => $request->getQueryParams(),
    ];
    return new React\Http\Message\Response(
        200,
        ['Content-Type' => 'application/json'],
        json_encode($data)
    );
});

$socket = new SocketServer('0.0.0.0:8081', [], $loop);
$server->listen($socket);

echo "Server running on http://0.0.0.0:8081\n";
$loop->run();
