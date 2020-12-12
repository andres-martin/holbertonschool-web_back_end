const { default: returnHowManyArguments } = require("./4-rest-parameter");

test('get Sum', () => {
    expect(returnHowManyArguments(2, 1, 1)).toBe(3);
  });
