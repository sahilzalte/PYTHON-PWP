for i in range(1, 5):       # i controls rows
    print("*", end=" ")     # Symbol for i (just once per row)
    for j in range(1, i + 1):   # j controls columns (nested)
        print("^", end=" ")     # Symbol for j
    print()  # New line after each row
