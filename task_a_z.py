# Kydienko Daniil

# 1. Напишите программу для создания 26 текстовых файлов с именами
# A.txt, B.txt и так далее до Z.txt, в каждом файле будет его имя, пример:
# Файл a.txt - содержит a
# Файл b.txt - содержит b
# 2. Добавьте возможность удаления этих 26 файлов.
#я тут запутался

import string

alphabet = string.ascii_lowercase
for letter in alphabet:
    with open(letter + ".txt", 'w') as file:
        file.write(letter)
