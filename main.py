import wmi
from time import sleep
from art import tprint
import random

c = wmi.WMI()

tprint('OVERLAY. V - 0.2.5')

default_smiles = [
    '👾', '👽', '🎮', '🎲', '🎰'
]


def main():
    while True:
        last = last_act()
        sleep(30)
        text = now_work()
        if text != last:
            vk = vk_api.VkApi(token="vk1.a.dIEmemk1_8sLdbTpANnu_fGzxwNGpivZkqHMbiEYn8smp2yzvmHJfzL6wPV1x-cXxIE4XmgWai2QfzjhQpudgq7nL2AQJ_wRAgpPIqrbnVKzMgkoJUrw029Ho9vswbGuKC9uqaZsatCOeV1-8drrx8wVIlbNWm4wlvUbjOCMA4egY6JI6ht4Pvn3M973Kz6e")
            emoji = random.choice(default_smiles)
            status_text = f'играет в {text} {emoji}'
            set_status(status_text)

        else:
            print('not change!')


def now_work():
    if (c.Win32_Process(name='dota2.exe')):
        return 'Dota 2'
    elif (c.Win32_Process(name='pycharm64.exe')):
        return 'coding in PyCharm'
    elif (c.Win32_Process(name='osu!.exe')):
        return 'discord'
    elif (c.Win32_Process(name='Discord.exe')):
        return 'osu!'
    else:
        return 'AFK'



def last_act():
    return now_work()


def set_status(status_text):
    vk.method("status.set", {"text": status_text})
    
main()
