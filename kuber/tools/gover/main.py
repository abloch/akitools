import subprocess

def get_go_version():
    ret = subprocess.check_output(["go", "version"])
    print(ret.decode("utf-8"))


if __name__ == "__main__":
    get_go_version()
