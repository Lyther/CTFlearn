# Git Is Good

Web Hard Rating: 4.57 / 5

[Link](https://ctflearn.com/challenge/109) address here.

## Description

Try to bypass my security measure on this site! http://165.227.106.113/header.php

## Solution

1. Access the given website, got error message `Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: ...`.
2. Check the source code of HTML page, find the following comment `<!-- Sup3rS3cr3tAg3nt  -->`.
3. Change the `User-Agent` header to `Sup3rS3cr3tAg3nt`, access again. Get response `Sorry, it seems as if you did not just come from the site, "awesomesauce.com".`.
4. Change the `Referer` header to `awesomesauce.com`, then access again. Get the flag.

