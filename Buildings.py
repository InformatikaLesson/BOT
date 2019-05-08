

class Building:

    def __init__(self):
        self.name = ""
        self.time_to_build = 0
        self.income = 0
        self.outcome = 0
        self.capacity = 0
        self.level = 1
        self.cost = 0

    def __repr__(self):
        return "Base Building class"


class Tavern(Building):
    info_list = ["**Уникальное здание (можно построить одно здание на город)**",
                      "**Инфо**: Позволяет нанимать рабочих-нпс.",
                      "**Характеристики**: 1 шпион, приносит 20$ в час (налог).",
                      "**Стоимость**: 2 500$",
                      "**Время строительства** 6:00:00",
                      "**Чтобы зайти в таверну введите '!таверна'**"]

    def __init__(self):
        self.name = "Таверна"
        self.time_to_build = 21600 # Seconds
        self.income = 20
        self.outcome = 0
        self.capacity = 200
        self.spies = 1
        self.cost = 2500
        self.level = 1
        self.max_amount = 1


    def _get_lvl_2(self):
        self.time_to_build = 43200
        self.income = 40
        self.capacity = 400
        self.spies = 2
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 43200
        self.income = 80
        self.capacity = 800
        self.spies = 3
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 64800
        self.income = 160
        self.capacity = 1600
        self.spies = 4
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 64800
        self.income = 240
        self.capacity = 2400
        self.spies = 5
        self.level = 5

    def spies_repr(self):
        text = f"Количество шпионов - {self.spies}. Вы можете использовать шпионов, чтобы устраивать диверсии другим игрокам. " \
               f"Диверсии приносят вам деньги, опыт, а также вредят вашей цели."
        return text


    def __repr__(self):
        return "Tavern(Building) class"


class Market(Building):

    info_list = ["**Уникальное здание (можно построить одно здание на город)**",
                 "**Инфо**: Позволяет продажу некоторых товаров в своем городе. Открывает слоты для торговых лавок "
                 "(Торговую лавку занимает торговец из Ясного Города, что позвозяет вам покупать ограниченое количество "
                 "товаров из Ясного Города находясь в своей столице.",
                 "**Характеристики**: 1 лавка, приносит 50$ в час (налог).",
                 "**Стоимость**: 10 000$",
                 "**Время строительства** 10:00:00",
                 "**Чтобы зайти в рынок введите '!рынок'**"]

    def __init__(self):
        self.name = "Рынок"
        self.time_to_build = 36000
        self.income = 50
        self.outcome = 0
        self.capacity = 500
        self.store = 1
        self.level = 1
        self.cost = 10000
        self.max_amount = 1


    def _get_lvl_2(self):
        self.time_to_build = 36000
        self.income = 75
        self.capacity = 750
        self.store = 2
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 43200
        self.income = 150
        self.capacity = 1500
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 64800
        self.income = 200
        self.capacity = 2000
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 72000
        self.income = 300
        self.capacity = 3000
        self.level = 5

    def __repr__(self):
        return "Market(Building) class"


class Blockpost(Building):

    info_list = [f"**Максимальное количество постов - 8**",
                      "**Инфо**: Уменьшает шанс успешного саботажа вашего города.",
                      "**Характеристики**: шанс успешного саботажа -2%, оплата 10$ в час",
                      "**Стоимость**: 1 000$",
                      "**Время строительства** 1:00:00",
                      "**Чтобы получить информацию о постах охраны введите '!охрана'**"]

    def __init__(self):
        self.name = "Пост Охраны"
        self.time_to_build = 3600
        self.income = 0
        self.outcome = 10
        self.bonus = 2
        self.level = 1
        self.cost = 1000
        self.max_amount = 8
        self.capacity = 0


    def _get_lvl_2(self):
        self.time_to_build = 7200
        self.outcome = 20
        self.bonus = 4
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 9000
        self.outcome = 30
        self.bonus = 6
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 10800
        self.outcome = 40
        self.bonus = 8
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 12600
        self.outcome = 50
        self.bonus = 10
        self.level = 5

    def __repr__(self):
        return "Blockpost(Building) class"

class Altar(Building):

    info_list = ["**Уникальное здание (можно построить одно здание на город)**",
                      "**Инфо**: Позволяет принять существующую веру или создать свою. После принятия определенной веры "
                      "игрок открывает ее бонусы. Для активации бонусов веры необходимо повышать уровень веры.",
                      "**Характеристики**: открывает доступ к пантеонам и вере",
                      "**Стоимость**: 20 000$",
                      "**Время строительства** 24:00:00",
                      "**Чтобы открыть меню алтаря введите '!алтарь'**"]

    def __init__(self):
        self.name = "Алтарь"
        self.time_to_build = 86400
        self.level = 1
        self.cost = 20000
        self.max_amount = 1
        self.capacity = 0


    def _get_lvl_2(self):
        self.time_to_build = 129600
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 172800
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 216000
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 259200
        self.level = 5

    def _power(self):
        self.name = "Первоалтарь"

    def __repr__(self):
        return "Altar(Building) class"

class WoodHarvester(Building):

    info_list = ["**Производственное здание**",
                      f"**Максимальное количество лесорубов - 4**",
                      "**Инфо**: постройте лесоруба, чтобы начать собирать дерево.",
                      f"**Характеристики**: собирает 10 дерева в час.",
                      "**Стоимость**: 2 000$",
                      "**Время строительства** 2:00:00"]

    def __init__(self):
        self.name = "Лесоруб"
        self.time_to_build = 7200
        self.level = 1
        self.cost = 2000
        self.max_amount = 4
        self.wood_harvest = 10
        self.product_cost = 0.1
        self.resource = "wood"

    def _get_lvl_2(self):
        self.time_to_build = 9000
        self.wood_harvest = 20
        self.cost = 4000
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 9900
        self.wood_harvest = 40
        self.cost = 6000
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 10700
        self.wood_harvest = 80
        self.cost = 8000
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 11600
        self.wood_harvest = 160
        self.cost = 10000
        self.level = 5


    def __repr__(self):
        return "WoodHarvester(Building) class"

class Sawmill(Building):

    info_list = ["**Производственное здание**",
                      f"**Максимальное количество лесопилок - 2**",
                      "**Инфо**: Лесопилка перерабатывает дерево в доски, которые "
                      "относятся к продвинутым материалам.",
                      f"**Характеристики**: производит 20 досок в час.",
                      "**Стоимость**: 5 000$",
                      "**Время строительства** 4:00:00"]

    def __init__(self):
        self.name = "Лесопилка"
        self.time_to_build = 14400
        self.level = 1
        self.cost = 5000
        self.max_amount = 2
        self.plank_harvest = 20
        self.product_cost = 0.3
        self.resource = "plank"

    def _get_lvl_2(self):
        self.time_to_build = 15300
        self.plank_harvest = 40
        self.cost = 4000
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 16200
        self.wood_harvest = 80
        self.cost = 6000
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 17100
        self.wood_harvest = 160
        self.cost = 8000
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 18000
        self.wood_harvest = 320
        self.cost = 10000
        self.level = 5

    def __repr__(self):
        return "Sawmill(Building) class"


class StoneHarvester(Building):

    info_list = ["**Производственное здание**",
                f"**Максимальное количество каменотёсов - 4**",
                "**Инфо**: Постройте каменотёса, чтобы начать собирать камень.",
                f"**Характеристики**: производит 20 камня в час.",
                "**Стоимость**: 4 000$",
                "**Время строительства** 2:30:00"]

    def __init__(self):
        self.name = "Каменотёс"
        self.time_to_build = 9000
        self.level = 1
        self.cost = 4000
        self.max_amount = 4
        self.stone_harvest = 20
        self.product_cost = 0.4
        self.resource = "stone"

    def _get_lvl_2(self):
        self.time_to_build = 10800
        self.stone_harvest = 40
        self.cost = 6000
        self.level = 2

    def _get_lvl_3(self):
        self.time_to_build = 12600
        self.stone_harvest = 80
        self.cost = 8000
        self.level = 3

    def _get_lvl_4(self):
        self.time_to_build = 16200
        self.stone_harvest = 120
        self.cost = 10000
        self.level = 4

    def _get_lvl_5(self):
        self.time_to_build = 18000
        self.stone_harvest = 160
        self.cost = 12000
        self.level = 5

    def __repr__(self):
        return "StoneHarvester(Building) class"


class Mine:

    time_to_build = 10800
    level = 1
    cost = 8000
    max_amount = 4
    resource_harvest = 50

    def __repr__(self):
        return f"General Mine ({self.name}) class"

class IronMine(Mine):

    resource = "iron_ore"

    info_list = ["**Здание для добычи руды**",
                f"**Максимальное количество железных шахт - 4**",
                "**Инфо**: Постройте железную шахту, чтобы начать собирать железную руду.",
                f"**Характеристики**: производит 50 железной руды в час.",
                "**Стоимость**: 8 000$",
                "**Время строительства** 3:00:00"]

    def __init__(self):
        self.name = "Железная шахта"
        self.mod = 1
        self.product_cost = 0.2

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*self.mod)
        self.cost = int(self.cost*lvl*self.mod)
        self.resource_harvest = int(self.resource_harvest*lvl*self.mod)


    def __repr__(self):
        return "IronMine(Mine) class"

class SilverMine(Mine):

    resource_harvest = 30
    time_to_build = 21600
    cost = 12000
    resource = "silver_ore"

    info_list = ["**Здание для добычи руды**",
                 f"**Максимальное количество серебряных шахт - 4**",
                 "**Инфо**: Постройте серебряную шахту, чтобы начать собирать серебряную руду.",
                 f"**Характеристики**: производит 30 серебряной руды в час.",
                 "**Стоимость**: 12 000$",
                 "**Время строительства** 6:00:00"]

    def __init__(self):
        self.name = "Серебряная шахта"
        self.mod = 1.5
        self.product_cost = 0.5

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*self.mod)
        self.cost = int(self.cost*lvl*self.mod)
        self.resource_harvest = int(self.resource_harvest*lvl*self.mod)

    def __repr__(self):
        return "SilverMine(Mine) class"

class GoldMine(Mine):

    max_amount = 2
    resource_harvest = 15
    time_to_build = 43200
    cost = 16000
    resource = "gold_ore"

    info_list = ["**Здание для добычи руды**",
                 f"**Максимальное количество золотых шахт - 2**",
                 "**Инфо**: Постройте золотую шахту, чтобы начать собирать золотую руду.",
                 f"**Характеристики**: производит 15 золотой руды в час.",
                 "**Стоимость**: 16 000$",
                 "**Время строительства** 12:00:00"]

    def __init__(self):
        self.name = "Золотая шахта"
        self.mod = 2
        self.product_cost = 2

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*self.mod)
        self.cost = int(self.cost*lvl*self.mod)
        self.resource_harvest = int(self.resource_harvest*lvl*self.mod)

    def __repr__(self):
        return "GoldMine(Mine) class"

class RubbiesMine(Mine):

    max_amount = 2
    resource_harvest = 60
    time_to_build = 10 #43200
    cost = 18000
    resource = "rubbies"

    info_list = ["**Здание для добычи редкого ресурса**",
                 f"**Максимальное количество золотых шахт - 2**",
                 "**Инфо**: Постройте добытчиков рубинов, чтобы начать собирать рубины.",
                 f"**Характеристики**: производит 60 рубинов в час.",
                 "**Стоимость**: 18 000$",
                 "**Время строительства** 12:00:00"]

    def __init__(self):
        self.name = "Шахта рубинов"
        self.mod = 1.5
        self.product_cost = 10

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*self.mod)
        self.cost = int(self.cost*lvl*self.mod)
        self.resource_harvest = int(self.resource_harvest*lvl*self.mod)

    def __repr__(self):
        return "RubbiesMine(Mine) class"

class DiamondsMine(Mine):

    max_amount = 1
    resource_harvest = 30
    time_to_build = 86400
    cost = 30000
    resource = "diamonds"

    info_list = ["**Здание для добычи редкого ресурса**",
                 f"**Максимальное количество алмазных шахт - 1**",
                 "**Инфо**: Постройте алмазную шахту, чтобы начать собирать алмазы.",
                 f"**Характеристики**: производит 30 алмазов в час.",
                 "**Стоимость**: 30 000$",
                 "**Время строительства** 24:00:00"]

    def __init__(self):
        self.name = "Алмазная шахта"
        self.mod = 5
        self.product_cost = 50

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*self.mod)
        self.cost = int(self.cost*lvl*self.mod)
        self.resource_harvest = int(self.resource_harvest*lvl*self.mod)

    def __repr__(self):
        return "DiamondsMine(Mine) class"

class Smelter:

    time_to_build = 9000
    level = 1
    cost = 10000
    max_amount = 2
    resource_smelting = 200
    iron_cost = 2
    silver_cost = 5
    gold_cost = 10
    name = "Плавильня"

    info_list = [f"**Максимальное количество плавилень - 2**",
                 "**Инфо**: Постройте плавильню, чтобы начать плавить руду. Переработаная в слитки руда стоит намного дороже.",
                 f"**Характеристики**: плавит 200 единиц руды в час.",
                 "**Стоимость**: 10 000$",
                 "**Время строительства** 2:30:00"]

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build*lvl*0.75)
        self.cost = int(self.cost*lvl*0.75)
        self.resource_harvest = int(self.resource_harvest*lvl*0.75)

    def __repr__(self):
        return "Smelter class"

class Storage:

    max_amount = 5
    level = 1
    resource_storage = 100
    time_to_build = 43200
    cost = 15000
    name = "Городской склад"
    outcome = 50
    income = 0

    info_list = [f"**Максимальное количество складов - 2**",
                 "**Инфо**: Постройте склад, чтобы увеличить количество ресурсов, которые вы можете хранить в городе.",
                 f"**Характеристики**: увеличивает вместимость складов в городе на 100 единиц товара.",
                 "**Стоимость**: 10 000$",
                 "**Время строительства** 2:30:00"]

    def get_level(self, lvl):
        self.time_to_build = int(self.time_to_build * lvl * 0.75)
        self.cost = int(self.cost * lvl * 0.75)
        self.resource_storage = int(self.resource_storage * lvl * 0.75)

    def __repr__(self):
        return "Storage class"

class Calculator:

    def __init__(self):
        pass

    def calculate_income(self, buildings):
        money_buildings_list = [Tavern, Altar, Market, Blockpost, Storage]
        result = {"money":0,}
        for each_building in buildings:
            if type(each_building) in money_buildings_list:
                income = each_building.income
                charge = each_building.outcome
                money = result["money"]
                money += income
                money -= charge
                result["money"] = money
            elif issubclass(type(each_building), Mine) or issubclass(type(each_building), Building):
                try:

                    resource_type = each_building.resource
                    resource_amount = result[resource_type]
                    resource_amount += each_building.resource_harvest
                    result[resource_type] = resource_amount

                except Exception as e:

                    result[resource_type] = each_building.resource_harvest
                    #print(e)
                #####
        #print("Calculation done, result: ", result)
        return result



    def __repr__(self):
        return "Income/Resource-calcuator class"