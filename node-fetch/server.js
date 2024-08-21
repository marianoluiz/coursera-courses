const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 3000;

const server = http.createServer(
    (req, res) => {
    if (req.url === '/') {

        /* if (req.url === '/'): This block works when the client requests the root URL (http://localhost:3000/). */

        const filePath = path.join(__dirname, 'public', 'index.html');

        /* __dirname represents the current directory of the file server.js. */

        fs.readFile(filePath, (err, content) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end(`Server Error: ${err.message}`);
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(content, 'utf-8');
            }
        });
    } else if (req.url === '/api/posts') {

        /* else if (req.url === '/api/posts'): This block works when the client requests the /api/posts URL */

        /* 
        req.url:
        This is a property of the request object (req) in Node.js. It contains the URL path of the incoming HTTP request.
        
        To handle different types of requests, you need to check if the req.url matches a specific endpoint.

        '/api/posts':
        This is a string representing a specific URL path.
        It is the endpoint that the server is checking for.

        http://localhost:3000/api/posts: This URL is used to access the /api/posts endpoint on your local server

        URL Path: The specific path in the URL that the client requests. For example, /api/posts is an endpoint.

        HTTP Method: The type of HTTP request (GET, POST, PUT, DELETE, etc.) that the client uses to interact with the endpoint. For example, a GET request to /api/posts might retrieve a list of posts, while a POST request to the same endpoint might create a new post.

        Server Logic: The code on the server that handles the request to the endpoint. This includes routing the request to the appropriate handler function and generating the response.
        */

        const posts = [
            { title: 'Post 1', body: 'This is the body of post 1' },
            { title: 'Post 2', body: 'This is the body of post 2' },
            { title: 'Post 3', body: 'This is the body of post 3' },
            { title: 'Post 4', body: 'This is the body of post 4' },
            { title: 'Post 5', body: 'This is the body of post 5' },
            { title: 'Post 6', body: 'This is the body of post 6' },
        ];

        /* This block handles requests to the /api/posts URL. When a request is made to this URL, the server responds with a JSON array of post objects. Each post object contains a title and a body. The array includes six posts in this example. */

        /* 
        URL Path: The endpoint /api/posts is defined by the condition else if (req.url === '/api/posts').

        Array posts: This array is defined within the block that handles the /api/posts endpoint. It is the data that will be sent back as a JSON response when this endpoint is accessed.
        Response: When the server receives a request to /api/posts, it responds with the JSON representation of the posts array. 
*/

        res.writeHead(200, { 'Content-Type': 'application/json' });

        /* writeHead is  is used to set the status code and headers for the HTTP response. It is a method of the http.ServerResponse object.
        
        Headers: { 'Content-Type': 'application/json' } sets the Content-Type header to application/json, indicating that the response body will be in JSON format.
        */

        res.end(JSON.stringify(posts));

        /* used to end the response process.  */
    } else {
        /* else: This block works for all other URLs. It attempts to serve static files from the public directory. If the file does not exist, it returns a 404 error. */

        // Serve static files from the public directory

        const filePath = path.join(__dirname, 'public', req.url);

        /* __dirname represents the current directory of the file server.js. The 'public' is a directory name, and req.url is the URL path that was requested by the client. 
     
         The resulting filePath will be the absolute path to a file in the public directory.
        
         For example, if __dirname is /home/user/project and req.url is /index.html, then the value of filePath will be /home/user/project/public/index.html. 
        
        In the context of the provided code, req.url is used to determine which file the client is requesting from the server.
        */
        
        fs.readFile(filePath, (err, content) => {
            if (err) {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('Not Found');
            } else {
                const ext = path.extname(filePath);
                let contentType = 'text/plain';
                switch (ext) {
                    case '.html':
                        contentType = 'text/html';
                        break;
                    case '.js':
                        contentType = 'application/javascript';
                        break;
                    case '.css':
                        contentType = 'text/css';
                        break;
                }
                res.writeHead(200, { 'Content-Type': contentType });
                res.end(content, 'utf-8');

                /* The res.writeHead method is used to send a response header to the client. It is not always necessary, but it is often used to set the status code and headers for the response. Here are some scenarios where it is necessary or useful: */
            }
        });
    }
});

server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});