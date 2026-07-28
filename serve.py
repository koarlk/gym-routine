#!/usr/bin/env python3
"""Kleiner lokaler Server, um die App im WLAN aufs Handy zu holen.

Starten:  python3 serve.py
Beenden:  Ctrl-C
"""
import http.server, os, socket, socketserver

PORT = 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # damit Aenderungen sofort ankommen und der Service Worker nicht veraltet
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("\n  Gym Tracker laeuft.\n")
    print("  Am Mac:     http://localhost:%d" % PORT)
    print("  Am iPhone:  http://%s:%d   (gleiches WLAN)\n" % (lan_ip(), PORT))
    print("  Beenden mit Ctrl-C\n")
    httpd.serve_forever()
