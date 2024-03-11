#!/usr/bin/node
let val = process.argv[2];
let msg = 'Not a number';
if (val !== undefined) {
  val = parseInt(val, 10);
  if (!(isNaN(val))) {
    msg = `My number: ${val}`;
  }
}
console.log(msg);
