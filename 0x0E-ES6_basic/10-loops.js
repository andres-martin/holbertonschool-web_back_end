export default function appendToEachArrayValue(array, appendString) {
  const temp = array;
  for (const value of array) {
    const i = array.indexOf(value);
    temp[i] = appendString + value;
  }

  return temp;
}
