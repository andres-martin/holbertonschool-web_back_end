const weakMap = new WeakMap();

const queryAPI = (endpoint) => {
  const total = weakMap.get(endpoint) || 0;
  if (total >= 5) throw new Error('Endpoint load is high');
  weakMap.set(endpoint, total + 1);
};

export { weakMap, queryAPI };
