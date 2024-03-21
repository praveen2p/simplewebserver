
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>sample web</title>
</head>
<body bgcolor="cyan">
<table border="3" cellspacing="8" >
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
