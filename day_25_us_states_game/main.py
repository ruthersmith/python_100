import turtle
import pandas
import time


class UsStateGame:
    IMAGE_PATH = "blank_states_img.gif"
    DATA_PATH = '50_states.csv'

    def __init__(self):
        self.data = pandas.read_csv(UsStateGame.DATA_PATH)
        self.correct_guesses = 0
        self.already_guessed = []
        self.screen = turtle.Screen()
        self.screen.title('U.S State Game')
        self.screen.addshape(UsStateGame.IMAGE_PATH)
        turtle.shape(UsStateGame.IMAGE_PATH)

        self.writer = turtle.Turtle()
        self.writer.penup()
        self.writer.hideturtle()

    def exist(self, answer):
        row_returned = self.data[self.data.state == answer]
        if len(row_returned) == 1 and row_returned.state.values[0] not in self.already_guessed:
            self.show_state(row_returned)
            self.already_guessed.append(row_returned.state.values[0])
            self.correct_guesses += 1

    def show_state(self, row_returned):
        self.writer.goto(int(row_returned.x), int(row_returned.y))
        self.writer.write(row_returned.state.values[0])

    def run(self):
        while self.correct_guesses < 50:
            answer = self.screen.textinput(title=f'{self.correct_guesses}/50 states correct',
                                           prompt="Enter other state")
            if answer is None:
                break
            else:
                answer = answer.title()
                self.exist(answer)
                time.sleep(0.5)

        # print all the state that are missing, if exit the game
        print("missing states:")
        print(self.data.state[~self.data.state.isin(self.already_guessed)].values)
        # alternative to exit on click, closes when x is clicked not just anywhere
        self.screen.mainloop()


if __name__ == "__main__":
    state_game = UsStateGame()
    state_game.run()
