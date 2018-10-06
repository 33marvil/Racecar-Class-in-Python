"""code goes here"""
class RaceCar:

    """method to get average speed"""
    def __init__(self, data):
        self.__name = data["name"]
        self.__lap_times = data["lap_times"]

    # getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        raise AttributeError

    @property
    def lap_times(self):
        return self.__lap_times

    @lap_times.setter
    def lap_times(self, lap_times):
        self.__lap_times = lap_times

    # """method for getting level of each racecar"""
    # # retorna la velocidad promedio
    # # distancia / tiempo = velocidad
    #
    def average_speed(self):
        lap = 100
        # tiempo promedio
        tiempo_promedio = sum(self.__lap_times) / len(self.__lap_times)
        # calcular velocidad promedio
        velocidad_promedio = lap / tiempo_promedio
        # round a 2 decimales
        return round(velocidad_promedio, 2)

    # return el level
    def status(self):
        # Si velocidad_promedio es mayor que o igual 9.0 and menor que o igual <= 9.99 "Principiante"
        if self.average_speed() >= 9 and self.average_speed() <= 9.99:
            return "Principiante"
        elif self.average_speed() >= 10 and self.average_speed() <= 11.99:
            return "Normal"
        elif self.average_speed() >= 12 and self.average_speed() <= 14.99:
            return "Medio"
        elif self.average_speed() >= 15 and self.average_speed() <= 17:
            return "Avanzado"
        else:
            return "No status"


# car1 = RaceCar({"name": "Force", "lap_times": [2, 2, 2, 2, 2]})
# print(car1.average_speed())
# print(car1.status())

class Team:

    def __init__(self, escuderias):
        self.__team = escuderias

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, team):
        raise AttributeError


    """method to add a new racecar"""

    def add(self, new_car):
        self.__team.append(new_car)

    """method to calculate average speed of team"""

    def average_speed_of_team(self):
        # Obtener el average_speed de cada carro es decir de cada objeto en la lista
        return (round(sum([car.average_speed() for car in self.__team ]) / len(self.__team), 2))



"""function to search a racecar in team"""


def search(name, equipo):
    return "{} is a racer".format(name) if len([racecar.name for racecar in equipo.team if name == racecar.name]) > 0 else "{} is not a racer".format(name)
    #     return name + " is a racer"
    # else:
    #     return name + " is not a racer"

    # Si el largo de lista es ==  1 return " Power is a racer"
    # Si no es == a 1 return " Duck is not a racer"











# search race car in team
#print(search("Power", team_one))
# >> "Power is a racer"
