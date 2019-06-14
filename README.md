# meet-in-the-middle
Find restaurants in the middle of two addresses at which to meet

## Setup
To run the app locally, you first need to signup for a free API key from [Here](http://here.com).  The app uses their API for the backend location data.  Then, follow the steps below:

1.  Clone the repo:
```bash
git clone https://github.com/matts80/meet-in-the-middle.git
```

2.  Create a new python3 virtualenv and install the requirements:
```bash
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