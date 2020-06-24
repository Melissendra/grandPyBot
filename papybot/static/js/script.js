let form = document.querySelector(".search");

async function getFormData(url){
    let response = await fetch(url);
    data = await response.json()
    return data;
}

getFormData("/ajax")
    .then(data => data.response);

form.addEventListener("submit", function(event){
    event.preventDefault();
    const input = document.querySelector("#grandPybot");
    let inputVal = input.value;
    const answer = new NewDiv(inputVal);
    answer.userDiv();
});