from kubiya_sdk.tools import Arg, Tool, FileSpec

from kubiya_sdk.tools.registry import tool_registry
import sys

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


class GoTool(Tool):
    def __init__(self, name, description, content, args, image="goland:latest"):

        super().__init__(
            name=name,
            description=description,
            icon_url=KUBERNETES_ICON_URL,
            type="docker",
            image=image,
            content="""go version""",
            args=args,
            with_files=list(),
        )


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