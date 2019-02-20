Create
======
The Refresh block accepts a valid JWT token and returns a new token with an updated `exp` timestamp.

Properties
----------
- **Secret**: The secret used to encrypt the token.
  - default `[[JWT_SECRET]]` (environment variable)
- **Algorithm**: The type of encryption used to create the token.
  - default `HS256` (environment variable)
- **New Expiration Date**: A unix timestamp to update in the token payload.
  - default: `{{ datetime.datetime.now() + datetime.timedelta(minutes=60) }}`
- **Output Attribute**: The attribute that will hold the token value
  - default: `token`
- **Exclude Existing?**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.

Outputs
-------
One outgoing signal containing the updated token.

Commands
--------
None
