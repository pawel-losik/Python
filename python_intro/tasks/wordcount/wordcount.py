import sys


def print_count(fname):
    '''
    Prints one per line '<word> <count>' sorted by word for the given file
    '''
    # !!!Your code here!!!
    file = open(fname)
    wordcount = {}
 
    for word in file.read().split():
        word = word.lower()
        word = word.strip().strip("'").strip('"').strip('.').strip(',').strip('!').strip(';').strip('?').strip('!').strip('-').strip('>').strip(';').strip(':').strip('(').strip(')').strip('--')
        if word not in wordcount:
            wordcount[word] = 1
	else:
	    wordcount[word] += 1
    for k,v in wordcount.items():
	#print (word,wordcount)
	print k, v

    

def print_top(fname):
    '''
    Prints the top count listing for the given file
    '''
    # !!!Your code here!!!

    file = open(fname)
    wordcount = {}
    wordlist = []

    for word in file.read().split():
	word = word.lower()
        word = word.strip().strip("'").strip('"').strip('.').strip(',').strip('!').strip(';').strip('?').strip('!').strip('-').strip('>').strip(';').strip(':').strip('(').strip(')').strip('--')
        if word not in wordcount:
            wordcount[word] = 1
	else:
	    wordcount[word] += 1
    wordsort = sorted(wordcount.items(),key = lambda x :x[1]) 
    i = 1
    while (i <= 20):  
        print wordsort[-i]
        i =i + 1



def main():
    if len(sys.argv) != 3:
        print 'Usage: ./wordcount.py {--count | --top} <file name>'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
