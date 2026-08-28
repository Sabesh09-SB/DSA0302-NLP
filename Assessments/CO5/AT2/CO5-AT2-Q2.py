cue_dict = {
    "therefore": "CAUSE_EFFECT",
    "as a result": "CAUSE_EFFECT",
    "so": "CAUSE_EFFECT",
    "then": "SEQUENCE",
    "after that": "SEQUENCE",
    "later": "SEQUENCE",
    "for example": "ELABORATION",
    "in addition": "ELABORATION",
    "however": "CONTRAST",
    "but": "CONTRAST"
}


def find_relation(sentence):
    s = sentence.lower()

    for cue, rel in cue_dict.items():
        if cue in s:
            return rel

    return "ELABORATION"   # Default relation


sentences = [
    "The roads were flooded after heavy rainfall",
    "Therefore, schools were closed for the day",
    "Students attended classes online"
]


for i in range(1, len(sentences)):
    rel = find_relation(sentences[i])

    print(f"{sentences[i-1]} --{rel}--> {sentences[i]}")
