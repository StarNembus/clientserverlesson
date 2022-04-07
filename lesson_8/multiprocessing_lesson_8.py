import multiprocessing
import time


def clock(interval):
    """Простая функция"""
    while True:
        time.sleep(interval)
        print(interval)
        print(f'The time is {time.ctime()}')
        break


if __name__ == '__main__':
    PROC = multiprocessing.Process(target=clock, args=(3, ))
    PROC.start()
    print(f'The time of main process is {time.ctime()}')