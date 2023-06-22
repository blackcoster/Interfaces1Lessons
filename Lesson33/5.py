import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()
if args.name == 'полина':
    print('здравствуйте хозяин')
else:
    print("я вас не знаю")
