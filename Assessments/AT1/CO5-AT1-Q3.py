senses = { 
    "bank": [ 
        {"name": "riverbank", "keywords": {"river", "flood", "water", "shore"}}, 
        {"name": "financial_institution", "keywords": {"money", "account", "loan", "deposit"}}, 
    ] 
} 
  
def disambiguate(word, context_tokens): 
    context = set(w.lower() for w in context_tokens) 
    scores = {} 
    for sense in senses[word]: 
        scores[sense["name"]] = len(sense["keywords"] & context) 
    best = max(scores, key=scores.get) 
    return best, scores 
  
sentence = "The bank by the river flooded after the storm but it was saved by quick action".split() 
best_sense, scores = disambiguate("bank", sentence) 
print("Sense scores:", scores) 
print("Selected sense:", best_sense)
