## Required Setup to Start the Server

Run the following cli commands from the repository's top level directory:
- `pip install virtualenv` 
  - virtualenv will be used to create a virtual environment where we can install packages particular to this project
- `python3 -m venv .venv` 
  - this will create a folder in your current directory named .venv which is where pip will store any packages that are installed
- `source .venv/bin/activate` 
  - this tells pip to install the packages in the new .venv directory. You can run `deactivate` to tell pip to start globally installing packages again
  - you can check that you are in the correct environment by running `which python`. This prints the path to the Python interpreter executable that will be used when you use the `python` command in the cli. If the executable location you see is in the .venv directory you just created, you are in the correct environment
- `pip install -r requirements.txt`
  - this will install the dependencies listed in the requirements.txt file. The packages will match the versions that they are "pinned" to in the requirements.txt file.
- `python3 app.y`
  - this runs the flask server! Happy exploring!
