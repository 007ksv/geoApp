# geoApp Backend
***
A backend API project of geoAPP using [FastAPI][1] framework


#### Requirements
***
1. Python 3.7+
2. virtualenv
3. poetry


#### Installation Steps
***
1. Clone repo to system using 
    ```
    $ git clone https://github.com/007ksv/geoApp.git
    ``` 
    and goto project root.
2. Create a virtualenv of name **.venv** using
    ```
    $ virtualenv -p python3.7 .venv
    ```
3. Activate the newly created virtualenv
    ```
    $ source .venv/bin/activate
    ```
4. Install all the python dependencies related to project.
    ```
    $ poetry install
    ```
5. To add new python package dependency
   ```
   $ poetry add dependency_name

   # if dependency is for development purpose only
   $ poetry add -D dependency_name
   ```

6. Also, update a `requirements.txt` files for other deployment choices.
    ```
    $ poetry export -f requirements.txt --without-hashes -o requirements.txt
    $ poetry export -f requirements.txt --without-hashes --dev -o requirements-dev.txt
    ```
### Test web app
[geoApp][2]


[1]: https://fastapi.tiangolo.com/
[2]: https://fast-api-geoapp.herokuapp.com/v1/
