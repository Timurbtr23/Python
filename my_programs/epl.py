from random import shuffle, randint


class League:

    def __init__(self):
        self.clubs = []

    def add(self, club):
        self.clubs.append(club)

    def print_table(self):
        sort_table_list = self.clubs
        sort_table_list.sort(key=lambda x: -x.score)
        print("\nEnglish Premier League Table")
        print("{} {:^18} {:>8} {:4} {:4} {:>2} {:>5} {:>4} {:>6}".format('pos', 'club', 'win', 'draw', 'lost', 'G', 'GC', 'GD', 'score'))
        for pos, club in enumerate(sort_table_list):
            print(f'{pos+1:^3} {club.name:^20} {club.wins:>5} {club.draws:>4} {club.lost:>4} {club.goals:^5} {club.goals_conceded:^4} {club.goals-club.goals_conceded:^4} {club.score:>4}')

    def make_draw(self, max_g, first_team, second_team):
        dice = randint(0, max_g)
        first_team.goals += dice
        second_team.goals += dice
        first_team.goals_conceded += dice
        second_team.goals_conceded += dice
        score = (dice, dice)
        return score

    def chance_of_match(self, difference, first_team, second_team):
        chance = randint(1, 100)

        if difference >= 10:
            if chance <= 85:
                dice = randint(1, 11)
                if dice <= 4:
                    goals = 1
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                elif 5 <= dice <= 7:
                    goals = 2
                    if dice == 6:
                        first_team.goals_conceded += 1
                        score = (goals, 1)
                        return score
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                elif 8 <= dice <= 9:
                    goals = 3
                    if dice == 8:
                        first_team.goals_conceded += 1
                        score = (goals, 1)
                        return score
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                else:
                    goals = 4
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (4, 0)
                    return score
            elif 85 < chance <= 92:
                score = self.make_draw(1, first_team, second_team)
                return score
            else:
                goals = 1
                second_team.goals += goals
                first_team.goals_conceded += goals
                score = (0, goals)
                return score

        if 5 < difference < 10:
            if chance <= 70:
                dice = randint(1, 10)
                if dice <= 5:
                    goals = 1
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                elif 5 <= dice <= 8:
                    goals = 2
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                else:
                    goals = 3
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
            elif 70 < chance <= 85:
                score = self.make_draw(2, first_team, second_team)
                return score
            else:
                goals = 1
                second_team.goals += goals
                first_team.goals_conceded += goals
                score = (0, goals)
                return score

        if 1 < difference <= 5:
            if chance <= 50:
                dice = randint(1, 10)
                if dice <= 5:
                    goals = 1
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                else:
                    goals = 2
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
            elif 50 < chance <= 70:
                score = self.make_draw(3, first_team, second_team)
                return score
            else:
                dice = randint(1, 5)
                if dice <= 3:
                    goals = 1
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                elif 3 < dice <= 5:
                    goals = 2
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (0, goals)
                    return score

        if -1 <= difference <= 1:
            if chance <= 33:
                dice = randint(1, 10)
                if dice <= 3:
                    goals = 1
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                elif 3 < dice <= 6:
                    goals = 2
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
                else:
                    goals = 3
                    first_team.goals += goals
                    second_team.goals_conceded += goals
                    score = (goals, 0)
                    return score
            elif 33 < chance <= 66:
                score = self.make_draw(3, first_team, second_team)
                return score
            else:
                dice = randint(1, 10)
                if dice <= 3:
                    goals = 1
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                elif 3 < dice <= 6:
                    goals = 2
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                else:
                    goals = 3
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score

        if -5 <= difference < -1:
            if chance <= 30:
                dice = randint(1, 10)
                if dice <= 5:
                    goals = 1
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                else:
                    goals = 2
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
            elif 30 < chance <= 50:
                score = self.make_draw(2, first_team, second_team)
                return score
            else:
                goals = 1
                second_team.goals += goals
                first_team.goals_conceded += goals
                score = (0, goals)
                return score

        if -10 < difference < -5:
            if chance <= 15:
                dice = randint(1, 10)
                if dice <= 5:
                    goals = 1
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                elif 5 <= dice <= 8:
                    goals = 2
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                else:
                    goals = 3
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
            elif 15 < chance <= 30:
                score = self.make_draw(2, first_team, second_team)
                return score
            else:
                goals = 1
                second_team.goals += goals
                first_team.goals_conceded += goals
                score = (0, goals)
                return score

        if difference <= -10:
            if chance <= 8:
                dice = randint(1, 10)
                if dice <= 4:
                    goals = 1
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                elif 5 <= dice <= 7:
                    goals = 2
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                elif 8 <= dice <= 9:
                    goals = 3
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
                else:
                    goals = 4
                    second_team.goals += goals
                    first_team.goals_conceded += goals
                    score = (0, goals)
                    return score
            elif 8 < chance <= 15:
                score = self.make_draw(1, first_team, second_team)
                return score
            else:
                goals = 1
                second_team.goals += goals
                first_team.goals_conceded += goals
                score = (0, goals)
                return score

    def result(self, result, first_team, second_team):
        if result[0] > result[1]:
            first_team.wins += 1
            second_team.lost += 1
            first_team.score += 3
            return f'{first_team.name:<20} {result[0]} : {result[1]} {second_team.name:>20}'
        elif result[0] == result[1]:
            first_team.score += 1
            second_team.score += 1
            first_team.draws += 1
            second_team.draws += 1
            return f'{first_team.name:<20} {result[0]} : {result[1]} {second_team.name:>20}'
        elif result[0] < result[1]:
            second_team.score += 3
            first_team.lost += 1
            second_team.wins += 1
            return f'{first_team.name:<20} {result[0]} : {result[1]} {second_team.name:>20}'

    def match(self, first_team, second_team):

        if 2 >= first_team.rating - second_team.rating >= -2:
            difference = first_team.rating - second_team.rating
            result = self.chance_of_match(difference, first_team, second_team)
            return self.result(result, first_team, second_team)

        elif first_team.rating > second_team.rating:
            difference = first_team.rating - second_team.rating
            result = self.chance_of_match(difference, first_team, second_team)
            return self.result(result, first_team, second_team)

        elif first_team.rating < second_team.rating:
            difference = first_team.rating - second_team.rating
            result = self.chance_of_match(difference, first_team, second_team)
            return self.result(result, first_team, second_team)

    def matches(self):
        fixtures = self.fixtures()
        print(f'{"Tour 1":*^46}')
        for i in range(1, 39):
            print("\n", " " * 18, "Tour {}".format(i))
            for fixture in fixtures[i-1]:
                print(self.match(fixture[0], fixture[1]))
            if i == 19:
                self.print_table()
        self.print_table()

    def fixtures(self):
        fixtures = []
        for i in range(38):
            fixture = []
            clubs = self.clubs
            shuffle(clubs)
            j = 0
            for club in clubs:
                if j % 2 == 0:
                    prev_club = club
                else:
                    fixture.append([prev_club, club])
                j += 1
            fixtures.append(fixture)
        return fixtures


class Club:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.score = 0
        self.goals = 0
        self.goals_conceded = 0
        self.wins = 0
        self.draws = 0
        self.lost = 0

    def __str__(self):
        return f"{self.name}, рейтинг: {self.rating}, очки: {self.score}"

    def __format__(self, fmt):
        return str(self).__format__(fmt)


epl = League()

arsenal = Club(name='Arsenal', rating=82)
epl.add(arsenal)
aston_villa = Club(name='Aston Villa', rating=75)
epl.add(aston_villa)
bournemouth = Club(name='Bournemouth', rating=76)
epl.add(bournemouth)
brighton = Club(name='Brighton', rating=76)
epl.add(brighton)
burnley = Club(name='Burnley', rating=77)
epl.add(burnley)
chelsea = Club(name='Chelsea', rating=82)
epl.add(chelsea)
crystal_palace = Club(name='Crystal Palace', rating=77)
epl.add(crystal_palace)
everton = Club(name='Everton', rating=79)
epl.add(everton)
leicester_city = Club(name='Leicester City', rating=79)
epl.add(leicester_city)
liverpool = Club(name='Liverpool', rating=85)
epl.add(liverpool)
manchester_united = Club(name='Manchester United', rating=83)
epl.add(manchester_united)
manchester_city = Club(name='Manchester City', rating=85)
epl.add(manchester_city)
newcastle_united = Club(name='Newcastle United', rating=76)
epl.add(newcastle_united)
norwich_city = Club(name='Norwich City', rating=74)
epl.add(norwich_city)
sheffield_united = Club(name='Sheffield United', rating=73)
epl.add(sheffield_united)
southampton = Club(name='Southampton', rating=77)
epl.add(southampton)
tottenham = Club(name='Tottenham', rating=84)
epl.add(tottenham)
watford = Club(name='Watford', rating=77)
epl.add(watford)
west_ham_united = Club(name='West Ham United', rating=78)
epl.add(west_ham_united)
wolverhampton = Club(name='Wolverhampton', rating=80)
epl.add(wolverhampton)

epl.matches()
