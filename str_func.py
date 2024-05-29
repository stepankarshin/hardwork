def upp_text(text):
    return text.upper()
"""моё крутое описание"""

def upp_first_letters(text):
    for i in range(len(text)):
        if text[i - 1] == ' ':
            text[i] = text[i].upper()
        text[0] = text[0].upper()
        return text
"""ещё одно моё крутое описание"""
