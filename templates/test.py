# нахождение файлов с окончанием txt в директории
import os


def collection_data():
    data = os.listdir('/home/kwazart/Рабочий стол/')
    result = []
    for item in data:
        if item.endswith('.txt'):
            result.append(item)
        print(result)