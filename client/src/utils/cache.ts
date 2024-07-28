// export const Cache = function () {
function save(k: string, v: any) {
    sessionStorage.setItem(k, JSON.stringify(v))
}

function get(k: string) {
    const v = sessionStorage.getItem(k) as string
    return JSON.parse(v);
}

function remove(k: string) {
    sessionStorage.removeItem(k)
}

export default {save, get, remove}
// }