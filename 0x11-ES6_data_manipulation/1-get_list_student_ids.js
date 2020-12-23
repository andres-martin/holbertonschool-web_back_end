const getListStudentIds = (listOfStudents) => (arr && Array.isArray(arr) ?
  listOfStudents.map((item) => item.id) : []);
export default getListStudentIds;
