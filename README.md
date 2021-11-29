<div>
<h1>Start docker container</h1>
<div>Start the app with this command : sudo docker-compose -f docker-compose.yml up -d(start the docker container)<div>
<div>go to: localhost:8000 (connect app)<div>
<div>When you want to close the app also use this command : sudo docker-compose down(stop the docker container)<div>
<div>

<br>

<div>

<div>
In order to find all routes and how requests and responses should look like you should go to:
<h1>
Swaggers : <h5>localhost:8000/swagger</h5>
</h1>
</div>

<div>
<h1>App usage</h1>
<div>

<div>
<h3>Log In process</h3>
</div>

<div>
In order to log in or log out you should go to: localhost:8000/auth
</div>

<div>
Log In: POST request with {"email":"mihai@yahoo.com","password":"mihai"}(example with a defined user from db)
</div>

<div>
Log Out: DELETE request on: localhost:8000/auth
</div>

<div>
<h3>Auth required endpoints</h3>
</div>

<div>
As a user you want to see your friends list or to add a new friend to your list you can make
<div>
 GET request on: localhost:8000/friends to get friends for a user , after the user has logged in (you will receive an Unauthenticated message if you are not logged in)
</div>
<div>
 POST request on: localhost:8000/friends to add a new friend for the user who makes the request , after the user has logged in (you can find in swagger what request must contain)
</div>
</div>

<div>
As a user you want to update a friend details or delete a friend.You should be logged in to access this routes. 
<div>
GET request on: localhost:8000/friend/pk/ to get details for the user's friend with pk=pk
</div>
<div>
PUT request on: localhost:8000/friend/pk/ to update the specified friend 
</div>
<div>
DELETE request on: localhost:8000/friend/pk/ to delete the specified friend 
</div>
</div>

<div>
If you want to see registration information , these are some provided information
<div>
GET request on: http://localhost:8000/api/register/ to get users list
</div>
<div>
POST request on: http://localhost:8000/api/register/ to add a new user
</div>
<div>
PUT request on: http://localhost:8000/api/register/pk to update the user with pk=pk
</div>
<div>
POST request on: http://localhost:8000/api/register/pk to delete the user with pk=pk
</div>
</div>

<div>
In app it's also a viewset that can provide information as for an admin: it shows all friends that were created : http://localhost:8000/api/friends/ , 
or you can update or delete a friend at : http://localhost:8000/api/friends/pk 
</div>

</div>

<br>

<h1>Testing</h1>
<div>
Run the following commands:
<div>sudo docker ps</div>
<div>Get the "CONTAINER ID" value for trainingdjango_api and than run: sudo docker exec -it "CONTAINER ID" bash</div>
<div>Now you can run the testing files with following commands</div>
<div>./manage.py test apps/ (in order to run all tests)</div>
<div>./manage.py test apps/friends (in order to run test for a specific app)</div>
<div>If you want to close the interactive terminal run: exit </div>
</div>
