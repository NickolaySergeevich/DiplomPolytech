from flask import Flask


# Flask and WSGI settings
application = Flask(__name__)
wsgi_app = application.wsgi_app


@application.route("/")
def hello() -> str:
    """
    Стартвоая страница (тестовая)

    :return: Строка с "Привет мир"
    """

    return "Hello, World! This is home api page!"


def main() -> None:
    """
    Для тестов

    :return: Ничего
    """

    application.run()


if __name__ == '__main__':
    main()
