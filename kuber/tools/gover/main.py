import argparse
from sh import go

def get_go_version():
    print(go.version())


if __name__ == "__main__":
    get_go_version()
