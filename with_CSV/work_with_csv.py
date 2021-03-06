import csv
import re

pattern = r'\d\d/\d\d/2015'  # Паттерн для поиска преступлений по дате
crimes_log = {}  # Словарь, где будем хранить преступления и их количество
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for item in row:
            if len(re.findall(pattern, item)) > 0:
                # поиск по регулярному выражению, если значение больше 0, разбираем строку на запчасти
                if row[5] not in crimes_log.keys():
                    crimes_log[row[5]] = 1
                else:
                    crimes_log[row[5]] += 1
for item in sorted(crimes_log.items(), key=lambda para: (-para[1], para[0])):
    print(item)

# ('THEFT', 596)
# ('BATTERY', 473)
# ('CRIMINAL DAMAGE', 297)
# ('NARCOTICS', 254)
# ('OTHER OFFENSE', 179)
# ('ASSAULT', 175)
# ('DECEPTIVE PRACTICE', 140)
# ('BURGLARY', 132)
# ('MOTOR VEHICLE THEFT', 123)
# ('ROBBERY', 88)
# ('CRIMINAL TRESPASS', 64)
# ('PUBLIC PEACE VIOLATION', 28)
# ('WEAPONS VIOLATION', 28)
# ('OFFENSE INVOLVING CHILDREN', 18)
# ('CRIM SEXUAL ASSAULT', 17)
# ('PROSTITUTION', 14)
# ('INTERFERENCE WITH PUBLIC OFFICER', 13)
# ('SEX OFFENSE', 9)
# ('HOMICIDE', 5)
# ('LIQUOR LAW VIOLATION', 4)
# ('ARSON', 3)
# ('GAMBLING', 2)
# ('INTIMIDATION', 2)
# ('KIDNAPPING', 2)
# ('STALKING', 2)