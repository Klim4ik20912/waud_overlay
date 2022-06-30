import wmi
from time import sleep
from art import tprint

c = wmi.WMI()

tprint('OVERLAY. V - 0.2.1')

def main():
    while True:
        last = last_act()
        sleep(5)
        text = now_work()
        if text != last:
            set_status(text)
        else:
            print('ничего не изменилось')


def now_work():
    if (c.Win32_Process(name='dota2.exe')):
        return 'Dota 2'
    else:
        return 'не играет сейчас :('


def last_act():
    return now_work()


def set_status(text):
    print(f'статус изменен на {text}')

def hours_counter():
    pass

main()
