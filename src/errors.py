def divide(num1, num2):
    try:
        return int(num1 / num2)
    except ZeroDivisionError as ex:
        print(f"{ex}")
    except TypeError as ex:
        print(f"{ex}")
    except:
        raise invalidTriangle("lol")


class invalidTriangle(Exception):
    "Something"


print(divide(5, "123"))
