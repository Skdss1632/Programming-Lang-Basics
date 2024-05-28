const getPromise = () => {
    return new Promise((resolve, reject) => {
        console.log("i am a promise");
        // resolve("success");
        reject("network error");
    });
};

let promise = getPromise();
promise.then((res) => {
    console.log("promise fulfiled", res);
});

promise.catch((err) => {
    console.log("promise rejected", err);
});