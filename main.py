# класс для хранения информации о стримере
class Streamer:
    def __init__(self, nick, subscribers):
        self.nick = nick
        self.donates = []
        self.subscribers = subscribers

    # добавление доната
    def add_donate(self, amount):
        self.donates.append(amount)

    # поодсчёт общей суммы донатов
    def total_donates(self):
        total = 0
        for donate in self.donates:
            total += donate
        return total

    # подсчёт среднего доната
    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)


# вывод статистики стримера
def print_stats(streamer):
    print("Стример:", streamer.nick)
    print("Донатов:", len(streamer.donates),
          "сумма:", streamer.total_donates())
    print("Средний донат:", round(streamer.average_donate(), 1))
    print("Подписчиков:", streamer.subscribers)


# проверка популярности
def is_popular(streamer):
    return streamer.subscribers > 1000


# главная часть программы
s = Streamer("ShadowStorm", 1500)
s.add_donate(100)
s.add_donate(250)
s.add_donate(50)

print_stats(s)
print("Популярен:", is_popular(s))