# SQL Injection on Member Page

This text describes a SQL injection vulnerability on a member page. The attacker can exploit this vulnerability by injecting SQL code into the search input to extract sensitive information from the database.

## Steps to Perform the Attack

1. Use a Boolean-based SQL injection to bypass authentication by injecting the following code: `1 OR 1=1`.
2. Retrieve all the users in the `users` table by injecting the following code: `-1 UNION SELECT *, 1 from users`.
3. Determine all the columns present in the `users` table by injecting the following code: `-1 UNION SELECT table_name, column_name FROM information_schema.columns`.
4. Concatenate all the columns in the `users` table into one by injecting the following code: `-1 UNION SELECT CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) as first_name, 1 from users`.
5. The last result shows the flag, which is a password that needs to be decrypted using MD5, converted to lowercase, and hashed with SHA256 to obtain the flag.

## Additional Information

The value of `-1` is typically used to make the original query return no results. It can be any value that doesn't exist in the database, depending on the context of the query.

Look for the MD5 decrypt of the script, then convert the string to lowercase and hash it with SHA256 to obtain the flag.

Flag: 5ff9d0165b4f92b14994e5c685cdce28
