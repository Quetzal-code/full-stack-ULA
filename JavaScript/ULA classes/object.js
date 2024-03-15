//Definicion del objeto libro
let bookObject={
    titulo:"Hobbit",
    autor:"Tolkien",
    Disponible:true
}

function verifDisponibilidad(libro){
    if (libro.Disponible===true){
    console.log("El libro esta disponible");}
    else{
        console.log("El libro no esta disponible");
    }
}

//Invocar la funcion
verifDisponibilidad(libro)