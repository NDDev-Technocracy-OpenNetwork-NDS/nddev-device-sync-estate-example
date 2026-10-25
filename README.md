# NDS estate example

Public, synthetic self-hosting example for NDDev Device Sync. The private
estate owns actual devices, addresses, secrets and deployment evidence.

Part of [NDDev OpenNetwork](https://nddev.ai).

The exact `modules/server` Gitlink selects the public server implementation,
its PostgreSQL image, migrations and Compose contract. This example supplies
only synthetic environment values. It does not duplicate the server's Compose
implementation or include company infrastructure.

## Inspect the example

Clone with `--recurse-submodules`, prepare Python 3.15 with uv and run:

```sh
uv sync --locked
just check
just render
```

`check` validates this repository's source selection and renders the real
upstream Compose contract without starting containers. Docker Compose is required.
`render` prints that same synthetic configuration. Neither command reads a real
estate, contacts a server, starts maintenance or creates credentials.

## Self-host NDS

Use the [selected server's self-hosting guide](https://github.com/NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync-server/blob/1b58725731088ad13b4a87d0bbb3cd61af49f76a/docs/self-hosting.md)
to prepare separate migration/runtime database credentials, TLS and optional
identity configuration outside Git. Copy `config/example.env` into your private
estate, replace its `.invalid` hostname and operator-owned directory references,
and bind the selected server Gitlink to the deployment's source/image receipt.
The example binds HTTPS to loopback. Publishing it requires an explicit private
deployment configuration and valid TLS for the chosen origin.

The server owns startup, readiness, migrations, identity and data retention.
Existing PostgreSQL data must be preserved during updates; changing a source pin
does not authorize replacing volumes or rotating keys. Client Git synchronization
is performed by authorized native clients, rather than by this server example.

Public CI uses GitHub-hosted Linux and only these synthetic inputs. Private
estate validation belongs on the organization's self-hosted runners. A passing
configuration check is not live deployment or authenticated client acceptance.
The adopted corporate structure validator is prepared separately for authorized
maintainers (`nddev check --root .`); public CI does not fetch that private tool
or require a credential to validate the example.

[GitHub Releases](https://github.com/NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync-estate-example/releases)
is the release journal. This source example does not publish a server release.
