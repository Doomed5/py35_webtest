import multiprocessing
import time

def dance():
    for i in range(3):
        print('tiaowu')
        time.sleep(2)

def sing():
    for i in range(3):
        print('changge')
        time.sleep(2)

if __name__ == '__main__':

    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)
    dance_process.start()
    sing_process.start()


