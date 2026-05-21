# Kave Python SDK

Install:

```bash
uv add kave-sdk
pip install kave-sdk
```

Quickstart:

```python
from kave import SyncClient
from kave.control.v1 import control_pb2

with SyncClient("localhost:19090", token="kv_...") as kave:
    org = kave.ensure_organization(control_pb2.CreateOrganizationRequest(name="Acme", slug="acme"))
    print(org.id)
```

## Auth

Pass `token="..."` to add `Authorization: Bearer ...` on every RPC. Direct proto
RPCs are reachable through `client.control`, `client.runtime`, and `client.audit`.

## TLS

Use `SyncClient(addr="api.example.com:443", tls=True)` for system-root TLS, or
pass custom `grpc.ChannelCredentials` with `credentials=...`.

## Retry

Idempotent `List*`, `Get*`, and `Watch*` RPCs retry 3 times by default: 200 ms
base, 2x exponential backoff, +/-20% jitter, 5 s cap. Mutating RPCs do not retry.
Use `retry=NO_RETRY` or pass a `RetryPolicy` to customize.

## Async

```python
from kave import AsyncClient

async with AsyncClient("localhost:19090") as kave:
    async for agent in kave.aiter_agents(env_id):
        print(agent.name)
```

## Errors

SDK calls wrap gRPC failures in `KaveError`. Use predicates such as
`is_not_found(err)`, `is_permission_denied(err)`, and `is_unavailable(err)`.

## Django

Install `kave-sdk[django]`, add `kave.contrib.django` to `INSTALLED_APPS`, define
`KAVE = {...}`, and run `python manage.py kave_reconcile` on deploy.

See `examples/` and `../CONTRACT.md` for the full parity contract.
