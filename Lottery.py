import random, math, discord

class Ticket:

    def __init__(self, mod):
        self.mod = mod


    def __repr__(self):
        return "Ticket class"




class Lottery:

    def __init__(self, name):
        self.name = name
        self.image_path = "Pictures/Три_лотерейных_билета.jpg"
        self.image = discord.File(fp=self.image_path)

    def check_possible_bet(self, bet):
        possible_bets_list = [10, 20, 50, 100, 200, 500]
        if int(bet) in possible_bets_list:
            return (True, int(bet))
        else:
            ### Return list of possible bets
            possible_bets_list = [f"{x}" for x in possible_bets_list]
            possible_bets = "$, ".join(possible_bets_list)
            possible_bets = possible_bets + "$"
            #
            return (False, possible_bets)


    def _create_three_tickets(self):
        #
        def mod_H():
            x1 = random.randint(0, 100)
            x2 = random.randint(0, 100)
            if x1 - x2 <= 5 and x1 - x2 >= (-5):
                return 10
            else:
                return 1.5
        #
        ticket_L = Ticket(round(random.random(), 2))
        ticket_M = Ticket(mod = 0.5)
        ticket_H = Ticket(mod_H())
        #
        ticket_list = [ticket_H, ticket_L, ticket_M]
        random_ticket_list = []
        for i in range(3):
            chose = random.choice(ticket_list)
            random_ticket_list.append(chose)
            ticket_list.remove(chose)
        return random_ticket_list


    def play_lottery(self, choice, bet):
        '''
        Choice must be 'int' in range [1 to 3]
        :param choice:
        :param bet:
        :return:
        '''
        # create random list with 3 tickets
        list = self._create_three_tickets()
        #
        chosen = list[choice-1]
        win = round(bet * chosen.mod, 2)
        return win


    def give_image(self):
        '''Returns an discord.File object'''
        return self.image

    def __repr__(self):
        return "Lottery class"