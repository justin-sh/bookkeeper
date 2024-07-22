import axiosFactory from 'axios'

import type {AxiosInstance} from 'axios'

import {stringify} from 'qs'

export const axios: AxiosInstance = axiosFactory.create({
    withCredentials: true,
    paramsSerializer: params => stringify(params, {arrayFormat: 'brackets', skipNulls: true})
})
