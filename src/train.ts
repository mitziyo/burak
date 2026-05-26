// TASK 

function getSquareNumbers(numbers: number[]) {
    return numbers.map((num) => {
        return {
            number: num,
            square: num*num}

        
    });

}

const result = getSquareNumbers([1, 2, 3]);
console.log(result);