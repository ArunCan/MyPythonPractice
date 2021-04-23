from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question Comes Here", font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.update_question()
        self.true_button = Button(image=self.true_image, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.window.mainloop()

    def update_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        self.score_label.config(text=f"Score:{self.quiz.score}")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, choice):
        if choice:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.update_question)
