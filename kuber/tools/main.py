from kubiya_sdk.tools import Arg, Tool

from kubiya_sdk.tools.registry import tool_registry
import sys

KUBERNETES_ICON_URL = "https://kubernetes.io/icons/icon-128x128.png"


gover = Tool(
    name="gover",
    description="checks go version.",
    image="golang:1.23.8-alpine3.20",
    content="""go version""",
    args=[
        {
            "name": "arg",
            "description": "arg",
            "type": "str",
            "required": False,
        },
    ]
)

enver = Tool(
    name="enver",
    description="gets the env vars",
    image="alpine:latest",
    content="env",
    args=[]
)

arger = Tool(
    name="arger",
    description="show the passed args",
    image="alpine:latest",
    content="""echo fruit is: $FRUIT, vegtable is $VEGTABLE""",
    args=[
        {
            "name": "fruit",
            "description": "the fruit you like most",
            "type": "str",
            "required": True,
        },
        {
            "name": "vegtable",
            "description": "your favoured vegtable",
            "type": "str",
            "required": False,
        },
    ]
)

try:
    tool_registry.register("gover", gover)
    tool_registry.register("enver", enver)
    tool_registry.register("arger", arger)
except Exception as e:
    print(f"❌ Failed to register gover tool: {str(e)}", file=sys.stderr)
    raise
