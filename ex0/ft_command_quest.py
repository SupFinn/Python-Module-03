import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    args_len = len(sys.argv)
    if args_len == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {args_len}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {args_len - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {args_len}")
