#!/usr/bin/node
const val = parseInt(process.argv[2]);
if (isNaN(val)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
}
