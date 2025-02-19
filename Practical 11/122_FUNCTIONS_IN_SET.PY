# Creating two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# 1. Union: Combines elements from both sets (duplicates removed)
union_set = setA.union(setB)
print("Union of set A and set B:", union_set)

# 2. Intersection: Elements that are common in both sets
intersection_set = setA.intersection(setB)
print("Intersection of set A and set B:", intersection_set)

# 3. Difference: Elements present in setA but not in setB
difference_set = setA.difference(setB)
print("Difference (set A - set B):", difference_set)

# 4. Symmetric Difference: Elements in either setA or setB, but not both
symmetric_difference_set = setA.symmetric_difference(setB)
print("Symmetric Difference of set A and set B:", symmetric_difference_set)
