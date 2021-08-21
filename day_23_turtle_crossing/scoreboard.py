from turtle import Turtle

FONT = ("Courier", 24, "normal")


def get_highest_level_reached():
    try:
        file = open("high_level.txt", 'r')
        highest_level = int(file.read())
        file.close()
    except:
        highest_level = 1

    return highest_level


class Scoreboard(Turtle):
    POSITION = (-280, 220)

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(Scoreboard.POSITION)
        self.level = 0
        self.highest_level = get_highest_level_reached()
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}\nHighest: {self.highest_level}", font=FONT)

    def game_over(self):
        self.goto(-40, 0)
        self.write(f"Game Over", font=FONT)
        self.record_highest_level_reached()

    def record_highest_level_reached(self):
        if self.level > self.highest_level:
            try:
                file = open("high_level.txt", 'w')
                file.write(str(self.level))
                file.close()
            except:
                print('Error recording High Score')
