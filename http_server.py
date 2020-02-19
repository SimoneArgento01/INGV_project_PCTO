"""
Server HTTP
"""
from http.server import BaseHTTPRequestHandler, HTTPServer


# crezione classe che riceverà e risponderà alle richieste HTTP
class Server(BaseHTTPRequestHandler):

    # metodo che risponde alle richieste GET
    def do_GET(self):

        if self.path == '/':
            self.path = '\\HTML_pages\\iscrizione.html'

        try:
            html_file = open(self.path[1:]).read()
            # codice di risposta (cod 200, richiesta arrivata con successo)
            self.send_response(200)

        except:
            html_file = open("HTML_pages\\page_404.html").read()
            self.send_response(404)

        # chiusura headers
        self.end_headers()

        # messaggio che costituisce il corpo della risposta
        self.wfile.write(bytes(html_file, "utf-8"))
        return


print("Avvio del server...")
httpd = HTTPServer(('0.0.0.0', 10000), Server)
httpd.serve_forever()
