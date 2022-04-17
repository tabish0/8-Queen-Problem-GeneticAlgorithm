# -*- coding: utf-8 -*-
"""l192323.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Od3lGTTKk7pv32Vf5ST3wu-Z5AarBrEi
"""

import random

population = []
popSize = 10
lenBoard = 8

#INITIALIZE POPULATION

def createChromosome():
  lst = list()
  lst.append(random.randint(0,lenBoard-1))
  while len(lst) != 8:
    x = random.randint(0,lenBoard-1)
    if x not in lst:
      lst.append(x)

  return lst


#MAKE BOARD

def makeBoard(chromosome):
  board = list()
  row = list()
  for i in range(0,lenBoard):
    row = []
    for j in range(0,lenBoard):
      row.append(0)
    board.append(row)

  for i in range(0, lenBoard):
    q = chromosome[i]
    board[q][i] = 1
    
  return board

#CHECK FITNESS BY NUMBER OF CLASHES

def fitness(chromosome):
  oriboard = makeBoard(chromosome)
  board = makeBoard(chromosome)
  fit = 0
  
  for i in range(0,lenBoard):
    x = chromosome[i]
    y = i

    #HORIZONTAL

    for j in range(0,y):
      if board[x][j] == 1:
        fit = fit + 1
    
    for  j in range(y+1,lenBoard):
      if board[x][j] == 1:
        fit = fit + 1

    #TOP LEFT    

    tempx = x - 1
    tempy = y - 1

    while tempx >= 0 and tempy >= 0:
      if board[tempx][tempy] == 1:
        fit = fit + 1
      tempx = tempx - 1
      tempy = tempy - 1

    #TOP RIGHT

    tempx = x - 1
    tempy = y + 1

    while tempx >= 0 and tempy < lenBoard:
      if board[tempx][tempy] == 1:
        fit = fit + 1
      tempx = tempx - 1
      tempy = tempy + 1

    #BOTTOM LEFT

    tempx = x + 1
    tempy = y - 1

    while tempx < lenBoard and tempy >= 0:
      if board[tempx][tempy] == 1:
        fit = fit + 1
      tempx = tempx + 1
      tempy = tempy - 1

    #BOTTOM RIGHT

    tempx = x + 1
    tempy = y + 1

    while tempx < lenBoard and tempy < lenBoard:
      if board[tempx][tempy] == 1:
        fit = fit + 1
      tempx = tempx + 1
      tempy = tempy + 1

    board[x][y] = 0

  return fit

def twoPointCrossover(p,q):
  cut1 = random.randint(0,7)
  cut2 = random.randint(0,7)

  if cut2 < cut1:
    cut1,cut2 = cut2,cut1

  if cut1 < cut2:
    for i in range(cut1,cut2):
      p[i],q[i] = q[i],p[i]


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
              arr[j], arr[j + 1] = arr[j + 1], arr[j]
              population[j], population[j + 1] = population[j + 1], population[j]

def mutate(arr):
  cut1 = random.randint(0,7)
  cut2 = random.randint(0,7)
  arr[cut1] = cut2



for i in range (0,popSize):
  population.append(createChromosome())

m = 0


while True:
  m = m + 1
  fitn = []
  for i in range(0,popSize):
   fitn.append(fitness(population[i]))


  bubbleSort(fitn)
  print("fitnes ",fitn)
  print(population[0])
  

  if fitn[0] == 0:
    print("Found")
    print(population[0])
    break

  newSol = list()

  newSol = [population[0],population[1],population[2],population[3],population[4],population[5]]

  twoPointCrossover(newSol[0],newSol[1])
  twoPointCrossover(newSol[1],newSol[2])
  twoPointCrossover(newSol[3],newSol[4])
  mutate(newSol[0])
  mutate(newSol[1])
  mutate(newSol[2])
  mutate(newSol[3])

  c = 0

  for i in range(0, len(newSol)):
    if newSol[i] not in population:
      del population[-1]
      c = c + 1


  for i in range(0,c):
      population.append(newSol[i])

