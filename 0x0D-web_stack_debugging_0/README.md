0x0D. Web stack debugging #0
Debugging to correct apache curl: (52) Empty reply from server
curl: (52) Empty reply from server rerurn 
when command curl 0:8080 is entered
The command curl 0:8080 is used to make an HTTP request to the server running on your local machine (localhost) at port 8080. Here’s a breakdown:

curl: This is a command-line tool used to transfer data from or to a server using various protocols, including HTTP.
0: This is shorthand for localhost, which refers to your local machine.
:8080: This specifies the port number on which the server is listening.
So, curl 0:8080 is essentially requesting the root page (“/”) from the web server running on your local machine at port 8080. If everything is set up correctly, it should return the content of the page, which in this case should be “Hello Holberton”.
