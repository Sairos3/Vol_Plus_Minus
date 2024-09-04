import json

class RemoteControl:
    def __init__(self, v):
        try:
            with open('remote_data.json', 'r') as file:
                data = json.load(file)
                self.volume = data.get('volume', v)
                self.programs = data.get('programs', ["ARD", "ZDF", "SAT1", "RTL", "CNN", "PRO7", "Arte", "Pgm_8"])
                self.__curr_program_number = data.get('current_program', 0)
        except FileNotFoundError:
            self.volume = v
            self.programs = ["ARD", "ZDF", "SAT1", "RTL", "CNN", "PRO7", "Arte", "Pgm_8"]
            self.__curr_program_number = 0

    def save_data(self):
        data = {
            'volume': self.volume,
            'programs': self.programs,
            'current_program': self.__curr_program_number
        }
        with open('remote_data.json', 'w') as file:
            json.dump(data, file)

    def plus_vol(self):
        if self.volume < 10:
            self.volume += 1
            self.save_data()

    def minus_vol(self):
        if self.volume > 0:
            self.volume -= 1
            self.save_data()

    def printProgram(self):
        return (f"Die Lautstärke beträgt {self.volume} - "
                f"Programm: {self.programs[self.__curr_program_number]}")

    def setProgramName(self, pgm):
        self.programs[self.__curr_program_number] = pgm
        self.save_data()

    def getProgramName(self):
        return self.programs[self.__curr_program_number]

    def next_program(self):
        if self.__curr_program_number < len(self.programs) - 1:
            self.__curr_program_number += 1
        else:
            self.__curr_program_number = 0
        self.save_data()

    def prev_program(self):
        if self.__curr_program_number > 0:
            self.__curr_program_number -= 1
        else:
            self.__curr_program_number = len(self.programs) - 1
        self.save_data()