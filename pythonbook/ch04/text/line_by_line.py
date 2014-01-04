import sys, re

def adjust_newline(text):
    tmp = text
    tmp = re.sub(r'([a-z,])\n[ ]*([A-Za-z*(])', r'\1 \2', tmp)
    tmp = re.sub(r'([a-z][.?]) ([A-Z*])', r'\1\n\2', tmp)
    result = tmp
    return result
	
def usage():
    print('Usage: python line_by_line.py <path>')

if len(sys.argv) == 2:
    path = sys.argv[1]
    	
    infile = open(path)
    src = infile.read()
    infile.close()

    dest = adjust_newline(src)
    
    outfile = open(path + '.out', 'w')
    outfile.write(dest)
    outfile.close()
else:
    usage()
