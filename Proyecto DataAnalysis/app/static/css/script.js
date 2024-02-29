document.addEventListener('DOMContentLoaded', function() {
    const selectPaises = document.getElementById('selectPaises');
    selectPaises.addEventListener('change', function() {
        const selectedCountry = selectPaises.value;
        obtenerCiudades(selectedCountry);
    });

    function obtenerCiudades(pais) {
        fetch(`/ciudades/${pais}`)
        .then(response => response.json())
        .then(data => {
            console.log(data); // Hacer algo con las ciudades devueltas por el servidor
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
