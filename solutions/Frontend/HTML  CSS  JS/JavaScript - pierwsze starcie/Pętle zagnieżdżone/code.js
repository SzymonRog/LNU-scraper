function numbersToStars(n) {
    let arr = []
    for(let i = 0; i < n.length; i ++){
        let string = ""
        for(let j = 0; j < n[i]; j ++){
            string += "*"
        }
        arr[i] = string
    }
    return arr
}