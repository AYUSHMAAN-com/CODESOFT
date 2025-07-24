import tkinter as tk
from tkinter import messagebox

# Your original code starts here (unchanged)
class Board():
    def __init__(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print("%s | %s | %s" %(self.cells[1],self.cells[2],self.cells[3]))
        print("----------")
        print("%s | %s | %s" %(self.cells[4],self.cells[5],self.cells[6]))
        print("----------")
        print("%s | %s | %s" %(self.cells[7],self.cells[8],self.cells[9]))

    def update_cell(self,cell_no,player):
        if self.cells[cell_no] ==" ":
            self.cells[cell_no]=player

    def is_winner(self,player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True
        if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            return True
        if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            return True
        if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            return True
        return False

    def is_tie(self):
        used_cells=0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        return False 
    def available_moves(self):
        return [i for i in range(1, 10) if self.cells[i] == " "]

    def minimax(self, is_maximizing):
        if self.is_winner("O"):
            return 1
        if self.is_winner("X"):
            return -1
        if self.is_tie():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for move in self.available_moves():
                self.cells[move] = "O"
                score = self.minimax(False)
                self.cells[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in self.available_moves():
                self.cells[move] = "X"
                score = self.minimax(True)
                self.cells[move] = " "
                best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -float("inf")
        best_move = None
        for move in self.available_moves():
            self.cells[move] = "O"
            score = self.minimax(False)
            self.cells[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        if best_move:
            self.update_cell(best_move, "O")

    def reset(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "]

board=Board()
# Your original code ends here

# GUI starts here
class GUI:
    def __init__(self, root):
        self.root = root
        self.buttons = {}
        self.build_grid()

    def build_grid(self):
        for i in range(1, 10):
            btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=(i-1)//3, column=(i-1)%3)
            self.buttons[i] = btn

    def make_move(self, cell):
        if board.cells[cell] != " ":
            return
        board.update_cell(cell, "X")
        self.update_buttons()

        if board.is_winner("X"):
            messagebox.showinfo("Game Over", "Player X wins!")
            self.ask_restart()
            return
        if board.is_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.ask_restart()
            return

        board.ai_move()
        self.update_buttons()

        if board.is_winner("O"):
            messagebox.showinfo("Game Over", "Player O wins!")
            self.ask_restart()
        elif board.is_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.ask_restart()

    def update_buttons(self):
        for i in range(1, 10):
            self.buttons[i].config(text=board.cells[i])

    def ask_restart(self):
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            board.reset()
            self.update_buttons()
        else:
            self.root.quit()

# Launch GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe - Human vs AI")
    app = GUI(root)
    root.mainloop()


    

