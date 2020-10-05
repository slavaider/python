import os
d = os.getcwdb()
print(d)
with open(r"C:/Users/User/PycharmProjects/first_project/file_name.txt", "w+") as file:
    file.write("data|lol")
    file.seek(0)
    print(file.read())
