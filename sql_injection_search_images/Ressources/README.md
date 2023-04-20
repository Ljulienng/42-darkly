# SQL Injection on Search Image Page

This text describes a SQL injection vulnerability in a search image page. The attacker can exploit this vulnerability by injecting SQL code into the search input to extract sensitive information from the database.

## Steps to Perform the Attack

The steps to perform the SQL injection attack are similar to the ones used in the `sql_injection_member` example:

1. Use a Boolean-based SQL injection to bypass authentication by injecting the following code: `1 OR 1=1`.
2. Use a UNION SELECT statement to extract information about the `list_images` table structure by injecting the following code: `-1 UNION SELECT table_name, column_name FROM information_schema.columns`.
3. Concatenate the columns found in the `list_images` table by injecting the following code: `-1 UNION SELECT CONCAT(url, title, comment) as url, 1 from list_images`.

## Additional Information

Url: borntosec.ddns.net/images.png

Hack me? If you read this, just use this MD5 decode lowercase then SHA256 to win this flag! : 1928e8083cf461a51303633093573c46
