import {acceptHMRUpdate, defineStore} from 'pinia';
import {reactive} from 'vue';

import {type LoginForm, type User, userLogin} from "@/api"

const anonymous: User = {name: ''}

export const useUserStore = defineStore('user', () => {
    /** @type { {id:string, name:string, email:string, imageUrl:string, isAdmin:boolean} } */
    let user = reactive(anonymous);

    async function login(loginForm: LoginForm) {
        const resp = await userLogin(loginForm)

        if (resp.status < 200 || resp.status > 300) {
            console.log(`login failed! reason:${resp.statusText}`)

            return false
        }
        user = resp.data
        this.$patch({...resp})

        setUserinfo(resp.data)

        return true
    }

    // @ts-ignore
    async function refresh() {

        // const _userinfo = getUserinfo()
        // if (_userinfo && _userinfo.hasOwnProperty('id') && _userinfo.id > 0) {
        //     this.user = _userinfo
        //     return
        // }
        //
        // const user = (await axios.get('/api/user/info')).data
        // this.user = user
        // this.$patch({...user})
        //
        // setUserinfo(user)
    }

    function getUserinfo(): User {
        return JSON.parse(sessionStorage.getItem('userinfo'))
    }

    function setUserinfo(userinfo: User) {
        sessionStorage.setItem('userinfo', JSON.stringify(userinfo))
    }

    async function logout() {

        // (await axios.post('/api/logout')).data
        //
        // this.user = anonymous
        // this.$patch(this.user)
        //
        // setUserinfo(anonymous)
    }

    return {user, refresh, login, logout}
})

// @ts-ignore
if (import.meta.hot) {
    // @ts-ignore
    import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot))
}
