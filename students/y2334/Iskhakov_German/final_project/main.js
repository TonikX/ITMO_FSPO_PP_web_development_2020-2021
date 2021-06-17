
const express = require('express');
const app = express();

const crypto = require('crypto');

const cookieParser = require('cookie-parser');

const path = require('path');

require('dotenv').config();

app.use(express.json());
app.use(cookieParser('key'));
app.use('/static', express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    if (!req.signedCookies.token) {
      res.redirect('/auth');
    }
    res.sendFile(path.join(__dirname, 'public/index.html'));
})

app.get('/auth', (req, res) => {
    if (req.signedCookies.token) {
      res.redirect('/');
    }
    res.sendFile(path.join(__dirname, 'public/html/auth.html'));
})

app.post('/api/exit', (req, res) => {
  if (!req.signedCookies.token) {
    res.redirect('/auth');
  }
  
  res.clearCookie('token');
  res.redirect('/auth');
  

})

app.get('/api/getMe', (req, res) => {
  if (!req.signedCookies.token) {
    res.redirect('/auth');
  }

  console.log(req.signedCookies.token)
  console.log('got')
  
  const collection = req.app.locals.collection;
  collection.find({token: req.signedCookies.token}).toArray(function(err, users){
    console.log({name: users[0].name, surname: users[0].surname, age: users[0].age, height: users[0].height, weight: users[0].weight, sex: users[0].sex})
    res.send(JSON.stringify({name: users[0].name, surname: users[0].surname, age: users[0].age, height: users[0].height, weight: users[0].weight, sex: users[0].sex}));
  });

})

app.get("/api/getMeals", function(req, res){
        
  const collection = req.app.locals.collection;
  collection.find({token: req.signedCookies.token}).toArray(function(err, users){

      if(err) return console.log(err);
    

      if (users.length == 1) {
        res.send(JSON.stringify({status: 'success', data: users[0].meals}));
      } else {
        res.send(JSON.stringify({status: 'error', message: 'User does not exist!'}));
      }
      
  });
 
});

app.post("/api/registerMeal", function(req, res){
        
  const collection = req.app.locals.collection;
  collection.findOneAndUpdate({token: req.signedCookies.token}, { $push: {meals: {'type': req.body.type, 'name': req.body.name, 'cal': req.body.cal}}}, function(err, users){

      if(err) return console.log(err);
      
      console.log(users)

      if (users.ok == 1) {
        res.send(JSON.stringify({status: 'success'}));
      } else {
        res.send(JSON.stringify({status: 'error', message: 'User does not exist!'}));
      }
      
  });
 
});

app.post("/api/updateUser", function(req, res){
        
  const collection = req.app.locals.collection;
  collection.findOneAndUpdate({token: req.signedCookies.token}, { $set: {age: req.body.age, weight: req.body.weight, height: req.body.height, sex: req.body.sex}}, function(err, users){

      if(err) return console.log(err);
      
      console.log(users)

      if (users.ok == 1) {
        res.send(JSON.stringify({status: 'success'}));
      } else {
        res.send(JSON.stringify({status: 'error', message: 'User does not exist!'}));
      }
      
  });
 
});

app.post("/api/logUser", function(req, res){
        
  let val = crypto.randomBytes(32).toString('hex');
  const collection = req.app.locals.collection;
  collection.findOneAndUpdate({login: req.body.login, password: crypto.createHash('sha256').update(req.body.login + req.body.password).digest('hex').toString('hex')}, { $set: {token: val}}, function(err, users){

      if(err) return console.log(err);
      
      console.log(users)

      if (users.ok == 1 && users.value != null) {
        console.log(val)
        res.cookie('token', val, {
          maxAge: 1000 * 60 * 15,
          signed: true,
          secure: false
        });
        res.send(JSON.stringify({status: 'success'}));
      } else {
        res.send(JSON.stringify({status: 'error', message: 'User does not exist!'}));
      }
      
  });
 
});

app.post("/api/createUser", function(req, res){
        
    const collection = req.app.locals.collection;
    collection.find({login: req.body.login}).toArray(function(err, users){
        
        if(err) return console.log(err);

        if (!(users.length)) {

          let secret = crypto.randomBytes(32).toString('hex');

          let user = {
            login: req.body.login,
            password: crypto.createHash('sha256').update(req.body.login + req.body.password).digest('hex').toString('hex'),
            name: req.body.name,
            surname: req.body.surname,
            height: req.body.height,
            weight: req.body.weight,
            age: req.body.age,
            sex: req.body.sex,
            meals: [],
            token: secret
          }

          collection.insertOne(user, function(err, result){
          
            if(err){ 
              console.log(err);
            }
            console.log(result.ops);
            res.cookie('token', secret, {
              maxAge: 1000 * 60 * 15,
              signed: true,
              secure: false
            });
            res.send(JSON.stringify({status: 'success'}));
          });

        } else {
          res.send(JSON.stringify({status: 'error', message: 'User already exists!'}));
        }
        
    });
   
});

app.listen(process.env.PORT || 3000, () => {
  console.log(`port: ${process.env.PORT || 3000}`);
})

module.exports = app;

const database = require('./database.js');
database.init();

process.on("SIGINT", () => {
  console.log('Graceful shutdown: server');
  process.exit();
});
