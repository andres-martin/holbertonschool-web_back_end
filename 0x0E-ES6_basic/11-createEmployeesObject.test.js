const { default: createEmployeesObject } = require("./11-createEmployeesObject");

test('loop', () => {
    expect(createEmployeesObject("Software", [ "Bob", "Sylvie" ])).toStrictEqual({ Software: [ 'Bob', 'Sylvie' ] });
  });

