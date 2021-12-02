const fs = require('fs');
const path = require('path');

startScript();

function startScript() {
    var input = getInput();
    var lines = getLinesFromInput(input);
    var numbers = parseStrArrayToNumArray(lines);
    var result = calcNumIncreasesCompToPrev(numbers);
    console.log(result);
}

function getInput() {
    return fs.readFileSync(path.join(__dirname, '../input.txt'), "utf-8");
}

function getLinesFromInput(input) {
    return input.split("\n");
}

function parseStrArrayToNumArray(strArray) {
    return strArray
        .map(str => parseInt(str, 10))
        .filter(number => !isNaN(number));
}

function calcNumIncreasesCompToPrev(numbers) {
    var result = 0;
    for (var i = 3; i < numbers.length; i++) {
    var prevSum = numbers[i-3];
    var currSum = numbers[i];

        if (currSum > prevSum) {
            result++;
        }
    }   
    return result;
}
