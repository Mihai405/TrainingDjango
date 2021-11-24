<div>
<h1>Start docker container</h1>
<div>sudo docker-compose -f docker-compose.yml up //start the container<div>
<div>localhost:8000 (connect app:)<div>
<div>sudo docker-compose down //stop the container<div>
<div>

<br>

<div>

<h1>
Swaggers : <h5>localhost:8000/swagger</h5>
</h1>

<div>
<h1>App usage</h1>
<div>

<div>If you go to <h5>localhost:8000/api</h5> , you will see two routes for all users and friends created.You can use GET/POST/PUT/DELETE on this routes.Both can be used without being loged in.
</div>

<div>
<h3>Log In process</h3>
</div>

<div>
In order to log in or log out you should go to <h5>localhost:8000/auth</h5>
</div>

<div>
Log In: POST request with {"email":"mihai@yahoo.com","password":"mihai"}(example with a defined user from db)
</div>

<div>
Log Out: DELETE request on <h5>localhost:8000/auth</h5>
</div>

<div>
<h3>Auth required endpoints</h3>
</div>

<div>
 GET,POST request on <h5>localhost:8000/friends</h5> to get friends for a user , after the user has logged in
</div>

<div>
GET,PUT,DELETE on <h5>localhost:8000/friend/<int:pk>/ to uptate a friend from his friends list</h5>
</div>

</div>
