mentions = ["John", "Mary", "He", "a ball", "She", "it", "The dog", "him", "they"] 
  
# Simple attribute table for candidate entities 
entities = { 
    "John": {"gender": "male", "number": "sing", "animate": True}, 
    "Mary": {"gender": "female", "number": "sing", "animate": True}, 
    "a ball": {"gender": "neutral", "number": "sing", "animate": False}, 
    "The dog": {"gender": "neutral", "number": "sing", "animate": True}, 
} 
  
def gender_number_ok(pronoun, entity): 
    table = { 
        "He": ("male", "sing"), "She": ("female", "sing"), 
        "it": ("neutral", "sing"), "him": ("male", "sing"), 
    } 
    if pronoun not in table: 
        return True 
    g, n = table[pronoun] 
    return entities[entity]["gender"] == g and entities[entity]["number"] == n 
  
def semantic_ok(pronoun, entity): 
    # 'him' after "chased" needs an animate target 
    if pronoun == "him": 
        return entities[entity]["animate"] 
    return True 
  
def resolve(pronoun, candidates_in_recency_order): 
    for cand in candidates_in_recency_order:      # recency: nearest first 
        if gender_number_ok(pronoun, cand) and semantic_ok(pronoun, cand): 
            return cand 
    return None 
  
print("He   ->", resolve("He",   ["John", "Mary"])) 
print("She  ->", resolve("She",  ["Mary", "John"])) 
print("it   ->", resolve("it",   ["a ball"])) 
print("him  ->", resolve("him",  ["John", "The dog"]))
