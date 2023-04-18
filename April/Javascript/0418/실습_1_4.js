const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
    if (p1_choice==='rock') {
        if (p2_choice==='rock') {
            console.log(0)
        }
        else if (p2_choice==='paper') {
            console.log(2)
        }
        else {
            console.log(1)
        }
    }

    else if (p1_choice==='paper') {
        if (p2_choice==='paper') {
            console.log(0)
        }
        else if (p2_choice==='scissors') {
            console.log(2)
        }
        else {
            console.log(1)
        }
    }

    else {
        if (p2_choice==='scissors') {
            console.log(0)
        }
        else if (p2_choice==='rock') {
            console.log(2)
        }
        else {
            console.log(1)
        }
    }
}

for (let index = 0; index < 10; index++) {

    playGame(p1[index], p2[index])

}

// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
