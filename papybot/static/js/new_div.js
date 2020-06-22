class NewDiv{
    constructor(sentence){
        this.sentence = sentence;
    }
    
    userDiv(){
        const firstSentence = document.querySelector(".sentence");
        const textValue = this.sentence;
        const newDiv = new CreateElement("div", {"class": "userSentence"}, firstSentence).newElement();
        const newUser = new CreateElement("p", {"class": "sentence"}, newDiv, "User").newElement();
        const newQuestion = new CreateElement("p", {"class": "sentence"}, newDiv, textValue).newElement();
    }
}