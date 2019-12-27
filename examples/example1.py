#!/usr/bin/env python3
from openpgp_requests import OpenPGPApiRequest

# Fingerprint for the local key we want to use:
fpr = 'AFINGERPRINTHERE'

# Location of the keyring where that key is stored:
homedir = '/path/to/keyring/folder/containing/that/fpr'

# The real URL is constructed from the server, port and ssl parameters.
# Parameters for API base:
server = 'www.example.net'
ssl = True
port = 5080

# Endpoint off that base we will be calling:
endpoint = 'api_endpoint'

# Construct the client
client = OpenPGPApiRequest(homedir=homedir,
                           my_fingerprint=fpr,
                           server=server,
                           port=port,
                           ssl=ssl,
                           passphrase='the_passphrase')

# Testing a GET method encapsulated in OpenPGP
z = client.get(endpoint=endpoint,
               headers={'X-extra-header': 'wow'})
print(z.body)

# Same, but using POST
z = client.post(endpoint=endpoint,
                headers={'X-header': 'X-value-post'},
                data={'data': 'dataaaaa in post payload'})
print(z.body)

# That's it
