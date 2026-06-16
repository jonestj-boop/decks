const http = require('http');
const fs = require('fs');
const path = require('path');
const ROOT = '/Users/melissacedeno/Desktop/Claude/blankslate_deck';
const types = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.pptx':'application/octet-stream'};
http.createServer((req,res)=>{
  let f = decodeURIComponent(req.url.split('?')[0]);
  if(f==='/') f='/Blank_Slate_GTM_Strategy_Scope.html';
  const fp = path.join(ROOT, f);
  fs.readFile(fp,(e,d)=>{
    if(e){res.writeHead(404);res.end('not found');return;}
    res.writeHead(200,{'Content-Type':types[path.extname(fp)]||'application/octet-stream'});
    res.end(d);
  });
}).listen(8099,()=>console.log('serving on 8099'));
