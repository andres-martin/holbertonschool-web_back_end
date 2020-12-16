import { createUser, uploadPhoto } from './utils';

const asyncUploadUser = async () => {
  const result = {
    photo: null,
    user: null,
  };

  try {
    result.photo = await uploadPhoto();
    result.user = await createUser();
    return result;
  } catch (error) {
    return result;
  }
};

export default asyncUploadUser;
