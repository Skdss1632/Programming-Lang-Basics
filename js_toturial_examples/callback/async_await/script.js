// 10:27:41
// example 1
// function api(){
//     return new promise((resolve, reject) =>{
//         setTimeout(() =>{
//             console.log("weather data");
//             resolve(200);
//         }, 2000);
//     });
// }

// async function getWeatherData(){
//     await api();
//     await api();
// }




// example 2
function getData(dataId){
    return new Promise((resolve, reject) => {
        setTimeout(() =>{
            console.log("data",dataId);
            resolve("success");
        }, 2000);
    });
}



//async await
// we have to call the getData func on console if not we can use iife function
// async function getAllData(){
//     console.log("gettting data1...");
//     await getData(1);
//     console.log("gettting data1...");
//     await getData(1);
//     console.log("gettting data1...");
//     await getData(1);
// }


// iife function

(async function (){
    console.log("gettting data1...");
    await getData(1);
    console.log("gettting data1...");
    await getData(1);
    console.log("gettting data1...");
    await getData(1);
})();