import myfunctions as my

testCases = [   
    "1,2,5",
    "1,3,5,7,9",
    "0,2,1001,3",
    "1\n,2,3",
    "1,\n2,4",
    "//;\n1;3;4",
    "//$\n1$2$3",
    "//@\n2@3@8",
    "//***\n1***2***3",
    "//$,@,*,^\n1$2@3*4^5",
    "//***,$$,@@\n1***2$$\n3@@4",
    "1,-2,3,-4,6,-5"
]

i = 0
for element in testCases:
    i += 1
    element = element.replace("\n","\\n")
    print("Test case",i,"with string:",element)
    str = my.processingDelimiters(element)
    str = my.removeNewLines(str)
    result = my.simpleAdd(str)
    print("Result :", result)
