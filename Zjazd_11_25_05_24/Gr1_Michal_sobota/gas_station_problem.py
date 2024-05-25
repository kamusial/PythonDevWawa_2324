"""
1. Przejeżdżamy przez N stacji, i zapamiętujemy najlepszą.
2. Przez pozostałe 100-N stacji przejeżdżamy i wybieramy pierwszą lepszą
niż najlepsza z pierwszych N.
3. Odpalamy algorytm wielokrotnie dla wszystkich N od 1 do 100
4. Które N jest najoptymalniejsze, żeby zmaksymalizować szansę zatrzymania się przy najlepszej stacji?
"""

import random
from dataclasses import dataclass
from typing import Optional
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


@dataclass
class GasStation:
    mark: int
    id: int

    def __str__(self):
        return f"Station {self.mark}/1000"

    def __repr__(self):
        return self.__str__()


def generate_gas_stations(n: int = 100) -> list[GasStation]:
    stations = []
    for i in range(n):
        mark = random.randint(0, 1000)
        station = GasStation(mark, i)
        stations.append(station)
    return stations


def set_standards(stations: list[GasStation], stopping_point: int) -> int:
    if stopping_point == 0:
        return 0
    first_n_stations = stations[:stopping_point]
    best_station = max(first_n_stations, key=lambda station: station.mark)
    return best_station.mark


def stop_at_best_station(stations: list[GasStation], starting_point: int, min_mark: int) -> Optional[GasStation]:
    for station in stations[starting_point:]:
        if station.mark > min_mark:
            return station
    return None


def get_best_station(stations: list[GasStation]) -> GasStation:
    return max(stations, key=lambda station: station.mark)


def finding_best_gas_station_simulation(stopping_point: int, n_stations: int = 100) -> bool:
    stations = generate_gas_stations(n=n_stations)
    min_mark = set_standards(stations, stopping_point)
    stopped_at = stop_at_best_station(stations, stopping_point, min_mark)
    if stopped_at is None:
        return False
    best_station = get_best_station(stations)
    found_best = stopped_at.mark == best_station.mark
    return found_best


def get_success_chance(stopping_point: int, n_stations: int = 100) -> float:
    successes = 0
    for _ in range(10000):
        best_station_found = finding_best_gas_station_simulation(stopping_point, n_stations)
        if best_station_found:
            successes += 1
    return successes / 10000


def main():
    x = range(101)
    y = []
    for stopping_point in x:
        success_chance = get_success_chance(stopping_point)
        y.append(success_chance*100)
        print(f"{stopping_point}, {success_chance*100}%")
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main()
