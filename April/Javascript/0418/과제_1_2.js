// 1번
const nums = [1,2,3,4,5,6,7,8]

for (const i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}

// for (const i = 0; i < nums.length; i++) {
// i의 형식을 지정해 주지 않았기 때문에 발생하는 에러이다.                                     ^

// TypeError: Assignment to constant variable.

// 2번
for (num in nums) {
  num = Number(num)
  console.log(num, typeof num)
}

// number 형태로 바꿔줌
// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
