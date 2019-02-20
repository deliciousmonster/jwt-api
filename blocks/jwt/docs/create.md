Create
======
The Create block will generate a JWT token encrypted with the selected algorithm.

Properties
----------
- **Secret**: The secret used to encrypt the token.
  - default `[[JWT_SECRET]]` (environment variable)
- **Algorithm**: The type of encryption used to create the token.
  - default `HS256`
- **Claims**: A list of JWT claim [key/pair values](https://www.iana.org/assignments/jwt/jwt.xhtml). Examples:
    - exp: `{{ int((datetime.datetime.now() + datetime.timedelta(minutes=60)).timestamp()) }}`
    - name: str
    - profile: object
- **Output Attribute**: The attribute that will hold the token value (default: `token`)
- **Exclude Existing?**: If checked (true), the attributes of the incoming signal will be excluded from the outgoing signal. If unchecked (false), the attributes of the incoming signal will be included in the outgoing signal.

Outputs
-------
One outgoing signal containing the new token.

Commands
--------
None

