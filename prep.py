import shlex
import sys
import re # regular expressions
import argparse
from collections import Counter

def lowercase(inFile, outFile):
  print("Lowercasing %s to %s" % (inFile, outFile))
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      o.write(f.read().lower())

def removePunct(inFile, outFile):
  print("Removing punctuation from %s to %s" % (inFile, outFile))
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      inString = f.read()
      rmContractions = re.sub(r"n[^\w\s]t", "nt", inString) # remove contractions eg. don't, won't
      rmPunct = re.sub(r"[^\w\s]", " ", rmContractions) # remove remaining non word & non space characters
      o.write(rmPunct)

# also removes extra white spaces and newlines
def removeStopwords(inFile, outFile):
  print("Removing stop words from %s to %s" % (inFile, outFile))
  # some of the more common stopwords in the Bible ("s" is a left over after removing possession apostrophes)
  stop_words = set(["s", "and", "the", "of", "that", "to", "in", "for", "a", "be", "is", "with", "it", "was", "as", "are", "were", "an", "at"])
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      words = f.read().split()
      filtered_words = [word for word in words if word.lower() not in stop_words]
      o.write(" ".join(filtered_words))

def removeChaptHeadings(inFile, outFile):
  print("Removing chapter headings from %s to %s" % (inFile, outFile))
  with open(inFile, "r") as f:
    with open(outFile, "w") as o:
      o.write(re.sub(r"\n\n[^\n]+\n[^\n]+\n\n", "\n", f.read()))

def word_frequency(inFile):
    with open(inFile, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        frequency = Counter(words)
        return frequency.most_common()


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

  stopwordParser = subparsers.add_parser('rmStopwords', help='remove stop words')
  stopwordParser.add_argument("-i", "--input", required=True, help="input file")
  stopwordParser.add_argument("-o", "--output", required=True, help="output file")

  chaptheadingParser = subparsers.add_parser('rmChaptHeadings', help='remove chapter headings')
  chaptheadingParser.add_argument("-i", "--input", required=True, help="input file")
  chaptheadingParser.add_argument("-o", "--output", required=True, help="output file")

  wordFreqParser = subparsers.add_parser('wordFreq', help='get word frequency')
  wordFreqParser.add_argument("-i", "--input", required=True, help="input file")

  parser.print_help()

  args = parser.parse_args()

  if(args.operation == "toLower"):
    lowercase(args.input, args.output)

  if(args.operation == "rmPunct"):
    removePunct(args.input, args.output)

  if(args.operation == "rmStopwords"):
    removeStopwords(args.input, args.output)

  if(args.operation == "rmChaptHeadings"):
    removeChaptHeadings(args.input, args.output)

  if(args.operation == "wordFreq"):
    print(word_frequency(args.input))

  return 0

if __name__ == "__main__":
  sys.exit(main())


