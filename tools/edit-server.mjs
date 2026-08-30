/* The desk, with a floor under it.
 *
 * The site is static and stays static: this serves the repo unchanged and adds
 * exactly one thing a file:// page cannot do, which is put what has been
 * written back into content.js. Nothing here ships - the deploy workflow copies
 * index.html, content.js and assets/ and never this.
 *
 * Run:  node tools/edit-server.mjs        then open http://localhost:5173/
 *
 * localhost is one of the three ways index.html decides it is being authored
 * rather than read, so the desk is there and the draft in this browser is on.
 *
 * Bound to the loopback address on purpose. It writes a file in the repo on an
 * unauthenticated request, which is safe from this machine and from nowhere
 * else.
 */
import {createServer} from "node:http";
import {readFile, writeFile} from "node:fs/promises";
import {resolve, extname, join} from "node:path";
import {fileURLToPath} from "node:url";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const PORT = Number(process.env.PORT || 5173);

/* The one file the page is allowed to write. Widening this is a decision, not
   a convenience: everything else in the repo is git's to change. */
const WRITABLE = new Set(["/content.js"]);

const TYPES = {
  ".html":"text/html; charset=utf-8", ".js":"text/javascript; charset=utf-8",
  ".css":"text/css; charset=utf-8",   ".json":"application/json",
  ".svg":"image/svg+xml", ".png":"image/png", ".jpg":"image/jpeg",
  ".webp":"image/webp",  ".pdf":"application/pdf", ".md":"text/plain; charset=utf-8"
};

function underRoot(urlPath){
  const clean = decodeURIComponent(urlPath.split("?")[0]);
  const full = resolve(join(ROOT, clean));
  return full === ROOT || full.startsWith(ROOT + "/") ? full : null;
}

async function body(req){
  const chunks = [];
  for await (const c of req) chunks.push(c);
  return Buffer.concat(chunks).toString("utf8");
}

createServer(async (req,res) => {
  const path = req.url === "/" ? "/index.html" : req.url;

  if(req.method === "PUT"){
    const key = path.split("?")[0];
    if(!WRITABLE.has(key)){
      res.writeHead(403,{"content-type":"text/plain"});
      return res.end(key + " is not one of the files the editor may write");
    }
    const text = await body(req);
    /* A truncated write here loses every word on the site, so the shape is
       checked before the file is replaced rather than after. */
    if(!text.includes("window.SITE_CONTENT=")){
      res.writeHead(400,{"content-type":"text/plain"});
      return res.end("that is not a content file — it sets no window.SITE_CONTENT");
    }
    await writeFile(underRoot(key), text, "utf8");
    console.log(new Date().toTimeString().slice(0,8) + "  wrote content.js  " +
                Math.round(text.length/1024) + "KB");
    res.writeHead(204); return res.end();
  }

  const full = underRoot(path);
  if(!full){ res.writeHead(403); return res.end("outside the repo"); }
  try{
    const data = await readFile(full);
    res.writeHead(200,{
      "content-type": TYPES[extname(full).toLowerCase()] || "application/octet-stream",
      "cache-control": "no-store"          /* editing is a reload-heavy loop */
    });
    res.end(data);
  }catch{
    res.writeHead(404,{"content-type":"text/plain"});
    res.end("no such file: " + path);
  }
}).listen(PORT, "127.0.0.1", () => {
  console.log("the desk is open at http://localhost:" + PORT + "/");
  console.log("Publish copy now writes content.js in place — commit it when you like.");
});
