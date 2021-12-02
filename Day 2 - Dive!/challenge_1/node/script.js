const fs = require('fs');
const path = require('path');

var text = fs.readFileSync(path.join(__dirname, '../input.txt'), "utf-8");
var lines = text.split("\n");


lines = lines.filter(line => {
    return line != "";
});

var depth = 0;
var horz = 0;

for (var i = 0; i < lines.length; i++) {

    var re = /^(\w+?)\s(\d+)$/g;
    var str = lines[i];
    var match = re.exec(str);

    var command = match[1];
    var number = parseInt(match[2], 10);

    if (command == "forward") {
        horz += number;
    } else if (command == "down") {
        depth += number;
    } else if (command == "up") {
        depth -= number;
    }
}

console.log(depth*horz);