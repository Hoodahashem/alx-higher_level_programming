#!/usr/bin/node

const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
