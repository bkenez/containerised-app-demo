## Documentation: GitHub SSH Key Conversion Web Application

This is a small, relatively useless web application that demonstrates a few basic concepts in order to showcase parts of my skillset. It communicates with GitHub over HTTP. The application's main goal is to convert the SSH public keys of a specified user on GitHub into another machine-readable format, specifically JSON.

We are using the https://github.com/bkenez.keys as our source

### Application

The web application consists of a single endpoint located at `/github_keys/<username>`. This endpoint is designed to retrieve the SSH keys for the specified GitHub user `<username>` and return a list of keys in the form of a JSON object.

#### Input

The application accepts `GET` requests to the `/github_keys/<username>` endpoint.

#### Output

The response from the endpoint is a JSON structure representing a list of SSH keys for the specified GitHub user. Each key in the list includes two fields: `key_type` and `key_value`.

Here is an example of the expected response format:
```json
[
  {
    "type": "<key_type>",
    "key": "<key_value>"
  }
]
```

#### Example

Suppose we make a `GET` request to the endpoint `/github_keys/USERNAME`. The response would be as follows:
```json
[
  {
    "type": "ssh-rsa",
    "key": "long string representing a public key"
  },
  {
    "type": "ssh-rsa",
    "key": "long string representing a public key"
  }
]
```

### Build

To build an image for the web application, a Dockerfile is provided. The Dockerfile contains the necessary instructions to create the image.

### Delivery Pipeline

A GitHub Actions pipeline has been created to automate the build and push process of the application image to the GitHub Actions registry. The suggested pipeline consists of the following stages: `test/lint`, `build image`, and `push image`. However, alternative pipeline configurations can be used as long as the ultimate goal of having the image in the registry is achieved.

### HTTP Response Code for Nonexistent User

If a requested user does not exist, the appropriate HTTP response code to be returned is `404 Not Found`.
