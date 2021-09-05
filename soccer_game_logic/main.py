import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SoccerMatchResults")


class Input:
    def __init__(self, input_file):
        logger.debug(f"Processing file:{input_file}")
        self.input_file = input_file

    def __iter__(self):
        with open(self.input_file, "r") as f:
            yield from f.readlines()


class Match:
    def __init__(self, raw_match_data):
        logger.debug(f"Raw Match Data: {raw_match_data}")
        self.raw_match_data = raw_match_data
        self.match_data = self.parse_raw_match_data()
        logger.debug(f"Processed Match Date: {self.match_data}")

    def parse_raw_match_data(self):
        return {
            x.strip()[: x.strip().rfind(" ")]: int(x.strip()[x.strip().rfind(" ") + 1])
            for x in self.raw_match_data.strip().split(",")
        }

    @property
    def match_result(self):
        scores = set(self.match_data.values())
        if len(scores) == 1:
            return {team: 1 for team in self.match_data}

        return {
            team: (score == max(scores)) * 3 for team, score in self.match_data.items()
        }


class MatchDay:
    def __init__(self):
        self.day = {}

    def __iter__(self):
        yield from self.day.items()

    def new_day(self, match):
        return any(team in self.day for team in match)

    def __call__(self, match):
        self.day.update(match)
        return self.day
