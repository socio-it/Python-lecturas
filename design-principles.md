# Principios de Diseño — App Interactiva

Este documento describe una aplicación React que enseña los **principios fundamentales de diseño de software** mediante una lista interactiva, una barra de progreso metálica y ventanas modales con ejemplos de código.

---

## Estructura de la App

La aplicación muestra una lista de principios de diseño. Cada principio tiene un checkbox y un botón de **Info** que abre un popup con explicaciones y ejemplos.

### Principios incluidos

1. **Encapsulación**  
   Oculta el estado interno y expone una interfaz controlada.
   - **Polimorfismo:** múltiples clases implementan el mismo método y son utilizadas mediante una interfaz común.
   - **Setter & Getter:** controlan el acceso y la validación del estado interno.
   - **Property:** simplifica el uso de getters y setters con una sintaxis de atributo.

   ```python
   class Animal:
       def speak(self):
           raise NotImplementedError

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   pets = [Dog(), Cat()]
   for p in pets:
       print(p.speak())  # mismo método, distinta implementación
   ```

---

2. **Programa contra interfaces, no implementaciones**  
   Reduce el acoplamiento y mejora la flexibilidad.
   - **ABC (Clase Abstracta):** define una interfaz con métodos obligatorios.
   - **Protocol (Estructural):** se centra en el contrato, no en la herencia.

   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

   class Circle(Shape):
       def __init__(self, r):
           self.r = r
       def area(self):
           return 3.14 * self.r * self.r
   ```

---

3. **Composición sobre herencia**  
   Prefiere combinar objetos a crear jerarquías complejas.

   ```python
   class StarBehavior:
       def __init__(self):
           self._starred = False
       def star(self):
           self._starred = True
       def unstar(self):
           self._starred = False
       def is_starred(self):
           return self._starred

   class Document:
       def __init__(self, title, behaviors=None):
           self.title = title
           self.behaviors = behaviors or []

       def __getattr__(self, name):
           for b in self.behaviors:
               if hasattr(b, name):
                   return getattr(b, name)
           raise AttributeError(name)

   doc = Document("spec.md", behaviors=[StarBehavior()])
   doc.star()
   print(doc.is_starred())  # True
   ```

---

4. **Bajo acoplamiento**  
   Los módulos deben depender lo menos posible entre sí.
   - **Inyección de dependencias:** el cliente recibe su dependencia desde fuera.
   - **Patrón Observer:** los objetos observadores reaccionan sin dependencia directa.

   ```python
   class Service:
       def do_work(self):
           return "ok"

   class Client:
       def __init__(self, service: Service):
           self.service = service
       def operate(self):
           return self.service.do_work()

   svc = Service()
   cli = Client(svc)
   print(cli.operate())
   ```

---

## Elementos visuales

### Barra metálica de progreso
- Representa el número de principios seleccionados.  
- Usa un degradado metálico de fondo con una barra dorada que avanza al marcar elementos.

### Modal de información
- Cada principio tiene un modal con pestañas (tabs).  
- Las pestañas permiten cambiar entre las diferentes opciones (por ejemplo, ABC vs Protocol).

---

## Tests incluidos

La app ejecuta tres pruebas automáticas:
1. Que existan exactamente **4 principios**.  
2. Que cada principio tenga **al menos una opción**.  
3. Que los principios contengan las **opciones requeridas** (e.g., *polymorphism*, *setter_getter*, *property* para Encapsulación).

---

## Resumen técnico

- Desarrollada en **React + TypeScript (TSX)**.  
- Usa solo **estilos inline**, sin dependencias externas.  
- Compatible con **Next.js** o cualquier entorno React estándar.

---

¿Quieres que este markdown conserve los bloques de código funcionales (como demostración didáctica) o los simplifico a pseudocódigo con explicaciones resumidas?
