import subprocess, platform


def pingOk(host):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', host), shell=True)
        print(output)
    except Exception:
        return False
    return True

print(pingOk('SKA-TESTING'))