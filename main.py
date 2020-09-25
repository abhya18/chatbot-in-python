from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk , Image
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

conversation = [
    "Hello",
    "Hi there!",
    "What is your name?",
    "My name is chatter. I am created by Abhya.",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your favorite hobby?",
    "Playing Badminton.",
    "Will you die?",
    "No, I am immortal.",
    "Can you breathe?",
    "My server has an exhaust fan.  That's as close as I can get.",
    "What do you like to do?",
    "I like to chat with people.  I find it stimulating.",
    "Why can you not eat?",
    "I will consume electricity",
    "Bye",
    "Bbye"

]

trainer = ListTrainer(bot)
trainer.train(conversation)
#answer = bot.get_response("Hello")
#print(answer)

#print("Talk To Bot")
#while True:
  #  query = input()
   # if query == "exit":
    #    break
  #  answer = bot.get_response(query)
   # print("Bot: ", answer)


main = Tk()
main.geometry("500x650")
main.title("My Chatbot")
img = ImageTk.PhotoImage(file="bot1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening... Try to speak...")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Not recognized")

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"You: " + query)
    msgs.insert(END, "Bot: " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand = sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(main, font=("Verdana", 13))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 13), command= ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target = repeatL)
t.start()

main.mainloop()