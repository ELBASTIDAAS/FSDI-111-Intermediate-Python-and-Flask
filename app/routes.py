# Import Flask to allow us to create our app.
from flask import Flask

# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)


# The "@" symbol designates a "decorator" which attaches the following
@app.get("/")
def index():                        # function to the '/' route. This means that whenever we send a request to
    out = {
        "fName": "Miguel",
        "lName": "Bastidas",
        "age": 24,
        "hobbies": ["Coding", "Gaming", "Reading"],
        "is_active": True
    }
    return out                      # Return the string 'out' as a response.
