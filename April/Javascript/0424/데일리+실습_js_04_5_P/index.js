// 코드를 작성해 주세요

// 모달 가져와서 display를 none으로 바꿔주기
const modal = document.querySelector(".modal")

// 모달 안보이게 하기
modal.addEventListener("click", function(e) {
    modal.style.display = "none"
})

// 사람 점수판, 사람
const pScore = document.querySelector(".counA")
let countP = 0

// 컴퓨터 점수판, 점수
const cScore = document.querySelector(".countB")
let countC = 0

// 가위바위보의 승자를 정해주는 함수
const whoWin = function(player, computer) {
    let winner = ""

    let p = "player"
    let c = "computer"

    if (player==="scissors") {
        if (computer==="paper") {
            countP += 1
            winner = p
        }
        else if (computer === "rock") {
            countC += 1
            winner = c
        }
    }

    else if (player==="paper") {
        if (computer==="rock") {
            countP += 1
            winner = p
        }
        else if (computer === "scissors") {
            countC += 1
            winner = c
        }
    }

    else if (player==="rock") {
        if (computer==="scissors") {
            countP += 1
            winner = p
        }
        else if (computer === "paper") {
            countC += 1
            winner = c
        }
    }

    pScore.innerText = countP
    cScore.innerText = countC 

    return winner
}


// 이벤트 함수 만들기
const pickHand = (hand) => (e) => {
    console.log(e.target)
}


// 버튼 비활성화 (중복 클릭 방지)
document.querySelector('button')/forEach((button) {
    button.disabled = true
})

// 가위바위보
let userPuck = hand

const picks = ['scissors', 'paper', 'rock']


// 이미지 소스 바꿔줄 태그

// 깃랩 확인해보기....