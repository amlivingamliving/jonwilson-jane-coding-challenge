#!/usr/bin/python3

import argparse
import logging
from soccer_game_logic.main import Results, Input, Match

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SoccerMatchResults")


def main():
    results = Results()
    matches = Input(args.filename)
    for match in matches:
        points = Match(match).match_result
        results(points)
    else:
        results.print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename", "-f", help="Input Filename to be Processed", required=True
    )
    args = parser.parse_args()
    logger.info(f"Calculating Results for {args.filename}")
    main()
