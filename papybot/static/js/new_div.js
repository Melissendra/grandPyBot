// function to create a new user div html element
function userDiv(sentence, el){
    const newSentenceDiv = createElement("div", {"class": "userSentences"}, el);
    const newDiv = createElement("div", {"class": "userSentence"}, newSentenceDiv);
    const newUser = createElement("p", {"class": "sentence"}, newDiv);
    const newUserStrong = createElement("strong", {"class": ""}, newUser, "User");
    const newQuestion =  createElement("p", {"class": "sentence"}, newUser, sentence);
    const arrow = createElement("div", {"class": "arrowLeft"}, newDiv);
    return newUser;
}

function papyDiv(sentence, url, el){
    const newPapy = createElement("div", {"class": "papySentence"}, el);
    const papy =  createElement("p", {"class": "sentence"}, newPapy);
    const papyName =  createElement("strong", {"class": ""}, papy, "Grand Py");
    const answer =  createElement("p", {"class": "sentence"}, papy, sentence);
    const urlLink = createElement("a", {"href": url, "class": "url"}, papy, url);
    const arrow =  createElement("div", {"class": "arrow"}, newPapy);
    return papy;
}

function mapDiv(el){
    const newPapy = createElement("div", {"class": "papySentence"}, el);
    const map = createElement("div", {"id": "map"}, newPapy);
    const arrow = createElement("div", {"class": "arrow"}, newPapy);
    return map;
}
