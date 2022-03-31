import sys

def stringAdd(str):
    if str[0:2] == "//":
        strStruc = str.split("\\n",1)
        if len(strStruc) == 2:
            delimitersString = strStruc[0][2:]
            delimitersArray = delimitersString.split(",")
            str = strStruc[1].replace("\\n","")
            for element in delimitersArray :
                str = str.replace(element,",")
        else:
            str = ""
    if str != "":        
        print("String Numbers to add:", str)
        strArray = str.split(',')
        exceptString = ""    
        sum = 0
        for str in strArray :
            try: 
                num = int(str)
                if num < 0 :
                    if exceptString == "": 
                        exceptString += str
                    else:
                        exceptString += "," + str
                if (num <= 1000)&(num >= 0) :
                    sum += num
            except ValueError:
                sys.exit("Can't convert String to Int")
        if exceptString !="" :
            ex = "Negatives not allowed:" + exceptString
            sys.exit(ex)
    else:
        sys.exit("Error: Something is wrong in format with // !")
    return sum

# Test with multiple-lines string
str = '''//#,@,***
1@2@
4#3***
5'''
print("String to add:",str)
str = str.replace("\n","\\n")
print("Result:",stringAdd(str))

#Test with string input from console
inputString = input("Enter String to calculate:")
print("Input String:", inputString)
print("Result:",stringAdd(inputString))

