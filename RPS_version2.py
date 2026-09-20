# workflow:
# computer takes a random string between the three strings ie 'rock','paper','scissors'
# if user enters rock and computer chooses paper then computer wins (computer: +1)
# if user enters rock and computer chooses scissors then user wins (user: +1)
# if user enters paper and computer chooses rock then user wins
# if user enters paper and computer chooses scissors then computer wins
# if user enters scissors and computer chooses rock then computer wins
# if user enters scissors and computer chooses paper then user wins
# if both enters same then draw (draw:+1)

# IM GAME!!!
import random
import sqlite3
connection=sqlite3.connect(r"game.db") #give correct game.db path
cursor=connection.cursor()

def draw():
    cursor.execute(
        '''UPDATE RPS
        SET PLR_DRAWS=PLR_DRAWS+1
        WHERE PLR_NAME=?;''',
        (username,)
    )
    connection.commit()
    return "Game Drawn..\n"
def loss():
    cursor.execute(
        '''UPDATE RPS
        SET PLR_LOSS=PLR_LOSS+1
        WHERE PLR_NAME=?;''',
        (username,)
    )
    connection.commit()
    return "You lost! Better luck next time...\n"
def win():
    cursor.execute(
        '''UPDATE RPS
        SET PLR_WINS=PLR_WINS+1
        WHERE PLR_NAME=?;''',
        (username,)
    )
    connection.commit()
    return "Congrats! You won!!\n"

print("========================\n   ROCK PAPER SCISSORS   \n========================\n")
username=input("Enter username to start the game: ").upper()
cursor.execute(
    '''SELECT *
    FROM RPS
    WHERE PLR_NAME=?''',
    (username,)
)
exists=cursor.fetchone()
if exists != None:
    print(f"Welcome Back {username}!")
else:
    cursor.execute(
        '''INSERT INTO RPS
        (PLR_NAME,PLR_WINS,PLR_LOSS,PLR_DRAWS)
        VALUES(?,0,0,0);''',
        (username,)
    )
    connection.commit()

while True:
    choices=['rock','paper','scissors']
    comp_choice=random.choice(choices)
    while True:
        print("Choose:\n1. Rock\n2. Paper\n3. Scissors\n")
        user_choice=input("Enter your choice: ").lower()
        if user_choice in choices:
            break
        else:
            print("Please enter valid choice...")
    print(f"Computers choice: {comp_choice}")
    if user_choice==comp_choice:
        print(draw())

    elif (user_choice=='rock' and comp_choice=='paper') or (user_choice=='paper' and comp_choice=='scissors') or (user_choice=='scissors' and comp_choice=='rock'):
        print(loss())

    elif (user_choice=='rock' and comp_choice=='scissors') or (user_choice=='paper' and comp_choice=='rock') or (user_choice=='scissors' and comp_choice=='paper'):
        print(win())

    while True:
        play_again_choices=['yes','no']
        play_again=input("Play again?\n").lower()
        if play_again in play_again_choices:
            break
        else:
            print("Please enter a valid input...")
    if play_again=='no':
        break
print()
print("           ===============\n              Scoreboard\n           ===============")
cursor.execute(
    '''SELECT *
    FROM RPS
    WHERE PLR_NAME=?;''',
    (username,)
)
result=cursor.fetchall()
score=result[0]
print("Player       Wins        Losses      Draws")
print(f"{score[0]}         {score[1]}            {score[2]}           {score[3]}")