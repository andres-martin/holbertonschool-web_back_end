import ClassRoom from './0-classroom.js';

const initializeRooms = () => {
  const array = [19, 20, 34];

  return array.map((n) => new ClassRoom(n));
}

export default initializeRooms;
