from app.domain.entities import Game, Movement


class GameService:
    __game: Game
    __movement: Movement

    def __init__(self, game: Game):
        self.__game = game

    @property
    def get_game(self) -> Game:
        return self.__game

    def check_move_validity(self, movement: Movement) -> bool:
        self.__movement = movement
        if self.__game.board[self.__movement['row']][self.__movement['column']] != 0:
            return False
        return True

    def make_move(self) -> Game:
        self.__update_board()
        self.__update_movements()
        is_draw = self.__check_draw()
        is_winner = self.__check_win()
        if is_winner or is_draw:
            self.__declare_winner(is_draw)
        return self.__game

    def __update_board(self):
        if self.__game.board[self.__movement['row']][self.__movement['column']] != self.__movement['value']:
            self.__game.board[self.__movement['row']][self.__movement['column']] = self.__movement['value']

    def __check_win(self):
        for i in range(3):
            if all(self.__game.board[i][0] == self.__game.board[i][j] != 0 for j in range(3)):
                return True
            if all(self.__game.board[0][i] == self.__game.board[j][i] != 0 for j in range(3)):
                return True
            if self.__game.board[0][0] == self.__game.board[1][1] == self.__game.board[2][2] != 0:
                return True
            if self.__game.board[0][2] == self.__game.board[1][1] == self.__game.board[2][0] != 0:
                return True

    def __check_draw(self):
        for row in self.__game.board:
            if 0 in row:
                return False
        return True

    def __declare_winner(self, is_draw: bool):
        self.__game.state = 'finished'
        if is_draw:
            self.__game.winner = 0
        else:
            self.__game.winner = self.__movement['value']

    def __update_movements(self):
        self.__game.movements = self.__game.movements or []
        self.__game.movements.append(self.__movement)
