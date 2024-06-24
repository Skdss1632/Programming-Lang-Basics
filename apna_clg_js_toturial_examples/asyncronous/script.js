console.log("one");
console.log("two");


//async means 1 to 4 will print and parallely wait for 4 seconds and then print hello 
setTimeout(() =>{
    console.log("hello");
}, 4000);  //4000ms == 4seconds


console.log("three");
console.log("four");