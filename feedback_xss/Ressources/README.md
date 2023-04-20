XSS breach on feedback page

In the input form "name"
<input name="txtName" type="text" size="30" maxlength="10">

The server doesn't escape characters so we can send script from this field
