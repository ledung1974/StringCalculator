let testCases = [
    "1,2,5",
    "1,3,5,7,9",
    "2,1001,3",
    "1\n,2,3",
    "1,\n2,4",
    "//;\n1;3;4",
    "//$\n1$2$3",
    "//@\n2@3@8",
    "//***\n1***2***3",
    "//$,@,*,^\n1$2@3*4^5",
    "//***,$$,@@\n1***2$$\n3@@4"
];

const {processingDelimiters, removeNewLines,simpleAdd } = require("./StringCalculate");
let i = 0;
testCases.forEach(element => {
    i += 1;
    console.log("Test case "+ i + " with string :" + element.replace(/\n/g,"\\n"));
    let str = processingDelimiters(element);
    str = removeNewLines(str);
    let result ="";
    try {
        result = simpleAdd(str);
    } catch (e) {
        result = e;
    }
    console.log("Result :" + result.toString());
});
