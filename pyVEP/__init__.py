
import urllib
import logging
import requests

__version__ == '0.0.1'

'''
Example curl command:
curl 'http://rest.ensembl.org/vep/Homo_sapiens/hgvs/9%3Ag.22125504G%3EC' \
-H 'Host: rest.ensembl.org' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:42.0) Gecko/20100101 Firefox/42.0' \
-H 'Accept: application/json, text/javascript, */*; q=0.01' \
-H 'Accept-Language: en-US,en;q=0.5' \
--compressed \
-H 'Referer: http://asia.ensembl.org/Tools/VEP?redirect=no' \
-H 'Origin: http://asia.ensembl.org' \
-H 'Connection: keep-alive'
'''

'''
TODO:
* Randomize headers 
    Similar to this: https://github.com/galkan/tools/blob/master/others/programming/python/random-http-headers-urllib.py 
'''

def VEP(variant):
	
	url_pattern = 'http://rest.ensembl.org/vep/Homo_sapiens/hgvs/{variant}'

	headers = {
		'Host': 'rest.ensembl.org',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:42.0) Gecko/20100101 Firefox/42.0',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Referer': 'http://asia.ensembl.org/Tools/VEP?redirect=no',
		'Origin': 'http://asia.ensembl.org',
		'Connection': 'keep-alive',
	}

	variant_quoted = urllib.quote(variant)
	url = url_pattern.format(variant=variant_quoted)

	logging.debug('URL: %s' % (url))
	r = requests.get(url, headers=headers)
	json_text = r.json()

	return json_text

def test():
	import json
	
	logging.basicConfig(level=logging.DEBUG)

	def try_variant(variant):
		logging.info('Trying variant: %s' % (variant))
		r = VEP(variant)
		logging.info('Result: %s' % json.dumps(r, indent=4))

	try_variant('9:g.22125504G>C')

