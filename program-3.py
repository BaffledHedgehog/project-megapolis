import csv

with open("space_new.txt",encoding="utf-8") as file:
    reader = csv.reader(file,delimiter='*')
    answer = list(reader)[1:]

    # Считываем имя корабля
    shipName_input = input()
    while shipName_input != "stop":
        success = 0
        for shipName, planet, coord_place, direction in answer:
            if shipName_input == shipName:
                
                # Выводим информацию если корабль найден
                print(f"Корабль {shipName} был отправлен с планеты: {planet} и его направление движения было: {direction}")
                success = 1
                break

        # Выводим информацию если корабль не найден
        if success == 0:
            print("error.. er.. ror..")

        # Считываем имя корабля
        shipName_input = input()
