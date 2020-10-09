def divide(num1, num2):
    try:
        return int(num1 / num2)
    except ZeroDivisionError as ex:
        return f"{ex}"
    except TypeError as ex:
        return f"{ex}"
    except Exception:
        raise invalidTriangle("lol")


class invalidTriangle(Exception):
    """Something"""


if __name__ == '__main__':
    print(divide(5, "123"))
    print(divide(0, 1))
    print(divide(0, 0))
