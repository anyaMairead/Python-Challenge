import zipfile
import re
import os

file = zipfile.ZipFile("channel.zip", "r")
nothing = '90025'
fileList = []

fileList.append(nothing)
text = file.read(nothing + '.txt')

#path = 'channel/'
#listing = os.listdir(path)
#def print_info('channel.zip')
#    zf = zipfile.ZipFile('channel.zip')
#    for info in zf.infolist:
#        print info.comment


#print file.infolist()
#def print_info(archive_name):
#    zf = zipfile.ZipFile(archive_name)
#    for info in zf.infolist():
        #print info.filename
#        print ''.join(info.comment)

#if __name__ == '__main__':
#    print_info('channel.zip')

#nothing = 'channel/90052.txt'
#for i in range(910):
#    f = open(nothing)
    #output = f
#    print_info(archive_name)
#    nothing = 'channel/' + re.search(r'\d+', output).group(0) + '.txt'
    
#for name in file.namelist():
#    data = file.read(namre.search(r'\d+', s).group(0)e)
#    print data
    

    
