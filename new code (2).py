from tkinter import Tk, Frame, Label, Button 
from PIL import ImageTk,Image

root = Tk()
root.geometry("300x250")

root.configure(background='lightblue')

img = ImageTk.PhotoImage(Image.open("picture1.png"))
canvas.create_image(20,20,anchor = NW, image=img)

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Correct!")
            right += 1
        else:
            label = Label(view, text="Incorrect!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(root)
        Label(view, text=self.question).pack()
        Button(view, bg='#ffff33', activebackground='#adff2f', text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, bg='#ffff33', activebackground='#adff2f', text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, bg='#ffff33', activebackground='#adff2f', text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, bg='#ffff33', activebackground='#adff2f', text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, root, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(root, text="Thanks for playing! " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(root).pack()

Label(root, text="Welcome to the Simpsons Quiz Game!").pack()
button = Button(root, text = 'Start Quiz', bg='#ffff33', activebackground='#adff2f',command= askQuestion)  
button.pack()

questions = []
file = open("example2.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)


root.mainloop()