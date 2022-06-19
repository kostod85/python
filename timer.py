import datetime
from http.client import FOUND
from time import strftime
import time
import json

from pyrsistent import s


def read_file():
    with open("numb.json", "r+", encoding = "utf-8") as file:
        x = file.read().split(",")[1]
        file.close()
        return x
    return "not FOUND 404"
    

t = datetime.datetime.now()
time = str(t)
print(time)
i = 1
#while i > 0:
    #print(time)
    #time.sleep(2)
A = { 'one' : "■", 'two' : "□" }


def namb_1():
    print(A['one'], A['one'], A['one'], A["two"], A['one'], A['one'])
    print(A['one'], A['one'], A["two"], A['two'], A['one'], A['one'])
    print(A['one'], A['two'], A['one'], A["two"], A['one'], A['one'])
    print(A['one'], A['one'], A['one'], A["two"], A['one'], A['one'])
    print(A['one'], A['one'], A['one'], A["two"], A['one'], A['one'])
    print(A['one'], A['one'], A['one'], A["two"], A['one'], A['one'])
  
print(read_file())