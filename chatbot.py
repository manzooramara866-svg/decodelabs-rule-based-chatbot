"""
DecodeLabs - Project 1: Rule-Based AI Chatbot
Author: [Ammara Manzoor]
Description: A simple rule-based chatbot that simulates basic
             human interaction using control flow (if-else) logic.
"""

import datetime


class RuleBasedChatbot:
    """A simple chatbot that responds to predefined user inputs
    using rule-based (if-else) decision logic."""

    def __init__(self, bot_name="DecodeBot"):
        self.bot_name = bot_name
        self.is_running = True

        # Rules stored as a dictionary for cleaner organization
        self.exit_commands = ["bye", "exit", "quit"]
        self.greetings = ["hi", "hello", "hey"]

    def get_greeting_message(self):
        """Returns a time-based greeting."""
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning!"
        elif hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"

    def respond(self, user_input):
        """Core decision-making logic: maps user input to a response."""
        user_input = user_input.lower().strip()

        if user_input in self.exit_commands:
            self.is_running = False
            return f"Goodbye! It was nice talking to you. "

        elif user_input in self.greetings:
            return f"{self.get_greeting_message()} How can I help you today?"

        elif "how are you" in user_input:
            return "I'm just lines of code, but I'm running smoothly! How about you?"

        elif "your name" in user_input:
            return f"I'm {self.bot_name}, your rule-based virtual assistant."

        elif "who made you" in user_input or "who created you" in user_input:
            return "I was developed as Project 1 at DecodeLabs."

        elif "help" in user_input:
            return ("I can respond to greetings, answer questions about myself, "
                    "and say goodbye. Try asking 'how are you' or 'what is your name'.")

        elif "thank" in user_input:
            return "You're most welcome!"

        else:
            return "I'm sorry, I didn't understand that. Could you please rephrase?"

    def run(self):
        """Runs the chatbot in a continuous loop until an exit command is given."""
        print(f" {self.bot_name}: Hello! I'm a rule-based chatbot. "
              f"Type 'bye' to exit anytime.\n")

        while self.is_running:
            user_input = input("You: ")
            response = self.respond(user_input)
            print(f" {self.bot_name}: {response}\n")


if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.run()
