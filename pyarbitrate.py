#Bitcoin Arbitrage by Steven Richards <sbrichards@mit.edu>
import pycurl
import StringIO
print '\nPolling for data from www.nyse-group.de\n'
c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.nyse-group.de/_external_rm/index_btc.php")
c.setopt(pycurl.HTTPHEADER, ["Accept:"])
result = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, result.write)
c.perform()
result = result.getvalue()
down = 'Data provider is currently not providing data. Please try again later.'
if result == down:
	print down + '\n'
else:
	buy = '<b>Buy</b> 1 BTC at'
	buystring = result[result.find(buy):result.find(buy) + len(buy) + 46]
	sell ='<b>Sell</b> 1 BTC at'
	sellstring = result[result.find(sell):result.find(sell) + len(sell) + 46]
	lastcall = 'Last call:'
	lcstring = result[result.find(lastcall):result.find(lastcall) + len(lastcall) + 24]
	for line in buystring:
		buystring = buystring.replace('<b>', '')
		buystring = buystring.replace('</b>', '')
		buystring = buystring.replace('<br>', '')
	for line in sellstring:
		sellstring = sellstring.replace('<b>', '')
        	sellstring = sellstring.replace('</b>', '')
        	sellstring = sellstring.replace('<br>', '')
	for line in lcstring:
		lcstring = lcstring.replace('Last call', '')
	print 'Top Opportunities as of' + lcstring + '\n' 	
	print buystring
	print sellstring	
	
