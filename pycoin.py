#Bitcoin Arbitrage by Steven Richards <sbrichards@mit.edu>
import pycurl
import StringIO
c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.nyse-group.de/_external_rm/index_btc.php")
c.setopt(pycurl.HTTPHEADER, ["Accept:"])
result = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, result.write)
c.perform()
result = result.getvalue()
b = '<b>Buy</b> 1 BTC at'
s = result[result.find(b):result.find(b) + len(b) + 46]
for line in s:
	s = s.replace('<b>', '')
	s = s.replace('</b>', '')
	s = s.replace('<br>', '')
print s	
	
	
