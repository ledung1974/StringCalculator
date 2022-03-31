import sys
#-----------------------------------------------------------------
def sumArray(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum
#-----------------------------------------------------------------
def simpleAdd(str):
    strArray = str.split(',')  #"," is used to separate numbers 
    arrNumber = []
    exceptString = ""    
    for strNumber in strArray:
        try: 
            num = int(strNumber)
            if num < 0: #Negative number --> add to ExceptString  
                if exceptString == "":
                    exceptString += strNumber
                else:
                    exceptString += "," + strNumber
            if (num <= 1000)&(num >= 0): #numbers to add should be in range 0 .. 1000 
                arrNumber.append(num)
        except ValueError:
            sys.exit("Error: Can't convert String to Int! ("+ strNumber+")")
    
    if exceptString !="":
        ex = "Negatives not allowed:" + exceptString
        sys.exit(ex)
     
    return sumArray(arrNumber)
#-----------------------------------------------------------------
def removeNewLines(str):
    return str.replace("\\n","")
#-----------------------------------------------------------------
def processingDelimiters(str):
    if str[0:2] == "//":
        endDelimiters = str.find("\\n")
        if endDelimiters != -1:
            delimitersString = str[2:endDelimiters]
            delimitersArray = delimitersString.split(",")
            str = str[endDelimiters+2:]
            for element in delimitersArray :
                str = str.replace(element,",")
        else:
            str = ""
    return str
