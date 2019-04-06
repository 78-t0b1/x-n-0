#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(baord):
    clear_output()
    print(baord[7]+'|'+baord[8]+'|'+baord[9])
    print(baord[4]+'|'+baord[5]+'|'+baord[6])
    print(baord[1]+'|'+baord[2]+'|'+baord[3])
    


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    '''OUTPUT IS IN FORM OF TUPLE ABOUT WHICH PLAYER CHOOSE WHICH X OR O '''
    
    marker =''
    
    while marker !='X' and marker != 'O':
        marker = input('Player1: choose X or O: ').upper()
        
    if marker =='X':
        
        return('X','O')
    else:
        return('O','X')
    
    
        


# In[4]:


def place_marker(board,marker,position):
    board[position]=marker
    


# In[ ]:


def win_check(board,mark):
    mark=mark.upper()
    return((board[7] == board[8] == board[9] == mark ) or
    (board[4] ==board[5] ==board[6] ==mark ) or
    (board[1] ==board[2] ==board[3] ==mark ) or
    (board[1] ==board[4] ==board[7] ==mark ) or
    (board[2] ==board[5] ==board[8] ==mark ) or
    (board[3] ==board[6] ==board[9] ==mark ) or
    (board[1] ==board[5] ==board[9] ==mark ) or
    (board[7] ==board[5] ==board[3] ==mark ) )

    
    
        


# In[ ]:


win_check(test_board,'x')


# In[ ]:


import random

def choose_first():
    
    flip=  random.randint(0,1)
    
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    


# In[ ]:


def space_check (board,position):
    return board[position] == ' '


# In[ ]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True


# In[ ]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int (input('choose a Position '))
        
    return position


# In[ ]:


def replay():
    
    choice = input ('Play again? Y/N ')
    
    choice = choice.upper()
    
    return choice == 'Y'


# In[ ]:


print ('Welcome to TIC TAC TOE!!!!!')

while True:
    #PLAY THE GAME
    
    ## SET UP EVERY THING
     
    the_board =[' ']*10
    turn= choose_first()
    print(turn+' will go first')
    player1_marker,player2_marker = player_input()
    
   
    gameon = True
    
    while gameon:
        if turn == 'Player 1':
            #Show the board
            display_board(the_board)
            #choose a position 
            position=player_choice(the_board)
            #Place marker on position 
            place_marker(the_board,player1_marker,position)
            #Check if they won
            if win_check(the_board,player1_marker) :
                display_board(the_board)
                print('Player 1 Won!!!!')
                gameon = False
                break
            # Or check there is a tie 
            else :
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print ('Its a tie!!!')
                    gameon = False
                    break
                 #No then next players turn
                else:
                    display_board(the_board)
                    turn = 'Player 2'





        else :
            #Show the board
            display_board(the_board)
            #choose a position 
            x=player_choice(the_board)
            #Place marker on position 
            place_marker(the_board,player2_marker,x)
            #Check if they won
            if win_check(the_board,player2_marker) == True:
                display_board(the_board)
                print('Player 2 Won!!!!')
                gameon = False
                break
            # Or check there is a tie 
            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)

                    print ('Its a tie!!!')
                    gameon = False
                    break
                 #No then next players turn
                else:
                    display_board(the_board)
                    turn = 'Player 1'
    
    
    if not replay():
        print ('See you soon... Have a good time')
        break
    # BREAK OUT OF THE WHILE LOOP i.e BREAK OUT OF THE GAME


# In[ ]:





# In[ ]:





# In[ ]:




