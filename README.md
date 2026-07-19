# decodelabs-rule-based-chatbot
# Rule-Based AI Chatbot

**DecodeLabs — Project 1: Foundation Phase**

A rule-based conversational chatbot built in Python, demonstrating core programming logic — control flow, decision-making, and continuous program execution — as the foundation before advancing to machine-learning-based AI systems.

---

## Project Overview

This project simulates basic human-like interaction using purely deterministic, if-else driven logic — no machine learning, no external APIs. The goal is to master control flow and structured decision-making, which forms the architectural basis of more advanced AI systems.

---

## Features

- Runs in a continuous loop until explicitly exited
- Recognizes and responds to greetings
- Handles predefined conversational queries (identity, status, help)
- Graceful exit on recognized commands
- Dynamic, time-based greeting messages
- Clean, object-oriented code structure for readability and scalability

---

## Tech Stack

| Component  | Details                     |
|------------|------------------------------|
| Language   | Python 3                    |
| Paradigm   | Object-Oriented Programming |
| Logic Type | Rule-Based (Deterministic)  |

---

## Project Structure

├── chatbot.py     # Main chatbot application
└── README.md      # Project documentation

---

## How to Run

1. Ensure Python 3 is installed on your system.
2. Clone this repository or download chatbot.py.
3. Run the following command in your terminal:

python chatbot.py

4. Interact with the chatbot by typing messages (e.g. hi, how are you, bye).

---

## Sample Interaction

DecodeBot: Hello! I'm a rule-based chatbot. Type 'bye' to exit anytime.

You: hi
DecodeBot: Good afternoon! How can I help you today?

You: what is your name
DecodeBot: I'm DecodeBot, your rule-based virtual assistant.

You: bye
DecodeBot: Goodbye! It was nice talking to you.

---

## Key Concepts Demonstrated

- Control Flow: Sequential and conditional logic (if / elif / else)
- Decision-Making Logic: Mapping user input to predefined responses
- Continuous Execution: Program loop (while) simulating persistent interaction
- Foundational AI Design: Deterministic ("System 2") behavior, as opposed to probabilistic, learning-based ("System 1") models

---

## Future Enhancements

- Keyword-scoring based intent matching
- Expanded rule set with regex pattern matching
- Transition toward NLP-based intent recognition
