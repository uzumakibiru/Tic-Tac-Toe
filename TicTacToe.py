from tkinter import *
from tkinter import messagebox

class TTT:
    def __init__(self):
       self.board=["" for _ in range(9)]
       self.buttons=[]
       self.player=""

# Function to create a board in the window
    def create_board(self):
        
        for i in range(9):
            row,col=divmod(i,3)
            self.button=Button(text="",width=10,height=5,command=lambda idx=i:self.on_click(idx))
            self.button.grid(row=row,column=col)
            self.buttons.append(self.button)
# Function that handle the button input that will be either X or O  
    def on_click(self,index):
        if self.board[index]=="":
            self.buttons[index].config(text=self.current_player(index))
            self.check_winner()

            
    
# Function to track the player . It can be made with two line code too.          
    def current_player(self,index=None):
        if index is not None:
            if self.board.count("")==9:
                self.player="X"
                self.board[index]=self.player
                
            elif self.board.count("X")>self.board.count("O"):
                self.player="O"
                self.board[index]=self.player
            else:
                self.player="X"  
                self.board[index]=self.player 
            
            return self.player     
#Function that will check the index of the board list for the winner selection.         
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for i in winning_combinations:
            x=0
            o=0
            for item in i:
                if self.board.count("")==0: 
                    messagebox.showinfo(title="Draw",message="No Chicken Dinner")
                    self.reset()
        
                if self.board[item]=="X":
                    x+=1
                    if x==3:
                        messagebox.showinfo(title="Winner",message="X is The Winner")
                        self.reset()
                if self.board[item]=="O":
                    o+=1
                    if o==3:
                        messagebox.showinfo(title="Winner",message="O is the winner.")
                        self.reset()
                
                    
                
    def reset(self):
        
        self.board=["" for _ in range(9)]
        for button in self.buttons:
            button.config(text="")



                   
                