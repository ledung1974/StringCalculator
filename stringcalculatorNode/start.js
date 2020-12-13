const { generalAdd } = require("./StringCalculate");
const prompt = require("prompt-sync")();
let inputString = prompt("Enter string to calculate: ");
console.log("Input: "+ inputString);
inputString = inputString.replace(/\\n/g,"\n");
let result = generalAdd(inputString);
console.log("Result: " + result); 