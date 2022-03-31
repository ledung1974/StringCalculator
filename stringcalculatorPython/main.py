import myfunctions as my

inputString = input("Enter string to calculate:")

#Step by step to process the input string 
str = my.processingDelimiters(inputString)
print("After processing delimiters:" + str)
if str != "":
    str = my.removeNewLines(str)
    print("After removing newLines:" +str)
    result = my.simpleAdd(str)
    print("Result:",result)
else:
    print("Error: Something is not right in format with //!")

