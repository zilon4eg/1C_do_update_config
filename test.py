import subprocess


def ping(hostname):
    try:
        cmd_line = f'ping {hostname}'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE)

        response = [line_data.decode("cp866", "ignore").rstrip().lower() for line_data in p.stdout]
        response = list(string for string in response if 'ответ' in string or 'reply' in response)
        # print(response)
        count = 0
        for string in response:
            if 'time' in string or 'время' in string:
                count += 1
        status = False if count < 3 else True
        if status:
            return {'status': status, 'message': f'OK'}
        else:
            return {'status': status, 'message': f'Узел "{hostname}" недоступен'}

    except subprocess.CalledProcessError as err:
        return {'status': False, 'message': err}
    except FileNotFoundError as err:
        return {'status': False, 'message': err}


print(ping('SKA-TESTING'))
