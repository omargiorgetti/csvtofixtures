import csv
import json

out_file = open("Comune.json","w")
with open('comuni.csv', 'r') as csvfile:
    file = csv.reader(csvfile, delimiter='|', quotechar=' ')
    model="GestioneRiferimenti.Comune"
    l=list(enumerate(file))
    
    for i,row in l:
        j=json.dumps({'model':model,'pk':(row[0]), \
                      'fields':{'descrizione':(row[1]),\
                                'codComune':(row[2]),\
                                'codProvincia':(row[3]),\
                                'codRegione':(row[4]),\
                                'codIstat':(row[5]),\
                                'regione':(row[6]),\
                                'provincia':(row[7]),\
                                'popolazione':(row[8]),\
                                'riparGeo':(row[9]),\
                                'CodRipartGeo':(row[10]),\
                                'capoluogo':(row[11])}}, indent=4)
        if i==0:
            out_file.write("[ ")
            out_file.write(j+",")
            
        elif i==len(l)-1:
            out_file.write(j)
            out_file.write("]")
        else:        
            out_file.write(j+",")
 
out_file.close()        
