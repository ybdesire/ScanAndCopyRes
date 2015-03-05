import os
import shutil

repoDir = "E:\\WebApp\\feature-l10n\\app\\"
dstDir = "E:\\WebApp\\feature-l10n\\enRes\\"
#dstLng = ['en', 'de', 'es', 'fr', 'ja', 'ko', 'zh-CN', 'nl', 'ru', 'pt-BR']
dstLng = ['en']
#resType = ['.json']
resType = ['.json', '.resx']

def main():
    isENResProcess = False
    if 'en' in dstLng:
        isENResProcess = True
    else:
        isENResProcess = False
    fileCounts = 0
    #scan and copy resource files to dstDir
    for root,dirs,files in os.walk(repoDir):
        for fileName in files:
            if os.path.splitext(fileName)[1] in resType:
                resFilePath = root + '\\' + fileName
                if(isValidResFile(fileName)):
                    fileCounts = fileCounts + 1
                    copyFileToDst(resFilePath)
                    print(fileName)

    #print result
    print( '\ncopied files: ' + str(fileCounts) )

#copy file to dstDir by keeping source directory structure
def copyFileToDst(filePath):
    basePath = repoDir
    baseFilePath = os.path.relpath(filePath, repoDir)
    baseDir = os.path.dirname(baseFilePath)
    dstWithBaseDir = dstDir + baseDir
    dstWithBaseFilePath = dstDir + baseFilePath
    if(os.path.exists(dstWithBaseDir)== False):
        os.makedirs(dstWithBaseDir)
    shutil.copyfile(filePath, dstWithBaseFilePath)
    #print(os.path.dirname(baseFilePath))

def isValidResFile(fileName):
    if(os.path.splitext(fileName)[1]=='.json'):#json file are sth like en.json/es.json
        if(os.path.splitext(fileName)[0] in dstLng):
            return True
    elif(os.path.splitext(fileName)[1]=='.resx'):
        if(os.path.splitext(os.path.splitext(fileName)[0])[1] in dstLng):#for non-en resource file such as index.es.resx
            return True
        elif(os.path.splitext(os.path.splitext(fileName)[0])[1] == ''):#for en resource file such as index.resx
            return True
    else:
        return False

def test():
    filePath = 'E:\\WebApp\\feature-l10n\\app\\_App\\Admin\\locales\\es.json'
    copyFileToDst(filePath)

if __name__=='__main__':
    main()
