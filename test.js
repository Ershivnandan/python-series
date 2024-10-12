// function solve(k){
//     let left = 0;
//   let right = Math.floor(Math.sqrt(k));

//   while (left <= right) {
//     const sumOfSquares = left * left + right * right;
//     if (sumOfSquares === k) {
//       return true;
//     } else if (sumOfSquares < k) {
//       left++;
//     } else {
//       right--;
//     }
//   }

//   return false;
// }


// n = 5

// for(let i=1; i<=n; i++){
//   let flag = false
//   str = ''
//     for(j=1; j<=i; j++){
//       if(flag == true){
//         str +='0'
//         flag= false
//       }
//       else{
//         str += '1'
//         flag = true
//       }
//     }
//   console.log(str)
// }



// *
// *
// *
// *
// *
// *
// * * * * * * *

// n = 5 

// for(let i=1; i<=5; i++){
//   console.log('*')
  
//   if(i==5){
//     str= ''
//     for(j=1; j<=5; j++){
//       str += '* '
//     }
//     console.log(str)
//     break
//   }
// }


// let i = 1;

// while(i <= n){
//   console.log('*');

//   if(i==5){
//     str = ""
//     let j = 1

//     while(j<=n){
//       str += '* '
//       j++
//     }
//     console.log(str)
//     break
//   }
//   i++
// }


// const print2largest = (arr) => {
       
//   let n = arr.length
//   let max_num1 = arr[0]
//   let max_num2 = arr[0]
    
//   for(let i=1; i<n; i++){
//       if(arr[i] > max_num1){
//         max_num1 = arr[i]
//       }
//       if(arr[i] > max_num2 && max_num1 > arr[i]){
//         max_num2 = arr[i]
//       }
//   }
//   return max_num2
// }

// arr = [2192, 13849, 3443, 20919, 10086, 31384, 4405]
// res = print2largest(arr)

// console.log(res)
 

const crypto = require('crypto');
const secretKey = crypto.randomBytes(32).toString('hex'); // 32 bytes key
console.log(secretKey);
