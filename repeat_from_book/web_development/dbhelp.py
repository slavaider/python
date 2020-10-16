import math

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


class Pagination:

    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.second_index = 10
        self.page = 1
        self.page_size = page_size

    def get_visible_items(self):
        return self.items[(self.page - 1) * self.page_size:self.second_index]

    # Undone
    # def prev_page(self):
    #     if self.items != [] and self.page != 1:
    #         self.page -= 1
    #         self.second_index -= self.page_size
    #     return self
    #
    # def next_page(self):
    #     if (self.second_index + self.page_size) > len(self.items):
    #         return self.last_page()
    #     if self.items != [] and self.second_index < len(self.items):
    #         self.page += 1
    #         self.second_index += self.page_size
    #     return self

    def first_page(self):
        self.page = 1
        self.second_index = self.page_size
        return self

    def last_page(self):
        self.page = int(len(self.items) / self.page_size) + 1
        self.second_index = len(self.items)
        return self

    def go_to_page(self, page):
        if not self.items:
            return self
        elif page > int(len(self.items) / self.page_size):
            return self.last_page()
        elif page < 1:
            return self.first_page()
        else:
            self.page = page
            self.second_index = (page - 1) * self.page_size + self.page_size
            return self

    def get_current_page(self):
        return self.page

    def get_page_size(self):
        return self.page_size

    def get_items(self):
        return self.items

    def get_pagination_list_of_nums(self):
        return list(range(1, math.ceil(len(self.items) / self.page_size) + 1))
