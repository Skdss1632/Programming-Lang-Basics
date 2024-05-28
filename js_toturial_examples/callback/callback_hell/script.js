function getData(dataId, getNextData){
    setTimeout(() => {
        console.log("data", dataId);
        if (getNextData){
            getNextData();
        }
    }, 2000);
}


//promise chain

getData(1).then((res) => {
    return getData(2);
})

.then((res) => {
    return getData(3);
})

.then((res) => {
    console.log(res);

});

// given is callback hell program example
// getData(1, () => {
//     console.log("getting data2...");
//     getData(2, () => {
//         console.log("getting data3...");
//         getData(3, () => {
//             console.log("getting data4...");
//             getData(4);
//         });
//     });
// });