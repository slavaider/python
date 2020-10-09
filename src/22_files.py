import os

if __name__ == '__main__':
    print(os.getcwdb())
    with open(r"C:/Users/User/PycharmProjects/first_project/files/file_name.txt", "w+") as file:
        file.write("data|lol")
        file.seek(0)
        print(file.read())
