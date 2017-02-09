/*jshint browser:true */
/*global $ */(function()
{
 "use strict";
 /*
   hook up event handlers 
 */
 function register_event_handlers()
 {
    
    
     /* button  #alertar */
    $.ajax({
        url: "http://10.1.14.143/teste/getcomodos.php",
        dataType: "json",
        success: function(result){
        
            var navli = "";
          

            for(var i = 0; i < result.length; i++) {
               
                navli = navli + '<li><a href="comodos.html?id=' + result[i].id + '">' +  result[i].nome; + '</a></li>';
                
            }

            $('#menu .navbar-nav').html(navli);

            
        },
        error: function(event, jqxhr, settings, thrownError){
            
//            navigator.notification.alert(event.statusText,  null, 'Resposta da Conexão', 'ok');
        },
        complete: function(){
//            navigator.notification.alert("Completo!",  null, 'Resposta da Conexão', 'ok');
        }
    });
    
    
    }
 document.addEventListener("app.Ready", register_event_handlers, false);
})();
