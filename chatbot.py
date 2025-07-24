import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from datetime import datetime

# Define chatbot pairs and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you ?", ["I'm good, thanks! How about you?", "Doing great. Hope you're well too!"]],
    [r"i am fine|i am good", ["That's great to hear!", "Awesome!"]],
    [r"(.*)your name ?", ["I'm ChatBuddy, your Python chatbot!"]],
    [r"(.*)created you ?", ["A Python programmer like you!"]],
    [r"what can you do ?", ["I can chat with you and answer basic questions."]],
    [r"(.*)tell me a joke", ["Why did the computer go to the doctor? Because it had a virus!"]],
    [r"thank you|thanks", ["You're welcome!", "Glad I could help!"]],
    [r"bye|exit|quit", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"(.*)your favorite color ?", ["I don't have feelings, but I like blue!", "Colors are fascinating!"]],
    [r"(.*) time is it?", [f"The current time is {datetime.now().strftime('%H:%M:%S')}"]],
    [r"(.*)", ["Interesting... tell me more!", "Hmm, I didn't get that. Can you rephrase?"]]
]

# Reflections dictionary
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "your": "my",
    "i 'm": "you 're",
    "i've": "you've",
    "i'll": "you'll",
    "i would": "you would",
    "i want": "you want",
    "me": "you"
}


chatbot = Chat(pairs, reflections)


def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n")

    if user_msg.lower() in ["bye", "exit", "quit"]:
        response = "Goodbye! Have a great day!"
        chat_window.insert(tk.END, "Bot: " + response + "\n")
        root.after(1500, root.destroy)
        return
    else:
        response = chatbot.respond(user_msg)
        chat_window.insert(tk.END, "Bot: " + response + "\n")

    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("ChatBuddy - NLTK Chatbot")
root.geometry("500x550")


chat_window = tk.Text(root, bg="white", fg="black", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


user_input = tk.Entry(root, font=("Arial", 12))
user_input.pack(padx=10, pady=5, fill=tk.X)


send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)


root.bind('<Return>', lambda event=None: send_message())


root.mainloop()
