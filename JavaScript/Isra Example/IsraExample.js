// Definiciones de direcciones para "Casa" y "Trabajo"
const homeStreet = "Calle de Casa 123";
const homeCity = "Ciudad Casa";
const homeState = "Estado Casa";
const homeCode = "00001";

const workStreet = "Calle de Trabajo 456";
const workCity = "Ciudad Trabajo";
const workState = "Estado Trabajo";
const workCode = "00002";

// Función para asignar los valores de dirección
function fillAddress(type) {
    // Identifica los elementos del formulario
    const streetInput = document.getElementById("street");
    const cityInput = document.getElementById("city");
    const stateInput = document.getElementById("state");
    const codeInput = document.getElementById("code");
    
    // Determina qué conjunto de datos usar y asigna los valores
    if (type === "home") {
        streetInput.value = homeStreet;
        cityInput.value = homeCity;
        stateInput.value = homeState;
        codeInput.value = homeCode;
    } else if (type === "work") {
        streetInput.value = workStreet;
        cityInput.value = workCity;
        stateInput.value = workState;
        codeInput.value = workCode;
    }
}

// Agrega los event listeners a los botones de radio
window.onload = function() {
    document.getElementById("homeoption").addEventListener("click", function() {
        fillAddress("home");
    });
    document.getElementById("workoption").addEventListener("click", function() {
        fillAddress("work");
    });
};
