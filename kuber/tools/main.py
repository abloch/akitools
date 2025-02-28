from kubiya_sdk.tools import Arg, Tool

from kubiya_sdk.tools.registry import tool_registry
import sys

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


gover = Tool(
    name="gover",
    description="checks go version4.",
    image="golang:latest4",
    content="""go version4""",
    args=[
        {
            "name": "arg4",
            "description": "arg4",
            "type": "str",
            "required": True,
        },
    ]
)

try:
    tool_registry.register("gover", gover)
except Exception as e:
    print(f"❌ Failed to register gover tool: {str(e)}", file=sys.stderr)
    raise
