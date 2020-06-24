class NewDiv{
    constructor(sentence){
        this.sentence = sentence;
    }
    
    userDiv(){
        const textValue = this.sentence;
        const firstSentence = document.querySelector(".sentences");
        const newDiv = new CreateElement("div", {"class": "userSentence"}, firstSentence).newElement();
        const newUser = new CreateElement("p", {"class": "sentence"}, newDiv, "User").newElement();
        const newQuestion = new CreateElement("p", {"class": "sentence"}, newUser, textValue).newElement();
        const arrow = new CreateElement("div", {"class": "arrowLeft"}, newDiv).newElement();
    }
}