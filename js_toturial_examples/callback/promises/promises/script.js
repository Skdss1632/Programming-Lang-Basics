// promises has three state pending, resolve,rejected..
let promise = new promise((resolve, reject) => {
    console.log("i am a promise");
    reject("some error occured");
    // resolve("success");
});