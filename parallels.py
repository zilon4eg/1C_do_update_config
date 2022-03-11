import subprocess
import shutil
import os
from threading import Thread


def get_pc_name_list():
    split_string = r'"\r\n"'
    b_comp_list = subprocess.check_output(['dsquery', 'computer', 'domainroot', '-scope', 'subtree', '-limit', '0'])
    # получаем список элементов AD с параметрами CN, OU, DC
    comp_list = str(b_comp_list)[3:-6].split(split_string)
    # pprint(comp_list)
    # получаем список СОКРАЩЕННЫХ имен ПК из каталога AD OU=SKA-Computers
    comp_list = sorted(list(list(comp.split(','))[0][3:] for comp in comp_list if 'ou=ska-computers' in comp.lower()))
    print(f'Найдено {len(comp_list)} ПК')
    return comp_list


def path_check_create(path):
    try:
        if not os.path.exists(path):
            print(f'{" " * indent_size}Путь "{path}" не существует')

            try:
                os.makedirs(path)
                print(f'{" " * indent_size}Путь "{path}" создан')
            except Exception as err:
                error = str(err).replace('\\\\', '\\').replace("'", '"')
                print(f'{" " * indent_size}{error}')

        else:
            print(f'{" " * indent_size}Доступность пути "{path}" проверена')
    except Exception as err:
        print(err)


def copy_nethasp_ini(pc_name):
    # for pc_name in pc_name_list:
    file_name = r'nethasp.ini'
    path_copy = r'\\fs\SHARE\Documents\PUBLIC\Soft\1C\config\conf'
    path_paste = f'\\\\{pc_name}\\C$\\Program Files\\1cv8\\conf'
    # проверяем наличие каталогов, если их нет - создаем.
    path_check_create(path_paste)
    # копируем файл
    try:
        shutil.copyfile(f'{path_copy}\\{file_name}', f'{path_paste}\\{file_name}')
        print(f'Файл "{file_name}" успешно скопирован')
    except Exception as err:
        error = str(err).replace('\\\\', '\\').replace("'", '"')
        print(f'{" " * indent_size}{error}')


def body():
    markup = f'=({pc_number:0{len(str(len(pc_name_list)))}})=({pc_name})'
    markup = f'{markup}{"=" * (40 - len(markup))}'
    print(markup)
    print('Копируем файл конфигурации nethasp.ini')
    copy_nethasp_ini(pc_name)


if __name__ == '__main__':
    indent_size = 2

    pc_name_list = get_pc_name_list()

    for pc_number, pc_name in enumerate(pc_name_list, 1):
        Thread(target=body).start()
