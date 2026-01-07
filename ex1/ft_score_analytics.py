#!/usr/bin/python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            score_list = []
            for score in sys.argv[1:]:
                score_list.append(int(score))
        except ValueError:
            print(f"Oops! One of the scores is not a number. Cheating detected! 🚫")
        else:
            score_len = len(score_list)
            score_sum = sum(score_list)
            score_max = max(score_list)
            score_min = min(score_list)
            score_range = score_max - score_min
            print(f"Scores processed: {score_list}")
            print(f"Total players: {score_len}")
            print(f"Total score: {score_sum}")
            print(f"Average score: {score_sum / score_len}")
            print(f"High score: {score_max}")
            print(f"Low score: {score_min}")
            print(f"Score range: {score_range}")
