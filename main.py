import subprocess
from pprint import pprint


if __name__ == '__main__':
    split_string = "\\r\\n"
    b_comp_list = subprocess.check_output(['dsquery', 'computer', 'domainroot', '-scope', 'subtree', '-limit', '0'])
    comp_list = str(b_comp_list)[2:-5].split(split_string)
    comp_list = sorted(list(comp[1:-1] for comp in comp_list if 'ou=ska-computers' in comp.lower()))
    pprint(comp_list)
