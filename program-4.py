import csv

with open("space.txt",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='*')
    answer = list(reader)[1:]
    answer_new = []
    for shipName, planet, coord_place, direction in answer:

        # Создаём пароль
        new_password = (planet[-1:-4:-1][::-1] + shipName[1:3][::-1] + planet[:3][::-1]).upper()
        answer_new.append([shipName, planet, coord_place, direction, new_password])


        
            
# Записываем исправленные данные в новый файл с названием space_uniq_password.txt
with open("space_uniq_password.csv",'w',encoding="utf-8",newline='') as file:
    w = csv.writer(file, delimiter='*')
    w.writerow(["ShipName","planet","coord_place","direction","password"])
    w.writerows(answer_new)
