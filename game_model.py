import random

class Board:

    board = [[0,0,0,0],
             [0,2,0,0],
             [0,2,0,4],
             [0,0,0,4]]

    score = 0
    high_score = 0
    starting_pieces = [2,4]

    def __init__(self):
        # put two random pieces around the board (either a 2 or 4)
        position_x_1, position_x_2 = random.sample(range(0, 4), 2)
        position_y_1, position_y_2 = random.sample(range(0, 4), 2)
        starting_piece_1, starting_piece_2 = random.choices(self.starting_pieces, k=2)
        
        self.board[position_x_1][position_y_1] = starting_piece_1
        self.board[position_x_2][position_y_2] = starting_piece_2

    def combine_like_pieces(self, direction):
        if direction == "LEFT":
            for i in range(len(self.board)):
                for j in range(len(self.board[i]-1)):
                    if self.board[i][j] == self.board[i][j+1]:
                        self.board[i][j] *= 2
                        self.board[i][j+1] = 0
        elif direction == "RIGHT":
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1,0,-1):
                    if self.board[i][j] == self.board[i][j-1]:
                        self.board[i][j] *= 2
                        self.board[i][j-1] = 0
        elif direction == "UP":
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1):
                    if self.board[j][i] == self.board[j+1][i]:
                        self.board[j][i] *= 2
                        self.board[j+1][i] = 0
        elif direction == "DOWN":
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1,0,-1):
                    if self.board[j][i] == self.board[j-1][i]:
                        self.board[j][i] *= 2
                        self.board[j-1][i] = 0

    def shift_piece_left(self, i, j):
        if (j == 0 or self.board[i][j-1] != 0):
            return
        else:
            self.board[i][j-1] = self.board[i][j]
            self.board[i][j] = 0
            self.shift_piece_left(i,j-1)

    def shift_all_left(self):
        self.combine_like_pieces(direction="LEFT")
        occupied_spots = []

        # add all spots that have numbers to list above
        for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] != 0:
                        occupied_spots.append((i,j))

        for i,j in occupied_spots:
            self.shift_piece_left(i,j)

    def shift_piece_right(self, i, j):
        if (j == len(self.board)-1 or self.board[i][j+1] != 0):
            return
        else:
            self.board[i][j+1] = self.board[i][j]
            self.board[i][j] = 0
            self.shift_piece_right(i,j+1)

    def shift_all_right(self):
        self.combine_like_pieces(direction="RIGHT")
        occupied_spots = []

        # add all spots that have numbers to list above
        for i in range(len(self.board)):
                for j in range(len(self.board[i])-1,-1,-1):
                    if self.board[i][j] != 0:
                        occupied_spots.append((i,j))

        for i,j in occupied_spots:
            self.shift_piece_right(i,j)

    def shift_piece_up(self, i, j):
        if (i == 0 or self.board[i-1][j] != 0):
            return
        else:
            self.board[i-1][j] = self.board[i][j]
            self.board[i][j] = 0
            self.shift_piece_up(i-1,j)

    def shift_all_up(self):
        self.combine_like_pieces(direction="UP")
        occupied_spots = []

        # add all spots that have numbers to list above
        for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[j][i] != 0:
                        occupied_spots.append((j,i))

        for i,j in occupied_spots:
            self.shift_piece_up(i,j)

    def shift_piece_down(self, i, j):
        if (i == len(self.board)-1 or self.board[i+1][j] != 0):
            return
        else:
            self.board[i+1][j] = self.board[i][j]
            self.board[i][j] = 0
            self.shift_piece_down(i+1,j)

    def shift_all_down(self):
        self.combine_like_pieces(direction="DOWN")
        occupied_spots = []

        # add all spots that have numbers to list above
        for i in range(len(self.board)):
                for j in range(len(self.board[i])-1,-1,-1):
                    if self.board[j][i] != 0:
                        occupied_spots.append((j,i))

        for i,j in occupied_spots:
            self.shift_piece_down(i,j)

    def generate_new_piece(self):
        if (not self.is_game_over()):
            available_spots = []

            # add all spots that contain a 0
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 0:
                        available_spots.append((i,j))

            # choose a random available spot and add a 2 or 4 in that spot
            random_spot = random.sample(available_spots)
            self.board[random_spot[0]][random_spot[1]] = random.sample(self.starting_pieces)
        else:
            # end game
            pass

    def is_game_over(self):
        return not any(0 in val for val in self.board)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0
        self.__init__()
        print("RESETTED GAME")
    
    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print()
        
        print(f"Score: {self.score}")
        print(f"High Score: {self.high_score}")