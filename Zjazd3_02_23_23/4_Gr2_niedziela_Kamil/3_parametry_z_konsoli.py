import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

print('Nazwa pliku to: ',args.filename)