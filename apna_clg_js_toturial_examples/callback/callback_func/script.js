//a callback is a func passed as an argumant to another func

// given example is for syncronous programming callback func
function sum(a,b){
    console.log(a + b);
}

function calculator(a, b, sumCallback){
    sumCallback(a, b);
}

calculator(1, 2, sum);

// asyncronous in callback func example:-

// const hello = () => {
//     console.log('hello');
// };

// setTimeout(hello, 3000);