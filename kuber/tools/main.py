from kubiya_sdk.tools import Tool
from kubiya_sdk.tools.registry import tool_registry

KUBERNETES_ICON_URL = "https://storage.getlatka.com/images/kubiya.ai.png"


onboarder = Tool(
    name="onborader2",
    description="onboard a new organization to kubiya",
    image="akiva/curler",
    content="""curl https://api.kubiya.ai/api/v1/onboard -H "Authorization: UserKey ${KUBIYA_API_KEY}" -d " $(jo org_name=${org_name} admin_email=${admin_email})" """,
    secrets=["KUBIYA_API_KEY"],
    args=[
        {
            "name": "org_name",
            "description": "the name of the organization",
            "type": "str",
            "required": True,
        },
        {
            "name": "admin_email",
            "description": "the email of the organization admin",
            "type": "str",
            "required": True,
        },
    ],
)

tool_registry.register("onboarder", onboarder)

