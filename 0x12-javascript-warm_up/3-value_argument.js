#!/usr/bin/node
const value = process.argv;
if (value.length === 2) {
  console.log('No argument');
} else {
  console.log(value[2]);
}
