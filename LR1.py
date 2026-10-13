import time
import sys
import os

BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
RED = '\u001b[41m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'

#Флаг

def flag():
    pixel = '    '
    lenght = 10
    height = lenght

    for i in range(height):
        if i < height // 2 - 1:
            print(WHITE + pixel * (lenght//2 - 2) + BLUE + pixel * 1 + WHITE + pixel * (lenght//2 + 2) + RESET)
        elif i == (height//2) - 1 :
            print(BLUE + pixel * (lenght + 1) + RESET)
        elif i == height //2:
            print(BLUE + pixel * (lenght + 1) + RESET)
        else:
            print(WHITE + pixel * (lenght//2 - 2) + BLUE + pixel * 1 + WHITE + pixel * (lenght//2 + 2) + RESET)
flag()


#Узор

def draw_line(offset=0, lenght=1, color=234):
    first_circle = f'{" " * offset}\x1b[48;5;{color}m{" " * lenght}\x1b[0m'
    gap = 31 - lenght
    second_circle = f'{" " * gap}\x1b[48;5;{color}m{" " * lenght}\x1b[0m'
    print(first_circle + second_circle)
def pattern():
    height = 13
    center = height // 2
    offset = height + 1
    step = 1
    lenght = 3
    colors = [15, 20, 196, 228]

    while True:
        for color in colors:
            for line in range(height):
                draw_line(offset, lenght, color)
                if line < center:
                    if line == 0 or line == 1:
                        offset -= step *4
                        lenght += step*8
                    elif line == 2 or line == 3:
                        offset -= step*2  
                        lenght += step*4
                    else:
                        offset -= step 
                        lenght += step*2
                else:
                    if line == height - 2 or line == height - 3:
                        offset += step*4
                        lenght -= step*8
                    elif line == height - 4 or line == height - 5:
                        offset += step*2  
                        lenght -= step*4
                    else:
                        offset += step
                        lenght -= step*2
            print(f'\x1b[{height + 2}A') #поднятие курсора вверх, чтобы узор рисовался поверх старого
            print(f'\x1b[{offset}D') #возврат курсора к началу строки
            lenght = 3
            offset = height + 1
            time.sleep(2)
pattern()


# #Анимация
frames = [
    '''     
            #
            #
        # # # # # 
            #  
            #
    ''',
    '''     

       
        # # # # # 
            
        
    ''',
    '''
         #   #
          # #
           #
          # #
         #   #
    ''',
    '''     
           #
    
        #######
    
           #
    ''',
]
height = 5
for cycle in range(5):
    for frame in frames:
        os.system('cls')
        if cycle > 0:
            print(f"\033[{height}A", end="", flush=True) # возвращает курсор вверх
        print(frame, end="", flush=True)
        time.sleep(1)


# Sequence


def sequence():
    file = open('sequence.txt', 'r')
    pos = []
    neg = []
    for line in file:
        if float(line) >= 5 and float(line) <=10:
            pos.append(float(line))
        elif float(line) >= -10 and float(line) <=-5:
            neg.append(float(line))
    file.close()
    print(f'{BLUE}{' ' * int(len(pos))}{RESET} {len(pos)/(len(neg)+ len(pos)) * 100}% - Числа в промежутке [5;10]')
    print(f'{RED}{' ' * int(len(neg))}{RESET} {len(neg)/(len(pos) + len(neg)) * 100}% - Числа в промежутке [-10;-5]')
sequence()


#График
height = 9
def draw_point(p_offset = 0):
    return f'{" " * p_offset}*'

def gr():
    height = 9
    p_offset = 53
    step = 1

    print(' y\n ^\n |')
    for new_line in range(height):
        print(f'{height - new_line}-{draw_point(p_offset)}')
        p_offset -= step * 6

gr()

print('  ──|──|──|──|──|──|──|──|──|──|──|──|──|──|──|──|──|──|──>x\n    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18')

