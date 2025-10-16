# Створюємо список
nums = [1, 2, 3]
print("Початковий список:", nums)

# append()
nums.append(4)
print("Після append(4):", nums)

# extend()
nums.extend([5, 6])
print("Після extend([5, 6]):", nums)

# insert()
nums.insert(2, 99)
print("Після insert(2, 99):", nums)

# remove()
nums.remove(99)
print("Після remove(99):", nums)

# sort()
nums.sort()
print("Після sort():", nums)

# reverse()
nums.reverse()
print("Після reverse():", nums)

# copy()
nums_copy = nums.copy()
print("Копія списку:", nums_copy)

# clear()
nums.clear()
print("Після clear():", nums)
