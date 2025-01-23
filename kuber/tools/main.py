import inspect

from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools.registry import tool_registry

gotool = Tool(
    name="goversion",
    type="docker",
    image="golang:1.22",
    description="gets the go version",
    content="""go version""",
    args=[
         Arg(name="stam", type="str", description="just a dumb arg", required=False),
    ],
)

tool_registry.register(gotool)