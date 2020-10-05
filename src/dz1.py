# task 1
import math

count = int(input('Скока надо '))
bonus = round(count / 6)
print(f"Бонусных чашек {bonus}")
# task 2
x_dot1 = input("x_dot1= ")
while (x_dot1 == ""):
    print("Введите что-то")
    x_dot1 = input("x_dot1= ")

y_dot1 = input("y_dot1= ")
while (y_dot1 == ""):
    print("Введите что-то")
    y_dot1 = input("y_dot1= ")

x_dot2 = input("x_dot2= ")
while (x_dot2 == ""):
    print("Введите что-то")
    x_dot2 = input("x_dot2= ")

y_dot2 = input("y_dot2= ")
while (y_dot2 == ""):
    print("Введите что-то")
    y_dot2 = input("y_dot2= ")

x_dot1 = int(x_dot1)
y_dot1 = int(y_dot1)
x_dot2 = int(x_dot2)
y_dot2 = int(y_dot2)
res = math.sqrt(pow(x_dot2 - x_dot1, 2) + pow(y_dot2 - y_dot1, 2))
print(f"{round(res, 3)}")
# task 3
chickens = int(input("chickens = "))
cows = int(input("cows = "))
pigs = int(input("pigs = "))
print(f"Ног у всех животных {chickens * 2 + cows * 4 + pigs * 4}")
