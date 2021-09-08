# bullsncows

This project is a service that will play the game of "Bulls and Cows" with you.  
I plan to use this as an educational project and implement a number of front-end solutions for it:
- Telegram bot
- Django app
- ???

## Rules
The rules are simple:
1. There are 2 players: **the Computer** and the **Person**
2. The Computer generates a number that's 4-digit (without replacement)
3. The Person makes a guess by sending a 4-digit number
4. The Computer lets the person know how close the Person's number and the generated number are by letting  
   the user know the number of _"bulls"_ and _"cows"_ that the user has scored:
   - a **cow** means that one of the digits in the user's number matches a digit in the generated number
   - a **bull** means that the number is also in the right position 

For example, the generated number is `4367`
- `5903` would yield **1 cow**
- `4175` would yield **1 bull and 1 cow** (4 is a bull and 7 is a cow)
- `7436` would yield **4 cows**

The game ends when the Person's number yields 4 bulls (thus guessing the generated number).

## REST API
**Host:** localhost:8000  
**Connection-type:** HTTP  

### Endpoints
The following endpoints are currently defined:
- `/game/new/{user_id}` -> start a new game. Generates a new number, adds an entry in the DB and returns the ID of the game.
- `/game/guess/{game_id}` -> guess the number in an existing game. Returns a count of bulls and cows in the received number.

### Swagger
Thanks to [FastAPI](https://fastapi.tiangolo.com/) library, Swagger documentation is conveniently available at `localhost:8000/docs`


