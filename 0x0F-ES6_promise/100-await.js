import { createUser, uploadPhoto } from './utils';

const asyncUploadUser = async () => {
  const photo = null;
  const user = null;

  const result = { photo, user };
  try {
    result.photo = await uploadPhoto();
    result.user = await createUser();
  } catch (error) {
    return result;
  }
  return result;
};

export default asyncUploadUser;
