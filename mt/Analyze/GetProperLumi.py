import os

DIR=[
     'EmbeddingRun2016B-v2',
     'EmbeddingRun2016C-v2',
     'EmbeddingRun2016D-v2',
     'EmbeddingRun2016E-v2',
     'EmbeddingRun2016F-v2',
     'EmbeddingRun2016G-v2',
     ]

for dataset in DIR:
    os.system("ls -d %s/submit/*/*.err  > AllList.txt"%dataset)

    print 'now is process %s'% dataset
    AllList=open('AllList.txt','r')
    search_word = "Successfully"
    TotalSuccess=0
    TotalFail=0
    for errFile in AllList.readlines():
        if search_word in open(errFile.replace('\n','')).read():
            xmlFile=open(errFile.replace('err','xml').replace('\n',''),'r')
            for line in xmlFile.readlines():
                if '<Branch Name="EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_MERGE." ReadCount=' in line:
                    Eve= int(line.replace('<Branch Name="EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_MERGE." ReadCount="','').replace('" />',''))
                    Total +=Eve

        else:
            xmlFile=open(errFile.replace('err','xml').replace('\n',''),'r')
                for line in xmlFile.readlines():
                    if '<Branch Name="EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_MERGE." ReadCount=' in line:
                        Eve= int(line.replace('<Branch Name="EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_MERGE." ReadCount="','').replace('" />',''))
                            TotalFail +=Eve

    print 'datatse is %s and TotalNumber of events is %d'%(dataset,TotalSuccess,TotalFail)


