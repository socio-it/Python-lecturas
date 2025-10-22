#Tipos de Dict en python 
#dict: general usos, una de sus particularidades es que su key deben ser hasables
json = { 'firt-node':
        {'name': 'node-name',
         'colour':'green',
         'descripcion': 'na'
         }}
for value in json.values():
    print({'desestrucutrar':'con **', **value})
    print(value)

#defaultDict: No lanza un error cuando la key no existe sino crea un objeto que deseemos crear
import collections
import re
positionWords = collections.defaultdict(list) # en este caso si la key no existia le crearemos una lista vacia

text = """El Corazón Versátil de Python: Explorando los Diccionarios y sus Parientes
En el ecosistema de Python, pocas estructuras de datos son tan fundamentales y omnipresentes como el diccionario, conocido por su tipo dict. Representando una colección no ordenada (aunque preserva el orden de inserción desde Python 3.7+) de pares clave-valor, el diccionario es la navaja suiza para manejar datos estructurados de manera eficiente y legible. Su concepto es simple: a cada clave única, que debe ser un objeto inmutable (como un string, número o tupla), se le asocia un valor, que puede ser cualquier objeto Python. Esta flexibilidad es una de sus mayores fortalezas.
La implementación subyacente de dict se basa en una tabla hash. Esto significa que, en promedio, las operaciones de búsqueda, inserción y eliminación de elementos por clave tienen una complejidad temporal constante, O(1). Esta eficiencia es crucial para el rendimiento en muchas aplicaciones, desde el análisis de datos hasta el desarrollo web. Cuando necesitas buscar rápidamente si un elemento existe o recuperar su valor asociado basándote en un identificador único, el diccionario es a menudo la herramienta ideal. Casos de uso comunes incluyen la representación de objetos JSON, el almacenamiento de configuraciones de aplicaciones, el conteo de frecuencias (aunque Counter es más especializado), o incluso simular estructuras de datos más complejas.
Antes de Python 3.7, si el orden en que se añadían los elementos era crucial, los desarrolladores recurrían a collections.OrderedDict. Esta subclase de dict mantenía explícitamente el orden de inserción usando una estructura interna adicional. Aunque la necesidad primordial de OrderedDict ha disminuido con las mejoras en dict, todavía ofrece funcionalidades específicas relacionadas con el orden, como move_to_end(), y garantiza el comportamiento ordenado en todas las versiones de Python 3, lo que puede ser importante para la compatibilidad o en algoritmos específicos como cachés LRU (Least Recently Used).
El módulo collections enriquece aún más el panorama de los mapeos. Cuando necesitamos manejar claves que podrían no existir sin escribir constantemente bloques if key in my_dict:, collections.defaultdict viene al rescate. Al inicializarlo con una función fábrica (como list, int, o set), defaultdict crea automáticamente un valor predeterminado para una clave la primera vez que se accede a ella si no existe, simplificando enormemente tareas como agrupar elementos en listas o acumular contadores.
Para tareas específicas de conteo de frecuencias, collections.Counter es una herramienta poderosa y conveniente. Optimizado para esta tarea, no solo cuenta elementos de manera eficiente a partir de iterables, sino que también ofrece métodos útiles como most_common(n) para encontrar los elementos más frecuentes y soporta operaciones aritméticas entre contadores.
A veces, necesitamos combinar múltiples diccionarios lógicamente, por ejemplo, para manejar configuraciones con valores predeterminados que pueden ser sobrescritos. collections.ChainMap agrupa varios diccionarios en una única vista actualizable. Las búsquedas recorren los diccionarios en orden hasta encontrar la clave, mientras que las escrituras solo afectan al primer diccionario de la cadena, ideal para simular contextos anidados.
Finalmente, cuando la persistencia es necesaria y no queremos la complejidad de una base de datos completa, shelve.Shelf ofrece una interfaz similar a un diccionario pero almacena los datos en archivos en disco. Aunque tiene limitaciones (las claves deben ser strings, los valores deben ser serializables, y es más lento debido al acceso a disco), es útil para guardar estados simples o cachés entre ejecuciones de un script.
En resumen, mientras que el dict incorporado es el caballo de batalla para la mayoría de las necesidades de mapeo en Python gracias a su velocidad y flexibilidad, el ecosistema se complementa con variantes especializadas en el módulo collections y shelve que abordan casos de uso específicos de manera más elegante y eficiente, demostrando la riqueza y adaptabilidad del lenguaje."""

WORD_RE = re.compile(r'\w+')

for match in WORD_RE.finditer(text):
    word = match.group().lower()
    position = match.start() + 1
    positionWords[word].append(position)

print(positionWords)


# OrderedDict: recuerda el orden de llegada, ya no usada ya que dict hace esto en la nueva
# version y ademas este es mas pesado en memoria, sin embargo tiene un metodo llamado move_to_end

#ejemplo cache de logs
import collections
logs = collections.OrderedDict()

def new_log(id, des):
    if len(logs) >= 3:
        key, _ = logs.popitem()
        print(f'DELETE {key}')
    logs[id] = des

def log_solve(id):
    logs.move_to_end(id)

new_log(1,'hacer tarea 1')
new_log(2,'hacer tarea 2')
new_log(3,'hacer tarea 3')
print(logs)
log_solve(1)
new_log(4,'hacer tarea 4')
print(logs)

# chainMap:hace una busqueda de varios dict y regresa las primeras coincidencias ademas solo 
#altera el primer dict que se le da

# ejemplo variables locales y globales
from collections import ChainMap
varsGlobal = {"x":16, "y":16}
varsLocal = varsGlobal.copy()

chain = ChainMap(varsLocal, varsGlobal)
print(chain['x'])
chain['x'] = 15
print(chain['x'])
print(f'vargloblal: {varsGlobal}, varslocal {varsLocal}')

#collection.counter: util para elemento hasables ya que cuenta los datos de manera mas optima
from collections import Counter

print(f"counter de letras = {Counter(text)}")
print(f"counter de letras = {Counter(text).most_common(4)}")

#Shelf: es un componete del modulo shelve, este sirve para guardar informacion persistentemente,
#  su problema es que no se puede ejecutar varias escrituras al mismo tiempo o se corrompe el archivo
from shelve import Shelf