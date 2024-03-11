#!/usr/bin/node
const args = process.argv;
let val = 'undefined';
let val2 = 'undefined';
if (args.length === 3) {
  val = args[2];
} else if (args.length >= 4) {
  val = args[2];
  val2 = args[3];
}
console.log(`${val} is ${val2}`);
