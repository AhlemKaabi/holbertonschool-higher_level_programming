#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbocc = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      nbocc = nbocc + 1;
    }
  }
  return nbocc;
};
