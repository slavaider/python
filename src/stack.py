# custom stack
class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        item = self.array.pop()
        return item

    def peek(self):
        return self.__current()

    def __current(self):
        return self.array[self.count() - 1]

    def count(self):
        return len(self.array)

    def __iter__(self):
        self.index = self.count() - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result


stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
