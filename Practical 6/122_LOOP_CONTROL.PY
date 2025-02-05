# Demonstrating "continue", "pass", "break", and "else" in a loop

print("For Loop with continue, pass, break, and else:")
for i in range(1, 11):
    if i == 3:
        print("Continue at i =", i)
        continue  
        print("Pass at i =", i)
        pass  
    elif i == 8:
        print("Breaking at i =", i)
        break  
    print(i)  
else:
    print("This will not be printed because the loop was broken.")
print("\nWhile Loop with continue, pass, break, and else:")

i = 1
while i <= 10:
    if i == 2:
        print("Continue at i =", i)
        i += 1
        continue  
    elif i == 5:
        print("Pass at i =", i)
        pass  
    elif i == 9:
        print("Breaking at i =", i)
        break  
    print(i)  
    i += 1
else:
    print("This will not be printed because the loop was broken.")
