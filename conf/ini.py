# create ini file for app
from os import path

inifile = 'conf.ini'

createFile = open(inifile,'w')


def textFile():
    tt = '''
    [DATABASE]
    type = 'mysql'
    port = 3306
    name = 'HR'
    pass = 'password'
    '''
    return tt

if createFile.writable():
    createFile.write(textFile())
    createFile.close()
else:
    print('Cannot open or write file: %s' % inifile)

