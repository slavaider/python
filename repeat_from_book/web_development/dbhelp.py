import psycopg2


class DataBaseUse:

    def __init__(self, config=None):
        if not config:
            config = {'dbname': 'test_database', 'user': 'postgres', 'password': 'admin'}
        self.configuration = config

    def __enter__(self):
        self.connection = psycopg2.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
