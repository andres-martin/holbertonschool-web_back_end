import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async (
  firstName = '',
  lastName = '',
  fileName = '',
) => {
  const result = [];
  try {
    const user = await signUpUser(firstName, lastName);
    result.push({ status: 'fullfilled', value: user });
    await uploadPhoto(fileName);
  } catch (error) {
    result.push({
      status: 'rejected',
      value: `Error: ${fileName} cannot be processed`,
    });
  }
  return result
};

export default handleProfileSignup;
