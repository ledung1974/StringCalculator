//----------------------------------------
function sumArray (ar){
    let sum = 0;
    ar.forEach(num => {
        sum += num;
    });
    return sum;
}
//----------------------------------------
function simpleAdd(str) {
    const stringArray = str.split(",");
    let numberArray = [];
    let exceptionString = ""; 
    stringArray.forEach(element => {
        if (element.substr(0, 1) === "-") {
            //a negative number should throw an exception
            if (exceptionString === "") {exceptionString += element}
            else {exceptionString +="," + element};
        } else {
            let parsed = parseInt(element, 10);
            //Bonus: Numbers larger than 1000 should be ignored
            if (parsed > 0 && parsed <= 1000) {
                numberArray.push(parsed);
            }
        }
    });
    //Check exception string before add (sum)
    if (exceptionString ==="") {
        return sumArray(numberArray);
    }else{
        throw "Exception: Negatives not allowed with the input number(s): " + exceptionString;
    }
}
//Process delimiters
function processingDelimiters(str){
    if (str.substr(0, 2) === "//"){
        const endDelimiters = str.indexOf("\n");
        str = str.replace(/\*|\+|\%|\$|\^|\//g,"&");//Can add more
        let delimitersString = str.slice(2,endDelimiters); 
        let delimitersArray = delimitersString.split(/,/);
        str = str.slice(endDelimiters);
        delimitersArray.forEach(element => {
            let replacer = new RegExp(element,'g')
            str = str.replace(replacer,",");
        });
    }
    return str;
}
//-----------------------------------
function removeNewLines(str){
    return str.replace(/\n/g,"");;
}
//-----------------------------------
function generalAdd(str) {
    //Step 1: Processing Delimiters
    str = processingDelimiters(str);
    console.log("After processing delimiters :" + str.replace(/\n/g,"\\n"));
    
    //Step 2: Removing all new lines "\n"
    str = removeNewLines(str);
    console.log("After removing new-lines :" + str);
    
    //Step 3: Simple add with sum(array)
    let result ="";
    try {
        result = simpleAdd(str);
    } catch (e) {
        result = e;
    }
    return result;
}

module.exports = {
    generalAdd,
    removeNewLines,
    processingDelimiters,
    simpleAdd,
}