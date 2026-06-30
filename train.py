# TASK Z
def sum_evens(arr):
    return sum(num for num in arr if num % 2 == 0)

print(sum_evens([1, 2, 3]))  
print(sum_evens([5, 8, 12]))  













# TASK Y

# def findIntersection(A, B):
#     result = []

#     for ele in A:
#         if ele in B:
#             result.append(ele)
#     return result

# natija = findIntersection([1, 2, 3], [3, 2, 0]) 
# print(natija)


# TASK X

# def count_occurences(obj, target_key):
#     count = 0

#     for key, value in obj.items():
#         if (key == target_key):
#             count += 1
#         if isinstance(value, dict):
#             count += count_occurences(value, target_key)
#     return count


# result = count_occurences({"model": "A", "s": {"model": "B"}}, "model")
# print(result)

# TASK W

# def chunkArray(arr, size):
#     result = []

#     for i in range(0, len(arr), size):
#         result.append(arr[i: i + size])

#     return result


# result = chunkArray([1, 2, 3, 4, 5], 2)
# print(result)


# TASK V

# def countChars(text):
#     result = {}

#     for char in text:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1

#     return result


# result = countChars("hello")
# print(result)

# TASK T

# def mergeSortedArrays(ar1, ar2):
#   merge = ar1 + ar2
#   return sorted(merge)


# result = mergeSortedArrays([0, 3, 4], [4, 6])
# print(result)

#  Task S
# def missingNumber(num):
#     num.sort()
#     for i, val in enumerate(num):
#         if i != val:
#             return i

#     return len(num)

# result = missingNumber([0, 1, 2])
# print(result)

# TASK R
# def calculate(str):
#     brinchi_qadam = str.split()
#     chap_son = brinchi_qadam[0]
#     operatorr = brinchi_qadam[1]
#     ong_son = brinchi_qadam[2]

#     chap_son = int(brinchi_qadam[0])
#     ong_son = int(brinchi_qadam[2])

#     if operatorr == "+":
#         return chap_son + ong_son
#     elif operatorr == "-":
#         return chap_son - ong_son
#     elif operatorr == "*":
#         return chap_son * ong_son
#     elif operatorr == "/":
#         return chap_son / ong_son


# result = calculate("1 + 3")
# print(result)


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
