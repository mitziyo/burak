// TASK N

function palindromeCheck(str: String) {
  const rev_text = str.split("").reverse().join("")
  return str == rev_text
}

const result = palindromeCheck("dad");
console.log("result:", result);

// TASK

// function getSquareNumbers(numbers: number[]) {
//     return numbers.map((num) => {
//         return {
//             number: num,
//             square: num*num}

//     });

// }

// const result = getSquareNumbers([1, 2, 3]);
// console.log(result);
