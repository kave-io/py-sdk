from kave.control.v1 import agent_pb2, control_pb2
from kave.iterators import SyncIteratorMixin


class Control:
    def __init__(self):
        self.cursors = []

    def ListAgents(self, req):
        self.cursors.append(req.cursor)
        if req.cursor == "":
            return control_pb2.ListAgentsResponse(
                agents=[agent_pb2.Agent(id="a1", name="one")],
                next_cursor="n2",
            )
        return control_pb2.ListAgentsResponse(
            agents=[agent_pb2.Agent(id="a2", name="two")],
            next_cursor="",
        )


class Client(SyncIteratorMixin):
    def __init__(self):
        self.control = Control()


def test_iter_agents_pages_until_exhausted():
    client = Client()
    assert [a.id for a in client.iter_agents("env_1")] == ["a1", "a2"]
    assert client.control.cursors == ["", "n2"]
