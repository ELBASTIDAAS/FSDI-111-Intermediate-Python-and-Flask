# Import Flask to allow us to create our app.
from flask import Flask
from flask import render_template

from datetime import datetime

# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)


# The "@" symbol designates a "decorator" which attaches the following
@app.get("/")
def index():                        # function to the '/' route. This means that whenever we send a request to
    out = {
        "first_Name": "Miguel",
        "last_Name": "Bastidas",
        "hobbies": "Coding, Reading, and Playing Video Games",
        "is_active": True
    }
    return out                      # Return the string 'out' as a response.


@app.get("/about")
def about():
    time_stamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("about.html", timestamp=time_stamp)
