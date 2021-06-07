# Glovo Promotion Automation Project.

Modules used for compiling an empty shell executable app for locally running a script hosted on a microframework.
Script hosted on https://promobot.pythonanywhere.com/promobot_code/


For building windows executable app (.exe):

1. download/clone the repository and open Terminal inside the directory
2. open terminal inside the directory
3. install pyinstaller: ```pip install pyinstaller```
4. create the exe app:
```bash
pyinstaller  -F -n Promobot --icon=app.ico main.py
```


For building a PEX file for mac os (.pex):

 1. download/clone the repository and open Terminal inside the directory
 2. install pex: ```pip install pex```
 3. create wheel: ```python setup.py bdist_wheel```
 4. move newly created wheel from "dist" folder to main directory. You can do this manually or automatically by executing the cleanup.command file.
    To do this programmatically: 
    ```bash
    chmod +x cleanup.command
    ./cleanup.command
    ```
 5. create PEX: 
 ```bash
 pex -f $PWD -r requirements.txt -e main -o PromoBot.pex
 ```



 
 
