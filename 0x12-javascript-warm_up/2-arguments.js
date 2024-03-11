#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('No arguments');
} else if (args.length === 3) {
  console.log('Arguemnt Found');
} else {
  console.log('Arguments Found');
}
