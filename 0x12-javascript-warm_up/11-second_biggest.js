#!/usr/bin/node

/**
 * Script that finds and prints the 2nd biggest
 * integer in a list of CL args.
 */

let nextBigest = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  nextBigest = args[args.length - 2];
}
console.log(nextBigest);
