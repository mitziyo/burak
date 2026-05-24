# TASK M

def getSquareNumbers(arr):
    getNumber = []
    for element in arr:
        result = element*element
        obj_dict = {
            "number": element,
            "square": result

        }
        getNumber.append(obj_dict)
    return getNumber


print(getSquareNumbers([1, 2, 3]))


# TASK L
# def reverseSentence(text):
#     words = text.split()
#     result = []

#     for element in words:
#         element[::-1]
#         result.append(element)

#     return " ".join(result)


# print (reverseSentence("we like cding"))
