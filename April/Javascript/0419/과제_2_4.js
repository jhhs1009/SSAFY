// 이곳에 코드를 작성합니다.
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // solution 함수 완성
  let i = 0
  let cnt = 0

  while (i<N) {
    let flag = 0
    for (let j = K; j > 0; j--) {
      for (let w=0; w<M; w++){
        if (i+j === chargers[w]) {
          i = i+j
          cnt += 1
          flag += 1 
          break
        }
      }
    }

    if (i==chargers[M-1]){
      cnt -= 1
      break
    }

    if (flag === 0) {
      cnt = 0
      break
      }
    
    }

    
  return console.log(`#${cnt}`)
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}