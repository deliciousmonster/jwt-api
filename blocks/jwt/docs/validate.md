Validate
========
The Validate block evaluates a JWT token and determines whether it is valid, both in terms of being able to decrypt it, as well as if it is expired based on the `exp` claim.

Properties
----------
- **Secret**: The secret used to encrypt the token.
  - default `[[JWT_SECRET]]` (environment variable)
- **Algorithm**: The type of encryption used to create the token.
  - default `HS256` (environment variable)
- **Input Attribute**: The attribute that holds the token value (default: `token`)
- **Exclude Existing?**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.

Outputs
-------
- **Valid**: Token is valid
- **Not Valid**: Token is not valid

Commands
--------
None
