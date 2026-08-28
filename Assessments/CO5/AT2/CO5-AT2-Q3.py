def classify_dialogue_act(utterance):
    u = utterance.lower()

    if "can you" in u or "could you" in u or "please" in u:
        return "Request"

    if u.strip().endswith("?") or u.startswith(("where", "what", "when", "do", "does")):
        return "Question"

    if "i want" in u or "i need" in u or "i would like" in u:
        return "Inform"

    if "has been" in u or "is done" in u or "booked" in u:
        return "Confirmation/Action"

    return "Statement"


conversation = [
    "Can you book a train ticket for me?",
    "Sure, where would you like to travel?",
    "I want to go to Chennai.",
    "Your ticket has been booked."
]


for utt in conversation:
    print(f"{utt!r:45} -> {classify_dialogue_act(utt)}")
