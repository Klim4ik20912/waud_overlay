import wmi
from time import sleep
from art import tprint
import random
import vk_api

c = wmi.WMI()

tprint('OVERLAY. V - 0.2.5')

default_smiles = [
    '👾', '👽', '🎮', '🎲', '🎰'
]


def main():
    while True:
        last = last_act()
        print(f'last act - {last}')
        sleep(5)
        text = now_work()
        print(f'now work - {text}')
        if text != last:
            emoji = random.choice(default_smiles)
            status_text = f'играет в {text} {emoji}'
            set_status(status_text)
            print('статус изменен')

        else:
            print('not change!')


def now_work():
    if (c.Win32_Process(name='dota2.exe')):
        return 'Dota 2'
    elif (c.Win32_Process(name='pycharm64.exe')):
        return 'coding in PyCharm'
    elif (c.Win32_Process(name='osu!.exe')):
        return 'osu!'
    elif (c.Win32_Process(name='Discord.exe')):
        return 'discord'
    else:
        return 'sleep'



def last_act():
    return now_work()


def set_status(status_text):
    vk = vk_api.VkApi(token="YOUR TOKEN")
    vk.method("status.set", {"text": status_text})


main()

