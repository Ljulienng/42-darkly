# XSS Injection on NSA Page

This text describes an XSS injection vulnerability on the NSA page. The attacker can exploit this vulnerability by injecting malicious code into the search input to execute arbitrary code on the page.

## Steps to Perform the Attack

1. Click on the NSA image to go to http://192.168.56.101/?page=media&src=nsa.
2. Enter a test string in the `src` parameter to see the 404 error page embedded in the center of the page.
3. Try entering the root `/` to see a small embedded homepage instead of the error 404.
4. Inject a script using the `data` tag to execute arbitrary code on the page: `http://192.168.56.101/?page=media&src=data:text/html,<script>alert('42');</script>`.
5. If the script is executed properly, encode it in base64: `http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnNDInKTs8L3NjcmlwdD4=`.
6. The flag should be displayed on the page.
