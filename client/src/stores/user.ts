import {acceptHMRUpdate, defineStore} from 'pinia';
import {reactive} from 'vue';

import {type LoginForm, type User, userLogin, getUserInfo} from "@/api"

const anonymous: User = {name: ''}

export const useUserStore = defineStore('user', () => {
    /** @type { {id:string, name:string, email:string, imageUrl:string, isAdmin:boolean} } */
    let user = reactive(anonymous);

    async function login(loginForm: LoginForm) {
        const resp = await userLogin(loginForm)

        if (resp.status < 200 || resp.status > 300 || 'errorMsg' in resp.data) {
            console.log(`login failed! reason:${resp.statusText}`)

            return false
        }

        user = resp.data
        this.$patch({...resp})

        saveUserinfo(resp.data)

        return true
    }

    // @ts-ignore
    async function refresh() {

        const _userinfo = getUserinfoFromLocal()
        if (_userinfo && Object.prototype.hasOwnProperty.call(_userinfo, 'name')) {
            user = _userinfo
            return
        }

        user = (await getUserInfo()).data
        this.$patch({...user})

        saveUserinfo(user)
    }

    function getUserinfoFromLocal(): User {
        return JSON.parse(sessionStorage.getItem('userinfo'))
    }

    function saveUserinfo(userinfo: User) {
        sessionStorage.setItem('userinfo', JSON.stringify(userinfo))
    }

    async function logout() {

        // (await axios.post('/api/logout')).data
        //
        // this.user = anonymous
        // this.$patch(this.user)
        //
        // saveUserinfo(anonymous)
    }

    return {user, refresh, login, logout}
})

// @ts-ignore
if (import.meta.hot) {
    // @ts-ignore
    import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot))
}
