# Custom Headers Breach (Referer and User-Agent)

This text describes how to access a page that requires specific headers (Referer and User-Agent) to be set in the HTTP request. The page can only be accessed if the Referer is set to "https://www.nsa.gov/" and the User-Agent is set to "ft_bornToSec".

## Steps to Perform the Attack

1. Set the Referer header to "https://www.nsa.gov/" in the HTTP request.
2. Set the User-Agent header to "ft_bornToSec" in the HTTP request.
3. Make the HTTP request to the page that requires the specific headers.
4. Access the page and retrieve the flag.

## Additional Information

Setting custom headers in an HTTP request can be used to bypass security measures and gain access to pages that are restricted.
