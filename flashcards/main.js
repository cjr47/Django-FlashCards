console.log('js loaded')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let cardForm = document.querySelector('#card-form')
cardForm.addEventListener('submit', function(event){
    // event.preventDefault()
    console.log(event.target)
})

let deckForm = document.querySelector('#deck-form')
deckForm.addEventListener('submit', function(event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(deckForm)
    fetch(cardURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data =>{
        console.log(data)
    })
})