#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !h || !w) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.h; i++) {
      for (let x = 0; x < this.w; i++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
