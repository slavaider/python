import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v))
        return result


if __name__ == '__main__':
    # copy and deepcopy
    lst = [1, 2, 3, [4, 5, 6]]
    # copy copied_lst inherit lst index
    copied_lst = lst.copy()
    copied_lst[3].append(7)
    print(lst)
    print(copied_lst)
    # deepcopy deepcopy_list divided from lst
    deepcopy_list = copy.deepcopy(lst)
    deepcopy_list[3].append(8)
    print(lst)
    print(deepcopy_list)

    # copy deepcopy classes
    a = Point(x=1, y=2)
    b = copy.deepcopy(a)
    a.x = 3
    print(f'{a.x=}')
    print(f'{b.x=}')
    b.x = 4
    print(f'{a.x=}')
    print(f'{b.x=}')
    l1 = Line(a, b)
    l2 = copy.deepcopy(l1)
    print(f'{l1.p1=}')
    print(f'{l2.p1=}')
    l1.p1.x = 5
    print(f'{l1.p1=}')
    print(f'{l2.p1=}')
