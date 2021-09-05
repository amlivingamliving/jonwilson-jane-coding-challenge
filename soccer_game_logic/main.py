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