#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="The input file", type=str)
parser.add_argument("-o", "--output", help="Output the result" + \
                    "to a file", type=str)
                    #"to a file", action="store_true", type=str)
args = parser.parse_args()

with open(args.file_name, 'r') as file:
    data = file.read().replace('\n', ' ').replace('.', '.\n').replace('?', '?\n').replace('\n ', '\n')

if args.output:
    output_filename = args.output
else:
    output_filename = "output"
output_file = open(output_filename, "w")
output_file.write(data)

print("Result outputted to " + output_filename)
