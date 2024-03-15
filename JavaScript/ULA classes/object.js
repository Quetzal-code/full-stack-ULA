//Definicion del objeto libro
let libro={
    titulo:"Hobbit",
    autor:"Tolkien",
    Disponible:true
};

function verifDisponibilidad(libro){
    if (libro.Disponible===true){
    console.log("El libro esta disponible");}
    else{
        console.log("El libro no esta disponible");
    }
}

//Invocar la funcion
verifDisponibilidad(libro);

//Cambiar disponibilidad
libro.Disponible=false;

console.log(libro.Editorial);

libro.paginas=null;
console.log(libro.paginas);