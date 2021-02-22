import json
import sys

base_tmpl = """<?xml version="1.0"?>
<XRDS xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">
    {}
</XRDS>"""

row_tmpl = """  <XRD>
    <Link rel="urn:oasis:names:tc:SAML:2.0:metadata" href="{}"/>
  </XRD>"""


if __name__ == '__main__':
    result = []
    with open(sys.argv[1]) as raw_json:
        json_cont = json.loads(raw_json.read())
        for i in json_cont['data']:
            result.append(row_tmpl.format(i['registry_url']))
    
    print(base_tmpl.format('\n'.join(result)))      
  
