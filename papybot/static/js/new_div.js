class NewDiv{
    constructor(sentence){
        this.sentence = sentence;
    }
    
    userDiv(){
        const firstSentence = document.querySelector(".sentence");
        const textValue = this.sentence;
        const newPhrase = new CreateElement("div", {"class":"userSentence"}, firstSentence, "user").newElement();
        const question = new CreateElement("p", {"class": "sentence"}, newPhrase, textValue).newElement();
        return question;
    }

    newDiv(){
        return this.userDiv;
    }
}