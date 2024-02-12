#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv.length <= 3)
{
  console.log(0);
} else {
  let biggest = 0;
  for (let i = 2; i < process.argv.length; i++)
  {
    if (biggest < process.argv[i])
    {
      biggest = process.argv[i]
    }
  }
  let secondbiggest = 0
  for (let x = 0; x < process.argv.length; x++) {
    if (process.argv[x] !== biggest && secondbiggest < process.argv[x])
    {
      secondbiggest = process.argv[x]
    }
  }
  console.log(secondbiggest)
}
