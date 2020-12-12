const {taskFirst, getLast, taskNext} = require("./0-constants")

test('taskFirst', () => {
  expect(taskFirst()).toBe('I prefer const when I can.');
});

test('getLast', () => {
  expect(getLast()).toBe(' is okay');
});

test('taskNext', () => {
  expect(taskNext()).toBe('But sometimes let is okay');
});
