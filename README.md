# 2023 GetBrit! - calculadoraDNI

Ejercicio de clase checksum: calculadora de letra DNI

## Calculadora de DNI en Python

Esta es una calculadora simple en Python que te permitirá obtener la letra del Documento Nacional de Identidad (DNI) español a partir de un número de DNI proporcionado. El número de DNI se utilizará para determinar la letra correspondiente siguiendo el algoritmo establecido por las autoridades.

¿Cómo se obtiene la letra del NIF?
[fuente](https://masquenomina.es/recursos-humanos-rrhh/calcular-letra-del-nif/)

Es el resultado de aplicar un algoritmo (que palabra tan de moda) que se conoce como módulo 23. Este algoritmo da como resultado un número que, en la tabla siguiente, podemos ver a qué letra equivale.

El algoritmo hace lo siguiente: se divide el número entero del DNI entre 23. Cogemos el resultado sin decimales y lo volvemos a multiplicar por 23.

Y a lo obtenido se resta del número del dni. El resto será siempre un número comprendido entre 0 y 22 y buscaremos la equivalencia en letras establecida por la Agencia Tributaria.

**Un ejemplo:**

09408901

9408901 / 23 = 409082,65

Nos quedamos con 409082 *23 = 9408886

Diferencia 9408901 – 9408886 = 15….    Buscamos y ..  es la “S”

    Resto 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
    Letra T R W A G M Y F P D X B N J Z S Q V H L C K E
