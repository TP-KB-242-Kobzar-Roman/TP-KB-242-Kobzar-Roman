# Початковий рядок з пробілами і змішаним регістром
text = "   Hello WORLD!   "

print("Оригінальний рядок:")
print(f"'{text}'")
print()

# 1. strip() - видаляє пробіли з початку та кінця рядка
stripped_text = text.strip()
print("1. Після strip() - видаляємо пробіли з обох кінців:")
print(f"'{stripped_text}'")
print()

# 2. capitalize() - робить першу літеру великою, решту - малими
capitalized_text = stripped_text.capitalize()
print("2. Після capitalize() - перша літера велика, решта малі:")
print(f"'{capitalized_text}'")
print()

# 3. title() - робить першу літеру кожного слова великою
title_text = stripped_text.title()
print("3. Після title() - кожне слово з великої літери:")
print(f"'{title_text}'")
print()

# 4. upper() - робить всі літери великими
upper_text = stripped_text.upper()
print("4. Після upper() - всі літери великі:")
print(f"'{upper_text}'")
print()

# 5. lower() - робить всі літери малими
lower_text = stripped_text.lower()
print("5. Після lower() - всі літери малі:")
print(f"'{lower_text}'")
