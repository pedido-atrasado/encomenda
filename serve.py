#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Servidor local do clone Loggi rastreador (site real espelhado).
Serve o mirror de app.loggi.com/rastreador com o botao de download do APK.
Forca charset UTF-8 e faz fallback SPA para o rastreador."""
import http.server, socketserver, os, sys

PORT = 8090
BASE = os.path.dirname(os.path.abspath(__file__))
# Estrutura local (mirror em beyond-mirror/app.loggi.com) ou raiz do repo (Pages)
ROOT = os.path.join(BASE, "beyond-mirror", "app.loggi.com")
if not os.path.isdir(ROOT):
    ROOT = BASE
INDEX = os.path.join(ROOT, "index.html")
if not os.path.exists(INDEX):
    INDEX = os.path.join(ROOT, "rastreador.html")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def guess_type(self, path):
        base = super().guess_type(path)
        if path.endswith((".js", ".css", ".html", ".json", ".svg")):
            return base + "; charset=utf-8"
        return base

    def do_GET(self):
        # SPA fallback: rotas sem extensao -> rastreador.html
        p = self.path.split("?")[0]
        if p != "/" and not os.path.splitext(p)[1] and p != "/favicon.ico":
            if not os.path.exists(os.path.join(ROOT, p.lstrip("/"))):
                self.path = "/rastreador.html"
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

with socketserver.ThreadingTCPServer(("127.0.0.1", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving {ROOT} on http://127.0.0.1:{PORT} (charset=utf-8 forcado)")
    httpd.serve_forever()
