
const hostname = 'localhost';
const port = 3000;
var express = import('express');
var app = express();
var server = require('http').createServer(app);

app.use('/', express.static(__dirname + '/'));

var io = require('socket.io')(server);
SOCKET_LIST = {}
io.on('connection', function (socket) {
  var id = Math.random();
  SOCKET_LIST[id] = socket;
  nodes.forEach(element => {
    socket.emit('updateNode', element) 
  });
  io.on('nodeUpdated', (e) => {
    nodes[e.id] = e;
    SOCKET_LIST.forEach(f,sock => {
      if(f != id) sock.emit('updateNode', e)
    })
})
})


server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
