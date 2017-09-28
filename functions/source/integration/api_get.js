var http = require('http');

exports.handler = function (event, context) {
    http.get('https://ylw7087h90.execute-api.us-east-1.amazonaws.com/develop', function (result) {
        console.log('Success, with: ' + result.statusCode);
        context.done(null);
    }).on('error', function (err) {
        console.log('Error, with: ' + err.message);
        context.done("Failed");
    });
};
