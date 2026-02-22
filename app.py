from save_to_csv import write_summary
from argparsing import parse_args
from aggregation import aggregate

def main():
    args = parse_args()

    summary = aggregate(args)

    write_summary(args, summary)

if __name__ == "__main__":
    main()