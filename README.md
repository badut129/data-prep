# data-prep

Source the virtual environment  

    . ./venv/bin/activate

Remove chapter headings  

    python rmChaptHeadings -i brb-noheader.txt -o 00-noChapts.txt

Remove punctuation  

    python rmPunct -i 00-noChapts.txt -o 01-noPunct.txt

Remove Stopwords  

    python rmStopwords -i 01-noPunct.txt -o 02-noStopwords.txt

To lower case

    python toLower -i 02-noStopwords.txt -o 03-lowerCase.txt

Print word frequency

    python wordFreq -i 03-lowerCase.txt
