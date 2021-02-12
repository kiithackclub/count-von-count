def readFile():
    f = open('count.txt','r')
    m = int(f.read().strip())
    f.close()
    return m

def writeFile(message):
    f = open('count.txt', 'w')
    f.write(message)
    f.close()
