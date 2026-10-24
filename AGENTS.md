# NDS estate example contract

This public AGPL-3.0-only component contains synthetic configuration and exact
public source Gitlinks. Follow `standarts.lock` and the NDS system root.
Actual hosts, owners, endpoints, private policy, credentials and runtime evidence
belong in the private estate. Never copy private estate files into this example.

The selected server owns its Compose implementation. Do not edit its submodule
to implement an example change. Update the Gitlink only to reviewed public
source, then run `just check` and `nddev check` with the adopted STD-0001 edition.
Generated `.nds` and agent adapters are owned by `nddev gen`.

Use task -> dev -> main with signed commits. Public workflows use GitHub-hosted
runners with read-only permissions and no estate secrets. Configuration rendering
must not start services, modify volumes, clean user caches or imply deployment.
