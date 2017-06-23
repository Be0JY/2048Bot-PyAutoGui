import pyautogui
from random import randint
import time

w, h = 4, 4
board = [[0 for x in range(w)] for y in range(h)] 
temp_board = [[0 for x in range(w)] for y in range(h)] 

board[0][0] = 868, 468
board[0][1] = 1110, 468
board[0][2] = 1352, 468
board[0][3] = 1594, 468
board[1][0] = 868, 710
board[1][1] = 1110, 710
board[1][2] = 1352, 710
board[1][3] = 1594, 710
board[2][0] = 868, 952
board[2][1] = 1110, 952
board[2][2] = 1352, 952
board[2][3] = 1594, 952
board[3][0] = 868, 1194
board[3][1] = 1110, 1194
board[3][2] = 1352, 1194
board[3][3] = 1594, 1194

def print_board():
  print(' ' + str(gboard[0][0]) + ' ' + str(gboard[0][1]) + ' ' + str(gboard[0][2]) + ' ' + str(gboard[0][3]))
  print(' |' + ' |' + ' |' + ' |')
  print(' ' + str(gboard[1][0]) + ' ' + str(gboard[1][1]) + ' ' + str(gboard[1][2]) + ' ' + str(gboard[1][3]))
  print(' |' + ' |' + ' |' + ' |')
  print(' ' + str(gboard[2][0]) + ' ' + str(gboard[2][1]) + ' ' + str(gboard[2][2])
  + ' ' + str(gboard[2][3]))
  print(' |' + ' |' + ' |' + ' |')
  print(' ' + str(gboard[3][0]) + ' ' + str(gboard[3][1]) + ' ' + str(gboard[3][2])
  + ' ' + str(gboard[3][3]))
              
def  combine():
  for i in range(0, 4):
    for j in range(0, 4):
      temp_board[i][j] = gboard[i][j] 

def botright(points):
  for i in range(0, 4):
    for j in range(0, 4):
      if gboard[3][3] >= gboard[i][j]:
        return("None")
      else:
        points - 10
        break
   
def brute_move(): 
  
  moves = [0,1,0,1]
  tree_moves = [0,1,0,1]
  #shiftup  
  for j in range(0,4):
    if temp_board != 0:
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
       
      if temp_board[2][j] != 0 and temp_board[1][j] == 0:
        temp_board[1][j] = temp_board[2][j]
        temp_board[2][j] = 0
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
      
      if temp_board[3][j] != 0 and temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        if temp_board[1][j] == 0:
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = 0
          if temp_board[0][j] == 0:
            temp_board[0][j] = temp_board[1][j]
            temp_board[1][j] = 0
              
      if temp_board[0][j] != 0 and temp_board[0][j] == temp_board[1][j]:
        if temp_board[2][j] == temp_board[3][j]:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = 0
          temp_board[3][j] = 0
          moves[0] = temp_board[0][j] + temp_board[1][j] + moves[0]
        else:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
          moves[0] = temp_board[0][j] + moves[0]
       
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[1][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        moves[0] = temp_board[1][j] + moves[0]
        
      if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[3][j] = 0
        moves[0] = temp_board[3][j] + temp_board[2][j] + moves[0]
        
  combine() 
  #shiftup tree 1
  for j in range(0,4):
    if temp_board != 0:
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
       
      if temp_board[2][j] != 0 and temp_board[1][j] == 0:
        temp_board[1][j] = temp_board[2][j]
        temp_board[2][j] = 0
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
      
      if temp_board[3][j] != 0 and temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        if temp_board[1][j] == 0:
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = 0
          if temp_board[0][j] == 0:
            temp_board[0][j] = temp_board[1][j]
            temp_board[1][j] = 0
              
      if temp_board[0][j] != 0 and temp_board[0][j] == temp_board[1][j]:
        if temp_board[2][j] == temp_board[3][j]:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = 0
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + temp_board[1][j] + tree_moves[0]
        else:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + tree_moves[0]
       
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[1][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[1][j] + tree_moves[0]
        
      if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[3][j] + temp_board[2][j] + tree_moves[0]

  combine()
  #shiftdown tree 1
  for j in range(0, 4):
    if temp_board[2][j] != 0:
      if temp_board[3][j] == 0:
        temp_board[3][j] = temp_board[2][j]
        temp_board[2][j] = 0
      
    if temp_board[1][j] != 0:
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[0][j] != 0 and temp_board[1][j] == 0:
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[3][j] != 0 and temp_board[3][j] == temp_board[2][j]:
      if temp_board[0][j] == temp_board[1][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = 0
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + temp_board[2][j] + tree_moves[1]
      else:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + tree_moves[1]
          
    if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
      temp_board[2][j] = temp_board[1][j]*2
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[2][j] + tree_moves[1]
      
    if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
      temp_board[1][j] = temp_board[0][j]*2
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[1][j] + tree_moves[1]
 
  combine()
  #shiftleft tree 1
  for i in range(0, 4):
    if temp_board[i][1] != 0 and temp_board[i][0] == 0:
      temp_board[i][0] = temp_board[i][1]
      temp_board[i][1] = 0
      
    if temp_board[i][2] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][2]
      temp_board[i][2] = 0
      if temp_board[i][0] == 0:
        temp_board[i][0] = temp_board[i][1]
        temp_board[i][1] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      if temp_board[i][1] == 0:
        temp_board[i][1] = temp_board[i][2]
        temp_board[i][2] = 0
        if temp_board[i][0] == 0:
          temp_board[i][0] = temp_board[i][1]
          temp_board[i][1] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][0] == temp_board[i][1]:
      if temp_board[i][2] == temp_board[i][3]:  
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = 0
        temp_board[i][3] = 0
        tree_moves[2] = temp_board[i][0] + temp_board[i][1] + tree_moves[2]
      else:
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2] 
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        tree_moves[2] = temp_board[i][0] + tree_moves[2]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][1] = temp_board[i][2]*2
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][1] + tree_moves[2]
      
    if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
      temp_board[i][2] = temp_board[i][3]*2
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][2] + tree_moves[2]

  combine()
  #shiftright tree 1
  for i in range(0, 4):
    if temp_board[i][2] != 0 and temp_board[i][3] == 0:
      temp_board[i][3] = temp_board[i][2]
      temp_board[i][2] = 0
      
    if temp_board[i][1] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][1]
      temp_board[i][1] = 0
      if temp_board[i][3] == 0:
        temp_board[i][3] = temp_board[i][2]
        temp_board[i][2] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      if temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = 0
        if temp_board[i][3] == 0:
          temp_board[i][3] = temp_board[i][2]
          temp_board[i][2] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][3] == temp_board[i][2]:
      if temp_board[i][0] == temp_board[i][1]:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = 0
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + temp_board[i][2] + tree_moves[3]
      else:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + tree_moves[3]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][2] = temp_board[i][1]*2
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][2] + tree_moves[3]
          
    if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
      temp_board[i][1] = temp_board[i][0]*2
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][1] + tree_moves[3] 
  combine()

  moves[0] = moves[0] + max(tree_moves)
  tree_moves = [0,1,0,1]
  
  #shiftdown
  for j in range(0, 4):
    if temp_board[2][j] != 0:
      if temp_board[3][j] == 0:
        temp_board[3][j] = temp_board[2][j]
        temp_board[2][j] = 0
      
    if temp_board[1][j] != 0:
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[0][j] != 0 and temp_board[1][j] == 0:
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[3][j] != 0 and temp_board[3][j] == temp_board[2][j]:
      if temp_board[0][j] == temp_board[1][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = 0
        temp_board[0][j] = 0
        moves[1] = temp_board[3][j] + temp_board[2][j] + moves[1]
      else:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
        moves[1]= temp_board[3][j] + moves[1]
          
    if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
      temp_board[2][j] = temp_board[1][j]*2
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      moves[1] = temp_board[2][j] + moves[1]
      
    if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
      temp_board[1][j] = temp_board[0][j]*2
      temp_board[0][j] = 0
      moves[1] = temp_board[1][j] + moves[1]

  combine()
  #shiftup trees 2
  for j in range(0,4):
    if temp_board != 0:
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
       
      if temp_board[2][j] != 0 and temp_board[1][j] == 0:
        temp_board[1][j] = temp_board[2][j]
        temp_board[2][j] = 0
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
      
      if temp_board[3][j] != 0 and temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        if temp_board[1][j] == 0:
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = 0
          if temp_board[0][j] == 0:
            temp_board[0][j] = temp_board[1][j]
            temp_board[1][j] = 0
              
      if temp_board[0][j] != 0 and temp_board[0][j] == temp_board[1][j]:
        if temp_board[2][j] == temp_board[3][j]:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = 0
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + temp_board[1][j] + tree_moves[0]
        else:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + tree_moves[0]
       
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[1][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[1][j] + tree_moves[0]
        
      if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[3][j] + temp_board[2][j] + tree_moves[0]

  combine()
  #shiftdown trees 2
  for j in range(0, 4):
    if temp_board[2][j] != 0:
      if temp_board[3][j] == 0:
        temp_board[3][j] = temp_board[2][j]
        temp_board[2][j] = 0
      
    if temp_board[1][j] != 0:
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[0][j] != 0 and temp_board[1][j] == 0:
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[3][j] != 0 and temp_board[3][j] == temp_board[2][j]:
      if temp_board[0][j] == temp_board[1][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = 0
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + temp_board[2][j] + tree_moves[1]
      else:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + tree_moves[1]
          
    if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
      temp_board[2][j] = temp_board[1][j]*2
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[2][j] + tree_moves[1]
      
    if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
      temp_board[1][j] = temp_board[0][j]*2
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[1][j] + tree_moves[1]

  combine()
  #shiftleft trees 2
  for i in range(0, 4):
    if temp_board[i][1] != 0 and temp_board[i][0] == 0:
      temp_board[i][0] = temp_board[i][1]
      temp_board[i][1] = 0
      
    if temp_board[i][2] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][2]
      temp_board[i][2] = 0
      if temp_board[i][0] == 0:
        temp_board[i][0] = temp_board[i][1]
        temp_board[i][1] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      if temp_board[i][1] == 0:
        temp_board[i][1] = temp_board[i][2]
        temp_board[i][2] = 0
        if temp_board[i][0] == 0:
          temp_board[i][0] = temp_board[i][1]
          temp_board[i][1] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][0] == temp_board[i][1]:
      if temp_board[i][2] == temp_board[i][3]:  
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = 0
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + temp_board[i][1] + moves[2]
      else:
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2] 
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + moves[2]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][1] = temp_board[i][2]*2
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][1] + tree_moves[2]
      
    if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
      temp_board[i][2] = temp_board[i][3]*2
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][2] + tree_moves[2]
  combine()  
  #shiftright trees2
  for i in range(0, 4):
    if temp_board[i][2] != 0 and temp_board[i][3] == 0:
      temp_board[i][3] = temp_board[i][2]
      temp_board[i][2] = 0
      
    if temp_board[i][1] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][1]
      temp_board[i][1] = 0
      if temp_board[i][3] == 0:
        temp_board[i][3] = temp_board[i][2]
        temp_board[i][2] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      if temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = 0
        if temp_board[i][3] == 0:
          temp_board[i][3] = temp_board[i][2]
          temp_board[i][2] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][3] == temp_board[i][2]:
      if temp_board[i][0] == temp_board[i][1]:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = 0
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + temp_board[i][2] + tree_moves[3]
      else:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + tree_moves[3]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][2] = temp_board[i][1]*2
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][2] + tree_moves[3]
          
    if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
      temp_board[i][1] = temp_board[i][0]*2
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][1] + tree_moves[3] 
  combine()
  moves[1] = moves[1] + max(tree_moves)
  tree_moves = [0,1,0,0]
  #shiftleft
  for i in range(0, 4):
      if temp_board[i][1] != 0 and temp_board[i][0] == 0:
        temp_board[i][0] = temp_board[i][1]
        temp_board[i][1] = 0
      
      if temp_board[i][2] != 0 and temp_board[i][1] == 0:
        temp_board[i][1] = temp_board[i][2]
        temp_board[i][2] = 0
        if temp_board[i][0] == 0:
          temp_board[i][0] = temp_board[i][1]
          temp_board[i][1] = 0
      
      if temp_board[i][3] != 0 and temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        if temp_board[i][1] == 0:
          temp_board[i][1] = temp_board[i][2]
          temp_board[i][2] = 0
          if temp_board[i][0] == 0:
            temp_board[i][0] = temp_board[i][1]
            temp_board[i][1] = 0
      
      if temp_board[i][0] != 0 and temp_board[i][0] == temp_board[i][1]:
        if temp_board[i][2] == temp_board[i][3]:  
          temp_board[i][0] = temp_board[i][1]*2
          temp_board[i][1] = temp_board[i][2]*2
          temp_board[i][2] = 0
          temp_board[i][3] = 0
          moves[2] = temp_board[i][0] + temp_board[i][1] + moves[2]
        else:
          temp_board[i][0] = temp_board[i][1]*2
          temp_board[i][1] = temp_board[i][2] 
          temp_board[i][2] = temp_board[i][3]
          temp_board[i][3] = 0
          moves[2] = temp_board[i][0] + moves[2]
        
      if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        moves[2] = temp_board[i][1] + moves[2]
        
      if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
        temp_board[i][2] = temp_board[i][3]*2
        temp_board[i][3] = 0
        moves[2] = temp_board[i][2] + moves[2]
  
  combine()
  #shiftup tree 3
  for j in range(0,4):
    if temp_board != 0:
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
       
      if temp_board[2][j] != 0 and temp_board[1][j] == 0:
        temp_board[1][j] = temp_board[2][j]
        temp_board[2][j] = 0
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
      
      if temp_board[3][j] != 0 and temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        if temp_board[1][j] == 0:
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = 0
          if temp_board[0][j] == 0:
            temp_board[0][j] = temp_board[1][j]
            temp_board[1][j] = 0
              
      if temp_board[0][j] != 0 and temp_board[0][j] == temp_board[1][j]:
        if temp_board[2][j] == temp_board[3][j]:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = 0
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + temp_board[1][j] + tree_moves[0]
        else:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + tree_moves[0]
       
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[1][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[1][j] + tree_moves[0]
        
      if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[3][j] + temp_board[2][j] + tree_moves[0]
  
  combine()
  #shiftdown tree 3
  for j in range(0, 4):
    if temp_board[2][j] != 0:
      if temp_board[3][j] == 0:
        temp_board[3][j] = temp_board[2][j]
        temp_board[2][j] = 0
      
    if temp_board[1][j] != 0:
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[0][j] != 0 and temp_board[1][j] == 0:
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[3][j] != 0 and temp_board[3][j] == temp_board[2][j]:
      if temp_board[0][j] == temp_board[1][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = 0
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + temp_board[2][j] + tree_moves[1]
      else:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + tree_moves[1]
          
    if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
      temp_board[2][j] = temp_board[1][j]*2
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[2][j] + tree_moves[1]
      
    if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
      temp_board[1][j] = temp_board[0][j]*2
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[1][j] + tree_moves[1] 
  combine()
  #shiftleft trees 3
  for i in range(0, 4):
    if temp_board[i][1] != 0 and temp_board[i][0] == 0:
      temp_board[i][0] = temp_board[i][1]
      temp_board[i][1] = 0
      
    if temp_board[i][2] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][2]
      temp_board[i][2] = 0
      if temp_board[i][0] == 0:
        temp_board[i][0] = temp_board[i][1]
        temp_board[i][1] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      if temp_board[i][1] == 0:
        temp_board[i][1] = temp_board[i][2]
        temp_board[i][2] = 0
        if temp_board[i][0] == 0:
          temp_board[i][0] = temp_board[i][1]
          temp_board[i][1] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][0] == temp_board[i][1]:
      if temp_board[i][2] == temp_board[i][3]:  
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = 0
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + temp_board[i][1] + moves[2]
      else:
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2] 
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + moves[2]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][1] = temp_board[i][2]*2
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][1] + tree_moves[2]
      
    if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
      temp_board[i][2] = temp_board[i][3]*2
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][2] + tree_moves[2] 
  combine()
  #shiftright trees 3
  for i in range(0, 4):
    if temp_board[i][2] != 0 and temp_board[i][3] == 0:
      temp_board[i][3] = temp_board[i][2]
      temp_board[i][2] = 0
      
    if temp_board[i][1] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][1]
      temp_board[i][1] = 0
      if temp_board[i][3] == 0:
        temp_board[i][3] = temp_board[i][2]
        temp_board[i][2] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      if temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = 0
        if temp_board[i][3] == 0:
          temp_board[i][3] = temp_board[i][2]
          temp_board[i][2] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][3] == temp_board[i][2]:
      if temp_board[i][0] == temp_board[i][1]:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = 0
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + temp_board[i][2] + tree_moves[3]
      else:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + tree_moves[3]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][2] = temp_board[i][1]*2
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][2] + tree_moves[3]
          
    if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
      temp_board[i][1] = temp_board[i][0]*2
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][1] + tree_moves[3] 

  moves[2] = moves[2] + max(tree_moves)
  tree_moves = [0,1,0,1]
  combine()
  #shift right
  for i in range(0, 4):
    if temp_board[i][2] != 0 and temp_board[i][3] == 0:
      temp_board[i][3] = temp_board[i][2]
      temp_board[i][2] = 0
      
    if temp_board[i][1] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][1]
      temp_board[i][1] = 0
      if temp_board[i][3] == 0:
        temp_board[i][3] = temp_board[i][2]
        temp_board[i][2] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      if temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = 0
        if temp_board[i][3] == 0:
          temp_board[i][3] = temp_board[i][2]
          temp_board[i][2] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][3] == temp_board[i][2]:
      if temp_board[i][0] == temp_board[i][1]:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = 0
        temp_board[i][0] = 0
        moves[3] = temp_board[i][3] + temp_board[i][2] + moves[3]
      else:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
        moves[3] = temp_board[i][3] + moves[3]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][2] = temp_board[i][1]*2
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      moves[3] = temp_board[i][2] + moves[3]
          
    if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
      temp_board[i][1] = temp_board[i][0]*2
      temp_board[i][0] = 0
      moves[3] = temp_board[i][1] + moves[3]

  combine()
  #shiftup trees 4
  for j in range(0,4):
    if temp_board != 0:
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
       
      if temp_board[2][j] != 0 and temp_board[1][j] == 0:
        temp_board[1][j] = temp_board[2][j]
        temp_board[2][j] = 0
      if temp_board[0][j] == 0:
        temp_board[0][j] = temp_board[1][j]
        temp_board[1][j] = 0
      
      if temp_board[3][j] != 0 and temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        if temp_board[1][j] == 0:
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = 0
          if temp_board[0][j] == 0:
            temp_board[0][j] = temp_board[1][j]
            temp_board[1][j] = 0
              
      if temp_board[0][j] != 0 and temp_board[0][j] == temp_board[1][j]:
        if temp_board[2][j] == temp_board[3][j]:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = 0
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + temp_board[1][j] + tree_moves[0]
        else:
          temp_board[0][j] = temp_board[1][j]*2
          temp_board[1][j] = temp_board[2][j]
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
          tree_moves[0] = temp_board[0][j] + tree_moves[0]
       
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[1][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[3][j]
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[1][j] + tree_moves[0]
        
      if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[3][j] = 0
        tree_moves[0] = temp_board[3][j] + temp_board[2][j] + tree_moves[0]
  
  combine()
  #shiftdown trees 4
  for j in range(0, 4):
    if temp_board[2][j] != 0:
      if temp_board[3][j] == 0:
        temp_board[3][j] = temp_board[2][j]
        temp_board[2][j] = 0
      
    if temp_board[1][j] != 0:
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[0][j] != 0 and temp_board[1][j] == 0:
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      if temp_board[2][j] == 0:
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = 0
        if temp_board[3][j] == 0:
          temp_board[3][j] = temp_board[2][j]
          temp_board[2][j] = 0
      
    if temp_board[3][j] != 0 and temp_board[3][j] == temp_board[2][j]:
      if temp_board[0][j] == temp_board[1][j]:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = 0
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + temp_board[2][j] + tree_moves[1]
      else:
        temp_board[3][j] = temp_board[2][j]*2
        temp_board[2][j] = temp_board[1][j]
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
        tree_moves[1] = temp_board[3][j] + tree_moves[1]
          
    if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
      temp_board[2][j] = temp_board[1][j]*2
      temp_board[1][j] = temp_board[0][j]
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[2][j] + tree_moves[1]
      
    if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
      temp_board[1][j] = temp_board[0][j]*2
      temp_board[0][j] = 0
      tree_moves[1] = temp_board[1][j] + tree_moves[1]
  combine()
  #shiftleft trees 4
  for i in range(0, 4):
    if temp_board[i][1] != 0 and temp_board[i][0] == 0:
      temp_board[i][0] = temp_board[i][1]
      temp_board[i][1] = 0
      
    if temp_board[i][2] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][2]
      temp_board[i][2] = 0
      if temp_board[i][0] == 0:
        temp_board[i][0] = temp_board[i][1]
        temp_board[i][1] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      if temp_board[i][1] == 0:
        temp_board[i][1] = temp_board[i][2]
        temp_board[i][2] = 0
        if temp_board[i][0] == 0:
          temp_board[i][0] = temp_board[i][1]
          temp_board[i][1] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][0] == temp_board[i][1]:
      if temp_board[i][2] == temp_board[i][3]:  
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = 0
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + temp_board[i][1] + moves[2]
      else:
        temp_board[i][0] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][2] 
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        moves[2] = temp_board[i][0] + moves[2]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][1] = temp_board[i][2]*2
      temp_board[i][2] = temp_board[i][3]
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][1] + tree_moves[2]
      
    if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
      temp_board[i][2] = temp_board[i][3]*2
      temp_board[i][3] = 0
      tree_moves[2] = temp_board[i][2] + tree_moves[2]
  combine()
  #shiftright trees 4
  for i in range(0, 4):
    if temp_board[i][2] != 0 and temp_board[i][3] == 0:
      temp_board[i][3] = temp_board[i][2]
      temp_board[i][2] = 0
      
    if temp_board[i][1] != 0 and temp_board[i][2] == 0:
      temp_board[i][2] = temp_board[i][1]
      temp_board[i][1] = 0
      if temp_board[i][3] == 0:
        temp_board[i][3] = temp_board[i][2]
        temp_board[i][2] = 0
      
    if temp_board[i][0] != 0 and temp_board[i][1] == 0:
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      if temp_board[i][2] == 0:
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = 0
        if temp_board[i][3] == 0:
          temp_board[i][3] = temp_board[i][2]
          temp_board[i][2] = 0
      
    if temp_board[i][3] != 0 and temp_board[i][3] == temp_board[i][2]:
      if temp_board[i][0] == temp_board[i][1]:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = 0
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + temp_board[i][2] + tree_moves[3]
      else:
        temp_board[i][3] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][1]
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
        tree_moves[3] = temp_board[i][3] + tree_moves[3]
      
    if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
      temp_board[i][2] = temp_board[i][1]*2
      temp_board[i][1] = temp_board[i][0]
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][2] + tree_moves[3]
          
    if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
      temp_board[i][1] = temp_board[i][0]*2
      temp_board[i][0] = 0
      tree_moves[3] = temp_board[i][1] + tree_moves[3]
  moves[3] = moves[3] + max(tree_moves)
  

  if max(moves) == moves[1] and max(moves) == moves[2]:
    pyautogui.press('down')
  
  elif max(moves) == moves[0]:
    pyautogui.press('up')
  elif max(moves) == moves[1]:
    pyautogui.press('down')
  elif max(moves) == moves[2]:
    pyautogui.press('left')
  elif max(moves) == moves[3]:
    pyautogui.press('right')
  
while True:
  im = pyautogui.screenshot()
  gboard = [[0 for x in range(w)] for y in range(h)] 
  for i in range(0, 4):
      for j in range(0, 4):
        board_space = im.getpixel(board[i][j])
        if board_space == (238, 228, 218, 255):
            gboard[i][j] = 2
        if board_space == (237, 224, 200, 255):
            gboard[i][j] = 4
        if board_space == (242, 177, 121, 255):
            gboard[i][j] = 8
        if board_space == (245, 149, 99, 255):
            gboard[i][j] = 16
        if board_space == (246, 124, 95, 255):
            gboard[i][j] = 32
        if board_space == (246, 94, 59, 255):
            gboard[i][j] = 64
        if board_space == (237, 207, 114, 255):
            gboard[i][j] = 128
        if board_space == (237, 204, 97, 255):
            gboard[i][j] = 256
        if board_space == (237, 200, 80, 255):
            gboard[i][j] = 512 

  print_board()
  print(' ')
  brute_move() 
  print_board()
  print(' ')




