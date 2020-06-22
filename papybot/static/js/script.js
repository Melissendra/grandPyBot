let form = document.querySelector(".search");

form.addEventListener("submit", function(event){
    event.preventDefault();
    const input = document.querySelector("#grandPybot");
    let inputVal = input.value;
    const firstSentence = document.querySelector(".sentence");
    const newDiv = new CreateElement("div", {"class": "userSentence"}, firstSentence).newElement();
    const newUser = new CreateElement("p", {"class": "sentence"}, newDiv, "User").newElement();
    const newQuestion = new CreateElement("p", {"class": "sentence"}, newUser, inputVal).newElement();
});