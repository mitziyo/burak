# TASK R
def calculate(str):
    brinchi_qadam = str.split()
    chap_son = brinchi_qadam[0]
    operatorr = brinchi_qadam[1]
    ong_son = brinchi_qadam[2]

    chap_son = int(brinchi_qadam[0])
    ong_son = int(brinchi_qadam[2])

    if operatorr == "+":
        return chap_son + ong_son
    elif operatorr == "-":
        return chap_son - ong_son
    elif operatorr == "*":
        return chap_son * ong_son
    elif operatorr == "/":
        return chap_son / ong_son


result = calculate("1 + 3")
print(result)


# Task Q
# def hasProperty(obj, propName):

#     for key in obj:
#         if key == propName:
#             return True

#     return False


# result = hasProperty({"name": "BMW"}, "name")
# print(result)
# TASK P

# def objectToArray(obj):
#     ready = []

#     for key, value in obj.items():
#         ready.append([key, value])


#     return ready


# result = objectToArray({"a": 10, "b": 20})
# print(result)


# TASK O
# def calculateSumOfNumbers(arr):
#     total = 0

#     for item in arr:
#         if type(item) == int or type(item) == float:
#             total = total + item

#     return total


# result = calculateSumOfNumbers([10, "10", {"son": 10}, True, 35])

# print(result)


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
