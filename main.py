import os
import math

def clear():
    os.system("clear")

symbols = {
    'x': [
        '\\     /',
        ' \\   / ',
        '  \\ /  ',
        '   X   ',
        '  / \\  ',
        ' /   \\ ',
        '/     \\',
    ],
    'o': [
        '._____.',
        '|     |',
        '|     |',
        '|     |',
        '|     |',
        '|     |',
        '\'-----\'',
    ]
}

def rgrid(gs):
    grid = {}
    for i in range(0, gs):
      grid[chr(97+i)] = []
      for j in range(0, gs):
          grid[chr(97+i)].append([])
    return grid
"""
def wchecker(data):
  for i in data:
    for j in data[i]:
      if j == 
  return winner
"""
def render(data):
    grid = ''
    bs = len(symbols['x'])  #Blank Size
    hm = math.floor(bs/2) #halfmark
    line = ' +' + ((('-' * bs) + '+') * len(data)) + '\n'
  
    #Number placement
    for i in range(0, len(data)):
        grid += (' '*(hm+2))+f'{i}'+(' '*(hm-1))
    grid += '\n'
    grid += line
    #Grid render
    for i in data:
        for j in range(0, len(symbols['x'])):
            if j == hm:
              grid+=i
            else:
              grid+=' '
            for k in data[i]:
                grid += '|'
                if k == []:
                    grid += ((' ' * (bs)))
                else:
                    grid += symbols[k[0]][j]
            grid += '|\n'
        grid += line
    print(grid)

while True:
    clear()
    print('TicTacToe ___ in a row.', end='\r')
    s = int(input('TicTacToe '))
  
    print('\nGrid size is ___.',end= '\r')
    gs = int(input('Grid size is '))
    clear()

    data = rgrid(gs)
    render(data)
    t = 'x'
    for i in range(0, gs * gs):
        if t =='x':
            m = input('X were is your move?(ex:a0)\n')
            t = 'o'
        else:
            m = input('O were is your move?(ex:a0)\n')
            t = 'x'
        data[m[0]][int(m[1])].append(t)
        clear()
        render(data)