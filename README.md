# Prácticas de programación en Python

Ejercicios académicos de Programación I de la Tecnicatura en Programación de la UTN. Aplican estructuras secuenciales, condicionales y repetitivas mediante programas interactivos de consola.

## Contenido

| Ejercicio | Qué permite practicar |
| --- | --- |
| Caja del kiosco | Carga de productos, descuentos, acumuladores y cálculo de totales |
| Acceso al campus y menú seguro | Validación de credenciales, límite de intentos y opciones de menú |
| Agenda de turnos | Reserva, cancelación y consulta de turnos mediante condicionales y ciclos |

## Cómo ejecutarlo

Requiere Python 3, sin dependencias externas.

```bash
git clone https://github.com/lucianoacq/UTN-TUPaDProgramacion1.git
cd UTN-TUPaDProgramacion1
python "TP integrador – Repetitivas- Condicionales y Secuenciales.py"
```

Los ejercicios están en un único archivo y se ejecutan uno después de otro. Al terminar la caja del kiosco comienza el acceso al campus; después, la agenda de turnos. En algunos sistemas el comando de Python es `python3`.

Para el ejercicio del campus se usan las credenciales ficticias `alumno` / `python123`. No corresponden a ninguna cuenta real.

## Conceptos trabajados

- Variables y conversión de tipos.
- Operadores y estructuras `if`, `elif` y `else`.
- Ciclos `for` y `while`.
- Validación de entradas y menús interactivos.
- Acumuladores y formato de resultados.

## Alcance académico

La agenda usa variables individuales en lugar de listas, según la consigna del ejercicio. Los datos se mantienen solo durante la ejecución. El cambio de clave es una práctica de ingreso y validación; no implementa persistencia ni un sistema real de autenticación. Los precios del kiosco se ingresan como enteros positivos.

Autor: Luciano Acquaviva.
