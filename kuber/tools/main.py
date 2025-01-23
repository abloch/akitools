from kubiya_sdk.tools import Arg
from .base import GoTool
from kubiya_sdk.tools.registry import tool_registry
import sys

gover = GoTool(
    name="gover",
    description="checks go version.",
    content="""go version""",
    args=[
        Arg(
            name="stam",
            type="str",
            description="dummy",
            required=False
        ),
    ],
)

try:
    tool_registry.register("gover", gover)
except Exception as e:
    print(f"❌ Failed to register gover tool: {str(e)}", file=sys.stderr)
    raise