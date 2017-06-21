# ITKST53 Lab 5

All exercises completed.

## Instructions

1. Switch branch:

> git checkout -b lab5 origin/lab5

2. Remember to create the port forwarding according to the instructions in lab PDF (following command for Linux):

> ssh -L localhost:8080:localhost:8080 httpd@VM-IP-ADDRESS

3. Run make:

> make

4. Run server:

> ./zookld

5. Run another server to serve the exploit pages using a different port:

>  python -m SimpleHTTPServer 8081

6. Create users attacker and victim using the Zoobar web site at localhost:8080/zoobar/. Log in with victim.

7. Exercise 1 checked by pasting the answer-1.txt content to Firefox address bar. The stolen cookie is printed by console.log so check Javascript console on the browser.

8. 
