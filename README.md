pyFF SPID PoC
-------------

pyFF is a simple but reasonably complete SAML metadata processor. It is intended to be used by anyone who needs to aggregate, validate, combine, transform, sign or publish SAML metadata.

pyFF is used to run infrastructure for several identity federations of signifficant size including edugain.org.

pyFF supports producing and validating digital signatures on SAML metadata using the pyXMLSecurity package which in turn supports PKCS#11 and other mechanisms for talking to HSMs and other cryptographic hardware.

pyFF is also a complete implementation of the SAML metadata query protocol as described in draft-young-md-query and draft-young-md-query-saml and implements extensions to MDQ for searching which means pyFF can be used as the backend for a discovery service for large-scale identity federations.

Possible usecases include running an federation aggregator, filtering metadata for use by a discovery service, generating reports from metadata (eg certificate expiration reports), transforming metadata to add custom elements.

Setup
-----

#### Environment and dependencies
````
virtualenv -ppython3 env
source env/bin/activate
pip install git+https://github.com/IdentityPython/pyFF.git
````

#### Certificates
````
openssl req -nodes -new -x509 -newkey rsa:2048 -days 3650 -keyout certificates/key.pem -out certificates/cert.pem
````

#### Usage

Start pyff as a scheduled batch, metadata will be available in the folder `md-idp/`.
A single, signed, metadata will be available in the same folder with name `md-idp/md-loaded.xml` as specified in `pipelines/spid_idp.fd`
````
pyff  pipelines/spid_idp.fd
````

The same as the previous but as a web service, browsable at _https://localhost:8089_:
````
pyffd -p pyff.pid -f -a --loglevel=DEBUG --dir=`pwd` --frequency=1800 -H 0.0.0.0 -P 8089 --no-caching pipelines/spid_idp.fd
````

References
----------

- https://pyff.readthedocs.io/


Authors
-------

- Giuseppe De Marco
- Michele D'Amico

