from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

KUBERNETES_ICON_URL = "https://storage.getlatka.com/images/kubiya.ai.png"


onboarder = Tool(
    name="onborader",
    description="onboard a new organization to kubiya",
    image="curlimages/curl",
    content="""bash -c 'curl https://api.kubiya.ai/api/v1/org -H "Authorization UserKey ${KUBIYA_API_KEY}"' """,
    secrets=["KUBIYA_API_KEY"],
)

tool_registry.register("onboarder", onboarder)

enver = Tool(
    name="enver",
    description="gets all the tools env-vars",
    image="alpine",
    content="""env""",
    secrets=["KUBIYA_API_KEY"],
)

tool_registry.register("enver", enver)