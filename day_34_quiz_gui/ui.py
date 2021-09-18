import tkinter as tk
from quiz_brain import QuizBrain


class QuizInterface:
    THEME_COLOR = "#375362"

    def __init__(self, quiz_brain: QuizBrain):
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=QuizInterface.THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {quiz_brain.score}", bg=QuizInterface.THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        # the width param is used to make sure that the text wraps around if it goes over that width
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text='test Question',
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        self.false_img = tk.PhotoImage(file='images/false.png')
        self.false_btn = tk.Button(image=self.false_img,
                                   highlightthickness=0,
                                   bg=QuizInterface.THEME_COLOR,
                                   command=self.user_says_false)

        self.false_btn.grid(row=2, column=0)

        self.true_img = tk.PhotoImage(file='images/true.png')
        self.true_btn = tk.Button(image=self.true_img,
                                  highlightthickness=0,
                                  bg=QuizInterface.THEME_COLOR,
                                  command=self.user_says_true)
        self.true_btn.grid(row=2, column=1)
        self.quiz_brain = quiz_brain
        self.get_next_question()

    def run(self):
        self.window.mainloop()

    def get_next_question(self):
        end_msg = f"You've completed the quiz Your final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}"
        if self.quiz_brain.still_has_questions():
            self.canvas.configure(bg='white')
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question_text, text=end_msg)
            self.false_btn.configure(state="disabled")
            self.true_btn.configure(state="disabled")


    def user_says_true(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def user_says_false(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.score_label.configure(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
