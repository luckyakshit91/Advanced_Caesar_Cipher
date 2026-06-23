from collections import Counter


def frequency_analysis(text):

    letters = [c.upper() for c in text if c.isalpha()]

    count = Counter(letters)

    output = ""

    for char, value in count.items():
        output += f"{char} : {value}\n"

    return output