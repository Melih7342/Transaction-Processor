import argparse, os

def parse_args() -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-u', '--user', help='Filter specific user(s) by UID', required=False, nargs='+')
    arg_parser.add_argument('-d', '--delimiter', help='Define custom delimiter',required=False, default=',')
    arg_parser.add_argument('-w', '--withdraw', help='Filter only withdrawing transactions', action='store_true' ,required=False)
    arg_parser.add_argument('-dp', '--deposit', help='Filter only deposit transactions', action='store_true' ,required=False)
    arg_parser.add_argument('-i', '--input', help="Provide an input CSV-file", required=True)
    arg_parser.add_argument('-o', '--output', help="Provide an output filename", required=False, default='summary.csv')
    arg_parser.add_argument('-v', '--verbose', help='Verbose output', required=False, action='store_true')
    arg_parser.add_argument('-c', '--currency', help='Filter transactions by currency', required=False, default='USD')


    args = arg_parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: The file '{args.input}' was not found")
        exit(1)

    return args
