words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    let element = ""

    for (let index = word.length-1; index >= 0; index--) {
        element = element+word[index];
    }
    if (element===word) {
        return true
    }
    else {
        return false
    }


  }
  
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
