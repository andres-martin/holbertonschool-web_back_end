const getStudentIdsSum = (list) => list.reduce((total, student) => total + student.id);

export default getStudentIdsSum;
