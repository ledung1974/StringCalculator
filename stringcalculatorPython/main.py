import myfunctions as my

inputString = input("Enter String to calculate:")
print("Input String:", inputString)

str = my.processingDelimiters(inputString)
print(str)
str = my.removeNewLines(str)
print(str)
result = my.simpleAdd(str)
print("Result:",result)

