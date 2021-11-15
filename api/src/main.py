from flask import Flask


# Flask and WSGI settings
application = Flask(__name__)
wsgi_app = application.wsgi_app


@application.route("/")
def hello() -> str:
    return "Hello, World! This is home api page!"


def main():
    application.run()


if __name__ == '__main__':
    main()
