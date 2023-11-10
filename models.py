from tkinter import messagebox
import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Хрестики-нолики")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_wins = {'X': 0, 'O': 0}

        # Створення кнопок для гри
        self.buttons = [[tk.Button(master, text=' ', font=('Helvetica', 24), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                         for col in range(3)] for row in range(3)]

        # Розміщення кнопок на формі
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        # Обробка кліку на кнопку
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.draw_winner_line()
                self.player_wins[self.current_player] += 1
                messagebox.showinfo("Гра закінчена", f"Гравець {self.current_player} переміг!\n"
                                                     f"Рахунок:\nГравець X:  - {self.player_wins['X']} "
                                                     f"\nГравець O: - {self.player_wins['O']}")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Гра закінчена", "Гра закінчилася в нічию!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        # Перевірка на перемогу
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        # Перевірка на нічию
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        # Зміна поточного гравця
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        # Скидання гри до початкового стану
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', bg='SystemButtonFace')  # Скидання кольору кнопок

    def draw_winner_line(self):
        # Малювання лінії переможця
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.draw_line((0, 0), (2, 2))
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.draw_line((0, 2), (2, 0))
        else:
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                    self.draw_line((i, 0), (i, 2))
                if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                    self.draw_line((0, i), (2, i))

    def draw_line(self, start, end):
        # Малювання лінії на кнопках гри
        start_row, start_col = start
        end_row, end_col = end
        for i in range(3):
            self.buttons[int(start_row)][int(start_col)].config(bg='red')
            start_row, start_col = start_row + (end_row - start_row) / 2, start_col + (end_col - start_col) / 2
        self.buttons[int(end_row)][int(end_col)].config(bg='red')
