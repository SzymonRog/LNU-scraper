function sumMatrix(matrix) {
    let suma = 0
    for(let i = 0; i < matrix.length; i ++){
        for(let j = 0; j < matrix[i].length; j ++){
            suma += matrix[i][j]
        }
    }
    return suma
}