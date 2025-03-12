import random

a = random.randint(1,10)
print(a)


# Pick a Random Item From a list
fruits = ["Apple", "Banana", "Cherry", "Mango"]
choice = random.choice(fruits)
print(f"Random fruit: {choice}")


# Generate a Floating Number Between 0 to 1
num = random.random()
print(f"Random float: {num}")