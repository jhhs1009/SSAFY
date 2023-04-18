for (let index = 1; index < 6; index++) {
    for (let i = 0; i<index; i++) {
        if (i==index-1) {
            console.log("*")
        }
        else {
            process.stdout.write("*")
        }   
    }
}