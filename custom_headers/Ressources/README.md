Custom headers breach (referer and user-agent)

At the bottom of the header when clicking on the borntosec copyright it redirects us to this link
http://192.168.56.101/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

When inspecting this page carefully we get those two interesting comments:

<!--
You must come from : "https://www.nsa.gov/".
-->

and:
Let's use this browser : "ft_bornToSec". It will help you a lot.

it means that we have to access this page with https://www.nsa.gov/ as referer and ft_bornToSec as user-agent
notes:

Referer is an optional header field that allows the client to specify, for the server’s benefit, the address ( URI ) of the document (or element within the document) from which the URI in the request was obtained.
source : https://resources.infosecinstitute.com/topic/sql-injection-http-headers/

User agent is an HTTP header field gives the software program used by the original client

curl --referer "https://www.nsa.gov/" http://192.168.56.101/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
we get this line:
FIRST STEP DONE<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">

now let's add the user-agent:
curl --referer "https://www.nsa.gov/" --user-agent "ft_bornToSec" http://192.168.56.101/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

Bingo we got the flag
