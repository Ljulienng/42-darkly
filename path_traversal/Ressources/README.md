Path traversal attack

"This attack is also known as “dot-dot-slash”, “directory traversal”, “directory climbing” and “backtracking”."

this type of attack aims to access files and directories that are stored outside the web root folder.
On the http://IP/?page=/etc/passwd page there is a :

<script>alert('Wtf ?');</script><!DOCTYPE HTML>

in the headers

We're going to make a python script to send multiple request til we find the right path

which is http://IP/?page=../../../../../../../etc/passwd
