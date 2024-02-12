#!/usr/bin/node

function second (myArray) {
  if (myArray.length <= 2) { return (0); }

  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < myArray.length; i++) {
    if (myArray[i] > max) {
      secondMax = max;
      max = myArray[i];
    } else if (myArray[i] > secondMax && myArray[i] < max) {
      secondMax = myArray[i];
    }
  }
  return (secondMax);
}

console.log(second(process.argv.slice(2).map(Number)));
