const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 3000;
let resources = {}; // In-memory JSON database

const requestHandler = (req, res) => {
  /* DISPLAY HTML */
  if (req.method === 'GET' && req.url === '/') {

  /* 
  Purpose: This block serves the index.html file when the user accesses the root URL (/).

  When you navigate to http://localhost:3000/ in your web browser (or use a tool like curl), the browser (or tool) sends an HTTP GET request to http://localhost:3000/
  */

    fs.readFile(path.join(__dirname, 'index.html'), (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: '500 Internal Server Error' }));
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
      }
    });
  } 
  /* DISPLAY ENDPOINT */
  
  else if (req.method === 'GET' && req.url === '/resources') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(resources));
    /* necessary because HTTP responses are sent as plain text */


  } else if (['POST', 'PUT', 'DELETE'].includes(req.method) && req.url === '/resources') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const jsonData = JSON.parse(body);
        if (req.method === 'POST') {
          // Create a new resource
          const id = Date.now().toString();
          resources[id] = jsonData;
          res.writeHead(201, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ message: 'Resource created', id: id, data: jsonData }));
        } else if (req.method === 'PUT') {
          // Update an existing resource
          const id = jsonData.id;
          if (resources[id]) {
            resources[id] = jsonData;
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Resource updated', id: id, data: jsonData }));
          } else {
            res.writeHead(404, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Resource not found' }));
          }
        } else if (req.method === 'DELETE') {
          // Delete a resource
          const id = jsonData.id;
          if (resources[id]) {
            delete resources[id];
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Resource deleted', id: id }));
          } else {
            res.writeHead(404, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Resource not found' }));
          }
        }
      } catch (error) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: '400 Bad Request' }));
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ message: '404 Not Found' }));
  }
};

const server = http.createServer(requestHandler);

server.listen(port, (err) => {
  if (err) {
    return console.log('Something went wrong:', err);
  }
  console.log(`Server running at http://localhost:${port}/`);
});