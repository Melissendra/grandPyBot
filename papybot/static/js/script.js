let form = document.querySelector(".search");

form.addEventListener("submit", function(event){
    event.preventDefault();
    console.log("je marche");
    const input = document.getElementById("grandPyBot");
    let inputVal = input.value;
    console.log(inputVal);
});