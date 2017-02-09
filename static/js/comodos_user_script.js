/*jshint browser:true */
/*global $ */(function()
{
 "use strict";
 /*
   hook up event handlers 
 */
 function register_event_handlers()
 {
    
     var get = getRouteParameter();
     var id = get.id;
     $.ajax({
        url: "http://localhost:5000/get_dispositivos",
        data: {id:id},
        dataType: "json",
        success: function(result){
        
            var content = '<div class="col-xs-12"><h3>' + result.comodo + '</h3></div>';
            var nome = "";
            var dispositivo = "";
            var button = "";
            var acao = "";
            var status;
    
            for(var i = 0; i < result.aparelhos.length; i++) {

                nome = '<h5>' + result.aparelhos[i].nome + '</h5>';

                dispositivo = '<h1><i class="glyphicon glyphicon-lamp"></i></h1>';

                if(result.aparelhos[i].status == 1) {

                    button = '<button class="btn btn-default btn-block btn-lg btn-equipamento btn-on" data-estado="on" data-id="' + result.aparelhos[i].id + '">';

                    status = '<p class="status">status: <span class="text-success">Ligado</span></p>';

                    acao = '<p class="acao">Desligar</p>';

                } else {

                    button = '<button class="btn btn-default btn-block btn-lg btn-equipamento btn-off" data-estado="off" data-id="' + result.aparelhos[i].id + '">';

                    status = '<p class="status">status: <span class="text-danger">Desligado</span></p>';

                    acao = '<p class="acao">Ligar</p>';

                }


                content = content + '<div class="col-xs-12 col-sm-6 col-md-4">' + button + nome + status + dispositivo + acao + ' </button> </div>';

            }

            $('#content').html(content);
            
            
            
            $('.btn-equipamento').click(function(){

                var estado = $(this).data('estado');
                var aparelho_id = $(this).data('id');

                var status = $(this).children('.status');
                var acao = $(this).children('.acao');
                var span = status.children('span');
                
                var equipamento = $(this);
                
                $.ajax({
                
                    url: "http://10.1.14.143/teste/trocar-estado.php",
                    data: {id:aparelho_id, estado:estado},
                    dataType: "json",
                    success: function(response){
                        
                        console.log(response);
                        if(response == 'turn-off') {
                            equipamento.data('estado','off');
                            equipamento.addClass('btn-off').removeClass('btn-on');
                            span.addClass('text-danger').removeClass('text-success');
                            span.html('Desligado');
                            acao.html('Ligar');

                        } else {
                            equipamento.data('estado','on');
                            equipamento.addClass('btn-on').removeClass('btn-off');
                            span.addClass('text-success').removeClass('text-danger');
                            span.html('Ligado');
                            acao.html('Desligar');

                        }
                        
                    },
                    error: function(event, jqxhr, settings, thrownError){

//                        navigator.notification.alert(event.statusText,  null, 'Resposta da Conexão', 'ok');
                    },
                    complete: function(){
//                        navigator.notification.alert("Completo!",  null, 'Resposta da Conexão', 'ok');
                    }

                });

                

            });
        },
        error: function(event, jqxhr, settings, thrownError){
            
            alert('erro');
        },
        complete: function(){
//            navigator.notification.alert("Completo!",  null, 'Resposta da Conexão', 'ok');
        }
    });

    
    
    
    }
 document.addEventListener("app.Ready", register_event_handlers, false);
})();
