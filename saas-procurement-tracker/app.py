"""SaaS Procurement Tracker - lokale webserver zonder externe packages."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import mimetypes
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST, PORT = "127.0.0.1", 8000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        requested = "/templates/index.html" if self.path in ("/", "/index.html") else self.path.split("?", 1)[0]
        path = (ROOT / requested.lstrip("/")).resolve()
        if ROOT not in path.parents or not path.is_file():
            self.send_error(404)
            return
        content = path.read_bytes()
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        if mime.startswith("text/") or mime in ("application/javascript", "application/json"):
            mime += "; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    url = f"http://{HOST}:{PORT}"
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"SaaS Procurement Tracker draait op {url}")
    print("Stoppen: Ctrl+C")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nTracker gestopt.")
    finally:
        server.server_close()
