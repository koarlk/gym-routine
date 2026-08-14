#!/usr/bin/env python3
"""Kleiner lokaler Server, um die App im WLAN aufs Handy zu holen.

Starten:  python3 serve.py
Beenden:  Ctrl-C
"""
import functools, http.server, os, socket, socketserver

PORT = 8765
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # damit Aenderungen sofort ankommen und der Service Worker nicht veraltet
        self.send_header("Cache-Control", "no-store")
        # JSON zum Herunterladen anbieten statt anzuzeigen: so landet eine
        # Sicherung am iPhone in der Dateien-App und laesst sich importieren,
        # ohne sie vorher per AirDrop zu uebertragen.
        # Nur Sicherungen, nicht manifest.json - das muss die App normal lesen.
        name = os.path.basename(self.path.split("?")[0])
        if name.startswith("gym-backup-") and name.endswith(".json"):
            self.send_header("Content-Disposition", 'attachment; filename="%s"' % name)
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
# Wurzelverzeichnis fest vorgeben: der Standardhandler ruft sonst bei jedem
# Request os.getcwd() auf, was unter macOS in geschuetzten Ordnern
# (Schreibtisch, Dokumente) mit "Operation not permitted" scheitert.
handler = functools.partial(Handler, directory=ROOT)
with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
    print("\n  Gym Tracker laeuft.\n")
    print("  Am Mac:     http://localhost:%d" % PORT)
    print("  Am iPhone:  http://%s:%d   (gleiches WLAN)\n" % (lan_ip(), PORT))
    print("  Beenden mit Ctrl-C\n")
    httpd.serve_forever()
