import {axios} from '@/utils/axios'

import {type User, type Account, type LoginForm} from "@/api/interface";


export const userLogin = (data: LoginForm) => axios.post<User>('/auth/login', data)

export const userRegister = (data: User) => axios.post<User>('/auth/register', data)

export const getAccounts = () => axios.get<Account[]>('/accounts')