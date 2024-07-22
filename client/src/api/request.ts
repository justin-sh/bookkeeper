import {axios} from '@/utils/axios'

import {type User, type Account, type LoginForm} from "@/api/interface";


export const login = (data: LoginForm) => axios.post<User>('/auth/login', data)

export const getAccounts = () => axios.get<Account[]>('/accounts')