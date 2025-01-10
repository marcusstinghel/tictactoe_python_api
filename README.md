# Tic Tac Toe Python API

This project is a Python API for the Tic Tac Toe game, implementing the entire game logic, player communication, and data storage. Additionally, the system integrates Machine Learning techniques to analyze past moves and suggest the best possible move.

The project's architecture follows the principles of Clean Architecture and Domain-Driven Design (DDD), ensuring a modular, scalable, and maintainable structure. The database is managed using SQLAlchemy as the ORM, and communication between the API and clients is handled via Flask. The Machine Learning component is built with PyTorch, allowing the system to continuously evolve based on the game history.

Training the AI for Tic Tac Toe involves collecting historical game data, processing it, and using a learning model, such as a neural network, to predict the best move. The model is adjusted during training to identify winning patterns and strategies. When evaluated with unseen data, it is fine-tuned to generalize well. Using historical data allows the AI to learn from past experiences, avoid bad moves, and recognize patterns to improve its predictions over time, making it a more efficient and stronger opponent.

---

## Running the API
1- Download the dependencies in your environment
```shell
pip install -r requirements.txt
```
2- Define environments vars in .env file. Look the example:
```text
DB_CONNECTION_STRING='sqlite:///C:\Users\you\Projects\tictactoe_api/tictactoe.db'
ML_PATH_FILE_PATH='C:\Users\you\Projects\tictactoe_api\tic_tac_toe_model.pth'
```
3- Run main.py
```shell
python .\main.py
```

---

## API Routes

| **Method** | **Endpoint**           | **Description**                                    |
|------------|------------------------|----------------------------------------------------|
| `POST`     | `/api/register`         | Creates a new player.                             |
| `POST`     | `/api/start`            | Starts a new game for the specified player. |
| `POST`     | `/api/move`             | Makes a move in the current game.         |
| `GET`      | `/api/ai-move`          | Gets the AI suggested move for the player.    |
| `POST`     | `/api/ai-train`         | Trains the AI based on a specified number of games. |

---

### 1. **Create Player**

- **Endpoint**: `/api/register`
- **Method**: `POST`
- **Description**: Creates a new player with first name, last name and nickname.
  
#### Request:
```bash
curl --location 'http://127.0.0.1:5000/api/register' \
--header 'Content-Type: application/json' \
--data '{
    "first_name": "Name",
    "last_name": "First",
    "nickname": "Mr. First"
}'
```
```text
Body Parameters for Create Player:
    first_name (string): The first name of the player.
    last_name (string): The last name of the player.
    nickname (string): The nickname of the player.
```

---

### 2. **Start Game**

- **Endpoint**: `/api/start`
- **Method**: `POST`
- **Description**: Starts a new game for the specified player.

#### Request:
```bash
Copiar código
curl --location 'http://127.0.0.1:5000/api/start' \
--header 'Content-Type: application/json' \
--data '{
    "player_id": 2
}'
```
```text
Body Parameters:
player_id (integer): The ID of the player who will start the game.
```

---

### 3. **Make Game Move**

- **Endpoint**: `/api/move`
- **Method**: `POST`
- **Description**: Makes a move in the ongoing game, specifying the column, row, and value of the move.

#### Request:
```bash
curl --location 'http://127.0.0.1:5000/api/move' \
--header 'Content-Type: application/json' \
--data '{
    "player_id": 2,
    "movement": {
        "column": 1,
        "row": 0,
        "value": 1
    }
}'
```
```text
Body Parameters:
    player_id (integer): The ID of the player making the move.
    movement (object): The move details.
    column (integer): The column where the move will be made. Accepts values 0, 1, or 2.
    row (integer): The row where the move will be made. Accepts values 0, 1, or 2.
    value (integer): The value of the move. Use 1 for player and -1 for AI.
```

---

### 4. **Get AI Move**

- **Endpoint**: `/api/ai-move`
- **Method**: `GET`
- **Description**: Retrieves the suggested move from the AI for the specified player.

#### Request:
```bash
curl --location 'http://127.0.0.1:5000/api/ai-move?player-id=1'
```
```text
Query Parameters:
    player-id (integer): The ID of the player for whom the AI will suggest the next move.
```

---

### 5. **Train AI**

- **Endpoint**: `/api/ai-train`
- **Method**: `POST`
- **Description**: Trains the AI based on a specified number of games.

#### Request:
```bash
curl --location 'http://127.0.0.1:5000/api/ai-train' \
--header 'Content-Type: application/json' \
--data '{
    "amount": 50
}'
```
```text
Body Parameters:
    amount (integer): The number of games to be used for training the AI. This should be a positive integer.
```