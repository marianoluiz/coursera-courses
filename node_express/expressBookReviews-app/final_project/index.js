const express = require('express');
const jwt = require('jsonwebtoken');
const session = require('express-session')
const customer_routes = require('./router/auth_users.js').authenticated;
const genl_routes = require('./router/general.js').general;

const app = express();
app.use(express.json());

app.use("/customer",session({secret:"fingerprint_customer",resave: true, saveUninitialized: true}))

// Middleware to authenticate customers
app.use("/customer/auth/*", function auth(req,res,next){
  if(req.session.authorization){
    //req . session . authorization

    /* 
      {
        "cookie": {
          "originalMaxAge": null,
          "expires": null,
          "httpOnly": true,
          "path": "/"
        },
        "authorization": {
          "accessToken": "your-jwt-token"
        },
        "userId": "12345",
        "username": "john_doe"
      }
    */
    let token = req.session.authorization['accessToken'];

    jwt.verify(token, "access", (err, user) => {
      if(!err) {
        req.user = user;
        next();
      } else {
        return res.status(401).send("Unauthorized Access");
      }
    });

  }else{
    res.status(401).send("Unauthorized Access");
  }

});
 
const PORT =5000;

app.use("/customer", customer_routes);
app.use("/", genl_routes);

//Middleware in Express.js is executed in the order it is defined. The authentication middleware only applies to routes that match /customer/auth/*. Since / does not match this pattern, it bypasses the authentication middleware. so i can access "/" without registering in.

app.listen(PORT,()=>console.log("Server is running"));
