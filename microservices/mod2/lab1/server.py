# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and name it "My Hello World Application"
app = Flask("My Hello World Application")

# Define a route for the root URL ('/')
@app.route("/")
def hello():
    # Return the string "Hello World!" as the response
    return "Hello World!"

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
    # When no port is specified, the server starts at the default port 5000