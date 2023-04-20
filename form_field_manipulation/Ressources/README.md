# Form Field Manipulation

This text describes how to exploit form field manipulation to gain access to a restricted page.

## Steps to Perform the Attack

1. Access the recover password page at http://IP/?page=recover.
2. Locate the input field with the name "mail" in the HTML source code.
3. Change the value of the "mail" input field to any desired value in the HTML source code. For example: `<input type="hidden" name="mail" value="hacker@example.com" maxlength="15">`
4. Submit the form.
5. The form will redirect you to the page with the flag.

## Additional Information

Form field manipulation is a technique used to modify the values of form fields in an HTML page. This technique can be used to exploit vulnerabilities and gain access to restricted pages.
