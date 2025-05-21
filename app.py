# Simple Math

x = 2
y = 3
z = x + y

print(x)
print(y)

a = 10
b = 5
c = a / b
d = a * b
e = a % b

name = "Anna"
surname = "Grey"

student_name = name + " " + surname
print(student_name)

# TASK 1. Write IF ELSE statement to validate if x is larger than y. Return TRUE if YES

def compareFunc(x, y):
    if y > x:
        return True
    return False

print(compareFunc(300, 200))

# TASK 2. Write IF ELSE statement to validate if x is larger than y and less than b. Return TRUE if YES

def compareFunc2(x, y, b):
    if (x > y) and (x < b):
        return True
    return False

print(compareFunc2(300, 200, 600))

# 08.04.2025. Day 2

# TASK 1

def mix_ingredients():
    return "Ingredients are ready"


def put_pizza_in_a_stove():
    return "In Stove"


def bake_pizza():
    return "Baked"


def serve_pizza():
    return "Pizza is served to my friends"


ingredients = (
    "onions",
    "tomatos",
    "salami",
    "salmon",
    "champignon",
    "cheese",
)


def cook_pizza():
    if len(ingredients) > 2 and {"cheese", "onions", "tomatos"}.issubset(ingredients):
        mix_ingredients()
    else:
        return "Please mix proper ingredients"

    status = put_pizza_in_a_stove()
    if status == "In Stove":
        bake_pizza()
    return serve_pizza()


# TASK 2

def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


# TASK 3

# Using for loop
print("Using for loop:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print("\n")

# Using while loop
print("Using while loop:")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
