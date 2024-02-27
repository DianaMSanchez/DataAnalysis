function restByCountry() {
    fetch('/rest_by_country', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Maneja los datos devueltos por la función si es necesario
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function restByClaimed() {
    fetch('/rest_by_claimed', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Maneja los datos devueltos por la función si es necesario
    })
    .catch(error => {
        console.error('Error:', error);
    });
}