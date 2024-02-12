#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv.length === 1)
{
  console.log(0);
} else {
  let biggest = 0;
  for (let i = 2; i < process.argv.length - 1; i++)
  {
    if (process.argv[i] >= biggest)
    {
      biggest = process.argv[i];
    }
  }
  let lst = splice(indexof(biggest),1)
  sec = 0;
  for (let x = 0; x < lst.length - 1; x++)
  {
    if (lst[x] > sec)
    {
      sec = lst[x];
    }
  }
}
