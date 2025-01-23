from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


gover = Tool(
    name="gover-private",
    description="checks go version private repo.",
    image="564407622114.dkr.ecr.eu-west-1.amazonaws.com/kubiya-base:golang-1.21",
    content="""go version""",
)

tool_registry.register("gover", gover)
