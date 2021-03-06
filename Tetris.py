#Python数据结构实战练习——俄罗斯方块
import os
import time
import msvcrt
import random
os.system('cls')
input('操作：左(a)，右(d)，变形(Enter)\n按Enter开始，CTRL+C退出')
def key_x():
    if msvcrt.kbhit():
        ret = msvcrt.getch()
    else:
        ret = 0
    return ret
def remainder(dividends):
    remainders = []
    for dividend in dividends:
        remainders.append(dividend % 10)
    return remainders
os.system('cls')
Squares = ['　']*200
Squares[160:170] = ['■']*10
tetrominoes_all = {
'I':[[4, 5, 6, 7], [5, 15, 25, 35]],
'J':[[5, 15, 24, 25], [4, 14, 15, 16], [4, 5, 14, 24], [4, 5, 6, 16]],
'L':[[5, 15, 25, 26], [4, 5, 6, 14], [4, 5, 15, 25], [6, 14, 15, 16]],
'O':[[4, 5, 14, 15]],
'S':[[5, 6, 14, 15], [5, 15, 16, 26]],
'T':[[5, 14, 15, 16], [5, 15, 16, 25], [4, 5, 6, 15], [6, 16, 15, 26]],
'Z':[[4, 5, 15, 16], [6, 15, 16, 25]]}
Tetromino_all = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
scores = 0
while True:
    key_sum = 0
    Tetrominoes = tetrominoes_all[random.choice(Tetromino_all)][0]
    #Tetrominoes = tetrominoes_all['I'][0]
    for x in range(16):       # 1帧
        # 键位捕获
        key_xx = key_x()
        if key_xx == b'a' and min(remainder(Tetrominoes))+key_sum > 0:
            key_sum = key_sum-1
        elif key_xx == b'd' and max(remainder(Tetrominoes))+key_sum < 9:
            key_sum = key_sum+1
        elif key_xx == b'\r':
            if Tetrominoes == tetrominoes_all['I'][0]:
                Tetrominoes = tetrominoes_all['I'][1]

            elif Tetrominoes == tetrominoes_all['I'][1]:
                Tetrominoes = tetrominoes_all['I'][0]

            elif Tetrominoes == tetrominoes_all['J'][0]:
                Tetrominoes = tetrominoes_all['J'][1]
            elif Tetrominoes == tetrominoes_all['J'][1]:
                Tetrominoes = tetrominoes_all['J'][2]
            elif Tetrominoes == tetrominoes_all['J'][2]:
                Tetrominoes = tetrominoes_all['J'][3]
            elif Tetrominoes == tetrominoes_all['J'][3]:
                Tetrominoes = tetrominoes_all['J'][0]

            elif Tetrominoes == tetrominoes_all['L'][0]:
                Tetrominoes = tetrominoes_all['L'][1]
            elif Tetrominoes == tetrominoes_all['L'][1]:
                Tetrominoes = tetrominoes_all['L'][2]
            elif Tetrominoes == tetrominoes_all['L'][2]:
                Tetrominoes = tetrominoes_all['L'][3]
            elif Tetrominoes == tetrominoes_all['L'][3]:
                Tetrominoes = tetrominoes_all['L'][0]

            elif Tetrominoes == tetrominoes_all['S'][0]:
                Tetrominoes = tetrominoes_all['S'][1]
            elif Tetrominoes == tetrominoes_all['S'][1]:
                Tetrominoes = tetrominoes_all['S'][0]

            elif Tetrominoes == tetrominoes_all['T'][0]:
                Tetrominoes = tetrominoes_all['T'][1]
            elif Tetrominoes == tetrominoes_all['T'][1]:
                Tetrominoes = tetrominoes_all['T'][2]
            elif Tetrominoes == tetrominoes_all['T'][2]:
                Tetrominoes = tetrominoes_all['T'][3]
            elif Tetrominoes == tetrominoes_all['T'][3]:
                Tetrominoes = tetrominoes_all['T'][0]

            elif Tetrominoes == tetrominoes_all['Z'][0]:
                Tetrominoes = tetrominoes_all['Z'][1]
            elif Tetrominoes == tetrominoes_all['Z'][1]:
                Tetrominoes = tetrominoes_all['Z'][0]
        for Tetromino in Tetrominoes:
            Squares[x*10+Tetromino+key_sum] = '■'
        for i in range(17):
            print(''.join(Squares[i*10:i*10+10]))    #逐行扫描
        print(f'得分：{scores}\n左:a 右:d 加速:s 变形:Enter\n暂停:p 退出:CTRL+C')
        for Tetromino in Tetrominoes:
            Squares[x*10+Tetromino+key_sum] = '　'
        #判断下一行是否已有方块
        Tetrominoes_add1 = []
        for Tetromino in Tetrominoes:
            Tetrominoes_add1.append((x+1)*10+Tetromino+key_sum)
        if (Squares[Tetrominoes_add1[0]] == '■') or (Squares[Tetrominoes_add1[1]] == '■') or (Squares[Tetrominoes_add1[2]] == '■') or (Squares[Tetrominoes_add1[3]] == '■'):
            #input('按Enter继续……')
            for Tetromino in Tetrominoes:
                Squares[x * 10 + Tetromino+key_sum] = '■'
            break
        if key_xx == b'p':
            input('按Enter继续……')
        if key_xx == b's':
            pass  #加速
        else:
            time.sleep(0.6)
        os.system('cls')
    #得分、消行、补行
    for i in range(16):
        if Squares[i*10:i*10+10] == ['■']*10:
            del Squares[i*10:i*10+10]
            add_Squares = ['　']*10
            Squares = add_Squares+Squares
            scores = scores+10
    #到顶游戏结束
    if '■' in ''.join(Squares[0:10]):
        break
    os.system('cls')
