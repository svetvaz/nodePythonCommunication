var express = require("express");
var app = require('express.io')()
app.http().io()
const redis = require('redis');
var pub = redis.createClient();
var sub = redis.createClient();
sub.select('11');


function subscribeToChannel(subscriber,channel) {
    subscriber = redis.createClient();
    subscriber.subscribe(channel);
    return subscriber;
}

function unsubscribeToChannel(subscriber,channel) {
    subscriber.unsubscribe(channel);
    subscriber.end();
}


app.get('/', function(req, res) {
    res.sendfile(__dirname + '/index.html')
});


app.io.route('requestData', function(req) {
    req.io.join(req.data);
    sub.subscribe("ResponseChannel");
    pub.publish('RequestChannel',req.data);

    sub.on("message",function(channel,msg){  
    obj = JSON.parse(msg);
     app.io.room(obj.bizId).broadcast('receivedData', {
        message: obj
    });
    unsubscribeToChannel(sub,'ResponseChannel');
    sub = subscribeToChannel(sub,'ResponseChannel');  // Reset.
   });

});

app.listen(7070)