import axiosInstance, { AxiosResponseProps } from './request';
import { apiUrl } from './url';

export const getTest = () => {
	return axiosInstance.get(apiUrl.TEST_PROXY);
};

export const getBook = (params: any) => {
	return axiosInstance.get(apiUrl.SEARCH_BOOK, { params: params });
};