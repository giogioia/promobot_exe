# Glovo Promotion Automation Project.

Modules used for compiling an empty shell executable app for locally running a script hosted on a microframework.

For building windows executable app (.exe):

1. clone repository

2. install pyinstaller: ```$ pip install pyinstaller```

3. inside the directory run the following:
```
$ pyinstaller  -F -n Promobot --icon=app.ico main.py
```

For building a PEX file for mac os:

 1. clone repository
 
 2. install pex: ```$ pip install pex```
 
 3. create wheel: ```$ python setup.py bdist_wheel```
 
 4. create PEX (run inside the directory): 
 
 ```
 $ pex -f $PWD -r requirements.txt -e main -o PromoBot.pex
 ```



 
 
