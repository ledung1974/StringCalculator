const {simpleAdd, generalAdd} = require("./StringCalculate");
const simpleTest = [
    {
        "input":"1,3,7",
        "result":11
    },
    {
        "input":"3,1001,4,1000",
        "result":1007
    }
]
//Testing simpleAdd
simpleTest.forEach(e =>{
    test('simpleAdd ['+e.input+'] = '+ e.result, () => {
        expect(simpleAdd(e.input)).toBe(e.result);
    });
})

//Testing simpleAdd with exception negatives numbers
test('simpleAdd ["1,-2,3,4,-5"] >> Exception', () => {
    expect(() => simpleAdd("1,-2,3,4,-5"))
     .toThrow(new TypeError('Negatives not allowed with the input number(s): -2,-5'));
});

test('simpleAdd ["-1,2,-3,4"] >> Exception', () => {
    expect(() => simpleAdd("-1,2,-3,4"))
     .toThrow(new TypeError('Negatives not allowed with the input number(s): -1,-3'));
});

//General testing simpleAdd with exception negatives numbers
const testCases = [
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
    "//***,$$,@@\n1***2$$\n3@@4",
    "1,-2,3,-4,5,-6"
];
const resultCases = [8,25,5,6,7,8,6,13,6,15,10,"Negatives not allowed with the input number(s): -2,-4,-6"];
 
for (let i=0;i<testCases.length;++i){
    test('generalAdd ['+testCases[i]+'] = '+ resultCases[i], () => {
        expect(generalAdd(testCases[i])).toBe(resultCases[i]);
      });
}
