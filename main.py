from tkinter import *
from TicTacToe import TTT
window=Tk()
window.title("Tic-Tac-Toe")
window.config(padx=100,pady=100)

board=TTT()
board.create_board()

window.mainloop()
