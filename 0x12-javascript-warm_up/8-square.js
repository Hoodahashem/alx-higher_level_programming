#!/usr/bin/node

const count = process.argv;

if (count.length <= 2) {
  console.log('Missing size')
} else if (isNaN(count[2])) {
  console.log('Missing size')
} else {
  for (let i = 0; i < Number(count); i++) {
    for (let x = 0; x < Number(count); x++) {
      process.stdout.write('#');
    }
    process.stdout.write('\n');
  }
}
