import psycopg2


class MyConnectionError(Exception):
    pass


class SQLError(Exception):
    pass


class CredentialError(Exception):
    pass


class DataBaseUse:

    def __init__(self, config=None):
        if not config:
            config = {'dbname': 'test_database', 'user': 'postgres', 'password': 'admin'}
        self.configuration = config

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(**self.configuration)
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.InterfaceError as ex:
            raise MyConnectionError(ex)
        except psycopg2.ProgrammingError as ex:
            raise CredentialError(ex)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is psycopg2.ProgrammingError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)