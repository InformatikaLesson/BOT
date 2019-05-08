

class Castle:

    def __init__(self):
        self.capital_castle_type = "Маленькое поселение"
        self.capital_castle_name = "Лагерь"
        self.self.level = 1
        self.building_spots = 3
        self.population = 0


    def get_lvl_info(self, lvl):
        #
        self.level = lvl
        #
        def _function_stuff():
            if lvl == 2:
                capital_castle_type = "Крупное поселение"
                capital_castle_name = "Деревня"
            elif lvl == 3:
                capital_castle_type = "Большое поселение"
                capital_castle_name = "Небольшой городишко"
            elif lvl == 4:
                capital_castle_type = "Огромное поселение"
                capital_castle_name = "Городище"
            elif lvl == 5:
                capital_castle_type = "Город"
                capital_castle_name = "Большой город"
            elif lvl == 6:
                capital_castle_type = "Город"
                capital_castle_name = "Крепость"
            elif lvl == 7:
                capital_castle_type = "Роскошный город"
                capital_castle_name = "Замок с крепостью"
            #
            return (capital_castle_type, capital_castle_name)
        #
        self.capital_castle_type, self.capital_castle_name = _function_stuff()
        self.building_spots = 3 + lvl*5
        return True


    def __repr__(self):
        return "Castle class"
