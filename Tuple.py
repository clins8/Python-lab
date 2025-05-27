# Creating tuples
t1 = (10, 20, 30, 40, 50)
t2 = (60, 70)

# 1. Accessing elements
print("First element:", t1[0])
print("Last element:", t1[-1])

# 2. Slicing
print("Slice t1[1:4]:", t1[1:4])

# 3. Length
print("Length of t1:", len(t1))

# 4. Membership test
print("Is 30 in t1?", 30 in t1)
print("Is 100 in t1?", 100 in t1)

# 5. Concatenation
print("Concatenation of t1 and t2:", t1 + t2)

# 6. Repetition
print("Repetition of t1:", t1 * 2)

# 7. Count occurrences
t3 = (1, 2, 2, 3, 2)
print("Count of 2 in t3:", t3.count(2))

# 8. Index of element
print("Index of 40 in t1:", t1.index(40))

# 9. Min and Max
nums = (4, 1, 9, 7)
print("Minimum value:", min(nums))
print("Maximum value:", max(nums))

# 10. Converting list to tuple
lst = [1, 2, 3]
tpl = tuple(lst)
print("List converted to tuple:", tpl)
