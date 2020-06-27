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

}

function papyAnswer(data, url){
    const papyAnswer = papyDiv(data, url);
}

function mapGet(lng, lat){
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
        title: ""
    });
}

form.addEventListener("submit", function(event){
    event.preventDefault();
    let inputVal = input.value;
    newQuestion();
    getFormData("/ajax", inputVal, {
        "Content-Type": "plain/text"
    })
    .then(response =>{
        console.log(response.wiki_article)
        papyAnswer(response.wiki_article, response.url);
        console.log(response.longitude, response.latitude)
        mapGet(response.longitude, response.latitude);
    })
});