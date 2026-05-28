import os
import http.server
import json

port = int(os.environ.get("PORT", 5000))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok", "app": "EagleMoney"}).encode())

    def log_message(self, format, *args):
        print(f"{args[0]} {args[1]} {args[2]}", flush=True)

print(f"Starting EagleMoney on port {port}", flush=True)
http.server.HTTPServer(("0.0.0.0", port), Handler).serve_forever()
