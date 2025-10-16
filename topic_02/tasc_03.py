def find_insert_position(sorted_list, new_value):
    for i in range(len(sorted_list)):
        if new_value < sorted_list[i]:
            return i
    return len(sorted_list)  # якщо новий елемент більший за всі — вставляємо в кінець

# Приклад використання:
numbers = [1, 3, 5, 7, 9]
print("Вихідний список:", numbers)

value = int(input("Введіть число для вставки: "))
pos = find_insert_position(numbers, value)

print(f"Елемент {value} потрібно вставити на позицію {pos}")

# Вставимо елемент для перевірки:
numbers.insert(pos, value)
print("Новий список:", numbers)
