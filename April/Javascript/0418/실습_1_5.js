const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// 3
// 100
// 62


for (let index = 0; index < participantNums.length; index++) {
    const dic = {}
    for (let j = 0; j < participantNums[index].length; j++) {
        if (participantNums[index][j] in dic) {
            dic[participantNums[index][j]] = dic[participantNums[index][j]] + 1
        } 
        else {
            dic[participantNums[index][j]] = 1
        }
        
    }

    for (k in dic) {
        if (dic[k] %2 == 1) {
            console.log(k)
        }
    } 
        
    
}

