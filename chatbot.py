# ============================================================
#  DecodeLabs – AI Internship | Project 1
#  Rule-Based AI Chatbot  🤖
#  Author : (Your Name)
#  Spec   : IPO Model  →  Input → Process → Output
# ============================================================

# ── PHASE 2 : KNOWLEDGE BASE (Dictionary / Hash Map) ────────
# O(1) lookup — far better than an if-elif ladder which is O(n)
RESPONSES = {
    # Greetings
    "hello"        : "Hey there! 👋 How can I assist you today?",
    "hi"           : "Hi! Welcome to DecodeLabs AI. What can I do for you?",
    "hey"          : "Hey! 😊 What's on your mind?",

    # Identity
    "who are you"  : "I'm DecoBot 🤖 — a rule-based AI built at DecodeLabs!",
    "what are you" : "I'm a rule-based chatbot. I use logic, not magic. 🧠",

    # Well-being
    "how are you"  : "Running at 100% efficiency. Thanks for asking! ⚙️",
    "are you okay" : "All systems nominal. Zero bugs detected… so far. 😄",

    # Help / capabilities
    "help"         : "I can answer basic questions. Try: 'who are you', 'what is ai', 'joke', etc.",
    "what can you do" : "I respond to greetings, tell jokes, explain AI basics, and more!",

    # AI knowledge
    "what is ai"   : "AI stands for Artificial Intelligence — making machines simulate human thinking.",
    "what is ml"   : "ML (Machine Learning) lets computers learn from data instead of explicit rules.",
    "what is a chatbot" : "A chatbot is a program that simulates conversation. Like me! 🤖",

    # Fun
    "joke"         : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "tell me a joke": "I told a joke about UDP once… I don't know if you got it. 😄",

    # Gratitude
    "thanks"       : "You're welcome! Happy to help. 😊",
    "thank you"    : "Anytime! That's what I'm here for. 🙌",

    # Farewell (non-exit)
    "bye"          : "See you later! Type 'exit' whenever you want to quit.",
    "goodbye"      : "Goodbye! Come back anytime. 👋",
    
    "what is python"  : "Python is the #1 language for AI/ML. Clean syntax, massive libraries.",
    "your name"       : "My name is DecoBot! Built with pure Python logic. 🤖",
    "what is decodelabs" : "DecodeLabs is a tech training platform that turns interns into engineers!",
}

# Exit keywords — the "Kill Command" as the slides call it
EXIT_COMMANDS = {"exit", "quit", "stop", "close"}


# ── PHASE 1 : INPUT & SANITIZATION ──────────────────────────
def sanitize(raw: str) -> str:
    """
    Normalize raw user input:
      .lower()  → removes case sensitivity  (Hello == hello)
      .strip()  → removes leading/trailing whitespace
    """
    return raw.lower().strip()


# ── PHASE 2 : PROCESS (Intent Matching) ─────────────────────
def get_response(clean_input: str) -> str:
    """
    Look up the cleaned input in the RESPONSES dictionary.
    dict.get(key, fallback) is an atomic O(1) operation:
      • If the key EXISTS  → returns its value (the reply)
      • If the key MISSING → returns the fallback string
    No if-elif ladder needed!
    """
    return RESPONSES.get(clean_input, "🤔 I don't understand that yet. Try 'help' for options.")


# ── PHASE 3 : OUTPUT + HEARTBEAT LOOP ───────────────────────
def run_chatbot():
    print("=" * 55)
    print("  🤖  DecoBot  |  Rule-Based AI  |  DecodeLabs 2026")
    print("=" * 55)
    print("  Type 'help' for commands.  Type 'exit' to quit.\n")

    # THE HEARTBEAT — infinite while loop (the organism stays
    # alive until the Kill Command is received)
    while True:

        # ── INPUT ──
        raw_input = input("You: ")

        # ── SANITIZATION ──
        clean_input = sanitize(raw_input)

        # Guard against empty input
        if not clean_input:
            print("Bot: Please type something. 😊\n")
            continue

        # ── EXIT STRATEGY (Kill Command) ──
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Session terminated. 👋")
            print("=" * 55)
            break                          # clean break — exits the while loop

        # ── PROCESS + OUTPUT ──
        reply = get_response(clean_input)
        print(f"Bot: {reply}\n")


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
