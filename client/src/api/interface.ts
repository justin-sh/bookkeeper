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

export interface Expense {
  date: Date
  account: Record<'id' | 'name', any>
  category: Record<'id' | 'name', any>
  subcategory: Record<'id' | 'name', any>
  amount: number
  currency: Record<'id' | 'name', any>
  qty: number //cent unit
  note: string
}