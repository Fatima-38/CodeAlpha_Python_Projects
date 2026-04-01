import random

# ─────────────────────────────────────────────
#  TASK 4 — Chatbot
# ─────────────────────────────────────────────

def get_response(user_input):
    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "howdy", "greetings"]):
        return random.choice(["Hi there! 😊", "Hello! How can I help?", "Hey! Nice to see you!"])

    # How are you
    elif any(phrase in text for phrase in ["how are you", "how r you", "how do you do", "you okay"]):
        return random.choice([
            "I'm doing great, thanks for asking! 😄",
            "Feeling fantastic! How about you?",
            "All good on my end! 👍"
        ])

    # Name
    elif any(phrase in text for phrase in ["your name", "who are you", "what are you"]):
        return "I'm PyBot 🤖 — your simple Python chatbot!"

    # What can you do
    elif any(phrase in text for phrase in ["what can you do", "help", "features"]):
        return ("I can chat with you! Try saying:\n"
                "  • hello / hi\n"
                "  • how are you\n"
                "  • what's your name\n"
                "  • tell me a joke\n"
                "  • bye")

    # Jokes
    elif any(word in text for word in ["joke", "funny", "laugh", "humor"]):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the computer cold? It left its Windows open! 🪟",
            "How do you comfort a JavaScript developer? You console them. 😂",
            "Why do Python programmers wear glasses? Because they can't C! 👓"
        ]
        return random.choice(jokes)

    # Time / Date
    elif any(word in text for word in ["time", "date", "today"]):
        from datetime import datetime
        now = datetime.now()
        return f"🕐 Current date & time: {now.strftime('%A, %B %d, %Y — %I:%M %p')}"

    # Thanks
    elif any(word in text for word in ["thanks", "thank you", "thx", "ty"]):
        return random.choice(["You're welcome! 😊", "Anytime!", "Happy to help! 🙌"])

    # Bye / Exit
    elif any(word in text for word in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "QUIT"

    # Fallback
    else:
        return random.choice([
            "Hmm, I didn't quite get that. 🤔 Type 'help' to see what I can do!",
            "I'm still learning! Could you rephrase that?",
            "Not sure about that one. Try asking something else!"
        ])


def chatbot():
    print("=" * 45)
    print("       🤖 Welcome to PyBot!")
    print("    (type 'bye' or 'quit' to exit)")
    print("=" * 45)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("PyBot: Please say something! 😊")
            continue

        response = get_response(user_input)

        if response == "QUIT":
            print("PyBot: Goodbye! Take care! 👋")
            break

        print(f"PyBot: {response}")

chatbot()