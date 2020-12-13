import sys

def sumArray(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum

def simpleAdd(str):
    strArray = str.split(',')
    arr = []
    exceptString = ""    
    for str in strArray :
        try: 
            num = int(str)
            if num < 0 :
                if exceptString == "": 
                    exceptString += str
                else:
                    exceptString += "," + str
            if (num <= 1000)&(num >= 0) :
                arr.append(num)
        except ValueError:
            sys.exit("Can't convert String to Int")
    if exceptString !="" :
        ex = "Negatives not allowed:" + exceptString
        sys.exit(ex)
    sum = sumArray(arr)
    return sum

def removeNewLines(str):
    return str.replace("\\n","")

def processingDelimiters(str):
    if str[0:2] == "//":
        endDelimiters = str.index("\\n")
        delimitersString = str[2:endDelimiters]
        delimitersArray = delimitersString.split(",")
        str = str[endDelimiters+2:]
        for element in delimitersArray :
            str = str.replace(element,",")
    return str
