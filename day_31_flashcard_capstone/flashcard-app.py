import pandas
import tkinter as tk
import random


class FlashCard:

    BACKGROUND_COLOR = "#B1DDC6"
    # after this amount of millisecond show translation
    SHOW_TRANSLATION_AFTER = 3000


    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Flashy')
        self.window.config(padx=50, pady=50, bg=FlashCard.BACKGROUND_COLOR)

        self.card_front_img = tk.PhotoImage(file='images/card_front.png')
        self.card_back_img = tk.PhotoImage(file='images/card_back.png')

        self.canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=FlashCard.BACKGROUND_COLOR)
        self.card_img = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.lang_text = self.canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
        self.word = self.canvas.create_text(400, 263, text="Word", font=('Ariel', 60, 'bold'))
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.wrong_btn_img = tk.PhotoImage(file="images/wrong.png")
        self.right_btn_img = tk.PhotoImage(file="images/right.png")

        self.wrong_btn = tk.Button(image=self.wrong_btn_img, highlightthickness=0, command=self.new_flashcard)
        self.wrong_btn.grid(row=1, column=0)

        self.right_btn = tk.Button(image=self.right_btn_img, highlightthickness=0, command=self.new_flashcard_remove)
        self.right_btn.grid(row=1, column=1)

        self.data = pandas.read_csv('data/spanish_words.csv')
        self.flashcard_list_dict = self.data.to_dict(orient="records")
        self.current_card = {}

        self.flip_timer = None

    def new_flashcard_remove(self):
        self.flashcard_list_dict.remove(self.current_card)
        self.new_flashcard()

    def new_flashcard(self):
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)

        self.canvas.itemconfig(self.card_img, image=self.card_front_img)
        self.current_card = random.choice(self.flashcard_list_dict)
        print(self.current_card)
        self.canvas.itemconfig(self.word, text=self.current_card['spanish'], fill="black")
        self.canvas.itemconfig(self.lang_text, text="Spanish", fill="black")
        self.flip_timer = self.window.after(FlashCard.SHOW_TRANSLATION_AFTER, func=self.show_translation)

    def show_translation(self):
        self.canvas.itemconfig(self.word, text=self.current_card['english'], fill="white")
        self.canvas.itemconfig(self.lang_text, text="English", fill="white")
        self.canvas.itemconfig(self.card_img, image=self.card_back_img)

    def run(self):
        self.new_flashcard()
        self.window.mainloop()


if __name__ == '__main__':
    flashcard = FlashCard()
    flashcard.run()
