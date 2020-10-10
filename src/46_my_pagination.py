class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.second_index = page_size
        self.page = 1
        self.page_size = page_size

    def get_visible_items(self):
        return self.items[(self.page - 1) * self.page_size:self.second_index]

    def prev_page(self):
        if self.items != [] and self.page != 1:
            self.page -= 1
            self.second_index -= self.page_size
        return self

    def next_page(self):
        if self.items != [] and self.second_index != len(self.items):
            self.page += 1
            self.second_index += self.page_size
        return self

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


if __name__ == '__main__':
    alphabet = list("abcdefghgklmnoprstuvwz")
    p = Pagination(alphabet, 4)
    print(p.get_visible_items())
    p.next_page()
    print(p.get_visible_items())
    p.next_page()
    print(p.get_visible_items())
    p.first_page()
    print(p.get_visible_items())
    p.last_page()
    print(p.get_visible_items())
    p.go_to_page(11)
    print(p.get_visible_items())
    print(len(p.get_items()))
    p.last_page()
    print(p.get_visible_items())
    p.go_to_page(3)
    print(p.get_visible_items())
    print(p.get_visible_items())
    print(p.next_page().get_current_page())
    print(p.prev_page().get_current_page())
    print(p.first_page().get_current_page())
    print(p.last_page().get_current_page())
    print(p.go_to_page(-1).get_current_page())
    print(p.go_to_page(1).get_current_page())
    print(p.go_to_page(2).get_current_page())
