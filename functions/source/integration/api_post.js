var request = require("request");

request({
  uri: "https://ylw7087h90.execute-api.us-east-1.amazonaws.com/develop",
  method: "POST",
  form: {
    type: "cat",
    price: 123.11
  }
}, function(error, response, body) {
  console.log(body);
});
