# TASK L
def reverseSentence(text):
    words = text.split()
    result = []

    for element in words:
        element[::-1]
        result.append(element)

    return " ".join(result)


print (reverseSentence("we like cding"))
