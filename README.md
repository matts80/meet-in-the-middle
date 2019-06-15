# meet-in-the-middle
Find restaurants in the middle of two addresses at which to meet

## Prerequisites
To run the app locally, first you need to signup for a free API key from [Here](http://here.com).  The app uses their API for the backend location services.  Then, follow the steps below:

### Run as a docker container
The easiest way to check out the app is to run it as a Docker container.  

1.  Download and install the latest Docker version for your OS.

2.  Clone this repo and `cd` into it:
```bash
git clone https://github.com/matts80/meet-in-the-middle.git
cd meet-in-the-middle
```

2.  Edit the `Dockerfile` and place your `APP ID` and `APP Code` in the proper place in the `ENV` docker directives and save the file.

3.  Run the following `docker-compose` command from your terminal:
```bash
docker-compose -f "docker-compose.yml" up -d --build
```

4.  A docker container will be composed running this application and listening on port 5000.  Open a browser and navigate to [localhost:500](http://localhost:5000).

5.  To stop the docker container, run the following command:
```bash
docker container ls
# reference the name of the running container in the next command
docker stop my_container
```

### Run locally without docker
If you don't want to run it in a docker container, do the following.  If you want to develop some features of the app you'll need to do this anyway.

1.  Clone this repo and `cd` into it:
```bash
git clone https://github.com/matts80/meet-in-the-middle.git
cd meet-in-the-middle
```

2.  From inside the project directory, create a new python3 virtualenv and install the requirements:
```bash
pip install virtualenv    # if not already installed
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
```

3.  Export the following environment variables.  Substitute your [Here](http://here.com) API ID and API Code:
```bash
export HERE_APP_ID=<your_here_app_id>
export HERE_APP_CODE=<your_here_app_code>
export FLASK_APP=mitm/app
```

4.  Run the app:
```bash
flask run
```

5.  Navigate to [localhost:5000](http://localhost:5000) to view the app.