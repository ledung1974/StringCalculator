import sys

def stringAdd(str):
    if str[0:2] == "//":
        strStruc = str.split("\\n",1)
        delimitersString = strStruc[0][2:]
        delimitersArray = delimitersString.split(",")
        str = strStruc[1].replace("\\n","")
        for element in delimitersArray :
            str = str.replace(element,",")
    
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
    
    return sum

inputString = input("Enter String to calculate:")
print("Input String:", inputString)
print("Result:",stringAdd(inputString))
