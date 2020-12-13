import { generalAdd } from "./myscript.js";
import {testCases} from "./testcases.js";

export function testRun() {
    testCases.forEach(element => {
        let h2Test = document.createElement("H2");
        h2Test.setAttribute("class", "h2-test");
        h2Test.innerHTML = "Input: " + element.replaceAll("\n","\\n");
        document.getElementById("test-container").appendChild(h2Test);

        let result = generalAdd(element);

        let pResult = document.createElement("P");
        pResult.setAttribute("class", "p-result");
        pResult.innerHTML = "Result: " + result;
        document.getElementById("test-container").appendChild(pResult);
    });
} 