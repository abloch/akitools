from kubiya_sdk.tools import Arg, Tool

from kubiya_sdk.tools.registry import tool_registry
import sys

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


gover = Tool(
    name="gover",
    description="checks go version5.",
    image="golang:1.23.8-alpine3.20",
    content="""go version""",
    args=[
        {
            "name": "arg5",
            "description": "arg5",
            "type": "str",
            "required": False,
        },
    ]
)

try:
    tool_registry.register("gover", gover)
except Exception as e:
    print(f"❌ Failed to register gover tool: {str(e)}", file=sys.stderr)
    raise
