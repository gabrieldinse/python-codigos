# Author: Gabriel Dinse
# File: api.py
# Date: 8/26/2020
# Made with PyCharm

# Standard Library

# Third party modules
import flask

# Local application imports
    

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype "\
           "API for distant reading of science fiction novels.</p>"



if __name__ == "__main__":
    app.run()
