class Pagination():

    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_page = 0
        self.current_page = 1

    def get_visible_items(self):
        if self.current_page == self.total_page:
            if (len(self.items) % self.page_size) != 0:
                visible_items = [self.items[i] for i in
                                 range(len(self.items) - (len(self.items) % self.page_size), len(self.items))]
            else:
                visible_items = [self.items[i] for i in range(self.page_size * (self.current_page - 1),
                                                              self.page_size * self.current_page)]
        else:
            visible_items = [self.items[i] for i in range(self.page_size * (self.current_page - 1),
                                                          self.page_size * self.current_page)]
        return visible_items

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            self.current_page = self.current_page
        return self

    def next_page(self):
        self.all_page()
        if self.current_page < self.total_page:
            self.current_page += 1
        else:
            self.current_page = self.current_page
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        if len(self.items) % self.page_size == 0:
            self.total_page = len(self.items) // self.page_size
        else:
            self.total_page = len(self.items) // self.page_size + 1
        self.current_page = self.total_page
        return self

    def go_to_page(self, page):
        self.page = page
        if len(self.items) % self.page_size == 0:
            self.total_page = len(self.items) // self.page_size
        else:
            self.total_page = len(self.items) // self.page_size + 1
        if self.page > self.total_page:
            self.current_page = self.total_page
        elif self.page < 1:
            self.current_page = 1
        else:
            self.current_page = self.page
        return self

    def all_page(self):
        if len(self.items) % self.page_size == 0:
            self.total_page = len(self.items) // self.page_size
        else:
            self.total_page = len(self.items) // self.page_size + 1

    def get_current_page(self):
        return self.current_page

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
    p.get_items()
    p.last_page()
    print(p.get_visible_items())
    p.go_to_page(3)
    print(p.get_visible_items())
    p.first_page()
    print(p.next_page().get_current_page())
    print(p.prev_page().get_current_page())
    print(p.first_page().get_current_page())
    print(p.last_page().get_current_page())
    print(p.go_to_page(-1).get_current_page())
    print(p.go_to_page(1).get_current_page())
    print(p.go_to_page(2).get_current_page())
    print(p.go_to_page(20).get_current_page())
