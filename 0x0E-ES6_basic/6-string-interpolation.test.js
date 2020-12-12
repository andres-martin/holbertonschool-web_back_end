const getSan = require("./6-string-interpolation");

test('get SanFrancisco', () => {
    expect(getSan())
    .toStrictEqual("As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.");
  });
