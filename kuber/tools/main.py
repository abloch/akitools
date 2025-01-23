from kubiya_sdk.tools import Arg, Tool

from kubiya_sdk.tools.registry import tool_registry
import sys

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


gover = Tool(
    name="gover",
    description="checks go version.",
    image="564407622114.dkr.ecr.eu-west-1.amazonaws.com/kubiya-base:golang-1.21",
    content="""go version""",
)

try:
    tool_registry.register("gover", gover)
except Exception as e:
    print(f"❌ Failed to register gover tool: {str(e)}", file=sys.stderr)
    raise