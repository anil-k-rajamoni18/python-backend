# 🟢 Node.js Crash Course — Complete Reference Guide

> **By:** Node.js Expert & Tutor | **Version:** Node.js 22 LTS | **Level:** Beginner → Advanced

---

## 📑 Table of Contents

1. [Node.js Fundamentals](#1-nodejs-fundamentals)
2. [Module Systems — CJS vs ESM](#2-module-systems--cjs-vs-esm)
3. [Core Built-in Modules](#3-core-built-in-modules)
4. [Asynchronous JavaScript](#4-asynchronous-javascript)
5. [Streams & Buffers](#5-streams--buffers)
6. [File System (fs)](#6-file-system-fs)
7. [Networking — HTTP & HTTPS](#7-networking--http--https)
8. [Events & EventEmitter](#8-events--eventemitter)
9. [Child Processes & Workers](#9-child-processes--workers)
10. [Error Handling](#10-error-handling)
11. [TypeScript with Node.js](#11-typescript-with-nodejs)
12. [Environment & Configuration](#12-environment--configuration)
13. [Logging](#13-logging)
14. [Testing](#14-testing)
15. [Project Management — npm](#15-project-management--npm)
16. [Project Management — yarn](#16-project-management--yarn)
17. [Project Management — pnpm](#17-project-management--pnpm)
18. [Build Tools — tsx, tsup, esbuild](#18-build-tools--tsx-tsup-esbuild)
19. [Resolving Vulnerabilities](#19-resolving-vulnerabilities)
20. [Commands Cheat Sheet](#20-commands-cheat-sheet)
21. [Important Websites & Links](#21-important-websites--links)

---

## 1. Node.js Fundamentals

### What is Node.js?
Node.js is an open-source, cross-platform **JavaScript runtime** built on Chrome's **V8 engine**. It uses a **single-threaded, non-blocking, event-driven** architecture, making it ideal for I/O-intensive applications.

- Created by **Ryan Dahl** in 2009
- Managed by the **OpenJS Foundation**
- Uses **libuv** for the event loop and async I/O under the hood
- LTS releases are supported for 30 months

### Installation
```bash
# Via official installer: https://nodejs.org

# Via nvm (Node Version Manager) — RECOMMENDED
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install --lts           # install latest LTS
nvm install 22              # install specific version
nvm use 22                  # switch version
nvm alias default 22        # set default
nvm ls                      # list installed versions

# Via fnm (Fast Node Manager — Rust-based)
curl -fsSL https://fnm.vercel.app/install | bash
fnm install --lts
fnm use 22

# Check versions
node --version              # v22.x.x
npm --version               # 10.x.x
```

### How Node.js Works — Event Loop

```
   ┌──────────────────────────────┐
   │          timers              │  ← setTimeout, setInterval
   ├──────────────────────────────┤
   │     pending callbacks        │  ← I/O errors from prev tick
   ├──────────────────────────────┤
   │        idle, prepare         │  ← internal
   ├──────────────────────────────┤
   │            poll              │  ← retrieve I/O events ← NEW I/O
   ├──────────────────────────────┤
   │           check              │  ← setImmediate
   ├──────────────────────────────┤
   │      close callbacks         │  ← socket.on('close',...)
   └──────────────────────────────┘

  process.nextTick()  ← runs after CURRENT operation, before next phase
  Promise microtasks  ← run after nextTick queue empties
```

```javascript
console.log("1 - sync");

setTimeout(() => console.log("2 - setTimeout"), 0);
setImmediate(() => console.log("3 - setImmediate"));
Promise.resolve().then(() => console.log("4 - Promise"));
process.nextTick(() => console.log("5 - nextTick"));

console.log("6 - sync");

// Output order: 1, 6, 5, 4, 2, 3
```

### Global Objects
```javascript
// Available everywhere — no import needed
console.log(__filename);          // current file path (CJS only)
console.log(__dirname);           // current directory (CJS only)
console.log(process.version);     // Node version
console.log(process.platform);    // 'linux', 'darwin', 'win32'
console.log(process.env.PATH);    // environment variables
console.log(process.argv);        // [node, script, ...args]
console.log(process.pid);         // process ID
process.exit(0);                  // exit with code 0 (success)
process.exit(1);                  // exit with code 1 (failure)
process.cwd();                    // current working directory
process.memoryUsage();            // { rss, heapTotal, heapUsed, ... }

// Timers
const t = setTimeout(fn, 1000);
clearTimeout(t);
const i = setInterval(fn, 500);
clearInterval(i);
setImmediate(fn);                 // after current poll phase
queueMicrotask(fn);               // microtask queue

// URL & Buffer (available globally in Node 18+)
const url = new URL("https://example.com/path?q=1");
const buf = Buffer.from("hello");
```

---

## 2. Module Systems — CJS vs ESM

### CommonJS (CJS) — Traditional
```javascript
// Exporting
const PI = 3.14159;
function area(r) { return PI * r * r; }
class Circle { constructor(r) { this.r = r; } }

module.exports = { PI, area, Circle };
// or shorthand single export:
module.exports = Circle;

// Importing
const { PI, area, Circle } = require("./math");
const fs = require("fs");            // core modules
const express = require("express");  // npm packages

// Dynamic require
const plugin = require(`./plugins/${name}`);

// __dirname and __filename available natively in CJS
console.log(__dirname);   // /home/user/project
```

### ES Modules (ESM) — Modern Standard
```javascript
// package.json: "type": "module"  ← enables ESM for .js files
// OR use .mjs extension

// Named exports
export const PI = 3.14159;
export function area(r) { return PI * r * r; }
export class Circle { constructor(r) { this.r = r; } }

// Default export
export default class Circle { ... }

// Named imports
import { PI, area, Circle } from "./math.js";  // extension REQUIRED in ESM

// Default import
import Circle from "./circle.js";

// Namespace import
import * as math from "./math.js";

// Side-effect import
import "./setup.js";

// Dynamic import (lazy loading)
const { default: lodash } = await import("lodash");

// __dirname equivalent in ESM
import { fileURLToPath } from "url";
import { dirname } from "path";
const __filename = fileURLToPath(import.meta.url);
const __dirname  = dirname(__filename);

// import.meta
console.log(import.meta.url);           // file URL
console.log(import.meta.dirname);       // Node 22+
console.log(import.meta.filename);      // Node 22+
```

### CJS vs ESM Comparison

| Feature | CJS | ESM |
|---------|-----|-----|
| Syntax | `require()` / `module.exports` | `import` / `export` |
| Loading | Synchronous | Asynchronous |
| Tree-shaking | ❌ | ✅ |
| Top-level `await` | ❌ | ✅ |
| `__dirname` | ✅ native | ❌ (use `import.meta`) |
| Dynamic imports | `require()` | `import()` |
| File extension | `.js` (default) | `.mjs` or `"type":"module"` |
| Default in Node | ✅ | Opt-in |
| Browser compat | ❌ | ✅ |

### package.json Type Field
```json
{
  "type": "module"    // all .js files treated as ESM
}
// Use .cjs extension to force CJS in an ESM package
// Use .mjs extension to force ESM in a CJS package
```

---

## 3. Core Built-in Modules

### Overview
```javascript
// All built-in modules — no npm install needed
import fs          from "fs";             // file system (callback)
import fsp         from "fs/promises";    // file system (promises)
import path        from "path";           // path utilities
import os          from "os";             // OS info
import http        from "http";           // HTTP server
import https       from "https";          // HTTPS server
import net         from "net";            // TCP server
import url         from "url";            // URL parsing
import crypto      from "crypto";         // cryptography
import stream      from "stream";         // streams
import readline    from "readline";       // CLI input
import child_process from "child_process"; // spawn processes
import worker_threads from "worker_threads"; // threads
import events      from "events";         // EventEmitter
import util        from "util";           // promisify, inspect
import buffer      from "buffer";         // Buffer class
import zlib        from "zlib";           // compression
import assert      from "assert";         // assertions
import cluster     from "cluster";        // multi-process
import dns         from "dns";            // DNS lookup
import timers      from "timers/promises"; // async timers
import vm          from "vm";             // sandboxed JS execution
import perf_hooks  from "perf_hooks";     // performance
import diagnostics  from "diagnostics_channel"; // telemetry
```

### path
```javascript
import path from "path";

path.join("/home", "user", "docs", "file.txt");  // /home/user/docs/file.txt
path.resolve("src", "index.js");                  // absolute path from cwd
path.dirname("/home/user/file.txt");              // /home/user
path.basename("/home/user/file.txt");             // file.txt
path.basename("/home/user/file.txt", ".txt");     // file
path.extname("/home/user/file.txt");              // .txt
path.parse("/home/user/file.txt");
// { root:'/', dir:'/home/user', base:'file.txt', ext:'.txt', name:'file' }
path.format({ dir: "/home/user", base: "file.txt" }); // /home/user/file.txt
path.isAbsolute("/home/user");                    // true
path.relative("/home/user", "/home/user/docs");   // docs
path.sep;    // '/' on Unix, '\' on Windows
path.delimiter; // ':' on Unix, ';' on Windows
```

### os
```javascript
import os from "os";

os.platform();       // 'linux', 'darwin', 'win32'
os.arch();           // 'x64', 'arm64'
os.cpus();           // array of CPU info objects
os.totalmem();       // total system memory in bytes
os.freemem();        // free system memory in bytes
os.homedir();        // '/home/user'
os.tmpdir();         // '/tmp'
os.hostname();       // machine hostname
os.networkInterfaces(); // network info
os.uptime();         // system uptime in seconds
os.EOL;              // '\n' on Unix, '\r\n' on Windows
os.loadavg();        // [1min, 5min, 15min] load averages
```

### crypto
```javascript
import crypto from "crypto";

// Hashing
const hash = crypto.createHash("sha256").update("secret").digest("hex");

// HMAC
const hmac = crypto.createHmac("sha256", "key").update("data").digest("hex");

// Random bytes
const token = crypto.randomBytes(32).toString("hex");
const uuid  = crypto.randomUUID();  // Node 15.6+

// Encryption / Decryption (AES-256-GCM)
const key = crypto.randomBytes(32);
const iv  = crypto.randomBytes(12);
const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
let encrypted = cipher.update("plaintext", "utf8", "hex");
encrypted    += cipher.final("hex");
const tag = cipher.getAuthTag();

const decipher = crypto.createDecipheriv("aes-256-gcm", key, iv);
decipher.setAuthTag(tag);
let decrypted = decipher.update(encrypted, "hex", "utf8");
decrypted    += decipher.final("utf8");

// Hashing passwords (use bcrypt/argon2 in production!)
const { scryptSync } = crypto;
const salt = crypto.randomBytes(16).toString("hex");
const derivedKey = scryptSync("password", salt, 64).toString("hex");
```

### util
```javascript
import util from "util";

// Promisify callback-based functions
import { exec } from "child_process";
const execAsync = util.promisify(exec);
const { stdout } = await execAsync("ls -la");

// Inspect (deep object printing)
console.log(util.inspect(obj, { depth: null, colors: true }));

// Format (like printf)
util.format("Hello %s, you are %d", "AK", 30);  // "Hello AK, you are 30"

// Inherits (old OOP — prefer class extends)
util.inherits(MyStream, EventEmitter);

// Type checks
util.types.isPromise(p);
util.types.isMap(m);
util.types.isSet(s);
util.types.isDate(d);
```

---

## 4. Asynchronous JavaScript

### Callbacks (legacy pattern)
```javascript
import fs from "fs";

fs.readFile("file.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error:", err.message);
        return;
    }
    console.log(data);
});

// Callback Hell — avoid this!
getUser(id, (err, user) => {
    getPosts(user.id, (err, posts) => {
        getComments(posts[0].id, (err, comments) => {
            // deeply nested — hard to read & maintain
        });
    });
});
```

### Promises
```javascript
// Creating a Promise
const delay = (ms) => new Promise((resolve, reject) => {
    if (ms < 0) reject(new Error("Negative delay"));
    else setTimeout(() => resolve(`Done after ${ms}ms`), ms);
});

// Chaining
delay(100)
    .then(msg => { console.log(msg); return delay(200); })
    .then(msg => console.log(msg))
    .catch(err => console.error(err))
    .finally(() => console.log("Cleanup"));

// Combinators
await Promise.all([delay(100), delay(200)]);       // all must succeed
await Promise.allSettled([p1, p2, p3]);            // get all results (fail or pass)
await Promise.race([delay(100), delay(500)]);      // first to settle wins
await Promise.any([p1, p2, p3]);                   // first SUCCESS wins
```

### async / await (preferred)
```javascript
import fsp from "fs/promises";

async function processFiles(dir) {
    try {
        const files = await fsp.readdir(dir);
        const contents = await Promise.all(
            files.map(f => fsp.readFile(`${dir}/${f}`, "utf8"))
        );
        return contents.join("\n");
    } catch (err) {
        throw new Error(`Failed to process ${dir}: ${err.message}`);
    }
}

// Top-level await (ESM only)
const result = await processFiles("./docs");

// Sequential vs Parallel
// Sequential (each waits for previous)
for (const url of urls) {
    const data = await fetch(url);
}

// Parallel (all start at once)
const results = await Promise.all(urls.map(url => fetch(url)));

// Parallel with concurrency limit
import pLimit from "p-limit";
const limit = pLimit(5);  // max 5 concurrent
const results = await Promise.all(
    urls.map(url => limit(() => fetch(url)))
);
```

### Async Iterators & for-await-of
```javascript
// Async generator
async function* paginate(endpoint) {
    let page = 1;
    while (true) {
        const res  = await fetch(`${endpoint}?page=${page}`);
        const data = await res.json();
        if (!data.items.length) break;
        yield* data.items;
        page++;
    }
}

// Consuming
for await (const item of paginate("https://api.example.com/items")) {
    console.log(item);
}

// Readable streams are async iterable
import { createReadStream } from "fs";
const stream = createReadStream("large.txt", { encoding: "utf8" });
for await (const chunk of stream) {
    process.stdout.write(chunk);
}
```

---

## 5. Streams & Buffers

### Buffer
```javascript
import { Buffer } from "buffer";

// Create
const buf1 = Buffer.alloc(10);                    // 10 zero bytes
const buf2 = Buffer.from("hello", "utf8");        // from string
const buf3 = Buffer.from([0x48, 0x65, 0x6c]);     // from array

// Convert
buf2.toString("utf8");    // 'hello'
buf2.toString("hex");     // '68656c6c6f'
buf2.toString("base64");  // 'aGVsbG8='

// Operations
Buffer.concat([buf2, buf3]);    // merge buffers
buf2.length;                    // 5
buf2[0];                        // 104 (ASCII 'h')
buf2.slice(1, 3);               // <Buffer 65 6c>
buf2.copy(buf1);                // copy into buf1
```

### Streams
```javascript
import { Readable, Writable, Transform, pipeline } from "stream";
import { pipeline as pipelineAsync } from "stream/promises";
import { createReadStream, createWriteStream } from "fs";
import { createGzip } from "zlib";

// Readable stream
const readable = new Readable({
    read() {
        this.push("chunk 1");
        this.push("chunk 2");
        this.push(null);   // EOF
    }
});

// Writable stream
const writable = new Writable({
    write(chunk, encoding, callback) {
        console.log("Received:", chunk.toString());
        callback();  // signal done
    }
});

// Transform stream
const upperCase = new Transform({
    transform(chunk, encoding, callback) {
        this.push(chunk.toString().toUpperCase());
        callback();
    }
});

// Pipeline (handles error + cleanup automatically)
await pipelineAsync(
    createReadStream("input.txt"),
    createGzip(),
    createWriteStream("output.txt.gz")
);

// Manual pipe
readable.pipe(upperCase).pipe(writable);

// Object mode streams
const objectStream = new Readable({
    objectMode: true,
    read() {
        this.push({ id: 1, name: "AK" });
        this.push(null);
    }
});
```

---

## 6. File System (fs)

```javascript
import fsp from "fs/promises";
import { createReadStream, createWriteStream, watch } from "fs";
import path from "path";

// ── READ ──────────────────────────────────────────────
const text   = await fsp.readFile("data.txt", "utf8");
const buffer = await fsp.readFile("image.png");          // Buffer

// ── WRITE ─────────────────────────────────────────────
await fsp.writeFile("out.txt", "Hello Node.js!", "utf8");
await fsp.appendFile("log.txt", "New line\n");

// ── COPY / MOVE / DELETE ───────────────────────────────
await fsp.copyFile("src.txt", "dest.txt");
await fsp.rename("old.txt", "new.txt");    // move or rename
await fsp.unlink("file.txt");              // delete file

// ── DIRECTORIES ────────────────────────────────────────
await fsp.mkdir("new-dir", { recursive: true });
await fsp.rmdir("empty-dir");
await fsp.rm("dir-with-contents", { recursive: true, force: true });
const entries = await fsp.readdir(".", { withFileTypes: true });
entries.filter(e => e.isFile()).map(e => e.name);

// ── STAT / INFO ────────────────────────────────────────
const stat = await fsp.stat("file.txt");
stat.size;          // bytes
stat.mtime;         // last modified Date
stat.isFile();      // true
stat.isDirectory(); // false

// ── SYMLINKS ───────────────────────────────────────────
await fsp.symlink("target.txt", "link.txt");
await fsp.readlink("link.txt");

// ── GLOB (Node 22+) ────────────────────────────────────
import { glob } from "fs/promises";
for await (const file of glob("**/*.ts")) {
    console.log(file);
}

// ── WATCH FILES ────────────────────────────────────────
const watcher = watch("./src", { recursive: true });
for await (const { eventType, filename } of watcher) {
    console.log(`${eventType}: ${filename}`);
}

// ── STREAMING LARGE FILES ──────────────────────────────
const input  = createReadStream("huge.csv");
const output = createWriteStream("processed.csv");
input.pipe(output);
```

---

## 7. Networking — HTTP & HTTPS

### Built-in HTTP Server
```javascript
import http from "http";

const server = http.createServer((req, res) => {
    const { method, url, headers } = req;

    // Parse URL
    const parsedUrl = new URL(url, `http://${headers.host}`);
    const pathname  = parsedUrl.pathname;
    const query     = Object.fromEntries(parsedUrl.searchParams);

    // Read request body
    let body = "";
    req.on("data", chunk => body += chunk);
    req.on("end", () => {
        const data = body ? JSON.parse(body) : null;

        // Routing
        if (method === "GET" && pathname === "/") {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ message: "Hello Node.js!", query }));
        } else if (method === "POST" && pathname === "/echo") {
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ received: data }));
        } else {
            res.writeHead(404, { "Content-Type": "application/json" });
            res.end(JSON.stringify({ error: "Not Found" }));
        }
    });
});

server.listen(3000, "0.0.0.0", () => {
    console.log("Server running at http://localhost:3000");
});

server.on("error", err => console.error("Server error:", err));
```

### Fetch API (Node 18+ built-in)
```javascript
// GET
const res  = await fetch("https://api.example.com/users");
const data = await res.json();

// POST with JSON
const res2 = await fetch("https://api.example.com/users", {
    method:  "POST",
    headers: { "Content-Type": "application/json", "Authorization": `Bearer ${token}` },
    body:    JSON.stringify({ name: "AK", role: "admin" }),
});
if (!res2.ok) throw new Error(`HTTP ${res2.status}: ${res2.statusText}`);
const created = await res2.json();

// Streaming response
const res3 = await fetch("https://example.com/large-file");
await pipeline(
    Readable.fromWeb(res3.body),
    createWriteStream("download.bin")
);
```

### HTTP/2
```javascript
import http2 from "http2";
import { readFileSync } from "fs";

const server = http2.createSecureServer({
    key:  readFileSync("server.key"),
    cert: readFileSync("server.crt"),
});

server.on("stream", (stream, headers) => {
    stream.respond({ ":status": 200, "content-type": "text/html" });
    stream.end("<h1>HTTP/2 response</h1>");
});

server.listen(443);
```

### WebSockets (with `ws` package)
```javascript
import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ port: 8080 });

wss.on("connection", (ws, req) => {
    console.log("Client connected:", req.socket.remoteAddress);

    ws.on("message", (data) => {
        // Broadcast to all clients
        wss.clients.forEach(client => {
            if (client.readyState === ws.OPEN) {
                client.send(data.toString());
            }
        });
    });

    ws.on("close", () => console.log("Client disconnected"));
    ws.on("error", err => console.error("WS error:", err));

    ws.send(JSON.stringify({ type: "welcome", msg: "Connected!" }));
});
```

---

## 8. Events & EventEmitter

```javascript
import { EventEmitter } from "events";

class Database extends EventEmitter {
    constructor() {
        super();
        this.connected = false;
    }

    async connect(url) {
        try {
            // Simulate connection
            await new Promise(r => setTimeout(r, 100));
            this.connected = true;
            this.emit("connect", { url, at: new Date() });
        } catch (err) {
            this.emit("error", err);
        }
    }

    query(sql) {
        if (!this.connected) throw new Error("Not connected");
        this.emit("query", { sql, at: Date.now() });
        return [];
    }

    disconnect() {
        this.connected = false;
        this.emit("disconnect");
    }
}

const db = new Database();

db.on("connect",    info => console.log("Connected:", info.url));
db.on("disconnect", ()   => console.log("Disconnected"));
db.on("query",      info => console.log("SQL:", info.sql));
db.on("error",      err  => console.error("DB Error:", err));

// One-time listener
db.once("connect", () => console.log("First connect!"));

// Remove listener
const handler = () => {};
db.on("query", handler);
db.off("query", handler);   // removeListener alias

// Async events (Node 12+)
import { on, once } from "events";

// Wait for one event
const [info] = await once(db, "connect");

// Iterate all events
for await (const [info] of on(db, "query")) {
    console.log(info);
    if (shouldStop) break;
}

// Max listeners (default 10; increase to avoid warnings)
db.setMaxListeners(20);
EventEmitter.defaultMaxListeners = 20;
```

---

## 9. Child Processes & Workers

### child_process
```javascript
import { exec, execSync, spawn, fork } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

// exec — shell command, buffer output
const { stdout, stderr } = await execAsync("ls -la");
console.log(stdout);

// execSync — synchronous (blocks event loop!)
const output = execSync("git log --oneline -5").toString();

// spawn — streaming output, no shell by default
const ls = spawn("ls", ["-la", "/home"], { stdio: "pipe" });
ls.stdout.on("data", data => process.stdout.write(data));
ls.stderr.on("data", data => process.stderr.write(data));
ls.on("close", code => console.log(`Exited: ${code}`));

// fork — spawn a new Node.js process with IPC channel
const child = fork("./worker.js");
child.send({ type: "start", payload: data });
child.on("message", msg => console.log("From child:", msg));
child.on("exit", code => console.log(`Child exited: ${code}`));
```

### Worker Threads (CPU-bound tasks)
```javascript
// main.js
import { Worker, isMainThread, parentPort, workerData } from "worker_threads";

if (isMainThread) {
    const worker = new Worker(import.meta.filename, {
        workerData: { numbers: [1, 2, 3, 4, 5] }
    });

    worker.on("message",  result => console.log("Result:", result));
    worker.on("error",    err    => console.error("Worker error:", err));
    worker.on("exit",     code   => console.log("Worker exited:", code));
} else {
    // Worker code
    const { numbers } = workerData;
    const sum = numbers.reduce((a, b) => a + b, 0);
    parentPort.postMessage({ sum });
}

// Worker Pool pattern (reuse workers)
import { StaticPool } from "node-worker-threads-pool"; // npm package
const pool = new StaticPool({
    size: 4,
    task: "./heavy-computation.js",
});
const result = await pool.exec(inputData);
```

### Cluster (multi-process HTTP server)
```javascript
import cluster from "cluster";
import http    from "http";
import os      from "os";

if (cluster.isPrimary) {
    const numCPUs = os.cpus().length;
    console.log(`Primary ${process.pid} running, forking ${numCPUs} workers`);

    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on("exit", (worker, code) => {
        console.log(`Worker ${worker.process.pid} died (${code}), respawning`);
        cluster.fork();
    });
} else {
    http.createServer((req, res) => {
        res.end(`Handled by worker ${process.pid}\n`);
    }).listen(3000);

    console.log(`Worker ${process.pid} started`);
}
```

---

## 10. Error Handling

### Synchronous Errors
```javascript
try {
    JSON.parse("invalid JSON");
} catch (err) {
    if (err instanceof SyntaxError) {
        console.error("JSON parse error:", err.message);
    } else {
        throw err;  // re-throw unexpected errors
    }
}
```

### Async Error Handling
```javascript
// async/await — always wrap in try/catch
async function fetchUser(id) {
    try {
        const res = await fetch(`/api/users/${id}`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (err) {
        // Classify errors
        if (err.name === "AbortError") throw err;   // timeout
        if (err.message.startsWith("HTTP 4")) {
            throw new NotFoundError(`User ${id} not found`);
        }
        throw new ServiceError("User fetch failed", { cause: err });
    }
}
```

### Custom Error Classes
```javascript
class AppError extends Error {
    constructor(message, options = {}) {
        super(message, { cause: options.cause });
        this.name        = this.constructor.name;
        this.statusCode  = options.statusCode  ?? 500;
        this.isOperational = options.isOperational ?? true;
        Error.captureStackTrace(this, this.constructor);
    }
}

class NotFoundError    extends AppError { constructor(msg, opts) { super(msg, { ...opts, statusCode: 404 }); } }
class ValidationError  extends AppError { constructor(msg, opts) { super(msg, { ...opts, statusCode: 400 }); } }
class UnauthorizedError extends AppError { constructor(msg, opts) { super(msg, { ...opts, statusCode: 401 }); } }
class ServiceError     extends AppError { constructor(msg, opts) { super(msg, { ...opts, statusCode: 503 }); } }

// Express error middleware
app.use((err, req, res, next) => {
    const status  = err.statusCode ?? 500;
    const message = err.isOperational ? err.message : "Internal Server Error";
    res.status(status).json({ error: message });
    if (status >= 500) logger.error(err);
});
```

### Global Error Handlers
```javascript
// Catch unhandled promise rejections
process.on("unhandledRejection", (reason, promise) => {
    console.error("Unhandled Rejection at:", promise, "reason:", reason);
    process.exit(1);  // recommended: fail fast
});

// Catch synchronous uncaught exceptions
process.on("uncaughtException", (err, origin) => {
    console.error("Uncaught Exception:", err, "Origin:", origin);
    // Cleanup resources, then exit
    process.exit(1);
});

// Graceful shutdown
const signals = ["SIGTERM", "SIGINT", "SIGUSR2"];
signals.forEach(sig => {
    process.on(sig, async () => {
        console.log(`\nReceived ${sig}, shutting down gracefully`);
        await server.close();
        await db.disconnect();
        process.exit(0);
    });
});
```

---

## 11. TypeScript with Node.js

### Setup
```bash
npm install -D typescript @types/node ts-node tsx
npx tsc --init   # create tsconfig.json
```

### tsconfig.json (Recommended for Node.js)
```json
{
  "compilerOptions": {
    "target":          "ES2022",
    "module":          "NodeNext",
    "moduleResolution": "NodeNext",
    "lib":             ["ES2022"],
    "outDir":          "./dist",
    "rootDir":         "./src",
    "strict":          true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "declaration":     true,
    "declarationMap":  true,
    "sourceMap":       true,
    "skipLibCheck":    true,
    "resolveJsonModule": true,
    "noUnusedLocals":  true,
    "noImplicitReturns": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### TypeScript Patterns for Node.js
```typescript
import { Request, Response, NextFunction } from "express";

// Typed environment variables
const config = {
    port:     Number(process.env.PORT)     || 3000,
    nodeEnv:  process.env.NODE_ENV         || "development",
    dbUrl:    process.env.DATABASE_URL     ?? (() => { throw new Error("DATABASE_URL required"); })(),
} as const;

// Typed async middleware
type AsyncHandler = (req: Request, res: Response, next: NextFunction) => Promise<void>;

const asyncWrap = (fn: AsyncHandler) =>
    (req: Request, res: Response, next: NextFunction) =>
        fn(req, res, next).catch(next);

// Typed EventEmitter
import { EventEmitter } from "events";

interface AppEvents {
    "user:created": [user: User];
    "user:deleted": [id: string];
    "error":        [err: Error];
}

class TypedEmitter extends EventEmitter {
    emit<K extends keyof AppEvents>(event: K, ...args: AppEvents[K]): boolean {
        return super.emit(event, ...args);
    }
    on<K extends keyof AppEvents>(event: K, listener: (...args: AppEvents[K]) => void): this {
        return super.on(event, listener as (...args: unknown[]) => void);
    }
}

// Zod for runtime validation
import { z } from "zod";

const UserSchema = z.object({
    name:  z.string().min(1).max(100),
    email: z.string().email(),
    age:   z.number().int().min(0).max(150).optional(),
    role:  z.enum(["admin", "user", "moderator"]).default("user"),
});

type User = z.infer<typeof UserSchema>;

function createUser(data: unknown): User {
    return UserSchema.parse(data);   // throws ZodError if invalid
}
```

---

## 12. Environment & Configuration

### dotenv
```bash
npm install dotenv
```

```javascript
// Load .env at app entry point
import "dotenv/config";             // ESM — auto-loads .env

// OR
import dotenv from "dotenv";
dotenv.config({ path: ".env.local" });

// Access
const dbUrl = process.env.DATABASE_URL;

// .env file
// DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
// PORT=3000
// NODE_ENV=development
// JWT_SECRET=supersecretkey
// LOG_LEVEL=info
```

### Zod-powered Config Validation
```typescript
import { z } from "zod";
import "dotenv/config";

const EnvSchema = z.object({
    NODE_ENV:     z.enum(["development", "test", "production"]).default("development"),
    PORT:         z.coerce.number().default(3000),
    DATABASE_URL: z.string().url(),
    JWT_SECRET:   z.string().min(32),
    LOG_LEVEL:    z.enum(["debug", "info", "warn", "error"]).default("info"),
    CORS_ORIGIN:  z.string().optional(),
});

const _env = EnvSchema.safeParse(process.env);
if (!_env.success) {
    console.error("Invalid environment variables:", _env.error.format());
    process.exit(1);
}

export const env = _env.data;
// Now env is fully typed!
```

### Multiple .env Files
```
.env               ← base defaults (safe to commit)
.env.local         ← local overrides (git-ignored)
.env.development   ← dev environment
.env.production    ← prod (never commit secrets!)
.env.test          ← test environment
```

```bash
# .gitignore
.env.local
.env.production
.env.*.local
```

---

## 13. Logging

### pino (high-performance — recommended)
```bash
npm install pino pino-pretty
```

```typescript
import pino from "pino";

const logger = pino({
    level: process.env.LOG_LEVEL || "info",
    transport: process.env.NODE_ENV !== "production"
        ? { target: "pino-pretty", options: { colorize: true } }
        : undefined,
    base:      { pid: process.pid, service: "my-api" },
    timestamp: pino.stdTimeFunctions.isoTime,
    redact:    ["req.headers.authorization", "*.password"],  // hide secrets
});

// Usage
logger.info({ userId: 1 }, "User logged in");
logger.warn({ url }, "Slow request");
logger.error({ err }, "Unhandled error");
logger.debug({ query }, "DB query executed");

// Child logger (inherit context)
const reqLogger = logger.child({ requestId: "abc123" });
reqLogger.info("Processing request");

// Express middleware
app.use((req, res, next) => {
    req.log = logger.child({ requestId: crypto.randomUUID() });
    next();
});
```

### winston (feature-rich)
```bash
npm install winston
```

```typescript
import winston from "winston";

const logger = winston.createLogger({
    level: "info",
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.errors({ stack: true }),
        winston.format.json()
    ),
    transports: [
        new winston.transports.Console({
            format: winston.format.combine(
                winston.format.colorize(),
                winston.format.simple()
            ),
        }),
        new winston.transports.File({ filename: "logs/error.log", level: "error" }),
        new winston.transports.File({ filename: "logs/combined.log" }),
    ],
});

logger.info("Server started", { port: 3000 });
logger.error("DB connection failed", new Error("timeout"));
```

---

## 14. Testing

### Vitest (recommended — fast, Vite-powered)
```bash
npm install -D vitest @vitest/coverage-v8 supertest
```

```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";
export default defineConfig({
    test: {
        globals:     true,
        environment: "node",
        coverage:    { provider: "v8", reporter: ["text", "html"] },
    },
});

// sum.test.ts
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";

describe("UserService", () => {
    beforeEach(() => { /* setup */ });
    afterEach(()  => { vi.restoreAllMocks(); });

    it("creates a user", async () => {
        const user = await UserService.create({ name: "AK", email: "ak@ex.com" });
        expect(user).toMatchObject({ name: "AK" });
        expect(user.id).toBeDefined();
    });

    it("throws on invalid email", async () => {
        await expect(UserService.create({ email: "bad" })).rejects.toThrow("Invalid email");
    });

    it("mocks external calls", async () => {
        const spy = vi.spyOn(db, "query").mockResolvedValue([{ id: 1 }]);
        const result = await UserService.findAll();
        expect(spy).toHaveBeenCalledOnce();
        expect(result).toHaveLength(1);
    });
});

// Parametrized tests
it.each([
    [1, 2, 3],
    [0, 0, 0],
    [-1, 1, 0],
])("adds %i + %i = %i", (a, b, expected) => {
    expect(a + b).toBe(expected);
});
```

### Jest
```bash
npm install -D jest @types/jest ts-jest
```

```json
// jest.config.json
{
  "preset": "ts-jest",
  "testEnvironment": "node",
  "moduleNameMapper": {
    "^@/(.*)$": "<rootDir>/src/$1"
  }
}
```

### Supertest (HTTP integration testing)
```typescript
import { describe, it, expect, beforeAll, afterAll } from "vitest";
import request from "supertest";
import app     from "../src/app";

describe("GET /api/users", () => {
    it("returns 200 with array", async () => {
        const res = await request(app)
            .get("/api/users")
            .set("Authorization", `Bearer ${token}`)
            .expect(200)
            .expect("Content-Type", /json/);

        expect(res.body).toBeInstanceOf(Array);
    });

    it("returns 401 without token", async () => {
        await request(app).get("/api/users").expect(401);
    });
});
```

### Node.js built-in test runner (Node 20+)
```javascript
import { test, describe, it, before, after, mock } from "node:test";
import assert from "node:assert/strict";

describe("Calculator", () => {
    it("adds numbers", () => {
        assert.equal(1 + 1, 2);
    });

    it("async test", async () => {
        const result = await fetchData();
        assert.deepStrictEqual(result, { status: "ok" });
    });
});

// Run: node --test
// Or:  node --test src/**/*.test.js
```

---

## 15. Project Management — npm

### What is npm?
npm (Node Package Manager) is the default package manager bundled with Node.js. It uses `package.json` and `package-lock.json`.

### Initialization
```bash
npm init              # interactive
npm init -y           # accept all defaults (quick)
```

### Dependency Management
```bash
npm install package             # add runtime dep
npm install -D package          # add dev dep (--save-dev)
npm install -g package          # global install
npm install "package@^2.0"      # version range
npm install                     # install all from package.json
npm ci                          # clean install from lock file (CI/CD)
npm uninstall package           # remove
npm update                      # update all
npm update package              # update specific
npm outdated                    # show outdated packages
npm list                        # list installed
npm list --depth=0              # top-level only
npm dedupe                      # deduplicate packages
npm prune                       # remove extraneous packages
```

### Scripts
```json
{
  "scripts": {
    "start":      "node dist/index.js",
    "dev":        "tsx watch src/index.ts",
    "build":      "tsup src/index.ts --format esm,cjs --dts",
    "test":       "vitest run",
    "test:watch": "vitest",
    "test:cov":   "vitest run --coverage",
    "lint":       "eslint src --ext .ts,.tsx",
    "lint:fix":   "eslint src --ext .ts,.tsx --fix",
    "format":     "prettier --write src/",
    "typecheck":  "tsc --noEmit",
    "audit":      "npm audit",
    "audit:fix":  "npm audit fix",
    "clean":      "rimraf dist",
    "prepare":    "husky install"
  }
}
```

```bash
npm run dev           # run script
npm start             # shorthand (no 'run' needed for start, test)
npm test              # shorthand

# Pass arguments to scripts
npm run build -- --minify

# Pre/Post hooks
# "prebuild": "npm run clean"   ← auto-runs before build
# "postbuild": "echo Done!"     ← auto-runs after build
```

### package.json Anatomy
```json
{
  "name":        "my-app",
  "version":     "1.0.0",
  "description": "Awesome Node app",
  "author":      "AK <ak@example.com>",
  "license":     "MIT",
  "private":     true,
  "type":        "module",
  "main":        "dist/index.cjs",
  "module":      "dist/index.js",
  "types":       "dist/index.d.ts",
  "exports": {
    ".": {
      "import":  "./dist/index.js",
      "require": "./dist/index.cjs",
      "types":   "./dist/index.d.ts"
    }
  },
  "engines": { "node": ">=20.0.0" },
  "dependencies": {
    "express": "^4.19.2",
    "zod":     "^3.23.0"
  },
  "devDependencies": {
    "typescript":  "^5.4.5",
    "@types/node": "^22.0.0",
    "vitest":      "^1.6.0",
    "tsup":        "^8.0.0",
    "tsx":         "^4.9.0"
  }
}
```

### Versioning — semver
```
MAJOR.MINOR.PATCH  →  2.4.1

^2.4.1  → >=2.4.1 <3.0.0  (same major)
~2.4.1  → >=2.4.1 <2.5.0  (same major.minor)
2.4.1   → exactly 2.4.1
>=2.4.1 → 2.4.1 or higher
*       → any version
```

### Publishing to npm
```bash
npm login
npm version patch      # 1.0.0 → 1.0.1
npm version minor      # 1.0.0 → 1.1.0
npm version major      # 1.0.0 → 2.0.0
npm publish
npm publish --access public  # for scoped packages (@scope/pkg)
npm unpublish pkg@1.0.0 --force
```

---

## 16. Project Management — yarn

### What is yarn?
Yarn is a fast, reliable, and secure dependency manager by Meta. Yarn v1 (Classic) and Yarn v4 (Berry) differ significantly.

### Installation
```bash
# Yarn v1 (Classic)
npm install -g yarn

# Yarn v4 (Berry) — per-project via corepack
corepack enable
yarn set version stable    # in project
```

### yarn v1 Commands
```bash
yarn init -y                    # init project
yarn add package                # add dep
yarn add -D package             # add dev dep
yarn add -g package             # global
yarn remove package             # remove
yarn install                    # install all
yarn install --frozen-lockfile  # CI — fails if lock file would change
yarn upgrade                    # upgrade all
yarn upgrade package            # upgrade specific
yarn upgrade-interactive        # interactive upgrade UI
yarn list                       # list packages
yarn why package                # why is this installed?
yarn info package               # package details
yarn run script                 # run npm script
yarn start / yarn test          # shorthand
yarn audit                      # security audit
yarn audit --fix                # attempt fixes
yarn link                       # link local package
yarn publish                    # publish to npm
```

### yarn Berry (v4) — Zero-Installs
```bash
yarn add package
yarn remove package
yarn up package           # update
yarn up "*"               # update all
yarn dlx create-next-app  # like npx
yarn workspaces list      # monorepo workspaces
yarn workspaces foreach run build   # run in all workspaces
```

### yarn vs npm vs pnpm

| Feature | npm | yarn v1 | pnpm |
|---------|-----|---------|------|
| Lock file | `package-lock.json` | `yarn.lock` | `pnpm-lock.yaml` |
| Speed | Moderate | Fast | Fastest |
| Disk usage | High | High | Low (hardlinks) |
| Workspaces | ✅ | ✅ | ✅ |
| Plug'n'Play | ❌ | ✅ (Berry) | ❌ |
| Strictness | Low | Low | High |
| Security | ✅ audit | ✅ audit | ✅ audit |

---

## 17. Project Management — pnpm

### What is pnpm?
pnpm uses a **content-addressable store** with hard links — packages are stored once on disk and linked into projects. This saves disk space and is significantly faster.

### Installation
```bash
npm install -g pnpm
# Or via corepack
corepack enable
corepack prepare pnpm@latest --activate

pnpm --version
```

### Commands
```bash
pnpm init                   # init project
pnpm add package            # add dep
pnpm add -D package         # add dev dep
pnpm add -g package         # global
pnpm remove package         # remove
pnpm install                # install all
pnpm install --frozen-lockfile  # CI
pnpm update                 # update all
pnpm update --interactive   # interactive
pnpm outdated               # show outdated
pnpm list                   # list packages
pnpm why package            # why installed?
pnpm run dev                # run script
pnpm exec vitest            # run local binary
pnpm dlx create-next-app    # like npx
pnpm store path             # content-addressable store path
pnpm store prune            # clean unused store
pnpm audit                  # security audit
pnpm audit --fix            # fix vulnerabilities
```

### pnpm Workspaces (Monorepo)
```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
  - "!**/node_modules/**"
```

```bash
pnpm -r run build                    # run in all packages
pnpm --filter @myorg/api run dev     # run in specific package
pnpm --filter "...@myorg/shared" run build  # and its dependents
pnpm add @myorg/shared --workspace   # add workspace package
```

---

## 18. Build Tools — tsx, tsup, esbuild

### tsx — Run TypeScript directly
```bash
npm install -D tsx

# Run TypeScript without compilation
tsx src/index.ts

# Watch mode (dev server)
tsx watch src/index.ts

# Execute inline
tsx -e "console.log('hello')"

# As script runner
# package.json: "dev": "tsx watch src/index.ts"
```

### tsup — Bundle TypeScript libraries
```bash
npm install -D tsup

# CLI
tsup src/index.ts --format esm,cjs --dts --clean

# Config file: tsup.config.ts
import { defineConfig } from "tsup";

export default defineConfig({
    entry:     ["src/index.ts"],
    format:    ["esm", "cjs"],
    dts:       true,           // generate .d.ts files
    sourcemap: true,
    clean:     true,           // clean dist/ before build
    splitting: false,
    minify:    process.env.NODE_ENV === "production",
    external:  ["express"],    // don't bundle — keep as peerDep
    shims:     true,           // ESM shims for __dirname etc.
    outDir:    "dist",
    target:    "node20",
});
```

### esbuild — Extremely fast bundler
```bash
npm install -D esbuild

# CLI — bundle for Node.js
esbuild src/index.ts \
    --bundle \
    --platform=node \
    --target=node20 \
    --format=esm \
    --outfile=dist/index.mjs \
    --sourcemap \
    --minify

# API (build script)
import { build } from "esbuild";

await build({
    entryPoints: ["src/index.ts"],
    bundle:      true,
    platform:    "node",
    target:      "node20",
    format:      "esm",
    outdir:      "dist",
    sourcemap:   true,
    external:    ["express", "pg", "redis"],  // don't bundle
    minify:      true,
});
```

### Recommended Stack
```
Development:  tsx watch src/index.ts       (fast, no compile step)
Production:   tsup or esbuild → dist/      (optimized bundle)
Type Check:   tsc --noEmit                 (separate from build)
Tests:        vitest                       (uses esbuild internally)
```

---

## 19. Resolving Vulnerabilities

### Tools for Scanning

#### 1. npm audit (built-in)
```bash
# Audit all dependencies
npm audit

# Audit only production deps
npm audit --omit=dev

# JSON output for CI parsing
npm audit --json

# Auto-fix (bumps versions — verify it doesn't break anything!)
npm audit fix

# Force fix (may include breaking changes)
npm audit fix --force

# Ignore specific advisories
npm audit --ignore-path .auditignore
```

#### 2. pnpm audit / yarn audit
```bash
pnpm audit
pnpm audit --fix

yarn audit
yarn audit --level high   # only high and critical
```

#### 3. Snyk (deeper scanning)
```bash
npm install -g snyk
snyk auth

snyk test                           # scan
snyk test --severity-threshold=high # only high+
snyk monitor                        # ongoing monitoring
snyk fix                            # auto-fix
snyk container test myimage:latest  # scan Docker image
snyk iac test k8s/                  # scan Kubernetes configs
```

#### 4. Socket.dev (supply chain security)
```bash
npx socket@latest report
# Analyzes packages for malicious behavior, not just CVEs
```

#### 5. retire.js (frontend + backend)
```bash
npm install -g retire
retire --node       # scan Node.js deps
retire --js         # scan JS files
```

#### 6. OWASP Dependency-Check
```bash
# Docker
docker run --rm \
  -v $(pwd):/src \
  owasp/dependency-check \
  --scan /src \
  --format HTML
```

### Common Node.js Vulnerabilities & Fixes

| Vulnerability | Tool | Fix |
|---------------|------|-----|
| Prototype pollution | `npm audit`, snyk | Update affected pkg, use `Object.create(null)` |
| ReDoS (regex DoS) | snyk | Update or replace vulnerable regex |
| Path traversal | bandit, manual | Validate & sanitize file paths |
| Command injection | code review | Use `execFile` / `spawn` with args array, never `exec(userInput)` |
| SQL injection | code review | Always use parameterized queries / ORM |
| XSS | code review | Sanitize with DOMPurify or escape HTML |
| Hardcoded secrets | `git-secrets`, trufflehog | Move to env vars, rotate secret |
| Insecure deserialization | code review | Avoid `JSON.parse` on untrusted without schema validation |
| Outdated dep | `npm outdated` | `npm update` or pin safe version |
| Malicious package | socket.dev | Verify publisher, check downloads, use lockfiles |

### Secure Node.js Patterns
```javascript
// ✅ Use execFile (not exec) — avoids shell injection
import { execFile } from "child_process";
execFile("git", ["log", "--oneline"], callback);

// ✅ Validate & sanitize paths
import path from "path";
const BASE = "/var/www/uploads";
function safePath(userInput) {
    const resolved = path.resolve(BASE, userInput);
    if (!resolved.startsWith(BASE)) {
        throw new Error("Path traversal detected!");
    }
    return resolved;
}

// ✅ Parameterized SQL (using pg)
const res = await pool.query(
    "SELECT * FROM users WHERE id = $1 AND role = $2",
    [userId, role]    // safe — never interpolated
);

// ✅ Load secrets from env, never hardcode
const secret = process.env.JWT_SECRET;
if (!secret) throw new Error("JWT_SECRET not set!");

// ✅ Set security headers (use Helmet for Express)
import helmet from "helmet";
app.use(helmet());

// ✅ Rate limiting
import rateLimit from "express-rate-limit";
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }));

// ✅ Validate all input (Zod)
const schema = z.object({ id: z.string().uuid() });
const { id } = schema.parse(req.params);

// ✅ Use crypto.randomBytes for tokens (not Math.random)
import crypto from "crypto";
const token = crypto.randomBytes(32).toString("hex");
```

### GitHub Actions — Security Workflow
```yaml
name: Security Audit

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: "0 6 * * 1"

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"

      - run: npm ci

      - name: npm audit
        run: npm audit --omit=dev --audit-level=high

      - name: Snyk scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      - name: OSSF Scorecard
        uses: ossf/scorecard-action@v2
```

### Keeping Dependencies Updated
```bash
# npx tools — no install needed
npx npm-check-updates          # show updates
npx npm-check-updates -u       # update package.json
npm install                    # install updated versions

# Interactive
npx npm-check-updates --interactive

# For pnpm
pnpm update --interactive --latest
```

---

## 20. Commands Cheat Sheet

### Node.js Runtime
```bash
node --version                        # version
node script.js                        # run script
node -e "console.log(process.version)"# inline eval
node -p "os.platform()"               # eval & print
node --inspect src/index.js           # debug mode
node --inspect-brk src/index.js       # debug, break on start
node --watch src/index.js             # auto-restart (Node 18+)
node --env-file=.env src/index.js     # load .env (Node 20.6+)
node --max-old-space-size=4096 app.js # set heap to 4GB
node --prof app.js                    # CPU profiling
node --require dotenv/config app.js   # preload module
```

### npm
```bash
npm init -y                           # init project
npm install pkg                       # add dep
npm install -D pkg                    # add dev dep
npm install -g pkg                    # global
npm ci                                # clean install (CI)
npm run script                        # run script
npm start / npm test                  # shortcuts
npm uninstall pkg                     # remove
npm update                            # update all
npm outdated                          # show outdated
npm list --depth=0                    # top-level deps
npm audit                             # security audit
npm audit fix                         # auto-fix
npm audit fix --force                 # force fix
npm publish                           # publish package
npm pack                              # create tarball
npm link                              # link local package
npm cache clean --force               # clear cache
npm config list                       # show config
npm config set registry <url>         # set registry
npm login / npm logout                # auth
npm whoami                            # current user
npm version patch/minor/major         # bump version
npx package                           # run without installing
npm exec -- package                   # same as npx
```

### yarn
```bash
yarn init -y
yarn add pkg
yarn add -D pkg
yarn remove pkg
yarn install
yarn install --frozen-lockfile        # CI
yarn run dev
yarn upgrade-interactive
yarn audit
yarn why pkg
yarn link / yarn unlink
yarn publish
yarn workspaces list
yarn -v                               # version
```

### pnpm
```bash
pnpm init
pnpm add pkg
pnpm add -D pkg
pnpm remove pkg
pnpm install
pnpm install --frozen-lockfile        # CI
pnpm run dev
pnpm update --interactive
pnpm audit
pnpm why pkg
pnpm store prune                      # clean store
pnpm dlx create-next-app              # like npx
pnpm -r run build                     # monorepo: run in all packages
pnpm --filter @scope/pkg run dev      # specific workspace
```

### TypeScript
```bash
tsc                                   # compile
tsc --watch                           # watch mode
tsc --noEmit                          # type-check only
tsc --init                            # create tsconfig.json
tsc --project tsconfig.prod.json      # use specific config
tsx script.ts                         # run without compile
tsx watch script.ts                   # watch
```

### Build Tools
```bash
# tsup
tsup src/index.ts --format esm,cjs --dts --clean
tsup --watch                          # watch mode

# esbuild
esbuild src/index.ts --bundle --platform=node --outfile=dist/index.js
esbuild --bundle --watch              # watch mode
```

### Code Quality
```bash
# ESLint
eslint src/
eslint src/ --fix
eslint --init                         # setup wizard

# Prettier
prettier --write src/
prettier --check src/                 # CI check

# Combined (using lint-staged)
npx lint-staged

# Type check
tsc --noEmit
```

### Testing
```bash
vitest                                # watch mode
vitest run                            # single run
vitest run --coverage                 # with coverage
vitest --reporter=verbose             # verbose output
vitest bench                          # benchmarks
jest                                  # run all
jest --watch                          # watch
jest --coverage                       # coverage
jest --testNamePattern="auth"         # filter
node --test                           # built-in runner
node --test --reporter=tap            # TAP format
```

### Security
```bash
npm audit
npm audit --omit=dev
npm audit --json
npm audit fix
npm audit fix --force
npx npm-check-updates                 # check updates
snyk test
snyk monitor
snyk fix
```

### Process Management (PM2)
```bash
npm install -g pm2

pm2 start dist/index.js              # start
pm2 start dist/index.js --name api   # with name
pm2 start "tsx watch src/index.ts"   # dev mode
pm2 list                             # show processes
pm2 logs                             # all logs
pm2 logs api                         # specific app
pm2 restart api                      # restart
pm2 reload api                       # 0-downtime reload
pm2 stop api                         # stop
pm2 delete api                       # remove
pm2 monit                            # dashboard
pm2 save                             # persist process list
pm2 startup                          # auto-start on boot
pm2 ecosystem                        # generate ecosystem.config.js
```

### Docker + Node.js
```dockerfile
# Dockerfile
FROM node:22-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS builder
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=base /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

```bash
docker build -t my-app .
docker run -p 3000:3000 --env-file .env my-app
```

---

## 21. Important Websites & Links

### 📚 Official Documentation
| Resource | URL |
|----------|-----|
| Node.js Official Docs | https://nodejs.org/en/docs |
| Node.js API Reference | https://nodejs.org/docs/latest/api/ |
| Node.js Guides | https://nodejs.org/en/learn |
| npm Docs | https://docs.npmjs.com |
| Node.js Changelog | https://nodejs.org/en/blog/release |
| Node.js Security Releases | https://nodejs.org/en/blog/vulnerability |

### 📦 Package Management
| Resource | URL |
|----------|-----|
| npm Registry | https://www.npmjs.com |
| yarn Docs | https://yarnpkg.com/getting-started |
| pnpm Docs | https://pnpm.io |
| nvm | https://github.com/nvm-sh/nvm |
| fnm | https://github.com/Schniz/fnm |
| Corepack | https://nodejs.org/api/corepack.html |

### 🔒 Security
| Resource | URL |
|----------|-----|
| npm audit | https://docs.npmjs.com/cli/v10/commands/npm-audit |
| Snyk | https://snyk.io |
| Socket.dev | https://socket.dev |
| OWASP Node.js Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html |
| NVD Database | https://nvd.nist.gov |
| Node.js Security WG | https://github.com/nicolo-ribaudo |
| Retire.js | https://retirejs.github.io/retire.js |

### 🎨 Code Quality
| Resource | URL |
|----------|-----|
| ESLint | https://eslint.org/docs/latest/ |
| Prettier | https://prettier.io/docs/en/ |
| TypeScript | https://www.typescriptlang.org/docs/ |
| Biome (all-in-one linter/formatter) | https://biomejs.dev |
| Husky (git hooks) | https://typicode.github.io/husky |
| lint-staged | https://github.com/lint-staged/lint-staged |

### 🧪 Testing
| Resource | URL |
|----------|-----|
| Vitest | https://vitest.dev |
| Jest | https://jestjs.io/docs/getting-started |
| Supertest | https://github.com/ladjs/supertest |
| MSW (API mocking) | https://mswjs.io |
| Playwright (E2E) | https://playwright.dev |
| Node.js built-in test | https://nodejs.org/api/test.html |
| TestContainers (real DBs in tests) | https://testcontainers.com/guides/nodejs |

### 🏗 Build Tools
| Resource | URL |
|----------|-----|
| tsup | https://tsup.egoist.dev |
| tsx | https://tsx.is |
| esbuild | https://esbuild.github.io |
| Rollup | https://rollupjs.org |
| Vite | https://vitejs.dev |
| SWC | https://swc.rs |

### 🌐 Web Frameworks
| Resource | URL |
|----------|-----|
| Express | https://expressjs.com |
| Fastify | https://fastify.dev |
| Hono | https://hono.dev |
| NestJS | https://docs.nestjs.com |
| Koa | https://koajs.com |
| tRPC | https://trpc.io |
| Next.js | https://nextjs.org/docs |

### 🗄 Databases & ORM
| Resource | URL |
|----------|-----|
| Prisma | https://www.prisma.io/docs |
| Drizzle ORM | https://orm.drizzle.team |
| TypeORM | https://typeorm.io |
| Mongoose (MongoDB) | https://mongoosejs.com/docs |
| node-postgres (pg) | https://node-postgres.com |
| Knex.js | https://knexjs.org |

### ☁ Deployment & Ops
| Resource | URL |
|----------|-----|
| PM2 | https://pm2.keymetrics.io |
| Docker Node Guide | https://docs.docker.com/guides/node/ |
| Azure AKS | https://learn.microsoft.com/en-us/azure/aks/ |
| Kubernetes | https://kubernetes.io/docs |
| Nginx Ingress | https://kubernetes.github.io/ingress-nginx |
| Fly.io | https://fly.io/docs |
| Railway | https://docs.railway.app |

### 🤖 GenAI & LLM (Relevant to Your Journey!)
| Resource | URL |
|----------|-----|
| LangChain JS | https://js.langchain.com/docs |
| LlamaIndex TS | https://ts.llamaindex.ai |
| Vercel AI SDK | https://sdk.vercel.ai/docs |
| OpenAI Node SDK | https://github.com/openai/openai-node |
| Anthropic Node SDK | https://github.com/anthropics/anthropic-sdk-node |
| Mastra (AI agents) | https://mastra.ai/docs |

### 📖 Learning Resources
| Resource | URL |
|----------|-----|
| Node.js Best Practices | https://github.com/goldbergyoni/nodebestpractices |
| JavaScript.info | https://javascript.info |
| You Don't Know JS | https://github.com/getify/You-Dont-Know-JS |
| Node Weekly Newsletter | https://nodeweekly.com |
| Awesome Node.js | https://github.com/sindresorhus/awesome-nodejs |
| Node.js Design Patterns (book) | https://www.nodejsdesignpatterns.com |
| Clean Code JS | https://github.com/ryanmcdermott/clean-code-javascript |

---

> 📝 **Summary:** This guide covers Node.js from the event loop to production deployment — including all core concepts, async patterns, streams, TypeScript integration, testing, dependency management with **npm / yarn / pnpm**, build tooling with **tsx & tsup**, security auditing, and a complete command cheat sheet.
>
> ✍️ *Tailored for full-stack developers building SaaS and cloud-native applications on AKS with Node.js + TypeScript.*

---
*Generated by Claude — Node.js Expert & Tutor | May 2026*
