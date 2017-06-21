# ITKST53 Lab 5

All exercises completed.

NOTE: ALL EXERCISES TESTED AND WORKING ON CHROME.

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

7. EXERCISE 1 checked by pasting the answer-1.txt content to Firefox address bar. The stolen cookie is printed by console.log so check Javascript console on the browser.

8. EXERCISE 2 Logged in as victim, go to VM-IP-ADDRESS:8081/answer-2.html (You will be redirected and zoobars are transferred, for some reason only works on Chrome).

9. EXERCISE 3.1 Log out of victim, open javascript console, go to VM-IP-ADDRESS:8081/answer-3.html (might have to restart the SimpleHTTPServer if it doesnt work after ex2). Stolen username and password printed to console.

10. EXERCISE 3.2 Log out. Create new user. Logged in as the new user go to VM-IP-ADDRESS:8081/answer-3.html. Refresh page and notice your zoobars are gone.

11. EXERCISE 4 Submit the contents of answer-4.txt as your profile. Log out and create new user. Logged in as new user inspect the previous user that has the profile worm as their profile. On the next page shows 10 zoobars, Scanning for viruses.. and no transfers. Check home and see that the profile worm code is injected to your profile as well and you are missing 1 zoobar.
