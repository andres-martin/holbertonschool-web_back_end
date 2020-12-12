const { getSumOfHoods } = require("./3-default-parameter");

test('get Sum', () => {
  expect(getSumOfHoods(2, 1, 1)).toBe(4);
  expect(getSumOfHoods(2,)).toBe(110);
});
