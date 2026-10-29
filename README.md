¿Qué problema resuelve el script?

Este script es un analizador de logs hecho en python, que detecta y ordena ips maliciosas, hace uso de un archivo (un access.log) para analizarlo


¿Cómo se ejecuta?

Se ejecuta con el archivo access.log añadido


¿Qué salida produce? 


Ejemplo: 


10.0.0.7 [DANGER] --> 8 tries


192.168.1.15 [DANGER] --> 5 tries


203.0.113.42 --> 3 tries


198.51.100.9 --> 2 tries


192.168.1.20 --> 1 tries


Ignored lines: 2


¿Qué formato de log espera?


2026-10-29 08:14:09 FAILED_LOGIN user=root ip=10.0.0.7


¿Qué no hace todavía?

Los pasos 5 y 7, estos eran los objetivos a cumplir

1.El script lee access.log y solo cuenta las líneas FAILED_LOGIN.

2.Cuenta cuántos intentos fallidos tiene cada IP.

3.Muestra el resultado ordenado de más a menos intentos.

4.Marca como [ALERTA] cualquier IP con 5 o más intentos fallidos.

5.Si el archivo no existe, el script muestra un mensaje claro y no se rompe con un traceback.

6.Si una línea está mal formada (le falta la IP, por ejemplo), la salta y sigue. Al final indica cuántas líneas se saltaron.

7.Las funciones deben tener una sola responsabilidad (por ejemplo, una para leer, otra para extraer la IP, otra para mostrar).


