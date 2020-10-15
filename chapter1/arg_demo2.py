# arg_demo2.py

import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    # version 1.0
    # parser.add_argument('-x', '--execute', action="store", required=True,
    #                    help='Help text for option X')
    # parser.add_argument('-y', help='Help text for option Y', default=False)
    # parser.add_argument('-z', help='Help text for option Z', type=int)

    # version 2.0
    #require argument
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store",
                       help='Help text for option X')
    group.add_argument('-y', help='Help text for option Y', default=False)

    # optional arguments
    parser.add_argument('-z', help='Help text for option Z', type=int)

    print(parser.parse_args())

if __name__ == '__main__':
    get_args()