import csv

with open("space.txt",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='*')
    answer = list(reader)[1:]
    answer_new = []
    for shipName, planet, coord_place, direction in answer:
        
        # Запишем координаты в массив из 2-х элементов
        coords = [int(el) for el in direction.split()]

        # Проверяем, пробиты ли координаты
        if coord_place == '0 0':

            # Получаем переменные, необходимые для формулы
            n=int(shipName[5])
            m=int(shipName[6])
            t=len(planet)


            # Получаем нужные координаты в соответствии с формулой

            if n > 5: x = n + coords[0]
            else: x = (-(n + coords[0])) * 4 + t
            if m > 3: y = m + t + coords[1]
            else: y = (-(n + coords[1])) * m

            # Записываем результат
            coord_place_new = str(x) + ' ' + str(y)
        else:
            x = coords[0]
            y = coords[1]
            coord_place_new = coord_place
        answer_new.append([shipName, planet, coord_place_new, direction])

        # Выводим названия кораблей и их координаты, если код корабля заканчивается на V
        if shipName[3] == 'V':
            print(f" {shipName} - ({x}, {y})")
            
# Записываем исправленные данные в новый файл с названием space_new.txt
with open("space_new.txt",'w',encoding="utf-8",newline='') as file:
    w = csv.writer(file, delimiter='*')
    w.writerow(["ShipName","planet","coord_place","direction"])
    w.writerows(answer_new)

