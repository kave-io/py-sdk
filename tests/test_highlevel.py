from kave.control.v1 import agent_pb2, control_pb2
from kave.highlevel import SyncHighLevelMixin


class Control:
    def __init__(self):
        self.created = []

    def ListAgents(self, req):
        return control_pb2.ListAgentsResponse(agents=[agent_pb2.Agent(id="a1", env_id=req.env_id, name="existing")])

    def CreateAgent(self, req):
        self.created.append(req)
        return agent_pb2.Agent(id="a2", env_id=req.env_id, name=req.name)


class Client(SyncHighLevelMixin):
    def __init__(self):
        self.control = Control()


def test_ensure_agent_returns_existing_by_name():
    client = Client()
    agent = client.ensure_agent(control_pb2.CreateAgentRequest(env_id="env_1", name="existing"))
    assert agent.id == "a1"
    assert client.control.created == []


def test_ensure_agent_creates_when_absent():
    client = Client()
    agent = client.ensure_agent(control_pb2.CreateAgentRequest(env_id="env_1", name="new"))
    assert agent.id == "a2"
    assert len(client.control.created) == 1
