import random

PELOTON_ATTACK_CARD = 0

# Rouleur deck with added 0 for 2/9 attack card
PELOTON_DECK = [2, 2, 2, 3, 3, 3, 4, 4, 4,
                5, 5, 5, 9, 9, 9, PELOTON_ATTACK_CARD]
MUSCLE_SPRINTER_DECK = [3, 3, 3, 4, 4, 4, 5, 5, 5, 5,
                        6, 6, 6, 7, 7, 7]  # Sprinter deck with added 5
MUSCLE_ROULEUR_DECK = [2, 2, 2, 3, 3, 3, 4, 4,
                       4, 5, 5, 5, 9, 9, 9]  # Basic rouleur deck


def selection_menu():
    selections = {}
    peloton_input = None
    while peloton_input is None:
        peloton_input = input("Do you want to include Peloton team? (y/n)\n")
        if peloton_input.lower() == 'y':
            selections['peloton'] = True
        else:
            selections['peloton'] = False

    amount_of_muscle_teams = None
    while amount_of_muscle_teams is None:
        try:
            amount_of_muscle_teams = int(
                input("How many muscle teams? [0-3]\n"))
        except:
            amount_of_muscle_teams = None
        if amount_of_muscle_teams is None or amount_of_muscle_teams < 0 or amount_of_muscle_teams > 3:
            amount_of_muscle_teams = None
            continue

        selections['muscle_teams'] = amount_of_muscle_teams

    return selections


class BotCyclist:

    def __init__(self, name, team):
        if team == 'PELOTON':
            self._cards = PELOTON_DECK.copy()
        elif team == 'MUSCLE-SPRINTER':
            self._cards = MUSCLE_SPRINTER_DECK.copy()
        elif team == 'MUSCLE-ROULEUR':
            self._cards = MUSCLE_ROULEUR_DECK.copy()

        self.name = name

        self.cards = self._cards.copy()
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) < 1:
            self.cards = self._cards.copy()
            random.shuffle(self.cards)

        return self.cards.pop()

    def __repr__(self):
        return f'<BotCyclist> {self.name}'

    def __str__(self):
        return self.__repr__()


def create_bots(selections):
    bots = []
    if selections['peloton']:
        peloton_team = BotCyclist('Peloton', 'PELOTON')
        bots.append(peloton_team)
    for num in range(selections['muscle_teams']):
        muscle_sprinter = BotCyclist(
            f'Muscle #{num + 1} Sprinter', 'MUSCLE-SPRINTER')
        muscle_rouleur = BotCyclist(
            f'Muscle #{num + 1} Rouleur', 'MUSCLE-ROULEUR')
        bots.append(muscle_sprinter)
        bots.append(muscle_rouleur)

    return bots


def print_setup_instructions(selections):
    print("")
    print("Let's setup the game.")
    if selections['peloton']:
        print(
            'First, add a Peloton team to the first and second position on the right lane.')
        print(
            f'Second, add {selections["muscle_teams"]} teams with sprinter first and rouleur second to best possible positions.')
        print('Last, setup player teams as they wish.')
    else:
        print(
            f'Add {selections["muscle_teams"]} muscle teams with sprinter first and rouler second into best possible positions.')
        print('Last, setup player teams as they wish.')
    print("")


if __name__ == '__main__':
    print("Let's play!")
    selections = selection_menu()

    while not selections['peloton'] and selections['muscle_teams'] == 0:
        print('You have not selected any bot teams. I\'ll ask you again.\n')
        selections = selection_menu()

    bots = create_bots(selections)

    print_setup_instructions(selections)
    input('Press ENTER to start the game  ')

    end_game = False
    while not end_game:
        print('\n===')
        for bot in bots:
            drawn = bot.draw()
            if drawn == PELOTON_ATTACK_CARD:
                drawn = 'PELOTON ATTACK (2/9)'
            print(f'{bot.name} drew {drawn}')

        print('===\n')
        input('Press enter for next round (or press CTRL-C to stop the program) ')
