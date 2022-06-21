import time

def gen_numbers():
    num = 0
    while True:
        yield num
        num +=1
        if num == 5:
            num += 1
        
gen = gen_numbers()
i = 0
while True :
    i = i + 1
    print(next(gen))
    time.sleep(0)
    if i == 5:
        print('Вася')
    elif i >= 11:
        break