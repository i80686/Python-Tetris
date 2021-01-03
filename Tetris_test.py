#Python练习算法太无聊了，来做点有趣的事，方块的初步实现
#我想做个方块游戏，首先要怎么显示
#我想了一办法，print打印16行，清屏，再打印
#梦幻般的游戏引擎的就完成了，笑~
import os
import time
os.system('cls')
Squares = [' ']*160
for x in range(16):       # 1帧
    Squares[x * 10 + 3:x * 10 + 3 + 4] = ['■'] * 4
    for i in range(16):
        print(''.join(Squares[i*10:i*10+10]))    #逐行扫描
    Squares[x * 10 + 3:x * 10 + 3 + 4] = [' '] * 4
    time.sleep(0.5)
    os.system('cls')
