#Bitcoin Arbitrage by Steven Richards <sbrichards@mit.edu>
import pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.nyse-group.de/_external_rm/index_btc.php")
c.setopt(pycurl.HTTPHEADER, ["Accept:"])
c.perform()

