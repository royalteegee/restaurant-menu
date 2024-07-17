# restaurant-menu
A flask app that shows the different restaurants and dish menus they have with full CRUD operations

## LOCAL SETUP

- Git clone the repository  
    `git clone https://github.com/royalteegee/restaurant-menu.git`
- Install python using your operating system terminal
- Change directory into the restaurant-menu directory
- Create a python virtual environment. For Window users, run:       
    `python -m venv [name of environment you want to use]`
- Activate the virtual environment by running:  
    `[name of environment you want to use]\Scripts\activate`
- Install dependecies and packages in requirements.txt file   
    `pip install -r requirements.txt`
- Create a .env file and include the environment variables. Add a SECRET_KEY    
    `DB_URI=sqlite:///restaurant-menu.db`  
    `HOST=0.0.0.0`  
    `PORT=5000`  
    `SECRET_KEY=`  
    if you choose to change the DB_URL, go to line 5 of shellrun.py to also change it there  
- Run the flask application  
    `python server.py`
- Populate the restaurant-menu.db with the shellrun.py script  
    `python shellrun.py`
- Open your browser and go to `localhost:5000` to view your flask application