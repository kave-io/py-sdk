from kave import SyncClient
from kave.runtime.v1 import action_pb2, run_pb2, runtime_pb2, span_pb2

project_id = "project_..."
env_id = "env_..."
agent_id = "agent_..."

with SyncClient("localhost:19090") as kave:
    run = kave.create_run(
        runtime_pb2.CreateRunRequest(
            project_id=project_id,
            env_id=env_id,
            agent_id=agent_id,
            name="example",
            trigger_type=run_pb2.TRIGGER_TYPE_MANUAL,
        )
    )
    action = kave.create_action(
        runtime_pb2.CreateActionRequest(
            run_id=run.id,
            project_id=project_id,
            env_id=env_id,
            agent_id=agent_id,
            action_type=action_pb2.ACTION_TYPE_LLM,
            connector="openai",
            method="chat.completions.create",
        )
    )
    with kave.with_span(
        runtime_pb2.OpenSpanRequest(
            span=span_pb2.SpanInput(
                project_id=project_id,
                env_id=env_id,
                agent_id=agent_id,
                run_id=run.id,
                action_id=action.id,
                name="llm.call",
            )
        )
    ):
        pass
