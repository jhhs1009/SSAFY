/*
promise 객체 사용법
new promise((resolve, reject) => {

    if (성공) {
        return resolve(value) => 비동기 작업이 성공했을 때 리턴하고 싶은 값은 value로
    } else if (실패조건) {
        return resolve(value) => 비동기 작업이 실패했을 때 리턴하고 싶은 값은 value로
    }
})

axios.get() 이 함수도 return 값이 promise 객체 였기 때문에 .then, .catch 사용 가능
*/


const water = function() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("A : 물을 넣는다.")
            return resolve(['물'])
        }, Math.random * 2000 + 1000)
    })
}

const soup = function() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("현재 재료 : ", ramen)
            console.log("B : 스프을 넣는다.")
            return resolve(['물'])
        }, Math.random * 2000 + 1000)
    })
}

