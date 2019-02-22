# JWT Auth Microservice

A nio project that creates a JWT-based Authentication Microservice backed by a MongoDB.

## Features

- **Sign up**: users can sign up with a username and password.
- **Log in**: log in with username and password and receive a JWT token with a configurable expiration date.
- **Refresh Token**: users can submit a valid token and receive a new token with an expiration date set in the future.
- **Validate Token**: users can submit a token and find whether it is valid, both in terms of being able to decrypt it, as well as (optionally) if it is expired based on the `exp` claim.

## Install using the nio CLI

  ```
  nio new jwt-auth-microservice --pubkeeper-hostname <your-system-id>.pubkeeper.nio.works --pubkeeper-token <your-pk-token> --template https://github.com/deliciousmonster/jwt-api && cd jwt-auth-microservice && pip3 install -r requirements.txt && niod
  ```

## File Reference

**blocks**<br>A directory that contains block types, as submodules. The project template comes with a few of the most commonly used block types. Block types can be added and removed. Additional block types can be found in the block library and added through the System Designer, or, you can add your own custom block types here.

**etc**
<br>A folder containing project configurations and scripts.

**service_tests**<br>A submodule for service tests that includes `NioServiceTestCase` and other tools for service testing.

**tests**<br>A folder for your tests with an example set up for a service test.

**Dockerfile**<br>An optional script to create a Docker image of the project. Docker can be used as a tool in deployments.

**docker-compose.yml**<br>A file optionally used in conjunction with Docker to configure your application so that all its dependencies can be started with a single command.

**nio.conf**
A simple project configuration file that has reasonable defaults set for you.

**nio.conf.example**
A file that contains the reference for all nio project configuration options. Default values are shown. If this file contains secrets, you will want to add it to the `.gitignore` file.

**pk_server.conf**
A project configuration file that can be included to run your binary with a standlone pubkeeper server. This is a partial config file so it should be included with another more complete configuration file. Example:
```
niod -s nio.conf -s pk_server.conf
```
