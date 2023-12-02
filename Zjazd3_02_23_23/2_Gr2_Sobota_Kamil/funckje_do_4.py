def make_split(text: str) -> list:
    return text.split()

def no_of_words(text: list) -> int:
    return len(text)

def no_of_unique_elements(elements: list) -> int:
    return len(set(elements))

def clear_text(text: str) -> str:
    sings_to_delete = '.,:;?"\'(){}[]\\'
    for sign in sings_to_delete:
        text = text.replace(sign, '')
    text = text.lower()
    return text

def reps_of_words(text: list) -> dict:
    reps = {}
    for word in text:
        if word in reps.keys():
            reps[word] += 1
        else:
            reps[word] = 1
    return reps
