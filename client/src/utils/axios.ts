import axiosFactory, {AxiosError} from 'axios'

import type {AxiosInstance} from 'axios'

import {stringify} from 'qs'

export const axios: AxiosInstance = axiosFactory.create({
    baseURL: 'http://192.168.1.2:5000',
    withCredentials: true,
    paramsSerializer: params => stringify(params, {arrayFormat: 'brackets', skipNulls: true})
})

axios.interceptors.response.use((resp) => resp, (error) => {
    if(error instanceof AxiosError){
        if(error.response?.status === 401){
            window.location.href = '/login'
            return
        }
    }
    console.log(error)
})

