/* eslint-disable jest/prefer-expect-assertions */
const { default: getFullBudgetObject } = require('./9-getFullBudget');

// eslint-disable-next-line jest/require-top-level-describe
test('object assignment', () => {
  const fullBudget = getFullBudgetObject(20, 50, 10);

  expect(fullBudget.getIncomeInDollars(fullBudget.income)).toBe('$20');
  expect(fullBudget.getIncomeInEuros(fullBudget.income)).toBe('20 euros');
});
