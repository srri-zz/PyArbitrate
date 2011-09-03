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
print result
