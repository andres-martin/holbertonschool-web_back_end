import { createUser, uploadPhoto } from './utils';

const asyncUploadUser = async () => {
  let photo = null;
  let user = null;

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
