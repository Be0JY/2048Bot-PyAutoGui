import pyautogui
from random import randint
import time

im = pyautogui.screenshot()
w, h = 4, 4

board = [[0 for x in range(w)] for y in range(h)] 
temp_board = [[0 for x in range(w)] for y in range(h)] 



board[0][0] = input("Enter the X coordinate for [0][0] on the grid."), input("Enter the Y coordinate for [0][0] on the grid.") 
board[0][1] = input("Enter the X coordinate for [0][1] on the grid."), input("Enter the Y coordinate for [0][1] on the grid.")
board[0][2] = input("Enter the X coordinate for [0][2] on the grid."), input("Enter the Y coordinate for [0][2] on the grid.")
board[0][3] = input("Enter the X coordinate for [0][3] on the grid."), input("Enter the Y coordinate for [0][3] on the grid.")
board[1][0] = input("Enter the X coordinate for [1][0] on the grid."), input("Enter the Y coordinate for [1][0] on the grid.")
board[1][1] = input("Enter the X coordinate for [1][1] on the grid."), input("Enter the Y coordinate for [1][1] on the grid.")
board[1][2] = input("Enter the X coordinate for [1][2] on the grid."), input("Enter the Y coordinate for [1][2] on the grid.")
board[1][3] = input("Enter the X coordinate for [1][3] on the grid."), input("Enter the Y coordinate for [1][3] on the grid.")
board[2][0] = input("Enter the X coordinate for [2][0] on the grid."), input("Enter the Y coordinate for [2][0] on the grid.")
board[2][1] = input("Enter the X coordinate for [2][1] on the grid."), input("Enter the Y coordinate for [2][1] on the grid.")
board[2][2] = input("Enter the X coordinate for [2][2] on the grid."), input("Enter the Y coordinate for [2][2] on the grid.")
board[2][3] = input("Enter the X coordinate for [2][3] on the grid."), input("Enter the Y coordinate for [2][3] on the grid.")
board[3][0] = input("Enter the X coordinate for [3][0] on the grid."), input("Enter the Y coordinate for [3][0] on the grid.")
board[3][1] = input("Enter the X coordinate for [3][1] on the grid."), input("Enter the Y coordinate for [3][1] on the grid.")
board[3][2] = input("Enter the X coordinate for [3][2] on the grid."), input("Enter the Y coordinate for [3][2] on the grid.")
board[3][3] = input("Enter the X coordinate for [3][3] on the grid."), input("Enter the Y coordinate for [3][3] on the grid.")
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
              
def combine():
  for i in range(0, 4):
    for j in range(0, 4):
      temp_board[i][j] = gboard[i][j]
      
def brute_move(): 
  def shiftup():
    for j in range(0,4):
      if temp_board[1][j] != 0:
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
          else:
            temp_board[0][j] = temp_board[1][j]*2
            temp_board[1][j] = temp_board[2][j]
            temp_board[2][j] = temp_board[3][j]
            temp_board[3][j] = 0
        
        if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
          temp_board[1][j] = temp_board[2][j]*2
          temp_board[2][j] = temp_board[3][j]
          temp_board[3][j] = 0
                   
        if temp_board[3][j] != 0 and temp_board[2][j] == temp_board[3][j]:
          temp_board[3][j] = temp_board[2][j]*2
          temp_board[3][j] = 0
  def shiftdown():
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
        else:
          temp_board[3][j] = temp_board[2][j]*2
          temp_board[2][j] = temp_board[1][j]
          temp_board[1][j] = temp_board[0][j]
          temp_board[0][j] = 0
          
      if temp_board[2][j] != 0 and temp_board[2][j] == temp_board[1][j]:
        temp_board[2][j] = temp_board[1][j]*2
        temp_board[1][j] = temp_board[0][j]
        temp_board[0][j] = 0
      
      if temp_board[1][j] != 0 and temp_board[1][j] == temp_board[0][j]:
        temp_board[1][j] = temp_board[0][j]*2
        temp_board[0][j] = 0 
  def shiftleft():
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
        else:
          temp_board[i][0] = temp_board[i][1]*2
          temp_board[i][1] = temp_board[i][2] 
          temp_board[i][2] = temp_board[i][3]
          temp_board[i][3] = 0
        
      if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
        temp_board[i][1] = temp_board[i][2]*2
        temp_board[i][2] = temp_board[i][3]
        temp_board[i][3] = 0
        
      if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
        temp_board[i][2] = temp_board[i][3]*2
        temp_board[i][3] = 0 
  def shiftright():
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
          temp_board[i][3] = temp_board[i][1]*2
          temp_board[i][2] = temp_board[i][1]*2
          temp_board[i][1] = 0
          temp_board[i][0] = 0
        else:
          temp_board[i][3] = temp_board[i][2]*2
          temp_board[i][2] = temp_board[i][1]
          temp_board[i][1] = temp_board[i][0]
          temp_board[i][0] = 0
        
      if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
        temp_board[i][2] = temp_board[i][1]*2
        temp_board[i][1] = temp_board[i][0]
        temp_board[i][0] = 0
            
      if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
        temp_board[i][1] = temp_board[i][0]*2
        temp_board[i][0] = 0 

  u_moves = 0
  d_moves = 0
  l_moves = 0
  r_moves = 0

  u_tree_moves1 = 0
  u_tree_moves2 = 0
  u_tree_moves3 = 0
  u_tree_moves4 = 0

  d_tree_moves1 = 0
  d_tree_moves2 = 0
  d_tree_moves3 = 0
  d_tree_moves4 = 0

  l_tree_moves1 = 0
  l_tree_moves2 = 0
  l_tree_moves3 = 0
  l_tree_moves4 = 0

  r_tree_moves1 = 0
  r_tree_moves2 = 0
  r_tree_moves3 = 0
  r_tree_moves4 = 0

  u_tree_moves = []
  d_tree_moves = []
  l_tree_moves = []
  r_tree_moves = []

  for k in range(0, 5): 
    combine()
    
    if k == 1:
      shiftup()
    if k == 2:
      shiftdown()
    if k == 3:
      shiftleft()
    if k == 4:
      shiftright()
   
    temp_board2 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    temp_board2 = temp_board

    #shift up with points
    for j in range(0, 4):
      if temp_board2[1][j]  != 0 and temp_board2[0][j] == 0:
        temp_board2[0][j] = temp_board2[1][j]
        temp_board2[1][j] = 0
         
      if temp_board2[2][j] != 0 and temp_board2[1][j] == 0:
        temp_board2[1][j] = temp_board2[2][j]
        temp_board2[2][j] = 0
        if temp_board2[0][j] == 0:
          temp_board2[0][j] = temp_board2[1][j]
          temp_board2[1][j] = 0
      
      if temp_board2[3][j] != 0 and temp_board2[2][j] == 0:
        temp_board2[2][j] = temp_board2[3][j]
        temp_board2[3][j] = 0
        if temp_board2[1][j] == 0:
          temp_board2[1][j] = temp_board2[2][j]
          temp_board2[2][j] = 0
          if temp_board2[0][j] == 0:
            temp_board2[0][j] = temp_board2[1][j]
            temp_board2[1][j] = 0
                 
      if temp_board2[0][j] != 0 and temp_board2[0][j] == temp_board2[1][j]:
        if temp_board2[2][j] == temp_board2[3][j]:
          if k == 0:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]*2
            temp_board2[2][j] = 0
            temp_board2[3][j] = 0
            u_moves += temp_board2[1][j] + temp_board2[0][j] 
          if k == 1:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]*2
            temp_board2[2][j] = 0
            temp_board2[3][j] = 0
            u_tree_moves1 += temp_board2[1][j] + temp_board2[0][j] 
          if k == 2:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]*2
            temp_board2[2][j] = 0
            temp_board2[3][j] = 0
            u_tree_moves2 += temp_board2[1][j] + temp_board2[0][j] 
          if k == 3:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]*2
            temp_board2[2][j] = 0
            temp_board2[3][j] = 0
            u_tree_moves3 += temp_board2[1][j] + temp_board2[0][j] 

          if k == 4:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]*2
            temp_board2[2][j] = 0
            temp_board2[3][j] = 0 
            u_tree_moves4 += temp_board2[1][j] + temp_board2[0][j] 
        else:
          if k == 0:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]
            temp_board2[2][j] = temp_board2[3][j]
            temp_board2[3][j] = 0
            u_moves += temp_board2[0][j] 
          if k == 1:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]
            temp_board2[2][j] = temp_board2[3][j]
            temp_board2[3][j] = 0
            u_tree_moves1 += temp_board2[0][j] 
          if k == 2:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]
            temp_board2[2][j] = temp_board2[3][j]
            temp_board2[3][j] = 0
            u_tree_moves2 += temp_board2[0][j] 
          if k == 3:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]
            temp_board2[2][j] = temp_board2[3][j]
            temp_board2[3][j] = 0
            u_tree_moves3 += temp_board2[0][j] 
          if k == 4:
            temp_board2[0][j] = temp_board2[1][j]*2
            temp_board2[1][j] = temp_board2[2][j]
            temp_board2[2][j] = temp_board2[3][j]
            temp_board2[3][j] = 0
            u_tree_moves4 += temp_board2[0][j] 

      if temp_board2[2][j] != 0 and temp_board2[2][j] == temp_board2[1][j]:
        if k == 0:
          temp_board2[1][j] = temp_board2[2][j]*2
          temp_board2[2][j] = temp_board2[3][j]
          temp_board2[3][j] = 0
          u_moves += temp_board2[1][j] 
        if k == 1:
          temp_board2[1][j] = temp_board2[2][j]*2
          temp_board2[2][j] = temp_board2[3][j]
          temp_board2[3][j] = 0
          u_tree_moves1 += temp_board2[1][j]  
        if k == 2:
          temp_board2[1][j] = temp_board2[2][j]*2
          temp_board2[2][j] = temp_board2[3][j]
          temp_board2[3][j] = 0
          u_tree_moves2 += temp_board2[1][j] 
        if k == 3:
          temp_board2[1][j] = temp_board2[2][j]*2
          temp_board2[2][j] = temp_board2[3][j]
          temp_board2[3][j] = 0
          u_tree_moves3 += temp_board2[1][j] 
        if k == 4:
          temp_board2[1][j] = temp_board2[2][j]*2
          temp_board2[2][j] = temp_board2[3][j]
          temp_board2[3][j] = 0
          u_tree_moves4 += temp_board2[1][j] 

      if temp_board2[3][j] != 0 and temp_board2[2][j] == temp_board2[3][j]:
        if k == 0:
          temp_board2[3][j] = temp_board2[2][j]*2
          temp_board2[3][j] = 0
          u_moves += temp_board2[3][j] 
        if k == 1:
          temp_board2[3][j] = temp_board2[2][j]*2
          temp_board2[3][j] = 0
          u_tree_moves1 += temp_board2[3][j]
        if k == 2:
          temp_board2[3][j] = temp_board2[2][j]*2
          temp_board2[3][j] = 0
          u_tree_moves2 += temp_board2[3][j]
        if k == 3:
          temp_board2[3][j] = temp_board2[2][j]*2
          temp_board2[3][j] = 0
          u_tree_moves3 += temp_board2[3][j] 
        if k == 4:
          temp_board2[3][j] = temp_board2[2][j]*2
          temp_board2[3][j] = 0
          u_tree_moves4 += temp_board2[3][j]

    if gboard == temp_board2:
      if k == 0:
        u_moves += -100000
      if k == 1:
        u_tree_moves1 += -100000
      if k == 2:
        u_tree_moves2 += -100000
      if k == 3:
        u_tree_moves3 += -100000
      if k == 4:
        u_tree_moves4 += -100000

    if max(max(temp_board2)) == temp_board2[3][3]:
      if k == 0:
        u_moves += 100
      if k == 1:
        u_tree_moves1 += 100
      if k == 2:
        u_tree_moves2 += 100
      if k == 3:
        u_tree_moves3 += 100
      if k == 4:
        u_tree_moves4 += 100 

    if k == 4:
      u_tree_moves.append(u_tree_moves1)
      u_tree_moves.append(u_tree_moves2)
      u_tree_moves.append(u_tree_moves3)
      u_tree_moves.append(u_tree_moves4)
      u_moves += max(u_tree_moves)     

    combine()
    
    if k == 1:
      shiftup()
    if k == 2:
      shiftdown()
    if k == 3:
      shiftleft()
    if k == 4:
      shiftright()

    temp_board2 = [[0 for x in range(w)] for y in range(h)] 
    temp_board2 = temp_board   
    #shift down with points
    for j in range(0, 4):
      if temp_board2[2][j] != 0 and temp_board2[3][j] == 0:
        temp_board2[3][j] = temp_board2[2][j]
        temp_board2[2][j] = 0
      
      if temp_board2[1][j] != 0:
        if temp_board2[2][j] == 0:
          temp_board2[2][j] = temp_board2[1][j]
          temp_board2[1][j] = 0
          if temp_board2[3][j] == 0:
            temp_board2[3][j] = temp_board2[2][j]
            temp_board2[2][j] = 0

      if temp_board2[0][j] != 0 and temp_board2[1][j] == 0:
        temp_board2[1][j] = temp_board2[0][j]
        temp_board2[0][j] = 0
        if temp_board2[2][j] == 0:
          temp_board2[2][j] = temp_board2[1][j]
          temp_board2[1][j] = 0
          if temp_board2[3][j] == 0:
            temp_board2[3][j] = temp_board2[2][j]
            temp_board2[2][j] = 0
       
      if temp_board2[3][j] != 0 and temp_board2[3][j] == temp_board2[2][j]:
        if temp_board2[0][j] == temp_board2[1][j]:
          if k == 0:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]*2
            temp_board2[1][j] = 0
            temp_board2[0][j] = 0
            d_moves += temp_board2[3][j] + temp_board2[2][j] 
          if k == 1:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]*2
            temp_board2[1][j] = 0
            temp_board2[0][j] = 0
            d_tree_moves1 += temp_board2[3][j] + temp_board2[2][j] 
          if k == 2:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]*2
            temp_board2[1][j] = 0
            temp_board2[0][j] = 0
            d_tree_moves2 += temp_board2[3][j] + temp_board2[2][j]  
          if k == 3:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]*2
            temp_board2[1][j] = 0
            temp_board2[0][j] = 0
            d_tree_moves3 += temp_board2[3][j] + temp_board2[2][j]  
          if k == 4:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]*2
            temp_board2[1][j] = 0
            temp_board2[0][j] = 0
            d_tree_moves4 += temp_board2[3][j] + temp_board2[2][j] 
        else:
          if k == 0:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]
            temp_board2[1][j] = temp_board2[0][j]
            temp_board2[0][j] = 0
            d_moves += temp_board2[3][j] 
          if k == 1:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]
            temp_board2[1][j] = temp_board2[0][j]
            temp_board2[0][j] = 0
            d_tree_moves1 += temp_board2[3][j]  
          if k == 2:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]
            temp_board2[1][j] = temp_board2[0][j]
            temp_board2[0][j] = 0 
            d_tree_moves2 += temp_board2[3][j] 
          if k == 3:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]
            temp_board2[1][j] = temp_board2[0][j]
            temp_board2[0][j] = 0
            d_tree_moves3 += temp_board2[3][j] 
          if k == 4:
            temp_board2[3][j] = temp_board2[2][j]*2
            temp_board2[2][j] = temp_board2[1][j]
            temp_board2[1][j] = temp_board2[0][j]
            temp_board2[0][j] = 0
            d_tree_moves4 += temp_board2[3][j] 

      if temp_board2[2][j] != 0 and temp_board2[2][j] == temp_board2[1][j]:
        if k == 0:
          temp_board2[2][j] = temp_board2[1][j]*2
          temp_board2[1][j] = temp_board2[0][j]
          temp_board2[0][j] = 0
          d_moves += temp_board2[2][j]
        if k == 1:
          temp_board2[2][j] = temp_board2[1][j]*2
          temp_board2[1][j] = temp_board2[0][j]
          temp_board2[0][j] = 0
          d_tree_moves1 += temp_board2[2][j] 
        if k == 2:
          temp_board2[2][j] = temp_board2[1][j]*2
          temp_board2[1][j] = temp_board2[0][j]
          temp_board2[0][j] = 0
          d_tree_moves2 += temp_board2[2][j] 
        if k == 3:
          temp_board2[2][j] = temp_board2[1][j]*2
          temp_board2[1][j] = temp_board2[0][j]
          temp_board2[0][j] = 0
          d_tree_moves3 += temp_board2[2][j]   
        if k == 4:
          temp_board2[2][j] = temp_board2[1][j]*2
          temp_board2[1][j] = temp_board2[0][j]
          temp_board2[0][j] = 0
          d_tree_moves4 += temp_board2[2][j]
      if temp_board2[1][j] != 0 and temp_board2[1][j] == temp_board2[0][j]:
        if k == 0:
          temp_board2[1][j] = temp_board2[0][j]*2
          temp_board2[0][j] = 0
          d_moves += temp_board2[1][j] 
        if k == 1:
          temp_board2[1][j] = temp_board2[0][j]*2
          temp_board2[0][j] = 0
          d_tree_moves1 += temp_board2[1][j] 
        if k == 2:
          temp_board2[1][j] = temp_board2[0][j]*2
          temp_board2[0][j] = 0
          d_tree_moves2 += temp_board2[1][j] 
        if k == 3:
          temp_board2[1][j] = temp_board2[0][j]*2
          temp_board2[0][j] = 0
          d_tree_moves3 += temp_board2[1][j] 
        if k == 4:
          temp_board2[1][j] = temp_board2[0][j]*2
          temp_board2[0][j] = 0
          d_tree_moves4 += temp_board2[1][j] 

    if gboard == temp_board2:
      if k == 0:
        d_moves += -100000
      if k == 1:
        d_tree_moves1 += -100000
      if k == 2:
        d_tree_moves2 += -100000
      if k == 3:
        d_tree_moves3 += -100000
      if k == 4:
        d_tree_moves4 += -100000 

    if max(max(temp_board2)) == temp_board2[3][3]:
      if k == 0:
        d_moves += 100
      if k == 1:
        d_tree_moves1 += 100
      if k == 2:
        d_tree_moves2 += 100
      if k == 3:
        d_tree_moves3 += 100
      if k == 4:
        d_tree_moves4 += 100 

    if k == 4:
      d_tree_moves.append(d_tree_moves1)
      d_tree_moves.append(d_tree_moves2)
      d_tree_moves.append(d_tree_moves3)
      d_tree_moves.append(d_tree_moves4)
      d_moves += max(d_tree_moves)

    combine()

    if k == 1:
      shiftup()
    if k == 2:
      shiftdown()
    if k == 3:
      shiftleft()
    if k == 4:
      shiftright()
    
    temp_board2 = [[0 for x in range(w)] for y in range(h)] 
    temp_board2 = temp_board
    #shift left
    for i in range(0, 4):
      if temp_board2[i][1] != 0 and temp_board2[i][0] == 0:
        temp_board2[i][0] = temp_board2[i][1]
        temp_board2[i][1] = 0
      
      if temp_board2[i][2] != 0 and temp_board2[i][1] == 0:
        temp_board2[i][1] = temp_board2[i][2]
        temp_board2[i][2] = 0
        if temp_board2[i][0] == 0:
          temp_board2[i][0] = temp_board2[i][1]
          temp_board2[i][1] = 0
      
      if temp_board2[i][3] != 0 and temp_board[i][2] == 0:
        temp_board2[i][2] = temp_board[i][3]
        temp_board2[i][3] = 0
        if temp_board2[i][1] == 0:
          temp_board2[i][1] = temp_board2[i][2]
          temp_board2[i][2] = 0
          if temp_board2[i][0] == 0:
            temp_board2[i][0] = temp_board2[i][1]
            temp_board2[i][1] = 0
 
      if temp_board2[i][0] != 0 and temp_board2[i][0] == temp_board2[i][1]:
        if temp_board2[i][2] == temp_board2[i][3]:
          if k == 0:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2]*2
            temp_board2[i][2] = 0
            temp_board2[i][3] = 0
            l_moves += temp_board2[i][0] + temp_board2[i][1] 
          if k == 1:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2]*2
            temp_board2[i][2] = 0
            temp_board2[i][3] = 0
            l_tree_moves1 += temp_board2[i][0] + temp_board2[i][1] 
          if k == 2:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2]*2
            temp_board2[i][2] = 0
            temp_board2[i][3] = 0
            l_tree_moves2 += temp_board2[i][0] + temp_board2[i][1]  
          if k == 3:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2]*2
            temp_board2[i][2] = 0
            temp_board2[i][3] = 0
            l_tree_moves3 += temp_board2[i][0] + temp_board2[i][1] 
          if k == 4:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2]*2
            temp_board2[i][2] = 0
            temp_board2[i][3] = 0
            l_tree_moves4 += temp_board2[i][0] + temp_board2[i][1] 
        else:        
          if k == 0:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2] 
            temp_board2[i][2] = temp_board2[i][3]
            temp_board2[i][3] = 0
            l_moves += temp_board2[i][0] 
          if k == 1:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2] 
            temp_board2[i][2] = temp_board2[i][3]
            temp_board2[i][3] = 0
            l_tree_moves1 += temp_board2[i][0] 
          if k == 2:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2] 
            temp_board2[i][2] = temp_board2[i][3]
            temp_board2[i][3] = 0
            l_tree_moves2 += temp_board2[i][0]   
          if k == 3:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2] 
            temp_board2[i][2] = temp_board2[i][3]
            temp_board2[i][3] = 0
            l_tree_moves3 += temp_board2[i][0] 
          if k == 4:
            temp_board2[i][0] = temp_board2[i][1]*2
            temp_board2[i][1] = temp_board2[i][2] 
            temp_board2[i][2] = temp_board2[i][3]
            temp_board2[i][3] = 0
            l_tree_moves4 += temp_board2[i][0] 

      if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][2] :
        if k == 0:
          temp_board2[i][1] = temp_board2[i][2]*2
          temp_board2[i][2] = temp_board2[i][3]
          temp_board2[i][3] = 0
          l_moves += temp_board2[i][1] 
        if k == 1:
          temp_board2[i][1] = temp_board2[i][2]*2
          temp_board2[i][2] = temp_board2[i][3]
          temp_board2[i][3] = 0
          l_tree_moves1 += temp_board2[i][1] 
        if k == 2:
          temp_board2[i][1] = temp_board2[i][2]*2
          temp_board2[i][2] = temp_board2[i][3]
          temp_board2[i][3] = 0
          l_tree_moves2 += temp_board2[i][1]
        if k == 3:
          temp_board2[i][1] = temp_board2[i][2]*2
          temp_board2[i][2] = temp_board2[i][3]
          temp_board2[i][3] = 0
          l_tree_moves3 = temp_board2[i][1] 
        if k == 4:
          temp_board2[i][1] = temp_board2[i][2]*2
          temp_board2[i][2] = temp_board2[i][3]
          temp_board2[i][3] = 0
          l_tree_moves4 += temp_board2[i][1] 

      if temp_board[i][3] != 0 and temp_board[i][2] == temp_board[i][3]:
        if k == 0:
          temp_board2[i][2] = temp_board2[i][3]*2
          temp_board2[i][3] = 0
          l_moves += temp_board2[i][2]
        if k == 1:
          temp_board2[i][2] = temp_board2[i][3]*2
          temp_board2[i][3] = 0
          l_tree_moves1 += temp_board2[i][2]  
        if k == 2:
          temp_board2[i][2] = temp_board2[i][3]*2
          temp_board2[i][3] = 0
          l_tree_moves2 += temp_board2[i][2] 
        if k == 3:
          temp_board2[i][2] = temp_board2[i][3]*2
          temp_board2[i][3] = 0
          l_tree_moves3 += temp_board2[i][2] 
        if k == 4:
          temp_board2[i][2] = temp_board2[i][3]*2
          temp_board2[i][3] = 0
          l_tree_moves4 += temp_board2[i][2]
          
    if gboard == temp_board2:
      if k == 0:
        l_moves += -100000
      if k == 1:
        l_tree_moves1 += -100000
      if k == 2:
        l_tree_moves2 += -100000
      if k == 3:
        l_tree_moves3 += -100000
      if k == 4:
        l_tree_moves4 += -100000

    if max(max(temp_board2)) == temp_board2[3][3]:
      if k == 0:
        l_moves += 100
      if k == 1:
        l_tree_moves1 += 100
      if k == 2:
        l_tree_moves2 += 100
      if k == 3:
        l_tree_moves3 += 100
      if k == 4:
        l_tree_moves4 += 100 
     
    if k == 4:
      l_tree_moves.append(l_tree_moves1)
      l_tree_moves.append(l_tree_moves2)
      l_tree_moves.append(l_tree_moves3)
      l_tree_moves.append(l_tree_moves4)
      l_moves += max(l_tree_moves)

    combine()    

    if k == 1:
      shiftup()
    if k == 2:
      shiftdown()
    if k == 3:
      shiftleft()
    if k == 4:
      shiftright()

    temp_board2 = [[0 for x in range(w)] for y in range(h)]    
    temp_board2 = temp_board
    r_tree_moves = []
    #shift right with points
    for i in range(0, 4):
      if temp_board2[i][2] != 0 and temp_board2[i][3] == 0:
        temp_board2[i][3] = temp_board2[i][2]
        temp_board2[i][2] = 0
      
      if temp_board2[i][1] != 0 and temp_board2[i][2] == 0:
        temp_board2[i][2] = temp_board2[i][1]
        temp_board2[i][1] = 0
        if temp_board2[i][3] == 0:
          temp_board2[i][3] = temp_board2[i][2]
          temp_board2[i][2] = 0
      
      if temp_board2[i][0] != 0 and temp_board[i][1] == 0:
        temp_board2[i][1] = temp_board[i][0]
        temp_board2[i][0] = 0
        if temp_board2[i][2] == 0:
          temp_board2[i][2] = temp_board2[i][1]
          temp_board2[i][1] = 0
          if temp_board2[i][3] == 0:
            temp_board2[i][3] = temp_board2[i][2]
            temp_board2[i][2] = 0
 
      if temp_board2[i][3] != 0 and temp_board2[i][3] == temp_board2[i][2]:
        if temp_board2[i][1] == temp_board2[i][0]:
          if k == 0:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1]*2
            temp_board2[i][1] = 0
            temp_board2[i][0] = 0
            r_moves += temp_board2[i][3] + temp_board2[i][2] 
          if k == 1:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1]*2
            temp_board2[i][1] = 0
            temp_board2[i][0] = 0
            r_tree_moves1 = temp_board2[i][3] + temp_board2[i][2] 
          if k == 2:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1]*2
            temp_board2[i][1] = 0
            temp_board2[i][0] = 0
            r_tree_moves2 = temp_board2[i][3] + temp_board2[i][2]  
          if k == 3:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1]*2
            temp_board2[i][1] = 0
            temp_board2[i][0] = 0
            r_tree_moves3 = temp_board2[i][3] + temp_board2[i][2]
          if k == 4:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1]*2
            temp_board2[i][1] = 0
            temp_board2[i][0] = 0
            r_tree_moves4 += temp_board2[i][3] + temp_board2[i][2] 
        else:        
          if k == 0:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1] 
            temp_board2[i][1] = temp_board2[i][0]
            temp_board2[i][0] = 0
            r_moves += temp_board2[i][3] 
          if k == 1:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1] 
            temp_board2[i][1] = temp_board2[i][0]
            temp_board2[i][0] = 0
            r_tree_moves1 += temp_board2[i][3] 
          if k == 2:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1] 
            temp_board2[i][1] = temp_board2[i][0]
            temp_board2[i][0] = 0
            r_tree_moves2 += temp_board2[i][3]   
          if k == 3:
            temp_board2[i][3] = temp_board2[i][2]
            temp_board2[i][2] = temp_board2[i][1] 
            temp_board2[i][1] = temp_board2[i][0]
            temp_board2[i][0] = 0
            r_tree_moves3 += temp_board2[i][3] 
          if k == 4:
            temp_board2[i][3] = temp_board2[i][2]*2
            temp_board2[i][2] = temp_board2[i][1] 
            temp_board2[i][1] = temp_board2[i][0]
            temp_board2[i][0] = 0
            r_tree_moves4 += temp_board2[i][3] 

      if temp_board[i][2] != 0 and temp_board[i][2] == temp_board[i][1]:
        if k == 0:
          temp_board[i][2] = temp_board[i][1]*2
          temp_board[i][1] = temp_board[i][0]
          temp_board[i][0] = 0
          r_moves += temp_board2[i][2] 
        if k == 1:
          temp_board[i][2] = temp_board[i][1]*2
          temp_board[i][1] = temp_board[i][0]
          temp_board[i][0] = 0 
          r_tree_moves1 += temp_board2[i][2] 
        if k == 2:
          temp_board2[i][2] = temp_board2[i][1]*2
          temp_board2[i][1] = temp_board2[i][0]
          temp_board2[i][0] = 0
          r_tree_moves2 += temp_board2[i][2]
        if k == 3:
          temp_board2[i][2] = temp_board2[i][1]*2
          temp_board2[i][1] = temp_board2[i][0]
          temp_board2[i][0] = 0
          r_tree_moves3 = temp_board2[i][2] 
        if k == 4:
          temp_board2[i][2] = temp_board2[i][1]*2
          temp_board2[i][1] = temp_board2[i][0]
          temp_board2[i][0] = 0
          r_tree_moves4 += temp_board2[i][2] 

      if temp_board[i][1] != 0 and temp_board[i][1] == temp_board[i][0]:
        if k == 0:
          temp_board2[i][1] = temp_board2[i][1]*2
          temp_board2[i][0] = 0
          r_moves += temp_board2[i][1]
        if k == 1:
          temp_board2[i][1] = temp_board2[i][0]*2
          temp_board2[i][0] = 0
          r_tree_moves1 += temp_board2[i][1]  
        if k == 2:
          temp_board2[i][1] = temp_board2[i][0]*2
          temp_board2[i][0] = 0
          r_tree_moves2 += temp_board2[i][1] 
        if k == 3:
          temp_board2[i][1] = temp_board2[i][0]*2
          temp_board2[i][0] = 0
          r_tree_moves3 += temp_board2[i][1] 
        if k == 4:
          temp_board[i][1] = temp_board[i][0]*2
          temp_board[i][0] = 0  
          r_tree_moves4 += temp_board2[i][1] 
          
    if gboard == temp_board2:
      if k == 0:
        r_moves += -100000
      if k == 1:
        r_tree_moves1 += -100000
      if k == 2:
        r_tree_moves2 += -100000
      if k == 3:
        r_tree_moves3 += -100000
      if k == 4:
        r_tree_moves4 += -100000

    if max(max(temp_board2)) == temp_board2[3][3]:
      if k == 0:
        r_moves += 100
      if k == 1:
        r_tree_moves1 += 100
      if k == 2:
        r_tree_moves2 += 100
      if k == 3:
        r_tree_moves3 += 100
      if k == 4:
        r_tree_moves4 += 100 

    if k == 4:
      r_tree_moves.append(r_tree_moves1)
      r_tree_moves.append(r_tree_moves2)
      r_tree_moves.append(r_tree_moves3)
      r_tree_moves.append(r_tree_moves4)
      r_moves += max(r_tree_moves)
        
    combine()
  
  print(u_moves)
   
  print(d_moves)
  
  print(l_moves)
  
  print(r_moves)
  #fix the problem 

  if u_moves > d_moves and u_moves > l_moves and u_moves > r_moves:
    pyautogui.press('up')
    print('board is moving up')
  if d_moves > u_moves and d_moves > l_moves and d_moves > r_moves:
    pyautogui.press('down')
    print('board is moving down')
  if l_moves > u_moves and l_moves > d_moves and l_moves > r_moves:
    pyautogui.press('left')
    print('board is moving left')
  if r_moves > u_moves and r_moves > d_moves and r_moves > l_moves:
    pyautogui.press('right')
    print('board is moving right')
  if r_moves == u_moves and r_moves == d_moves and r_moves == l_moves:
    pyautogui.press('right')
    print('board is moving right')
  if d_moves == r_moves and d_moves > l_moves and d_moves > u_moves:
    pyautogui.press('right')
    print('board is moving right')
  if d_moves == u_moves and d_moves > l_moves and d_moves > r_moves:
    pyautogui.press('down')
    print('board is moving down')
  if r_moves == d_moves and r_moves == l_moves and r_moves == u_moves:
    pyautogui.press('right')
    print('board is moving right')
  if u_moves == l_moves and l_moves > d_moves and l_moves > r_moves:
    pyautogui.press('left')
    print('board is moving left')
  if r_moves > u_moves and r_moves == d_moves and r_moves == l_moves:
    pyautogui.press('right')
    print('board is moving right')
  if r_moves == l_moves and r_moves > u_moves and r_moves > d_moves:
    pyautogui.press('right')
    print('board is moving right')
  if d_moves == l_moves and l_moves > u_moves and l_moves > r_moves:
    pyautogui.press('down')
    print('board is moving down')
  if r_moves == d_moves and r_moves == u_moves and r_moves > l_moves:
    pyautogui.prees('right')
    print('board is moving right')

count = 0
while True:
  count += 1
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
  if count == 1:
    time.sleep(1) 
    pyautogui.press('right')
  if count == 2:
    time.sleep(1)
    pyautogui.press('down')
  if count > 2:
    brute_move()
    time.sleep(1)

