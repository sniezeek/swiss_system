from pprint import pprint
players = [
    {'name': 'Gracz 1', 'points': 0, 'opponents': []},
    {'name': 'Gracz 2', 'points': 0, 'opponents': []},
    {'name': 'Gracz 3', 'points': 0, 'opponents': []},
    {'name': 'Gracz 4', 'points': 0, 'opponents': []},
    {'name': 'Gracz 5', 'points': 0, 'opponents': []},
    {'name': 'Gracz 6', 'points': 0, 'opponents': []}
]

class Swiss:
    def __init__(self, players):
        self.players = players

    def pair(self):
        self.players.sort(key=lambda x: x['points'], reverse=True)
        used_players = set()
        pprint(self.players)
        pairs = []
        for i, player in enumerate(self.players):
            if player['name'] in used_players:
                continue
            for j in range(i+1, len(self.players)):
                opponent = self.players[j]
                if opponent['name'] not in used_players and opponent['name'] not in player['opponents']:
                    pairs.append([player, opponent])
                    self.players[i]['opponents'].append(opponent['name'])
                    self.players[j]['opponents'].append(player['name'])
                    used_players.add(opponent['name'])
                    used_players.add(player['name'])
                    break
        for player in self.players:
            if player['name'] not in used_players:
                pairs.append([player, None])
        pairs_names = [[player['name'], opponent['name']] if opponent else [player['name'], 'Bye'] for player, opponent in pairs]
        pprint('Parowania:')
        pprint(pairs_names)
        return pairs
    
    def round(self, pairs):
        pprint('---Wyniki---')
        for pair in pairs:
            a = input(str(pair[0]['name']) + ' ' + str(pair[1]['name'] if pair[1] else 'Bye') + ' :')
            if a == 'w':
                add_points_by_name(self.players, pair[0]['name'], 1)
            if a == 'd':
                add_points_by_name(self.players, pair[0]['name'], 0.5)
                add_points_by_name(self.players, pair[1]['name'], 0.5)
            if a == 'l':
                add_points_by_name(self.players, pair[1]['name'], 1)


def add_points_by_name(players, name, points_to_add):
    for player in players:
        if player['name'] == name:
            player['points'] += points_to_add
            break

tournament = Swiss(players)
pprint('/n')
pprint('---RUNDA 1---')
tournament.round(tournament.pair())
pprint('/n')
pprint('---RUNDA 2---')
tournament.round(tournament.pair())

tournament.players.sort(key=lambda x: x['points'], reverse=True)
pprint(tournament.players)
