from app.application.use_cases import MLTrainer
from app.infra.ai.use_cases import AILearning
from app.infra.db.repositories import GameRepository
from app.infra.settings import EnvVarsHandler


def test_train():
    EnvVarsHandler.read_env_vars('C:/Users/vinio/Projects/tictactoe_api/.env')
    ai_learning = AILearning()
    game_repository = GameRepository()
    ml_trainer = MLTrainer(ml_learning=ai_learning, game_repository=game_repository)
    ml_trainer.train(games_amount=50, pth_file_path='../../tic_tac_toe_model.pth')
