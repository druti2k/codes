//####3 ----------------------------------->>>>>>>>>>>>>>DataTypes<<<<<<<<<<<<-----------------------------------------###
// #####--------->>>>>>List(Arrays)<<<<<<<--------------#####

// let pracList = ["ram", "shiva", "shyam"];

// console.log(pracList.indexOf("ram"));

// // // Looping
// for (let i = 0; i < pracList.length; i++) {
//   console.log(pracList[i]);
// }

// pracList.forEach(item => console.log(item));
 
// // #####--------->>>>>>Tuples (use Arrays in JS)<<<<<<<--------------#####
// let tup = [1233, 33, 44, 53, 5, 66];
// console.log(tup.slice(1)); // Equivalent slicing

// // #####--------->>>>>>Dictionaries (Objects)<<<<<<<--------------#####
// let employeeData = { name: "Subham", age: 24, sex: "male" };
// console.log(employeeData);

// // Iteration
// for (let key in employeeData) {
//   console.log(key + ": " + employeeData[key]);
// }

// // #####--------->>>>>>Sets<<<<<<<--------------#####
// let avengers = new Set(["Ironman", "Loki", "Thar"]);
// avengers.add("Hulk");
// avengers.delete("Thar");

// for (let item of avengers) {
//   console.log(item);
// }
// // #####--------->>>>>> Functions<<<<<<<--------------#####
// function hello() {
//   console.log("Druti");
// }
// hello();

// function add(x, y) {
//   console.log(x + y);
// }
// add(10, 22);
// // #####--------->>>>>>Recursion<<<<<<<--------------#####
// function fact(n) {
//   if (n === 1) return 1;
//   else return n * fact(n - 1);
// }
// console.log(fact(5));

// // #####--------->>>>>> Arrow Functions<<<<<<<--------------#####
// let a = b => b * 5;
// console.log(a(4));

// let x = (d, e, f) => (d + e) * f;
// console.log(x(3, 4, 5));

// // #####--------->>>>>>Global vs Local Variables<<<<<<<--------------#####
// let x = 2;
// function localVar() {
//   let x = 3;
//   return x;
// }
// console.log(localVar());

// let e = 4;
// function globalVar() {
//   e = 5;
// }
// globalVar();
// console.log(e);
// // #####--------->>>>>>Built-in Modules (Date, Math, Random)<<<<<<<--------------#####

// let now = new Date();
// console.log(now);

// let rand = Math.floor(Math.random() * 10) + 1;
// console.log(rand);

// console.log(Math.min(1, 2, 3));
// // #####--------->>>>>>NumPy-like Array with JS (2D Arrays)<<<<<<<--------------#####

// let a = [20, 12, 33];
// let b = [21, 42, 65];
// let result = a.map((num, i) => num + b[i]);
// console.log(result);

// let d = [
//   [11, 33, 23],
//   [21, 4, 21]
// ];
// console.log(d[1].slice(0, 3));

// // #####--------->>>>>> Fibonacci Series<<<<<<<--------------#####
// let n = parseInt(prompt("Enter a number:"));
// let a1 = 0, b1 = 1;
// console.log(a1);
// console.log(b1);
// for (let i = 2; i < n; i++) {
//   let c = a1 + b1;
//   console.log(c);
//   a1 = b1;
//   b1 = c;
// }
// // #####--------->>>>>>Prime Number Check<<<<<<<--------------#####

// let n1 = parseInt(prompt("Enter a number:"));
// let isPrime = true;
// if (n1 <= 1) {
//   isPrime = false;
// } else {
//   for (let i = 2; i < n1; i++) {
//     if (n1 % i === 0) {
//       isPrime = false;
//       break;
//     }
//   }
// }
// console.log(n1, isPrime ? "is a prime number" : "is not a prime number");

