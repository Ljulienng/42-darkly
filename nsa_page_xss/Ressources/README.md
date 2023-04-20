xss injection on the nsa page

Clicking on the nsa image sends use to http://192.168.56.101/?page=media&src=nsa
"src=" seems to be the path of a ressource if we try "test" we'll get a 404 small page embedded in the center of the error page
now let try the root "/", we get a small embedded homepage instead of the error 404

Let's try to send a script by using the data tag:
http://192.168.56.101/?page=media&src=data:text/html,<script>alert('42');</script>

The page seems to exec the script properly but we still didn't get the flag

let's try to encode it in base64
http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnNDInKTs8L3NjcmlwdD4=

Et voilà
