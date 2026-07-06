let puntos = 78;

function penalizar(){

    puntos -= 10;

    if(puntos < 0){
        puntos = 0;
    }

    document.getElementById("puntaje").innerHTML = puntos;

    document.getElementById("progreso").style.width = puntos + "%";

    if(puntos >= 70){

        document.getElementById("nivel").innerHTML =
        "Nivel: Excelente";

        document.getElementById("progreso").style.background =
        "green";

    }

    else if(puntos >= 40){

        document.getElementById("nivel").innerHTML =
        "Nivel: Riesgo Moderado";

        document.getElementById("progreso").style.background =
        "orange";

    }

    else{

        document.getElementById("nivel").innerHTML =
        "Nivel: Riesgo Alto";

        document.getElementById("progreso").style.background =
        "red";

    }

    if(puntos === 0){

        alert(
        "Cuenta suspendida permanentemente por llegar a 0 puntos."
        );

    }

}
function login(){

    let tipo =
    document.getElementById("tipo").value;

    if(tipo === "Pasajero"){
        window.location.href =
        "pasajero.html";
    }

    if(tipo === "Conductor"){
        window.location.href =
        "conductor.html";
    }

    if(tipo === "Administrador"){
        window.location.href =
        "administrador.html";
    }

}