#!/usr/bin/env python3
from openpgp_requests import OpenPGPApiRequest

base_url = 'https://example.net/api'
fpr = 'AFINGERPRINTHERE'
homedir = '/path/to/keyring/folder/containing/that/fpr'
client = OpenPGPApiRequest(homedir=homedir,
                           my_fingerprint=fpr,
                           passphrase='the_passphrase')

# Testing a GET method encapsulated in OpenPGP
z = client.get(url=base_url,
               headers={'X-extra-header': 'wow'})
print(z.body)

# Same, but using POST
z = client.post(url=base_url,
                headers={'X-header': 'X-value-post'},
                data={'data': 'dataaaaa in post payload'})
print(z.body)

# That's it
