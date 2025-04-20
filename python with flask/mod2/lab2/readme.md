# run
flask --app server --debug run

# '/' endpoint
curl -X GET -i -w '\n' localhost:5000

# custom terminal
export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "

# 'no content endpoint'
curl -X GET -i -w '\n' localhost:5000/no_content

- curl:
A command-line tool used to send HTTP requests and interact with web servers.

- X GET:
Specifies the HTTP method to use. In this case, it is GET, which is the default method for curl. This is optional here since GET is the default, but it makes the intent explicit.

- i:
Instructs curl to include the HTTP response headers in the output. This is useful for debugging or inspecting the status code, content type, and other metadata returned by the server.

- w '\n':
Adds a newline (\n) at the end of the output. This ensures the output is cleanly formatted when displayed in the terminal.

- localhost:5000/no_content:
  The URL of the endpoint being accessed:
    localhost: Refers to the local machine where the Flask application is running.
    5000: The default port for Flask's development server.
    /no_content: The specific route defined in your Flask app.

# curls

- curl -X GET -i -w '\n' "localhost:5000/count"

- curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111

- curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287

- curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

- curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{}'

- curl -X POST -i -w '\n' http://localhost:5000/notvalid

