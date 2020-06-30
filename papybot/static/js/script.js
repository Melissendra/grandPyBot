const form = document.querySelector(".search");
const input = document.querySelector("#grandPybot");


function getFormData(url, data, headers){
    return fetch(url, {
        method : 'POST',
        body: data,
        headers: headers
    })
    .then(
        response => response.json()
    )
    .catch(
        error => console.log(error)
    );
}

function newQuestion(){
    let inputVal = input.value;
    const question = userDiv(inputVal);
    question.scrollIntoView({behavior: "smooth"});
    return question
}

function papyAnswer(data, url){
    const papyAnswer = papyDiv(data, url);
    papyAnswer.scrollIntoView({behavior: "smooth"});
    return papyAnswer;
}

function mapGet(lng, lat, title){
    const newMapDiv = mapDiv();
    const latLong = {
        lat : lat,
        lng: lng
    }

    const map = new google.maps.Map(newMapDiv,{
        zoom: 10,
        center: latLong
    });

    const marker = new google.maps.Marker({
        position: latLong,
        map: map,
        title: title
    });
    newMapDiv.scrollIntoView({behavior:"smooth"});
}

form.addEventListener("submit", function(event){
    event.preventDefault();
    let inputVal = input.value;
    getFormData("/ajax", inputVal, {
        "Content-Type": "plain/text"
    })
    .then(response =>{
        if(inputVal != ""){
            if(response.ok){
                newQuestion();
                papyAnswer(response.wiki_article, response.url);
                mapGet(response.longitude, response.latitude, response.title);
                input.value = "";
            }
            else {
                newQuestion();
                papyAnswer(response.failed_message);
                input.value = "";
            }    
        }
        else{
            papyAnswer(response.empty_message);
            input.value = "";
        }
    });
});