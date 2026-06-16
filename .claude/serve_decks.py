import http.server, os
os.chdir("/Users/melissacedeno/Desktop/Claude/embertribe-decks/decks")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080, bind="127.0.0.1")
