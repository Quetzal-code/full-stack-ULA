//Declaring the variables
const homeStreet = "1 Main St.";
const homeCity = "Sicilia";
const homeState = "Quebec";
const homeCode = "021038";

const workStreet = "15 Oak Ln.";
const workCity = "Central City";
const workState = "Nova Scotia";
const workCode = "021048";


/*
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

*/

 function homeAddress() {
     document.getElementById("street").value = homeStreet;
     document.getElementById("city").value = homeCity;
     document.getElementById("state").value = homeState;
     document.getElementById("code").value = homeCode;
 }
 function workAddress() {
    document.getElementById("street").value = workStreet;
    document.getElementById("city").value = workCity;
     document.getElementById("state").value = workState;
     document.getElementById("code").value = workCode;
 }


// Agrega los event listeners a los botones de radio
//  window.onload = function() {
//      document.getElementById("homeoption").addEventListener("click", function() {
//          fillAddress("home");
//      });
//      document.getElementById("workoption").addEventListener("click", function() {
//          fillAddress("work");
//      });
//  };
