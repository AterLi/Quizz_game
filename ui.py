from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 19, "bold")


class QuizzUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizzGame")
        self.window.config(pady=40, padx=40, background=THEME_COLOR)

        # Score text
        self.score_text = Label(text=f"Score: {0}", font=("Times New Roman", 16, "bold"), background=THEME_COLOR,
                                highlightcolor="white", foreground="white", pady=30)
        self.score_text.grid(row=0, column=1)

        # Canvas, image in image
        self.canvas = Canvas(width=450, height=450)
        self.q_text = self.canvas.create_text(225, 225, text="Question", font=FONT, fill=THEME_COLOR, width=420)
        self.canvas.grid(row=1, column=0, columnspan=2)

        # Buttons
        false_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=false_image, command=self.choose_false)
        self.wrong_button.grid(row=2, column=0, pady=30)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.choose_true)
        self.true_button.grid(row=2, column=1, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question)
        else:
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.q_text, text=f"Quizz finished")

    def choose_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, func=self.reset_color)

    def reset_color(self):
        self.get_next_question()
