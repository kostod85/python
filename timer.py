from datetime import datetime
import os
import time
from pyrsistent import s

нуль = ["■ □ □ □ □ ■",
        "■ □ ■ ■ □ ■",
        "■ □ ■ ■ □ ■",
        "■ □ ■ ■ □ ■",
        "■ □ ■ ■ □ ■",
        "■ □ ■ ■ □ ■",
        "■ □ □ □ □ ■"]

один = ["■ ■ ■ □ ■ ■" ,
        "■ ■ □ □ ■ ■" ,
        "■ □ ■ □ ■ ■" ,
        "■ ■ ■ □ ■ ■" ,
        "■ ■ ■ □ ■ ■" ,
        "■ ■ ■ □ ■ ■",
        "■ ■ ■ □ ■ ■"]

два =  ["■ □ □ □ □ ■" ,
        "□ ■ ■ ■ ■ □" ,
        "■ ■ ■ ■ ■ □" ,     
        "■ ■ ■ ■ □ ■" ,   
        "■ ■ ■ □ ■ ■" ,
        "■ ■ □ ■ ■ ■" ,   
        "□ □ □ □ □ □"]

три =  ["■ □ □ □ □ ■" ,
        "□ ■ ■ ■ ■ □" ,
        "■ ■ ■ ■ □ ■" ,
        "■ □ □ □ ■ ■" ,
        "■ ■ ■ ■ □ ■" ,
        "□ ■ ■ ■ ■ □",
        "■ □ □ □ □ ■"]

четыре =   ["■ □ ■ ■ □ ■" ,
            "■ □ ■ ■ □ ■" ,
            "■ □ ■ ■ □ ■" ,
            "■ □ □ □ □ □" ,
            "■ ■ ■ ■ □ ■" ,
            "■ ■ ■ ■ □ ■" ,
            "■ ■ ■ ■ □ ■"]

пять = ["□ □ □ □ □ □" ,
        "□ ■ ■ ■ ■ ■" ,
        "□ ■ ■ ■ ■ ■" ,
        "□ □ □ □ □ □" ,
        "■ ■ ■ ■ ■ □" ,
        "□ ■ ■ ■ ■ □" ,
        "■ □ □ □ □ ■" ]

шесть = ["■ ■ □ □ □ □" ,
         "■ □ ■ ■ ■ ■" ,
         "□ ■ ■ ■ ■ ■" ,
         "□ □ □ □ □ ■" ,
         "□ ■ ■ ■ ■ □" ,
         "□ ■ ■ ■ ■ □" , 
         "■ □ □ □ □ ■"] 

семь = ["□ □ □ □ □ □",
        "■ ■ ■ ■ ■ □", 
        "■ ■ ■ ■ □ ■",
        "■ ■ ■ □ ■ ■",
        "□ □ □ □ □ ■", 
        "■ □ ■ ■ ■ ■", 
        "□ ■ ■ ■ ■ ■" ]

восемь = ["□ □ □ □ □ □",
          "□ ■ ■ ■ ■ □" ,
          "□ ■ ■ ■ ■ □",
          "■ □ □ □ □ ■",
          "□ ■ ■ ■ ■ □" ,
          "□ ■ ■ ■ ■ □" ,
          "□ □ □ □ □ □"]

девять =   ["■ □ □ □ □ ■",
            "□ ■ ■ ■ ■ □" ,
            "□ ■ ■ ■ ■ □",
            "■ □ □ □ □ □",
            "■ ■ ■ ■ ■ □" ,
            "■ ■ ■ ■ □ ■" ,
            "□ □ □ □ ■ ■"]

точки =["■ ■ ■ ■ ■ ■",
        "■ ■ □ □ ■ ■",
        "■ ■ □ □ ■ ■",
        "■ ■ ■ ■ ■ ■",
        "■ ■ □ □ ■ ■",
        "■ ■ □ □ ■ ■",
        "■ ■ ■ ■ ■ ■"]

dct = {'0': нуль,
       '1': один,
       '2': два,
       '3': три,
       '4': четыре,
       '5': пять,
       '6': шесть,
       '7': семь,
       '8': восемь,
       '9': девять,
       ':': точки}    
    

while True:
    string = datetime.now().strftime("%H:%M:%S")
    watch = []
    for x in string:
        if x in dct.keys():
            watch.append(dct[x])
    print(watch[0][0] + watch[1][0] + watch[2][0] + watch[3][0] + watch[4][0] + watch[5][0] + watch[6][0] + watch[7][0])
    print(watch[0][1] + watch[1][1] + watch[2][1] + watch[3][1] + watch[4][1] + watch[5][1] + watch[6][1] + watch[7][1])
    print(watch[0][2] + watch[1][2] + watch[2][2] + watch[3][2] + watch[4][2] + watch[5][2] + watch[6][2] + watch[7][2])
    print(watch[0][3] + watch[1][3] + watch[2][3] + watch[3][3] + watch[4][3] + watch[5][3] + watch[6][3] + watch[7][3])
    print(watch[0][4] + watch[1][4] + watch[2][4] + watch[3][4] + watch[4][4] + watch[5][4] + watch[6][4] + watch[7][4])
    print(watch[0][5] + watch[1][5] + watch[2][5] + watch[3][5] + watch[4][5] + watch[5][5] + watch[6][5] + watch[7][5])
    print(watch[0][6] + watch[1][6] + watch[2][6] + watch[3][6] + watch[4][6] + watch[5][6] + watch[6][6] + watch[7][6])
    time.sleep(1)
    os.system('cls')
     

#print(read_file()[11])
#sTime = time.time()
#while True:
    #print(datetime.datetime.now())
    #time.sleep(15.0 - ((time.time() - sTime) % 15.0))
    # #def read_file():
    #with open("numb.json", "r+", encoding = "utf-8") as file: это я пытался осуществить вывод из файла numb.json

        #x = file.read().split(",")
        #file.close()
        #return x
    #return "not FOUND 404"
#h = read_file()