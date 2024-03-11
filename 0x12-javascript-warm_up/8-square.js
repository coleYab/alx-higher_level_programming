#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let msg = 'X';
  for (let i = 1; i < size; i++) {
    msg += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(msg);
  }
}
