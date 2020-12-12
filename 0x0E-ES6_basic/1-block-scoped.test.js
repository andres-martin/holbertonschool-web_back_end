const { default: taskBlock } = require("./1-block-scoped")

test('taskBlock-True', () => {
  expect(taskBlock(true)).toStrictEqual([false, true]);
});

test('taskBlock-False', () => {
  expect(taskBlock(false)).toStrictEqual([false, true]);
});
