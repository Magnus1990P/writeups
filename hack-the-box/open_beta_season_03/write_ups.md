# Codify

Easy, linux

10.10.11.239

nmap
```
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache/2.4.52 (Ubuntu)
443/tcp   open  https?
12345/tcp open  http    Node.js (Express middleware)
```

## Ports
### 80
Server: Apache/2.4.52 (Ubuntu)
Location: http://codify.htb/

Interface giving you the ability to load certain Node.JS libraries and run arbitrary code.
Solution is probably to run a script discovering, and reading the flag file from the OS using the node.js libraries

### 443
### 12345
http, Node.js
HTTP svarer med not found