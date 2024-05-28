const URL = "https://cat-fact.herokuapp.com/facts";
const factPara = document.querySelector("#fact");
const btn = document.querySelector("#btn");

const getFacts = async () =>{
    console.log("getting data...");
    let responce = await fetch(URL);
    console.log(responce); // getting json format
    let data = await responce.json();
    factPara.innerText = data[1].text;

};

btn.addEventListener("click", getFacts);