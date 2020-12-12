const { default: getBudgetForCurrentYear } = require("./8-getBudgetCurrentYear");

test('object assignment', () => {
  expect(getBudgetForCurrentYear(1, 2, 3)).toEqual({"income-2020": 1, "gdp-2020": 2, "capita-2020": 3});
});
