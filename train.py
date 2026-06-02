# TASK O
def calculateSumOfNumbers(arr):
    total = 0

    for item in arr:
        if type(item) == int or type(item) == float:
            total = total + item

    return total


result = calculateSumOfNumbers([10, "10", {"son": 10}, True, 35])

print(result)


#  TASK N

# def palindromeCheck(text):
#     rev_text = text[::-1]
#     return text == rev_text
# print(palindromeCheck("dad"))


# TASK M

# def getSquareNumbers(arr):
#     getNumber = []
#     for element in arr:
#         result = element*element
#         obj_dict = {
#             "number": element,
#             "square": result

#         }
#         getNumber.append(obj_dict)
#     return getNumber


# print(getSquareNumbers([1, 2, 3]))


# TASK L
# def reverseSentence(text):
#     words = text.split()
#     result = []

#     for element in words:
#         element[::-1]
#         result.append(element)

#     return " ".join(result)


# print (reverseSentence("we like cding"))
