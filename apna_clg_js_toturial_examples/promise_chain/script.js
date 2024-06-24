function asyncFunc1(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("some data1");
            resolve("success");
            }, 3000);
        });
}

function asyncFunc2(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("some data2");
            resolve("success");
            }, 3000);
        });
}



console.log("fetching data1...");
asyncFunc1().then((res) => {
    console.log("fetching data2...");
    asyncFunc2().then((res) => {});
    // console.log(res);
});