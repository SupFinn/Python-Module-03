#!/usr/bin/python3

import sys


def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        try:
            score_list = []
            for score in sys.argv[1:]:
                score_list.append(int(score))
        except ValueError:
            print(
                "Oops! One of the scores is not a "
                "number. Cheating detected! 🚫"
                )
        else:
            print(f"Scores processed: {score_list}")
            print(f"Total players: {len(score_list)}")
            print(f"Total score: {sum(score_list)}")
            print(f"Average score: {sum(score_list) / len(score_list)}")
            print(f"High score: {max(score_list)}")
            print(f"Low score: {min(score_list)}")
            print(f"Score range: {max(score_list) - min(score_list)}")


if __name__ == "__main__":
    main()
