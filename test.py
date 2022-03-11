import subprocess
from pprint import pprint


try:
    cmd_line = "ping SKA-TESTING"
    p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE)

    # response = ''
    # for line_data in p.stdout:
    response = [line_data.decode("cp866", "ignore").rstrip() for line_data in p.stdout]
    pprint(response)
    # p.wait()
    # print(p.returncode)  # =1 если  сайт не существует.   0 - если все в порядке.

except subprocess.CalledProcessError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
