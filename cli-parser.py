"""
 Parsowanie parametrów linii poleceń
"""
import sys
from argparse import ArgumentParser
#print(sys.argv)

parser = ArgumentParser()
parser.add_argument("-n", "--name",
                    required=True, help="file name", metavar="FILENAME")
parser.add_argument("-d", type=int, default=2, metavar="2", help="number")
parser.add_argument("-f", "--folder", nargs="+", default=".", type=str)
parser.add_argument("-t", type=float, default=10.)
parser.add_argument("-v","--verbose", action="store_true")

arguments = parser.parse_args()
print(arguments.name)
print(arguments.d)
print(arguments.t)
print(arguments.folder)
print(arguments.verbose)
