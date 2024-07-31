export interface LoginForm {
    name: string
    passwd: string
}

export interface User {
    id: number
    name: string
    passwd?: string
    sec_tip?: string
    sec_ans?: string
}

export type CurrencyType = 'AUD' | 'RMB'

export interface Account {
    id: number
    name: string
    // userId: number,
    // currency: CurrencyType
    desc?: string
    balance: number
}

export interface Expense {
    id: number
    date: Date
    account: Record<'id' | 'name', any>
    category: Record<'id' | 'name', any>
    subcategory: Record<'id' | 'name', any>
    amount: number
    currency: Record<'id' | 'name', any>
    qty: number //cent unit
    note: string
}