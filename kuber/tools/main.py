import inspect

from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools.registry import tool_registry

go_tool = Tool(
    name="go_version",
    type="docker",
    image="golang:1.22",
    description="gets the go version",
    content="""go version""",
)

tool_registry.register(go_tool)