
originalDiv = document.querySelector(".sentences")
    
    
function userDiv(sentence){
    const textValue = sentence;
    const newDiv = createElement("div", {"class": "userSentence"}, originalDiv);
    const newUser = createElement("p", {"class": "sentence"}, newDiv);
    const newUserStrong = createElement("strong", {"class": ""}, newUser, "User");
    const newQuestion =  createElement("p", {"class": "sentence"}, newUser, textValue);
    const arrow = createElement("div", {"class": "arrowLeft"}, newDiv);
    return newUser;
}

function papyDiv(sentence, url){
    const textValue = sentence;
    const urlDiv = url;
    const newPapy = createElement("div", {"class": "papySentence"}, originalDiv);
    const papy =  createElement("p", {"class": "sentence"}, newPapy);
    const papyName =  createElement("strong", {"class": ""}, papy, "Grand Py");
    const answer =  createElement("p", {"class": "sentence"}, papy, textValue);
    const urlLink = createElement("a", {"href": url, "class": "url"}, papy, urlDiv);
    const arrow =  createElement("div", {"class": "arrow"}, newPapy);
    return papy;
}

function mapDiv(){
    const newPapy = createElement("div", {"class": "papySentence"}, originalDiv);
    const map = createElement("div", {"id": "map"}, newPapy);
    const arrow = createElement("div", {"class": "arrow"}, newPapy);
    return map;
}
