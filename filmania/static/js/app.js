
function add_to_favourite(id)
{
   
   

    if( document.getElementById('fav').innerHTML == "Dodaj do ulubionych")
    {
        document.getElementById('fav').innerHTML = "Usuń z ulubionych";
    }
    else if(document.getElementById('fav').innerHTML == "Usuń z ulubionych")
    {
        document.getElementById('fav').innerHTML = "Dodaj do ulubionych";

    }
    

    var movie_data ={};
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    movie_data['csrfmiddlewaretoken'] = csrf_token;
    movie_data['id'] = id;

    

    $.ajax({
        type: "POST",
        url: "/accounts/add_fav/" ,
        data: movie_data, 

        
      });

      
            
}