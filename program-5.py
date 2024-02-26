import csv

ship_name=hash(input())
with open("space.txt",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='*')
    answer = list(reader)[1:]
    hash_table = []
    for shipName, planet, coord_place, direction in answer:

        # Создаём хеш-таблицу
        hashed = [hash(planet),hash(shipName)]
        hash_table.append(hashed)
    if ship_name == hashed[1]:
        print(shipName, planet, coord_place, direction)

# выводим 10 элементов
for num in range(10):
    key = hash_table[num][0]
    number = hash_table[num][1]
    print(f"{key}: {number}")
