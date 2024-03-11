Cabecera
========
Para escribir párrafos solo tenemos que escribir sin marcador especial.

Si queremos remarcar con *cursiva*.

Si queremos remarcar con **negrita**.

Para ejemplos de código hay que usar doble apóstrofe: ``import sys``.

**Especificaciones:**

* No puedo estar anidado.
* El contenido no puede comenzar con un espacio en blanco: * texto* no funciona.
* Tiene que estar separado por caracteres separadores. Se puede usar la barra de escape para permitir unir palabras: Esto\ **es**\ una\ **palabra**.

.. Este es un comentario
.. Hola

---------------------------------------------

.. _Secciones:

Secciones
=========

Subsecciones
------------

Subsecciones
^^^^^^^^^^^^

---------------------------------------------

Los distintos niveles de sección se escriben de la siguiente forma:

* = Para secciones

* `-` Para subsecciones (sin comillas).

* ^ Para subsecciones

* " Para párrafos

---------------------------------------------


LISTAS
^^^^^^

Listas desordenadas
^^^^^^^^^^^^^^^^^^^
**Un ejemplo:**

- Elemento 1
- Elemento 2
- Elemento 3

**Otro ejemplo:**

* Lista simple
* Otro elemento de la lista

 * Con subniveles

    * Otro subniveles
    * Muy facilmente

Listas ordenadas
^^^^^^^^^^^^^^^^
1. Primer elemento
2. Elemento.

 1. Con subnivel
 2. Otro subnivel

ó



- Primer elemento

  - Subelemento 1
  - Subelemento 2
- Segundo elemento

ó

#. Otro tipo de lista
#. Ordenada

-----------------------------------------------

Lista de definiciones
^^^^^^^^^^^^^^^^^^^^^
Término (primera linea de texto)
    Definición del término, que tiene que estar tabulada.

    Puede tener varias líneas o varios párrafos.

   Siguiente término.
    Con su definición.

Bloques literales
^^^^^^^^^^^^^^^^^
Después de un texto normal, podemos dejar un párrafo con un ejemplo de código poniendo doble doble punto(::)::

    def funcion (self):
        print (variable)
        return None

    def otraFuncion:
        print (otraVariable)

El texto continúa normal después del bloque.

Bloques Doctest
^^^^^^^^^^^^^^^

Para los bloques de Doctest no se requiere ninguna marca especial, excepo una tabulación con un espacio:

 >>> 1+1
 2

ó

Para los bloques de Doctest no se requiere ninguna marca especial, excepo una tabulación con un espacio:
 >>> 1+1
 2

Hipervínculos
^^^^^^^^^^^^^
Enlaces externos
````````````````
Podemos consultar la documentación en `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_. usando
el apóstrofe invertido con la palabra-enlace, el enlace entre <> y terminar con " _. ".

El párrafo tiene un enlace a la página del centro `Daniel Castelao`_.

.. _Daniel Castelao: https://www.danielcastelao.org/

Enlaces internos
````````````````
Puedo hacer referencia con una etiqueta colocada antes del título de la sección. Por ejemplo, la sección :ref:`Secciones`.

O así `listas`_.


TABLAS
^^^^^^


+-----------------+-----------------+
| Cabecera 1      | Cabecera 2      |
+=================+=================+
| Celda 1         | Celda 2         |
+-----------------+-----------------+
| Celda 3         | Celda 4         |
+-----------------+-----------------+


+------------------------------+------------+------------+-------------+
| Cabecera 1, fila 0, columna 0| Cabecera 2 | Cabecera 3 |  Cabecera 4 |
+==============================+============+============+=============+
| Contenido 1, fila 1, columna0| Columna 2  | Columna 3  |  Columna 4  |
+------------------------------+------------+------------+-------------+
| Contenido 2, fila 2, columna0| Columna 2  | Columna 3  |  Columna 4  |
+------------------------------+------------+------------+-------------+

**Outra forma:**

======== ========  ========= ======== =========
Lunes    Martes    Miércoles Jueves   Viernes
======== ========  ========= ======== =========
Libre    DI        PMDM      Libre    Libre
Di       Di        PMDM      Libre    Libre
Di       Libre     PMDM      Libre    Libre
Di       Libre     Libre     Libre    Libre
Descanso Descanso  Descanso  Descanso Descanso
SXE      Libre     Libre     Libre    Libre
SXE      Libre     Libre     Libre    Libre
SXE      Libre     Libre     Libre    Libre
======== ========  ========= ======== =========

IMÁGENES (PNG)
^^^^^^^^^^^^^^
Para poner una imagen, se puede hacer de la siguiente forma:

.. image:: _static/check.png
    :width: 200
    :height: 200
    :scale: 50
    :alt: Esta foto se supone que es un check


Notas de pie
^^^^^^^^^^^^



Este texto está realizado con Sphinx [#n1]_ para realizar la documentación:

.. rubric:: Notas

.. [#n1] Podemos encontrar más ionformación en `Sphinx`_.

.. _Sphinx: https://www.sphinx-doc.org


DIRECTIVAS
^^^^^^^^^^
    Las posibilidades de las directivas son:
    Attention, caution, danger, error,
    hint, important, note, tip, warning

.. Danger::
    Cuidado con esto...

.. Attention::
    Fijaos en la estructura...

.. Caution::
    Seguid alerta!

.. Important::
    Prestad atención a esto.

.. tip::
    Este truco es resaltable.





