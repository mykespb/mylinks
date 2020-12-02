MyLinks -- private web links organizer
==========================================

Usage
------------------------------------------

Simply type in address you need,
and possibly its description.
The program will add it to the list of your favourite sites,
getting its title from real page.

You will see all the list at every reload.

Installation
------------------------------------------

Use 
```
docker-compose up --build
```

Details
------------------------------------------

There were problems with access using 'requests' and 'httplib3'
libraries. Only adding 'pyopenssl' library saved it.

Future
------------------------------------------

To test and extend.
