
function add_to_favourite(id)
{
   

    
    

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