// Install: npm install xlsx
var XLSX = require("xlsx");
const fs = require("fs");
var workbook = XLSX.readFile("data.xlsx");
var sheet_name_list = workbook.SheetNames;
console.log(sheet_name_list); // getting as Sheet1
var headers = {};
var data = [];
sheet_name_list.forEach(function (y) {
  var worksheet = workbook.Sheets[y];
  //getting the complete sheet
  // console.log(worksheet);

  for (z in worksheet) {
    if (z[0] === "!") continue;
    //parse out the column, row, and value
    var col = z.substring(0, 1);
    // console.log(col);

    var row = parseInt(z.substring(1));
    // console.log(row);

    var value = worksheet[z].v;
    // console.log(value);

    //store header names
    if (row == 1) {
      headers[col] = value;
      // storing the header names
      continue;
    }

    if (!data[row]) data[row] = {};
    data[row][headers[col]] = value;
  }
  //drop those first two rows which are empty
  data.shift();
  data.shift();
  console.log(data);
});

var jsonContent = JSON.stringify(data);
console.log(jsonContent);

// jsonContent.forEach(async (data) => {
  // await fs.writeFileSync("/tmp/data",data);
 fs.writeFileSync("./data.json", jsonContent, null, 2, "utf-8");
// });
