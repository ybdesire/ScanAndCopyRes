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
                fileLocaleName = os.path.splitext(os.path.splitext(fileName)[0])[0]                
                resFilePath = root + '\\' + fileName
                if(isENResProcess and ( (fileLocaleName == '' ) or ( fileLocaleName == 'en' and os.path.splitext(fileName)[1] == '.json'))):#EN resource file
                    print('EN: ' + resFilePath)
                    copyFileToDst(resFilePath)
                    fileCounts = fileCounts + 1
                elif (fileLocaleName in dstLng):#non-EN resource file
                    print('non-EN: ' + resFilePath)
                    copyFileToDst(resFilePath)
                    fileCounts = fileCounts + 1

    #print result
    print( '\ncopied files: ' + str(fileCounts) )

def copyFileToDst(filePath):
    basePath = repoDir
    baseFilePath = os.path.relpath(filePath, repoDir)
    baseDir = os.path.dirname(baseFilePath)
    dstWithBaseDir = dstDir + baseDir
    dstWithBaseFilePath = dstDir + baseFilePath
    if(os.path.exists(dstWithBaseDir)== False):
        os.makedirs(dstWithBaseDir)
    shutil.copyfile(filePath, dstWithBaseFilePath)
    print(os.path.dirname(baseFilePath))

def test():
    filePath = 'E:\\WebApp\\feature-l10n\\app\\_App\\Admin\\locales\\es.json'
    copyFileToDst(filePath)

if __name__=='__main__':
    main()
