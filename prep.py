import shlex
import sys
import re # regular expressions
import argparse

def lowercase(inFile, outFile):
  print("Lowercasing %s to %s" % (inFile, outFile))
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      o.write(f.read().lower())

def removePunct(inFile, outFile):
  print("Removing punctuation from %s to %s" % (inFile, outFile))
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      o.write(re.sub(r"[^\w\s]", "", f.read()))

def main() -> int:
  args = shlex.join(sys.argv)
  print(args)
  parser = argparse.ArgumentParser(prog='prep.py',
                    description='Prepares BSB text for vectorization',
                    epilog='END')
  subparsers = parser.add_subparsers(dest='operation', required=True, help='Operation to perform')

  caseParser = subparsers.add_parser('toLower', help='lowercase')
  caseParser.add_argument("-i", "--input", required=True, help="input file")
  caseParser.add_argument("-o", "--output", required=True, help="output file")

  punctParser = subparsers.add_parser('rmPunct', help='remove punctuation')
  punctParser.add_argument("-i", "--input", required=True, help="input file")
  punctParser.add_argument("-o", "--output", required=True, help="output file")

  parser.print_help()

  args = parser.parse_args()

  if(args.operation == "toLower"):
    lowercase(args.input, args.output)

  if(args.operation == "rmPunct"):
    removePunct(args.input, args.output)

  return 0

if __name__ == "__main__":
  sys.exit(main())


