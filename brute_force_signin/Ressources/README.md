Brute force sign in script

No password were found during the sql injections
So let's make a script to brute force the sign in form

We're going to do search for most used usernames and passwords.
Make a list of it and then iterate until we find a "flag" string on the response text:

"http://192.168.56.101/?page=signin&username={username}&password={password}&Login=Login"

The script stops at username: admin password: shadow
But it seems like only the password was needed to get the flag.
