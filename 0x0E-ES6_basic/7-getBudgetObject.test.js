const { default: getBudgetObject } = require("./7-getBudgetObject");

test('object assignment', () => {
  expect(getBudgetObject(1, 2, 3)).toEqual({"income": 1, "gdp": 2, "capita": 3});
});
