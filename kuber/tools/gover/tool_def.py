import inspect

from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools.registry import tool_registry

import main

go_tool = Tool(
    name="go version",
    type="docker",
    image="564407622114.dkr.ecr.eu-west-1.amazonaws.com/kubiya-base:golang-1.22",
    description="gets go version",
    content="""
python /tmp/main.py
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
        # FileSpec(
        #     destination="/tmp/requirements.txt",
        #     content=open("requirements.txt").read(),
        # ),
    ],
)

tool_registry.register(go_tool)
