import time
from threading import Thread

def clock(interval):
    """Функция котоая может быть запущена в потоке"""

    while True:
        time.sleep(interval)
        print(interval)
        print(f'Текущее время: {time.ctime()}')
        break


THR1 = Thread(target=clock, args=(2, ))
THR2 = Thread(target=clock, args=(3, ))


print(f'Время запуска основной программы: {time.ctime()}')
start = time.time()

THR1.start()
THR2.start()


end = time.time()
print(f'Время ококнчания основной программы: {time.ctime()}')
print('end-start = ', end-start)
