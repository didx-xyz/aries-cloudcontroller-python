<p align="center">
  <br />
  <img
    alt="Hyperledger Aries logo"
    src="https://raw.githubusercontent.com/didx-xyz/aries-cloudcontroller-python/main/assets/aries-logo.png"
    height="250px"
  />
</p>
<h1 align="center"><b>Aries CloudController Python</b></h1>
<p align="center">
  <a href="https://pypi.org/project/aries-cloudcontroller/">
    <img alt="aries-cloudcontroller version" src="https://badge.fury.io/py/aries-cloudcontroller.svg"/>
  </a>
  <a
    href="https://raw.githubusercontent.com/didx-xyz/aries-cloudcontroller-python/main/LICENSE"
    ><img
      alt="License"
      src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"
  /></a>
  <a href="https://www.python.org/"
    ><img
      alt="Python"
      src="https://img.shields.io/badge/%3C%2F%3E-Python-%230074c1.svg"
  /></a>
</p>
<br />

<p align="center">
  <a href="#features">Features</a> &nbsp;|&nbsp;
  <a href="#usage">Usage</a> &nbsp;|&nbsp;
  <a href="#available-apis">Available APIs</a> &nbsp;|&nbsp;
  <a href="#contributing">Contributing</a> &nbsp;|&nbsp;
  <a href="#license">License</a>
</p>

The Aries CloudController is a Python-based client library for interacting with an instance of
[Aries Cloud Agent](https://github.com/hyperledger/aries-cloudagent-python) (ACA-Py). It leverages
the OpenAPI definition from ACA-Py to provide a fully-typed, rich API experience for cloud agent interaction.

**Versioning Update:**
As of version 0.8.0, the Aries CloudController has aligned its versioning with ACA-Py.
This means that each new version of ACA-Py will correspond directly to the same version of the
Aries CloudController. This change ensures a more straightforward and predictable upgrade path for users.

In other words, CloudController 0.8.0 is compatible with ACA-Py 0.8.0,
CloudController 0.9.0 is compatible with ACA-Py 0.9.0, etc.

For legacy versions, please review our release history to found the version compatible with ACA-Py pre-0.8.0.

## Features

Aries CloudController Python provides a robust client for interacting with Aries Cloud Agents (ACA-Py).

- **Fully Typed**: Offers a strongly-typed wrapper around the Aries Cloud Agent Python,
  enhancing developer experience and reducing errors.
- **Up-to-Date Support**: Compatible with the latest ACA-Py version (1.1.0),
  ensuring access to the most recent features and improvements.
- **Auto-Generated Client**: Utilizes OpenAPI definitions for automatic generation,
  ensuring timely updates in line with new ACA-Py releases.
- **Multi-Tenancy and Authentication Support**: Facilitates working with multi-tenant APIs
  and integrates various authentication mechanisms.
- **Asynchronous API**: Supports asynchronous operations, enabling efficient handling of I/O-bound tasks.

## Usage

Install Aries Cloud Controller Python via pip:

```sh
pip install aries-cloudcontroller
```

### Creating a Client

Easily initialize the AcaPyClient:

```python
from aries_cloudcontroller import AcaPyClient

client = AcaPyClient(
    base_url="http://localhost:8000",
    api_key="myApiKey"
)
```

**Admin Insecure Mode**: If running ACA-Py with the `--admin-insecure-mode` flag and without an API key:

```python
client = AcaPyClient(
    base_url="http://localhost:8000",
    admin_insecure=True  # No API key needed
)
```

**Multitenancy**: For specific tenant contexts:

```python
client = AcaPyClient(
    base_url="http://localhost:8000",
    tenant_jwt="eyXXX"
)
```

### Interacting with the Client

The API, being fully typed, is best explored through the ACA-Py Swagger UI,
which mirrors the available client properties.

**Example**: Creating and receiving an invitation:

```python
invitation = await client.connection.create_invitation(
    body=CreateInvitationRequest(my_label="Cloud Controller")
)

connection = await client.connection.receive_invitation(body=invitation.invitation)
```

## Available APIs

The client encompasses various APIs, each corresponding to ACA-Py Swagger UI topics:

- `action_menu`
- `anoncreds_credential_definitions`
- `anoncreds_revocation`
- `anoncreds_schemas`
- `anoncreds_wallet_upgrade`
- `basicmessage`
- `connection`
- `credential_definition`
- `credentials`
- `default`
- `did_exchange`
- `did_rotate`
- `discover_features`
- `discover_features_v2_0`
- `endorse_transaction`
- `introduction`
- `issue_credential_v1_0`
- `issue_credential_v2_0`
- `jsonld`
- `ledger`
- `mediation`
- `multitenancy`
- `out_of_band`
- `present_proof_v1_0`
- `present_proof_v2_0`
- `resolver`
- `revocation`
- `schema`
- `server`
- `settings`
- `trustping`
- `vc`
- `wallet`

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING](/CONTRIBUTING.md) guidelines
for more information on how to get involved.

## License

This project is licensed under the [Apache License Version 2.0 (Apache-2.0)](/LICENSE).
