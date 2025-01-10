import ast
from typing import Literal, Union
from sqlalchemy.orm import Session

from app.domain.entities import Game, Board, Movements
from app.infra.db.entities import Game as GameDBEntity
from app.infra.db.repositories import decorators as dc
from app.domain.repositories import GameRepositoryInterface


class GameRepository(GameRepositoryInterface):
    session: Session

    @classmethod
    @dc.use_db_session
    def create_game(cls,
                    player_id: int,
                    board: Board,
                    state: Literal['in_progress', 'finished'],
                    winner: Literal[-1, 0, 1],
                    movements: Union[Movements, None]
                    ) -> Game:
        board = str(board)
        movements = str(movements)
        db_game = GameDBEntity(
            player_id=player_id,
            board=board,
            state=state,
            movements=movements,
            winner=winner,
        )
        cls.session.add(db_game)
        cls.session.commit()
        game_board_formatted = ast.literal_eval(db_game.board)
        game_movements_formatted = ast.literal_eval(db_game.movements) if db_game.movements is not 'None' else None
        game_state_formatted: Literal['in_progress', 'finished'] = db_game.state if db_game.state in ['in_progress',
                                                                                                      'finished'] else 'finished'
        game_winner_formatted: Literal[-1, 0, 1] = db_game.winner if db_game.winner in [-1, 0, 1] else 0
        game = Game(
            id=db_game.id,
            board=game_board_formatted,
            state=game_state_formatted,
            player_id=db_game.player_id,
            movements=game_movements_formatted,
            winner=game_winner_formatted
        )
        return game

    @classmethod
    @dc.use_db_session
    def get_game(cls, id: int) -> Game:
        db_game = cls.session.query(GameDBEntity).get(id)
        game_board_formatted = ast.literal_eval(db_game.board)
        game_movements_formatted = ast.literal_eval(db_game.movements) if db_game.movements is not 'None' else None
        game_winner_formatted: Literal[-1, 0, 1] = db_game.winner if db_game.winner in [-1, 0, 1] else 0
        game = Game(
            id=db_game.id,
            board=game_board_formatted,
            state=db_game.state,
            player_id=db_game.player_id,
            movements=game_movements_formatted,
            winner=game_winner_formatted
        )
        return game

    @classmethod
    @dc.use_db_session
    def get_in_progress_game(cls, player_id: int) -> Game:
        db_game = cls.session.query(GameDBEntity).filter(
            GameDBEntity.player_id == player_id,
            GameDBEntity.state == 'in_progress'
        ).first()
        game_board_formatted = ast.literal_eval(db_game.board)
        game_movements_formatted = ast.literal_eval(db_game.movements) if db_game.movements is not 'None' else None
        game_state_formatted: Literal['in_progress', 'finished'] = db_game.state if db_game.state in ['in_progress',
                                                                                                      'finished'] else 'finished'
        game_winner_formatted: Literal[-1, 0, 1] = db_game.winner if db_game.winner in [-1, 0, 1] else 0
        game = Game(
            id=db_game.id,
            board=game_board_formatted,
            state=game_state_formatted,
            player_id=db_game.player_id,
            movements=game_movements_formatted,
            winner=game_winner_formatted,
        )
        return game

    @classmethod
    @dc.use_db_session
    def update_game(cls,
                    id: int,
                    player_id: int,
                    board: Board,
                    state: Literal['in_progress', 'finished'],
                    winner: Literal[-1, 0, 1],
                    movements: Movements = None,
                    ) -> Game:
        db_game = cls.session.query(GameDBEntity).get(id)
        db_game.player_id = player_id
        db_game.board = str(board)
        db_game.state = state
        db_game.movements = str(movements)
        db_game.winner = winner
        cls.session.commit()
        game_board_formatted = ast.literal_eval(db_game.board)
        game_movements_formatted = ast.literal_eval(db_game.movements) if db_game.movements is not 'None' else None
        game_state_formatted: Literal['in_progress', 'finished'] = db_game.state if db_game.state in ['in_progress',
                                                                                                      'finished'] else 'finished'
        game_winner_formatted: Literal[-1, 0, 1] = db_game.winner if db_game.winner in [-1, 0, 1] else 0
        game = Game(
            id=db_game.id,
            board=game_board_formatted,
            state=game_state_formatted,
            player_id=db_game.player_id,
            movements=game_movements_formatted,
            winner=game_winner_formatted,
        )
        return game
