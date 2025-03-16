import re
import datetime
import random
import operator

# Dictionary of predefined responses
responses = {
    "greetings": ["Hello! 😊", "Hi there! 👋", "Greetings! 🌍"],
    "help": "I can assist with time checks, jokes, basic math, and simple info!",
    "unknown": "I'm still learning. Could you rephrase that? 🤔",
    "weather": "I'm not connected to weather services, but I hope it's pleasant outside! ☀️"
}

# List of jokes with setup and punchline
jokes = [
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("What do you call a fake noodle?", "An impasta!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("How does a penguin build its house?", "Igloos it together!"),
    ("Why did the math book look sad?", "Because it had too many problems.")
]

# Supported math operations
math_operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def evaluate_math(expression):
    try:
        # Extract numbers and operator
        match = re.search(r'(-?\d+)\s*([+\-*/**])\s*(-?\d+)', expression)
        if match:
            num1, op, num2 = match.groups()
            num1, num2 = int(num1), int(num2)
            return math_operations[op](num1, num2)
        else:
            return "Invalid math expression. Try something like '2 + 2'"
    except Exception:
        return "Math error! Make sure you're using correct numbers and operators."

def chatbot():
    print("ChatBot: Hello! I'm here to help. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        cleaned_input = re.sub(r"[^\w\s+\-*/?]", '', user_input)
        
        if re.search(r'\b(bye|exit|quit)\b', cleaned_input):
            print("ChatBot: Goodbye! Have a nice day! 👋")
            break
        
        elif re.search(r'\b(hi|hello|hey|hola)\b', cleaned_input):
            print(f"ChatBot: {random.choice(responses['greetings'])}")
        
        elif re.search(r'\b(help|support|assist)\b', cleaned_input):
            print(f"ChatBot: {responses['help']}")
        
        elif re.search(r'\b(time|current time|what time)\b', cleaned_input):
            print(f"ChatBot: The current time is {get_time()} ⏰")
        
        elif re.search(r'\b(joke|funny|laugh)\b', cleaned_input):
            setup, punchline = random.choice(jokes)
            print(f"ChatBot: {setup}\n        {punchline}")
        
        elif re.search(r'\b(weather|forecast|rain|sun)\b', cleaned_input):
            print(f"ChatBot: {responses['weather']}")
        
        elif re.search(r'\d+\s*[+\-*/**]\s*\d+', cleaned_input):
            print(f"ChatBot: {evaluate_math(cleaned_input)}")
        
        else:
            print(f"ChatBot: {responses['unknown']}")

if __name__ == "__main__":
    chatbot()
