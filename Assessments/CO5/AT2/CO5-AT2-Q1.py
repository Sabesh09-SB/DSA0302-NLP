def resolve_references(text):
    entities = {
        "Ravi": {"gender": "M", "role": "subject"},
        "Arun": {"gender": "M", "role": "object"},
        "a book": {"gender": "N", "role": "object"}
    }

    sentences = text.split(". ")

    resolved = [sentences[0]]

    last_subject = "Ravi"
    last_neutral = "a book"

    s2 = sentences[1]

    # Resolve pronouns
    s2 = s2.replace("He", last_subject)
    s2 = s2.replace("it", "the book")

    resolved.append(s2)

    return ". ".join(resolved)


print(resolve_references(
    "Ravi met Arun at the library. He borrowed a book and later returned it."
))
