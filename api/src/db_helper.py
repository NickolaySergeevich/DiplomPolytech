import mysql.connector


class DbHelper:
    """
    Класс для работы с базой данных MySql
    """

    def __init__(self, user: str, password: str, host: str, database: str):
        """
        Инициализация

        :param user: Имя пользователя
        :param password: Пароль пользователя
        :param host: ip-адрес базы данных
        :param database: Название базы данных
        """

        # Настройки подключения к бд
        self._user = user
        self._password = password
        self._host = host
        self._database_name = database

        # Создание подключения
        self._connection = mysql.connector.connect(
            user=self._user, password=self._password,
            host=self._host, database=self._database_name
        )

    def __del__(self):
        """
        Очистка памяти и всех подключений

        :return: Ничего
        """

        self._connection.close()


def main() -> None:
    """
    Для тестов

    :return: Ничего
    """

    pass


if __name__ == '__main__':
    main()
