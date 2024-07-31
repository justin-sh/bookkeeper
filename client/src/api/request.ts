import {axios} from '@/utils/axios'

import {type User, type Account, type LoginForm, type Expense} from "@/api/interface";


export const userLogin = (data: LoginForm) => axios.post<User>('/auth/login', data)

export const userRegister = (data: User) => axios.post<User>('/auth/register', data)

export const getUserInfo = () => axios.get<User>('/auth/user-info')

export const getAccounts = () => axios.get<Account[]>('/accounts/')
export const getAllOptions = () => axios.get<Record<'id' | 'name', any>[]>('/options/all')
export const getOptions = (type: string, parent: string) => axios.get<Record<'id' | 'name', any>[]>('/options/', {
        params: {
            type,
            parent
        }
    }
)

export const getExpenses = () => axios.get<Expense[]>('/expenses/')
export const createExpense = (data: Expense) => axios.post<Record<'id', number>>('/expenses/create', data)