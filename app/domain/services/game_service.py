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
        if self.__check_win():
            self.__declare_winner()
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

    def __declare_winner(self):
        self.__game.state = 'finished'
        self.__game.is_player_winner = True

    def __update_movements(self):
        self.__game.movements = self.__game.movements or []
        self.__game.movements.append(self.__movement)
