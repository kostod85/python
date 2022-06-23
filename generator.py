import time


def gen_numbers():
    num = 0
    while True:
        yield num
        num +=1
        if num // 3:
            print('Вася')
        elif num != (num // 3):
            return num


gen = gen_numbers()

while True:
    print(next(gen))
    time.sleep(1.5)

