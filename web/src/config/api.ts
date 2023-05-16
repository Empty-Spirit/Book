import axiosInstance, { AxiosResponseProps } from './request';
import { apiUrl } from './url';

export const getTest = () => {
	return axiosInstance.get(apiUrl.TEST_PROXY);
};