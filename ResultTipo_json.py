import csv
import json

tipo='Tipo.json'

ente = open("result.json","w")

def getclass (classfile,descr):
    with open(classfile) as json_data:
        d = json.load(json_data)
        ris={}
        for value in d:
            a=value['fields']
            ris[value['pk']]=a['descr']
        key = next((key for key,value in ris.items() if value.upper()==descr.upper()),'')
        return key

def CreateResult(model):
    for i,row in l:
        #print '#'.join(row)
        print i
        gettipo=getclass(tipo,row[1])
        
        j=json.dumps({'model':model,\
                      'pk':(row[0]),\
                      'fields':{
                                'tipo': (None if gettipo=="" else getente),\
				'descr':(row[2]),\
                                }
                      }, indent=4)  
        
        if i==0:
            ente.write("[ ")
            ente.write(j+",")
            
        elif i==len(l)-1:
            ente.write(j)
            ente.write("]")
        else:        
            ente.write(j+",")
    ente.close()
  
with open('result.csv', 'r') as csvfile:
    file = csv.reader(csvfile, delimiter='|', quotechar=' ')
    CreateResult("Result")
    

    
    
        
