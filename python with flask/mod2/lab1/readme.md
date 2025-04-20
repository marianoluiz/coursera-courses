
### Install Flask
pip install flask

### shorten the prompt
export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "

### run 
flask --app server --debug run

### check
$ curl -X GET -i -w '\n' localhost:5000