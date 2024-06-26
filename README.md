# EX01 Developing a Simple Webserver
## Date:12.02.2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>sample web</title>
</head>
<body bgcolor="cyan">
<table border="3" cellspacing="40" >
<caption>TOP SIX REVENUE GENERATING</caption>
<caption>SOFTWARE COMPANIES</caption>
<tr>
<th>FY</th>
<th>HEADGUARTERS</th>
<th>MARKET CRAP</th>

</tr>
<tr>
<td>Microsoft</td>
<td>$86.6</td>
<td>2014</td>
<td>USA</td>  
<td>$370.3</td>     
</tr>
<tr>
<td>Oracie</td>
<td>$37.1</td>
<td>2013</td>
<td>Redwood city</td>
<td>$79.4</td> 
</tr>
<tr>
<td>SAP</td>
<td>$20.9</td>
<td>2013</td>
<td>Waldort</td>
<td>$35.5</td> 
</tr>
<tr>
<td>Vmware</td>
<td>$5.2</td>
<td>2013</td>
<td>USA</td>
<td>$41.03</td> 
</tr>
<tr>
<td>CA technologies</td>
<td>$4.7</td>
<td>2013</td>
<td>USA</td>
<td>$11.6</td> 
</tr>
<tr>
<td>INTUT</td>
<td>$4.5</td>
<td>2013</td>
<td>Mountain view</td>
<td>$5.1</td> 
</tr>
</table>
</body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```
## OUTPUT:

![alt text](<WhatsApp Image 2024-03-21 at 23.15.14_101acbdc.jpg>)
![alt text](<WhatsApp Image 2024-03-21 at 23.15.33_bdd3208f.jpg>)

## RESULT:
The program for implementing simple webserver is executed successfully.