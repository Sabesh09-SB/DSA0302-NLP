import random

def analyze(sentence):
    return {
        "predicate": "Play",
        "agent": "boy",
        "object": "football",
        "tense": "present",
        "aspect": "continuous"
    }


def generate_candidates(interlingua):
    return [
        "Le garcon joue au football.",
        "Le garcon est en train de jouer au football.",
        "Un garcon joue football."
    ]


# Toy bigram language-model scores (higher = more fluent)
lm_scores = {
    "Le garcon joue au football.": 0.82,
    "Le garcon est en train de jouer au football.": 0.55,
    "Un garcon joue football.": 0.30
}


def translate(sentence):
    il = analyze(sentence)
    candidates = generate_candidates(il)
    best = max(candidates, key=lambda c: lm_scores[c])
    return il, candidates, best


il, candidates, best = translate("The boy is playing football.")

print("Interlingua:", il)
print("Candidates :", candidates)
print("Best       :", best)
