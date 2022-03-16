import subprocess
import shutil
import os
from threading import Thread
from pprint import pprint


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
            return {'name': 'ping', 'status': status, 'message': f'ok'}
        else:
            return {'name': 'ping', 'status': status, 'message': f'узел недоступен'}

    except subprocess.CalledProcessError as err:
        return {'name': 'ping', 'status': False, 'message': err}
    except FileNotFoundError as err:
        return {'name': 'ping', 'status': False, 'message': err}


def get_hostname_list():
    split_string = r'"\r\n"'
    b_host_list = subprocess.check_output(['dsquery', 'computer', 'domainroot', '-scope', 'subtree', '-limit', '0'])
    # получаем список элементов AD с параметрами CN, OU, DC
    host_list = str(b_host_list)[3:-6].split(split_string)
    # pprint(comp_list)
    # получаем список СОКРАЩЕННЫХ имен ПК из каталога AD OU=SKA-Computers
    host_list = sorted(list(list(comp.split(','))[0][3:] for comp in host_list if 'ou=ska-computers' in comp.lower()))
    return host_list


def path_check_create(path):
    try:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                return {'name': 'path', 'status': True, 'message': f'Путь "{path}" создан'}
            except Exception as err:
                error = str(err).replace("'", '"')
                return {'name': 'path', 'status': False, 'message': error}

        else:
            return {'name': 'path', 'status': True, 'message': f'ok'}
    except Exception as err:
        return {'name': 'path', 'status': False, 'message': err}


def copy_nethasp_ini(hostname):
    # for pc_name in pc_name_list:
    file_name = r'nethasp.ini'
    path_copy = r'\\fs\SHARE\Documents\PUBLIC\Soft\1C\config\conf'
    path_paste = f'\\\\{hostname}\\C$\\Program Files\\1cv8\\conf'
    # проверяем наличие каталогов, если их нет - создаем.
    path_check_create(path_paste)
    # копируем файл
    try:
        shutil.copyfile(f'{path_copy}\\{file_name}', f'{path_paste}\\{file_name}')
        return {'name': 'nethasp.ini', 'status': True, 'message': f'ok'}
    except Exception as err:
        error = str(err).replace("'", '"')
        return {'name': 'nathasp.ini', 'status': False, 'message': error}


def copy_1cestart_cfg(hostname):
    file_name = r'1cestart.cfg'
    path_copy = r'\\fs\SHARE\Documents\PUBLIC\Soft\1C\config\1CEStart'
    path_users_dir = f'\\\\{hostname}\\C$\\Users'
    default_account = ['AMS User', 'Default', 'docflow', 'Public', 'All Users', 'Default User', 'Администратор', 'Все пользователи']
    try:
        user_dirs = list(dir_name for dir_name in os.listdir(path_users_dir) if dir_name not in default_account and not os.path.isfile(f'{path_users_dir}\\{dir_name}'))
    except Exception as err:
        user_dirs = False
        error = str(err).replace("'", '"')
        return {'name': '1cestart.cfg', 'status': False, 'message': error}

    if user_dirs:
        result = []
        for user_dir in user_dirs:
            path_paste = f'{path_users_dir}\\{user_dir}\\AppData\\Roaming\\1C\\1CEStart'
            path_check_create(path_paste)
            try:
                shutil.copyfile(f'{path_copy}\\{file_name}', f'{path_paste}\\{file_name}')
                result.append({'name': '1cestart.cfg', 'status': True, 'message': f'{user_dir} - ok'})
            except Exception as err:
                error = str(err).replace("'", '"')
                result.append({'name': '1cestart.cfg', 'status': False, 'message': f'{user_dir} - {error}'})
        return result


def body(hostname):
    local_output = []
    local_output.append({'hostname': hostname, 'status': True})
    ping_resp = ping(hostname)
    local_output.append(ping_resp)
    if ping_resp['status']:
        local_output.append(copy_nethasp_ini(hostname))
        [local_output.append(message) for message in copy_1cestart_cfg(hostname)]
    output.append(local_output)


def print_data(data):
    for host in data:
        for count, line in enumerate(host, 1):
            if count == 1:
                print(line['hostname'])
            if count > 1:
                name = line['name']
                message = line['message'].replace('\\\\', '\\')
                print(f'{" " * 3}{name} - {message}')


if __name__ == '__main__':
    output = []
    hostname_list = get_hostname_list()
    hostname_list = ['SKA-SUHORUKOV', 'SKA-TESTING', 'SKA-BUH']  # заглушка

    for pc_number, hostname in enumerate(hostname_list, 1):
        Thread(target=body, args=(hostname, )).start()

    while True:
        if len(output) == len(hostname_list):
            complete = []
            error = []
            # pprint(output)

            for host in output:
                # msg_list = list(list(dictionary.values()) for dictionary in msg)
                all_status = []
                for line in host:
                    all_status.append(line['status'])

                if False in all_status:
                    error.append(host)
                else:
                    complete.append(host)

            print('======== COMPLETE ========')
            print_data(complete)
            print('======== ERROR ========')
            print_data(error)
            break
