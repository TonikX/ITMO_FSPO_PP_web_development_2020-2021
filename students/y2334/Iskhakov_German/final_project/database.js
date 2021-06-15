const MongoClient = require("mongodb").MongoClient;
const objectId = require("mongodb").ObjectID;

require('dotenv').config();

const app = require('./main.js');

const mongoClient = new MongoClient("mongodb://localhost:27017/", { useUnifiedTopology: true });
 
let dbClient;

let database = {

    init: function() {
        mongoClient.connect(function(err, client){
            if(err) return console.log(err);
            dbClient = client;
            app.locals.collection = client.db(process.env.DATABASE || 'calCalcDB').collection(process.env.COLLECTION || 'users');
            console.log("MongoDB ready!");
        });
    }

};

module.exports = database;

process.on("SIGINT", () => {
    dbClient.close();
    console.log('Graceful shutdown: database');
});