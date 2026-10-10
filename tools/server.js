const http = require("http");
const fs = require("fs");
const path = require("path");
const root = path.resolve(__dirname, "..");
const types = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".ico": "image/x-icon",
};

http
  .createServer((req, res) => {
    const urlPath = decodeURIComponent((req.url || "/").split("?")[0]);
    let file = path.join(root, urlPath === "/" ? "index.html" : urlPath);
    if (!file.startsWith(root)) {
      res.writeHead(403);
      return res.end("Forbidden");
    }
    fs.stat(file, (err, stat) => {
      if (!err && stat.isDirectory()) file = path.join(file, "index.html");
      fs.readFile(file, (readErr, data) => {
        if (readErr) {
          res.writeHead(404);
          return res.end("Not found");
        }
        res.writeHead(200, { "Content-Type": types[path.extname(file)] || "application/octet-stream" });
        res.end(data);
      });
    });
  })
  .listen(4173, "127.0.0.1", () => {
    console.log("http://127.0.0.1:4173");
  });
