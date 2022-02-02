# https://medium.com/@svobodavsem/582ec5cc0110

from flask import Flask

server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
   server.run()