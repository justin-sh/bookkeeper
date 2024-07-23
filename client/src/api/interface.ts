export interface LoginForm {
    name: string
    passwd: string
}

export interface User {
    name: string,
    passwd?:string,
    sec_tip?: string,
    sec_ans?: string
}

export type CurrencyType = 'AUD' | 'RMB'

export interface Account {
    name: string,
    // userId: number,
    currency: CurrencyType
    note?: string,
    balance: number
}