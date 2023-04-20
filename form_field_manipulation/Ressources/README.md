Form field manipulation

How to find the breach

In the recover password page (http://IP/?page=recover)

Change the input's value in the the submit form with whatever value
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">

Now submit the form, it'll redirect you to the flag
