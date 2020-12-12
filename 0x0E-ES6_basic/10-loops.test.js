const { default: appendToEachArrayValue } = require("./10-loops");

test('loop', () => {
  expect(appendToEachArrayValue(["2"], "this is ")).toStrictEqual(["this is 2"]);
});
