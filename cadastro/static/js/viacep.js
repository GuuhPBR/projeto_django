$(document).on('ready', function(){
    $("#busca_cep").on('click', function(){
        var cep = $("#inputCep").val();
        $.ajax({
            method: "GET",
            url: `https://viacep.com.br/ws/${cep}/json/`
        })
        .done(function( data ) {
            console.log(data);
            $("#inputEndereco").val(data.logradouro);
            $("#inputBairro").val(data.bairro);
            $("#inputComplemento").val(data.complemento);
            $("#inputUf").val(data.uf);
            $("#inputCidade").val(data.localidade);
        });
    })
})
