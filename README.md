# Deploy flask app on IIS


- youtube video: https://www.youtube.com/watch?v=Q4AaFNX6LBY&t=305s


## Instruction

- Create a virtual environment
- Install dependencies
    - ``` pip install flask wfastcgi```
- Go to IIS on windows:
    - Right Click on sites and add new site (site name: FlaskWebApp, port: 5090)
- Go inside the site:
    - Double Click on Handler Mappings 
    - Click on Add Module Mapping
        - Request path: *
        - Module: FastCgiModule
        - Executable:
            - Run Command prompt as administrator
            - change directory to the project path (for example: ```cd E:\workspace\deploy-flask-app-on-iis```)
            - Activate the virtual environment
            - use ```wfastcgi-enable``` command to get the excecutable path (something like this: E:\workspace\deploy-flask-app-on-iis\env\Scripts\python.exe|E:\workspace\deploy-flask-app-on-iis\env\lib\site-packages\wfastcgi.py)
            - Name: (anything like: FlaskHandler)
            - In the request restrictions: disable invoke handler
            - Click Ok and click yes
- Click on the root of IIS (DESKTOP-....)
    - click on FastCGI Settings
        - Double click on the created handler
            - In the collection, open the EnvironmentVariable Collection Editor
                - Add two variables
                    - The first:
                        - Name: PYTHONPATH
                        - Value: path to the flask project (like: ```E:\workspace\deploy-flask-app-on-iis```)
                    - The second:
                        - Name: WSGI_HANDLER
                        - Value: name of the main flask file (like:```app.app```)