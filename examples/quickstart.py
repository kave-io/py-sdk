import asyncio

from kave import KaveClient
from kave.control.v1 import control_pb2  # type: ignore[import]
from kave.runtime.v1 import runtime_pb2  # type: ignore[import]


async def main() -> None:
    async with KaveClient("localhost:8080", token="your-kave-token") as kave:
        org = await kave.control.CreateOrganization(
            control_pb2.CreateOrganizationRequest(name="acme", slug="acme")
        )
        print("org:", org.id)

        proj = await kave.control.CreateProject(
            control_pb2.CreateProjectRequest(
                org_id=org.id, name="my-agent", slug="my-agent"
            )
        )
        print("project:", proj.id)

        runs = await kave.runtime.ListRuns(runtime_pb2.ListRunsRequest(limit=10))
        print(f"{len(runs.runs)} runs")


if __name__ == "__main__":
    asyncio.run(main())
