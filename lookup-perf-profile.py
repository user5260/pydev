#!/usr/bin/env python3
'''
PERFORMANCE PROFILE - lookup; python3.x script
----------------------------------------------
Added a call to "cProfile.run()" to my "lookup"
script. This script connects to the internet
and retrieves a web page based on user input.

The same desired effects can be achieved by
calling the "cProfile" as a module from the
command line.

$> python3 -m cProfile <script_path> <args> <...>

Probably do ^this^ from now on.
'''
from bs4 import BeautifulSoup
import requests,sys,cProfile

def main():
    # Print usage if no words/args.
    if len(sys.argv) == 1:
        print('USAGE:\n$> lookup <word1> <word2> <...>')
    # Request URL and soupify. Print Definition(s).
    elif len(sys.argv) > 1:
        # Loop through cmdline args.
        iterCount = 1
        while iterCount < len(sys.argv):
            # Request web page; pass contents to bs4.
            lookupWord = sys.argv[iterCount]
            webAddr = 'https://www.merriam-webster.com/dictionary/'+lookupWord+'/'
            # Handle exception in case of no internet connection.
            # socket.gaierror (get address info error); name resolution failure.
            # Presumably, the first thing these modules try to do is resolve
            # the domain name through the dns. Raises an exception.
            try:
                req = requests.get(webAddr)
            except Exception:
                print('An error has occurred while trying to establish a connection with the internet.')
                break
            # Soupify; create soup object & designate the python built-in html parser.
            soup = BeautifulSoup(req.text,'html.parser')
            # Create list of CSS class attributes
            # Tag is <span class="dtText"><\span>
            resultList = soup.select('.dtText')
            # Print the word & its definition(s).
            entryNum = 1
            print('*',lookupWord.upper(),sep='')
            if len(resultList) == 0:
                print('No dictionary entries found.')
            else:
                for r in resultList:
                    print(entryNum,r.getText())
                    entryNum += 1
            iterCount += 1
        
    print('\nPowered by Merriam-Webster.com\nAuthored by brianc2788@gmail.com')

if __name__ == '__main__':
    cProfile.run('main()')
