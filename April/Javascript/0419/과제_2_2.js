for (let index = 5; index >0; index--) {
    for (let i = 0; i<index-1; i++) {
        process.stdout.write(" ")
    }
    for (let k=0; k<(9-(index-1)*2); k++) {
        process.stdout.write("*")
    }  
    console.log()
}

