#!/usr/bin/env python
# coding:utf-8
#Philipp = ****
import random
random.seed()

Nothing=ord('.')
Player1=ord('O')
Player2=ord('X')
Player1has4='OOOO'
Player2has4='XXXX'
Player1Wins='human wins'
Player2Wins='computer wins'
Player2Take='computer takes '
DirectionHorizontal='horizontal' 
DirectionVertical  ='vertical'
DirectionDiagonal  ='diagonal'
ErrorMessage='Error on setting Column to '
RatingString='Rating :  '

# The play field , size: 7 Columns x 6 Rows
A=[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]
# How high a column is filled with stones. Heigth (Row) = 1..6
ColumnHeigth =[0,0,0,0,0,0,0]
# BestColumn is used for Rating the best computermoves
BestColumn   =[0,0,0,0,0,0,0]

def ClearA():                       # clear the play field wich is stored in array A , and also clear the column heigths
    for x in range(7):
        ColumnHeigth[x]=0
        for y in range(6):
            A[x][y]=Nothing
    return

def PrintA():                       # print the play field wich is stored in array A
    print('\n')
    for z in range(6):
        y=5-z                       # print order is upside down
        S=''
        for x in range(7):
            S=S+chr(A[x][y])+' '
        print('           '+S)
    print('           1 2 3 4 5 6 7')
    print('\n') 
    return

def IsColumnOK(Column):              # valid column 1..7 ?  and column is not full ?  than it is OK -> Result = True
    OK=False
    if Column>0:
       if Column<8:
          AboveRow=ColumnHeigth[Column-1]
          AboveRow+=1 
          if AboveRow<7:
             OK=True
    return OK

def SetAbove(Column,Value):          # drop the play stone in a column and increase column heigth ... Value : Player1 or Player2 
    OK=IsColumnOK(Column)
    if OK==True: 
       AboveRow=ColumnHeigth[Column-1]
       AboveRow+=1
       ColumnHeigth[Column-1]=AboveRow
       A[Column-1][AboveRow-1]=Value
    return OK

def IsColumnEmpty(Column):
    return ColumnHeigth[Column-1]==0

########################### Find 4 to check if someone has won ########################################

def Has4(String):                  #  find  'XXXX' or 'OOOO'  in a string
    Result=-1                      #  return Player1 or Player2 or -1 
    if Player1has4 in String:
       Result=Player1
    if Player2has4 in String:
       Result=Player2
    return Result

def Horizontal():                  #   make Array a 7 character string like 'O.XXXXO' to find 4 in one row
    Result=-1                      #   return Player1 or Player2 or -1
    for y in range(6):
        s=''
        for x in range(7):         
            s=s+chr(A[x][y])    
        Result=Has4(s)
        if Result>0:
           break
    return Result     

def Vertical():                    #   make Array a 6 character string like '.OOOOX' to find 4 in one column
    Result=-1                      #   return Player1 or Player2 or -1
    for x in range(7):
        s=''
        for y in range(6):        
            s=s+chr(A[x][y])     
        Result=Has4(s)
        if Result>0:
           break  
    return Result  

def Diagonal():                   #   make Array a 4 character string like 'XXXX' to find 4 diagonal
    Result=-1                     #   return Player1 or Player2 or -1      
    for x in range(4):           
        for y in range(3):
            s=chr(A[x][y])+chr(A[x+1][y+1])+chr(A[x+2][y+2])+chr(A[x+3][y+3]) # diagonal left downside to rigth upside
            Result=Has4(s)
            if Result>0:
               break
            s=chr(A[x][y+3])+chr(A[x+1][y+2])+chr(A[x+2][y+1])+chr(A[x+3][y]) # diagonal left upside to rigth downside
            Result=Has4(s)
            if Result>0:
               break
        if Result>0:
           break 
    return Result

def HasSomeoneWon():  # if one Players has won : return Player1 or Player2 , else return -1, and return Direction in wich he won
    Direction=0
    Winner=Horizontal()
    if Winner>0:
       Direction=DirectionHorizontal
    else:
         Winner=Vertical()
         if Winner>0:
            Direction=DirectionVertical 
         else:
              Winner=Diagonal()     
              if Winner>0:
                 Direction=DirectionDiagonal      
    return Winner , Direction

####################  HUMAN MOVE  ##################################################

def HumanMove():           # get and check input from the human in a terminal , return valid Column Number 1..7
    Column=0
    while IsColumnOK(Column)==False:
          S=str(input('1..7 : '))
          if S in ['1','2','3','4','5','6','7']:
             Column=int(S) 
    return Column  

#################### COMPUTER MOVE ################################################################

def RandomColumn():                   # get a random column wich is not already full
    Column=0
    if Moves>(7*6)-3:                 # at the first move take a column somewhere in the middle of the play field
       Empty=False                    # to not give human the chance to make somewhat like this :  X.OOO.X
       while Empty==False:
             Column=random.choice([3,4,5])
             Empty=IsColumnEmpty(Column) 
    else:                             # after the first moves take any column who is free  
       while IsColumnOK(Column)==False:
             Column=random.choice([1,2,3,4,5,6,7])
    return Column

def save(Deep):
    for x in range(7):                       # make a copy of playfield and column heigths to restore it later   
        DeepColumnHeigth[Deep,x]=ColumnHeigth[x]
        for y in range(6):
            DeepA[Deep,x,y]=A[x][y] 
    return

def restore(Deep):
    for x in range(7):                      # restore original playfield and column heigths   
        ColumnHeigth[x]=DeepColumnHeigth[Deep,x]
        for y in range(6):
            A[x][y]=DeepA[Deep,x,y]
    return

# Set temporary a playstone to check if the computer move will make him or the human win. Rate the move in BestColumn[]
def CheckWinAndIncBestColumn(move,column,Player):
    global ColumnOfMove1
    global ColumnOfMove2
    global ColumnOfMove3
    global ColumnOfMove4

    OK=SetAbove(column,Player)
    if OK==True: 
       [Winner,Direction]=HasSomeoneWon()

       if move==1:                               
          ColumnOfMove1=column
          if Winner==Player2:
             BestColumn[ColumnOfMove1-1]+=1000000  # Computer wins on first move ? that is the best Column he can ever get !
             return   
          if Winner==Player1:
             BestColumn[ColumnOfMove1-1]-=10000
      
       if move==2:                                   
          ColumnOfMove2=column                                  
          if Winner==Player1:
             if ColumnOfMove1!=ColumnOfMove2:
                BestColumn[ColumnOfMove2-1]+=10000 # Human wins on second move after computer has choosen an other column before
             if ColumnOfMove1==ColumnOfMove2:
                BestColumn[ColumnOfMove2-1]-=10000 # Human wins on second move after computer has choosen the same column before

       if move==3:                                
          ColumnOfMove3=column                   
          if Winner==Player1:                     
             BestColumn[ColumnOfMove1-1]-=100
          if Winner==Player2:                     
             BestColumn[ColumnOfMove1-1]+=100

       if move==4:                                
          ColumnOfMove4=column                   
          if Winner==Player1:                     
             BestColumn[ColumnOfMove1-1]-=1
          if Winner==Player2:                     
             BestColumn[ColumnOfMove1-1]+=1

       if move==2:                                 # Next move for Computer and then test again what Human can do...
             save(move)                            # make a copy of playfield to restore it later
             CheckAndRate(move)                    # Try out column 1..7 of Computer and then column 1..7 of Human
             restore(move)                         # restore original playfield afterwards

    #----- reset if Human -----
    if Player==Player1:                            # Human : restore his move after testing 
       Row=ColumnHeigth[column-1] 
       A[column-1][Row-1]=Nothing                  
       ColumnHeigth[column-1]=Row-1
    return

def CheckAndRate(move):
    # Begin with Player2 to move,let his playstone there till all combinations of Player1 afterwards has checked
    for Cp2 in range(7): 
        column2=Cp2+1
        CheckWinAndIncBestColumn(move+1,column2,Player2)     # Rating of the Computer move by checking someone has won
        for Cp1 in range(7):
            column1=Cp1+1                    
            CheckWinAndIncBestColumn(move+2,column1,Player1) # Rating of the Human move by checking someone has won
        restore(move)                                        # Computer : restore his move after testing 
    return

def ComputerMove():                          # **** let the computer calculate his move ****
    # Dictionarys for saving and restoring A 
    # and BestColumn while thinking Deep about 
    # a move to make
    global DeepA
    global DeepColumnHeigth   

    Column=RandomColumn()                    # Random move

    DeepA={}
    DeepColumnHeigth={}

    if Moves<=(7*6)-3:                       # if not the first move ...
       for x in range(7):                    # try to find the best Column,but first make an empty array for Rating                
           BestColumn[x]=0  
              
       save(0)                               # make a copy of playfield to restore it later
       CheckAndRate(0)                       # Try out move 1..7 of Player2 and then move 1..7 of Player1
       restore(0)                            # restore original playfield


       value=-10000000000
       s=RatingString
       for x in range(7):                    # the best Column was ...
           s=s+str(BestColumn[x])+' '           
           if IsColumnOK(x+1)==True:
              if BestColumn[x]>value:        # choose best column
                 value=BestColumn[x]
       #print(s) # rating

       SameRatings=[]                       # Same Ratings of Columns ... choose a Random Column out of same Ratings
       for x in range(7):
           if BestColumn[x]==value:          
              SameRatings.append(x+1)

       if SameRatings:
          trys=20
          while trys>0:
                trys-=1         
                Column=random.choice(SameRatings) 
                if IsColumnOK(Column)==True:
                   break

       if IsColumnOK(Column)==False:         # no choice ? take someting random
          Column=RandomColumn()

    return Column

########################  MAIN PROGRAM  #############################################

ClearA()                                 # Clear the play field Array
PrintA()
Player=random.choice([Player1,Player2])  # who of the Players will begin ?

Moves=7*6
while Moves>0:
      if Player==Player1:
         Column=HumanMove()
         OK=SetAbove(Column,Player1)     # set the play stone of human move
         if OK==False:
            print(ErrorMessage+str(Column))
         else: 
            Player=Player2
      else:
         Column=ComputerMove()
         OK=SetAbove(Column,Player2)        # set the play stone of computer move
         print(Player2Take+str(Column)) 
         if OK==False:
            print(ErrorMessage+str(Column))
         else: 
            Player=Player1
      PrintA()                           # print the playfield
      [Winner,Direction]=HasSomeoneWon()
      if Winner==Player1:                # someone is the winner ? --> print winner and exit the program
         print(Player1Wins+' , '+Direction)
         exit() 
      if Winner==Player2:
         print(Player2Wins+' , '+Direction)
         exit()               
      Moves-=1                           # exit the program when 42 moves are done, play field is full (Remis)

