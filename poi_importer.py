import csv
import os

from guide.models import Point


def run():
    csv_file_name = input("Введите имя файла для импорта: ")

    if not os.path.exists(csv_file_name):
        raise FileNotFoundError(f'{csv_file_name} does not exist.')

    with open(csv_file_name, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        Point.objects.all().delete()

        for row in reader:
            print(row)

            name = ' '.join(row[0].split(' ')[1:])
            if name:
                description = row[1]
                x_coord = float(row[2])
                y_coord = float(row[3])
                new_point = Point(name=name, description=description, x_coord=x_coord, y_coord=y_coord)
                new_point.save()
