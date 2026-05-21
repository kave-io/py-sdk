import grpc

from kave.errors import Code, KaveError, is_not_found, is_unavailable, wrap_error


class FakeRpcError(grpc.RpcError):
    def __init__(self, code, details="boom"):
        self._code = code
        self._details = details

    def code(self):
        return self._code

    def details(self):
        return self._details


def test_wraps_grpc_error_to_kave_error():
    err = wrap_error(FakeRpcError(grpc.StatusCode.NOT_FOUND, "missing"))
    assert isinstance(err, KaveError)
    assert err.code == Code.NOT_FOUND
    assert str(err) == "missing"
    assert is_not_found(err)


def test_predicates_accept_raw_rpc_error():
    assert is_unavailable(FakeRpcError(grpc.StatusCode.UNAVAILABLE))
