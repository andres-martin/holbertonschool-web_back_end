const concatArrays = require("./5-spread-operator");

test('get Sum', () => {
    expect(concatArrays(['a', 'b'], ['c', 'd'], 'Hello')).toStrictEqual(["a", "b", "c", "d", "H", "e", "l", "l", "o"]);
  });
