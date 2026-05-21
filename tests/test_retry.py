import grpc

from kave.errors import wrap_error
from kave.retry import RetryPolicy, backoff_ms, retry_sync, should_retry_rpc


class FakeRpcError(grpc.RpcError):
    def code(self):
        return grpc.StatusCode.UNAVAILABLE


def test_retries_retriable_errors(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda _: None)
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        if calls["n"] < 3:
            raise wrap_error(FakeRpcError())
        return "ok"

    assert retry_sync(RetryPolicy(max_attempts=3, base_ms=1), fn) == "ok"
    assert calls["n"] == 3


def test_mutating_rpcs_are_not_marked_for_retry():
    assert should_retry_rpc("ListAgents")
    assert should_retry_rpc("/kave.control.v1.ControlPlaneService/GetAgent")
    assert not should_retry_rpc("CreateAgent")


def test_backoff_is_capped(monkeypatch):
    monkeypatch.setattr("random.random", lambda: 0.5)
    assert backoff_ms(RetryPolicy(max_attempts=3, base_ms=200, cap_ms=300), 5) == 300
