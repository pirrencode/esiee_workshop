# MCP ReactPHP Plugin

This sample WordPress plugin demonstrates how ReactPHP can be used to run a lightweight HTTP server alongside a traditional WordPress plugin. The plugin also shows how to send asynchronous requests to a php-mcp server.

* `mcp-react-plugin.php` – main plugin file. It registers a shortcode `[mcp_test]` and starts/stops a background ReactPHP server on activation and deactivation.
* `server.php` – standalone ReactPHP HTTP server listening on port 8081. It simply echoes request information as JSON.

The shortcode triggers an asynchronous POST request to an MCP endpoint running at `http://localhost:8080/endpoint` and prints the response.

This is a minimal example intended for experimentation only.
