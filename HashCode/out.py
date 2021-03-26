def datos(interseccion):
     calles = interseccion.calles 
     n = len(calles) 
     identidad = interseccion.id 
     info = identidad + '\n' + n + '\n' 
     for calle in calles: 
         nombre, tiempo = calle[0], calle[1] 
         info += nombre + " " + tiempo + '\n' 
     return info 
         
final = open('final.txt', 'w') 
n = len(intersecciones) 
final.write('{0}'.format('n')) 
outfile.write('\n') 
for interseccion in intersecciones: 
    info = datos(interseccion) 
    final.write(info) 
    outfile.write('\n') 
final.close() 