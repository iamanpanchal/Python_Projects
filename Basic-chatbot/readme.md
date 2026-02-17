# 🤖 Basic Python Chatbot

A simple rule-based chatbot built using Python.
This chatbot responds to user inputs based on predefined prompt–response pairs stored in a dictionary.

Perfect beginner project for learning:

* Python dictionaries
* Loops and conditions
* Functions
* User input handling
* Basic chatbot logic

---

## 🚀 Features

✅ Simple and beginner-friendly
✅ Fast response using dictionary lookup
✅ Multiple conversation prompts
✅ Exit command support
✅ Easy to customize with new data

---

## 📂 Project Structure

```
Basic-Chatbot/
│── chatbot.py
│── README.md
```

---

## 🧠 How It Works

1. User enters a message.
2. Program converts input into text.
3. Chatbot searches the dictionary for a matching prompt.
4. If found → response is displayed.
5. If not found → default message is shown.

---

## 💻 Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Basic-chatbot.git
```

### 2️⃣ Navigate to Folder

```bash
cd Basic-chatbot
```

### 3️⃣ Run Program

```bash
python chatbot.py
```

---

## 📜 Example Code

```python
chat_data = {
    "hello": "Hi 😊",
    "who are you": "I am an AI assistant",
    "bye": "See ya!"
}

def chatbot():
    print("🤖 Chatbot: Hello! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("🤖 Chatbot: Goodbye!")
            break

        if user_input in chat_data:
            print("🤖 Chatbot:", chat_data[user_input])
        else:
            print("🤖 Chatbot: Sorry, I don't understand that yet.")

chatbot()
```

---

## 🛠️ Technologies Used

* Python 3
* VS Code / Any Python IDE

---

## 👨‍💻 Author

**Aman Panchal**

* GitHub: https://github.com/iamanpanchal

---

## ⭐ Contributing

Contributions are welcome!
Feel free to fork this repository and improve the chatbot.

---