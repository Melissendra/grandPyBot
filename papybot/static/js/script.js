const { constants } = require("buffer");

let form = document.querySelector(".search")
const input= document.querySelector("#grandPyBot")
let inputValue = input.value;

form.addEventListener("submit", function(event){
    event.preventDefault();
    // send a form
    // fetch("/ajax", {
    //     method: "POST",
    //     body: new FormData(form)
    // });
    let answer = NewDiv(form);
    answer.newDiv()
});