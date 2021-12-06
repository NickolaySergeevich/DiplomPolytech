import mysql.connector


class DbHelper:
    """
    Класс для работы с базой данных MySql
    """

    def __init__(self, user: str, password: str, host: str, database_name: str):
        """
        Инициализация

        :param user: Имя пользователя
        :param password: Пароль пользователя
        :param host: ip-адрес базы данных
        :param database_name: Название базы данных
        """

        # Настройки подключения к бд
        self._user = user
        self._password = password
        self._host = host
        self._database_name = database_name

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

    @staticmethod
    def read_settings_file(file_name: str) -> dict:
        """
        Считывает настройки из файла и возвращает словарь с оными

        :param file_name: Имя файла с настройками

        :return: Словарь с настройками
        """

        answer = dict()

        with open(file_name, 'r') as settings_file:
            for line in settings_file:
                options = line.split("=")
                # Мы подразумеваем, что пользователь заполнил файл с настройками верно
                answer[options[0]] = options[1][:-1]

        return answer


def main() -> None:
    """
    Для тестов

    :return: Ничего
    """

    db_helper = DbHelper(**DbHelper.read_settings_file("../program_files/mysql_settings.dk"))


if __name__ == '__main__':
    main()
