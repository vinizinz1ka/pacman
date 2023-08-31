
$(function (){

    var ip = "localhost";

    $.ajax({
        url: "http://"+ip+":5000/listar/Resultado",
        method: "GET",
        dataType: "json",
        success: listar,
        error: function () {
            alert("Erro ao conectar com o back-end!")
        }
    });

    function listar(retorno){
        if (retorno.resultado == "ok"){
            for (let d of (retorno.detalhes)){

                var linha = "<tr>" +
                    "<td>" + d.id + "</td>" + 
                    "<td>" + d.pontuacao_alcancada + "</td>" + 
                    "</tr>";

                    $("#dados").append(linha);
            }
        }else{
            alert(retorno.resultado + retorno.detalhes);
        }
    }
});