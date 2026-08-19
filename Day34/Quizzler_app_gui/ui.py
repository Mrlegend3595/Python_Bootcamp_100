from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzInterface:
    # definition of data type for parameters of function
    def __init__(self ,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR , padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0" ,fg="white" , bg=THEME_COLOR,)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                width= 280,
                                                text="" ,
                                                font=("Arial",20, "italic") ,
                                                fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2 , pady= 50)

        true_image = PhotoImage(file="images/true.png")
        self.true_butt = Button(image=true_image , highlightthickness=0, command=self.true_pressed)
        self.true_butt.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_butt = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_butt.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.true_butt.config(state="disabled")
            self.false_butt.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

