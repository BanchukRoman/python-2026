# система умного дома
# реализовать классы базовый класс умные девайсы
# название девайса и атрбут вкл,выкл методы для вкл выкл и узнать состояние
# классы наследники деваайсы: свет бытоввая техника и тд.
# уровень яркости. температуру менять водоснабжения на эконоимию воды
# класс контроля добавить сутройства на проверку всез девайсов
import time as t
class SmartDevice:
    def __init__(self, name, state = False):
        self.name = name
        self.state = state

    def turn_on_or_off_device(self, flag):
        if flag == 'on':
            self.state = True
            print(f'{self.name} включен')
        elif flag == 'off':
            self.state = False
            print(f'{self.name} выключен')

    def find_out_state(self):
        if self.state:
            print(f'{self.name} включен')
        else:
            print(f'{self.name} выключен')

class Kettle(SmartDevice):
    options = {
        1: 'Включить чайник',
        2: 'Выключить чайник',
        3: 'Вскипятить воду',
        4: 'Поменять воду',
        5: 'Узнать состояние',
        6: 'Выбрать другое устройство',
        7: 'Выйти из управления устройствами'
    }
    def __init__(self, name, state = False):
        super().__init__(name, state)
        self.volume = 0
        self.max_volume = 1500
        self.water_temperature = 20

    def pour_water(self, volume):
        if volume < self.max_volume:
            self.volume = volume
            self.water_temperature = 20
        elif volume > self.max_volume:
            self.volume = self.max_volume
            self.water_temperature = 20

    def boil_water(self):
        if self.state:
            if self.volume >= 500 and self.water_temperature <= 20:
                    print('Начал кипятить воду')
                    self.water_temperature = 100
                    t.sleep(5)
                    print('Вода вскипятилась')
            elif self.volume <= 500:
                print('Слишком мало воды')
            elif self.water_temperature > 20:
                print('Воду нельзя кипятить второй раз, замените воду на новую')
        else:
            print('Для начала включите прибор')


class Lamp(SmartDevice):
    options = {
        1: 'Включить лампу',
        2: 'Выключить лампу',
        3: 'Выбрать яркость',
        4: 'Узнать состояние',
        5: 'Выбрать другое устройство',
        6: 'Выйти из управления устройствами'
    }
    def __init__(self, name, state = False):
        super().__init__(name, state)
        self.brightness = 0


    def turn_on_or_off_device(self, flag):
        if flag == 'on':
            self.state = True
            self.brightness = 1
            print(f'{self.name} включен')
        elif flag == 'off':
            self.state = False
            print(f'{self.name} выключен')

    def choice_brightness(self, brightness):
        if self.state:
            if 1<= brightness <= 10:
                self.brightness = brightness
            elif brightness == 0:
                print(f'Выключаю лампу {self.name}')
                self.state = False
            else:
                print('Диапазон яркости от 1 до 10')

devices = {}
device_count = 1
while True:
    option_choice_input = input('Введите номер опции\n'
                                '1 - добавить лампу\n'
                                '2 - добавить чайник\n'
                                '3 - управление девайсами\n'
                                '4 - выход\n'
                                'Ваш выбор: ')
    match option_choice_input:
        case '1':
            name_input = input('Введите название: ')
            devices[device_count] = Lamp(name_input)
            device_count += 1

        case '2':
            name_input = input('Введите название: ')
            devices[device_count] = Kettle(name_input)
            device_count += 1

        case '3':
            while True:
                for key, value in devices.items():
                    print(f'{key} : {value.name}')
                device_choice_input = int(input('Введите номер девайса: '))
                if devices[device_choice_input].__class__.__name__ == 'Kettle':
                    for key, value in Kettle.options.items():
                        print(f'{key} : {value}')
                    option_choice = int(input('Введите номер опции: '))
                    match option_choice:
                        case 1:
                            devices[device_choice_input].turn_on_or_off_device(flag = 'on')
                        case 2:
                            devices[device_choice_input].turn_on_or_off_device(flag='off')
                        case 3:
                            devices[device_choice_input].boil_water()
                        case 4:
                            volume_input = int(input('Введите объем сколько вы хотите налить воды: '))
                            devices[device_choice_input].pour_water(volume = volume_input)
                        case 5:
                            devices[device_choice_input].find_out_state()
                        case 6:
                            continue
                        case 7:
                            break
                elif devices[device_choice_input].__class__.__name__ == 'Lamp':
                    for key, value in Lamp.options.items():
                        print(f'{key} : {value}')
                    option_choice = int(input('Введите номер опции: '))
                    match option_choice:
                        case 1:
                            devices[device_choice_input].turn_on_or_off_device(flag = 'on')
                        case 2:
                            devices[device_choice_input].turn_on_or_off_device(flag='off')
                        case 3:
                            brightness_input = int(input('Введите яркость для лампы: '))
                            devices[device_choice_input].choice_brightness(brightness = brightness_input)
                        case 4:
                            devices[device_choice_input].find_out_state()
                        case 5:
                            continue
                        case 6:
                            break
        case '4':
            break

