from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

KUBERNETES_ICON_URL = "https://storage.getlatka.com/images/kubiya.ai.png"


onboarder = Tool(
    name="onborader",
    description="onboard a new organization to kubiya",
    image="curlimages/curl",
    content="""curl https://api.kubiya.ai/api/v1/org -H "Authorization UserKey ${KUBIYA_API_KEY}" """,
)

tool_registry.register("onboarder", onboarder)