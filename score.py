from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def food_got_eaten(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER!!!', align=ALIGNMENT, font=FONT)
