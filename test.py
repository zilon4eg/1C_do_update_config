import subprocess
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
            return {'status': status, 'message': f'OK'}
        else:
            return {'status': status, 'message': f'Узел "{hostname}" недоступен'}

    except subprocess.CalledProcessError as err:
        return {'status': False, 'message': err}
    except FileNotFoundError as err:
        return {'status': False, 'message': err}


if __name__ == '__main__':
    zz = [[{'hostname': 'SKA-SUDEREVKAIA', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'suderevskaia.rv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'TTA - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KOKORIN', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'kokorin.aa - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KOLESNIKOVA', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'admin - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'kolesnikova.ev - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'TTA - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-ZOLOTOREVA', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zolotoreva.ev - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KOROTKOV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'korotkov.as.SKA - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-POLEGENKO', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'polegenko.ae - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-RUDAKOVA', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'nikolaev.kv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'rudakova.og - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-IASTREBOV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'iastrebov.al - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'troyanok.ta - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KATRICHENKO', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'katrichenko.aa - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'troyanok.ta - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'TTA - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-TOKAREVA-TL', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'ska - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'tokareva.tl - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KAMENEV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'd.zubikhin - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'kamenev.ae - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-GURENKO', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'gurenko.za - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'troyanok.ta - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-MANKEVICH', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'Mankevich.KV - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'mankevich.kv.SKA - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-RATSKEVICH', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'kryzhevskaya.mf - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'ratskevich.ap - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-KUBASOV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'kubasov.vs - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'matiash.av.SKA - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'troyanok.ta - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-SUHORUKOV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'grigorev.ia - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'yu.mironova - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'yu.mironova.SKA - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}],
          [{'hostname': 'SKA-GETMANOV', 'status': True},
          {'message': 'ok', 'name': 'ping', 'status': True},
          {'message': 'ok', 'name': 'nethasp.ini', 'status': True},
          {'message': 'd.zubikhin - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'getmanov.ma - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'suhorukov.iv - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'troyanok.ta - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'User - ok', 'name': '1cestart.cfg', 'status': True},
          {'message': 'zapevalov.av - ok', 'name': '1cestart.cfg', 'status': True}]]

    xx = sorted(zz, key=lambda x: x[0]['hostname'])
    pprint(xx)
