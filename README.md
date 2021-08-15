# IMDB
www.imdbworld.herokuapp.com is a web application completely developed on Django and DjangoREST 
Framework and hosted on Heroku. This web application will let you to do CRUD operations on the movies
stored on database using the following APIs.

Base URL = https://imdbworld.herokuapp.com/

1. For site admins-:
    endpoint = admin/imdbapi/
    
    requirements-:
        
        >Fields of Movies in Payload = {
            "popularity": <Float>,
            "director": <String>,
            "genre": <List of Strings>
            "imdb_score": <Float>,
            "name": <String>}
        >URL = Base URL+endpoint
        >Data = Payload
        >username of admin
        >password of admin
        >Headers = {'content-Type': 'application/json'}
        
    * For POST Method-:For POST Method, all the fields are mandatory in Payload.
    
        Use-:
        
        response = requests.post(url=URL, data=payload, auth=HTTPBasicAuth(username='****', password='****'),
                          headers=headers)
                      
    * For PUT Method-:For PUT Method, filed "name" is required in payload along with other field details which the user wants to edit.
    
        Use-:
        
        response = requests.put(url=URL, data=payload, auth=HTTPBasicAuth(username='****', password='****'), headers=headers)
    
    * For GET Method-: For GET Method, if the payload is having field(key) 'name' in it, then the response will be having the details of the movie having that name.
      If no field(key) of 'name' is given in payload or if the payload is empty, then the response will be having all the data from database.
      
        Use-: 
        
        response = requests.get(url=URL, data=payload, auth=HTTPBasicAuth(username='****', password='****'), headers=headers)     
    
    * For DELETE Method-: For DELETE Method, the payload must contain the field(key) 'name' of the movie which is to be removed from database.
    
        Use-:
        
        response = requests.delete(url=URL, data=payload, auth=HTTPBasicAuth(username='****', password='****'), headers=headers)
       
2. For site Users-:

    endpoint = user/imdbapi/
    
    requirements-:
        
        >Fields of Movies in Payload = {
            "popularity": <Float>,
            "director": <String>,
            "genre": <List of Strings>
            "imdb_score": <Float>,
            "name": <String>}
        >URL = Base URL+endpoint
        >Data = Payload
        >username of user
        >password of user
        >Headers = {'content-Type': 'application/json'}
        
    NOTE-:For site registered users, only GET Method is allowed. The Methods 'POST','PUT' and 'DELETE' are forbidden for the users.
    
    * For GET Method-: For GET Method, if the payload is having field(key) 'name' in it, then the response will be having the details of the movie having that name.
      If no field(key) of 'name' is given in payload or if the payload is empty, then the response will be having all the data from database.
      
        Use-: 
        
        response = requests.get(url=URL, data=payload, auth=HTTPBasicAuth(username='****', password='****'), headers=headers)
    
    
    