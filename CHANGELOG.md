# Python SDK Changelog

## 0.1.0

- Renamed the PyPI distribution to `kave-sdk` with import package `kave`.
- Added `SyncClient`, `AsyncClient`, shared `ClientOptions`, and top-level exports.
- Added unified `KaveError` and error predicates.
- Added retry policy helpers, request logging, and optional OpenTelemetry propagation.
- Added high-level helpers matching `sdk/go/highlevel.go`.
- Added sync and async pagination helpers for list RPCs.
- Added `kave.contrib.django` with settings, client singleton, decorators, DRF hooks, and `kave_reconcile`.
