## Project Setup Instructions
The Project uses
1. Django 
2. Alembic (for managing migrations)
3. SQLAlchemy (for ORM)
4. jinja2 (template rendering)
5. RQ Worker (for async tasking)

## Already in Project
#### In the project the word <project> refers to the project that you are working on, change this reference before starting anythin in this boiler template. start by changing the name of the directory src/project to src/project_name and run the server, change at other places where you see any error
* ### helper.py
	* strip_tags - to strip input tags for html tags
	* save_file - to save any uploaded file
	* InputValidation - Class to validate input fields
	* QueueStatus - Class to manage Queue
* Middleware
  * admin auth middleware - general purpose middleware
  * disable csrf middleware - for disabling csrf on specific paths
* migrations
  * env.py - update this file to generate migrations using alembic
* models
   * demo_user_model.py - delete this model, this is just for refence to help you create your first model
* static/main 
  * css - already has bootstrap.min.css, keep updating it's content to update bootstrap version
  * main.css - for custom css
  * js/app.js - included in all pages
  * js/bootstrap.bundle.min.js - bootstrap.js + popper.js
  *  js/custom-validation.js - custom input validation works with parsley.js
  *  js/jquery.min.js - update the content of this file to update jquery version
  *  js/parsley.js - input validation js
* tasks
  * send_email.py - to send emails, should be scheduled using rq worker
* templates
  * layouts/base.html - this is the base html containg all the js and css, this must be extended
  * pages/index.html - this is a demo page for you to get started
* views
  * demo_user_view.py - this is a demo view for you to get started, delete this when working
* custom_jinja_filter.py - contains all the custom jinja filters
* jinja2.py - register all the custom filters 

### Set up instructions
* Clone the project at `/opt/edugem/apps/`
* now after cloning go inside the folder using `cd mirror-ui`
* Now create a virtual environment using python 3.6. If you do not have python 3.6 installed on you system 
  * Follow `https://www.tecmint.com/install-python-in-ubuntu/`
  * Make python3.6 as your default python by creating aliase in bashrc file, open bashrc file using `sudo nano ~/.bashrc` now add `python=python3.6` in the file at the top. Now run `source ~/.bashrc` to reflect the changes

* Create virtual environment named `venv` using `virtualenv venv -p python3.6` 
* Activate Virtual environment and run all the commands related to the project in the virtual environment. run `cd /opt/edugem/apps/mirror-ui`
* Now run `source venv/bin/activate`.  The environment is now active.
* Install dependencies using `pip install -r requirements.txt`.
* Install `sudo apt-get install -y gifsicle`
### Create Database
* The project uses postgres database


```
# Login to postgres session
sudo -u postgres psql

# Create a database named mirror 
CREATE DATABASE mirror
WITH OWNER = postgres
ENCODING = 'UTF8' CONNECTION LIMIT = -1;
# Press \q to exit the postgres session
\q
```
* You can use PGadmin to create the database and for an intuitive user interface `https://www.pgadmin.org/download/pgadmin-4-apt/`
* Once setup its time to run the migrations
* go to `cd /opt/edugem/apps/mirror-ui/src/apps/main`
* run `alembic upgrade head`


### For running asynchronous task
* Install redis `https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04`. Do not keep any password as of now. SKIP step 4 of the tutorial.
* go to `/etc/edugem/apps/mirror/src/`
* run `rq worker`

### Config.yml
* run `cp /opt/edugem/apps/mirror/src/config/config.sample.yml /opt/edugem/apps/mirror/src/config/config.yml`
* Now update the newly created `config.yml` file.

### Run Project
* go to `/opt/edugem/apps/mirror-ui/src`
* run `python manage.py runserver`
