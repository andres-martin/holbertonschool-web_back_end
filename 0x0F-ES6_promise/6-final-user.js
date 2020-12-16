import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async (
  firstName = '',
  lastName = '',
  fileName = '',
) => {
  const data = await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((data) => {
    return data;
  });
};

export default handleProfileSignup;
