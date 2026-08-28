irregular_past = {
    "buy": "bought",
    "go": "went",
    "eat": "ate"
}

determiners = {
    "Student": "the student",
    "Book": "a book"
}


def generate_sentence(frame):
    agent = determiners.get(frame["Agent"], frame["Agent"].lower())
    obj = determiners.get(frame["Object"], frame["Object"].lower())
    action = frame["Action"].lower()

    if frame["Tense"] == "Past":
        action = irregular_past.get(action, action + "ed")

    sentence = f"{agent.capitalize()} {action} {obj}."
    return sentence


frame = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

print(generate_sentence(frame))
