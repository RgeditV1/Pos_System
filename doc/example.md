# Guia Rapida de UI

Este documento explica la estructura de archivos de interfaz del proyecto.

## Estructura

- `*.ui`: archivo editable en Qt Designer.
- `*_ui.py`: archivo generado desde el `.ui`. No se recomienda editarlo manualmente.
- `*_view.py`: capa donde se conecta la logica, señales, validaciones y ajustes de widgets.

## Flujo recomendado

1. Edita el diseño en el archivo `.ui`.
2. Regenera `*_ui.py` cuando hagas cambios visuales.
3. Implementa o ajusta comportamiento en `*_view.py`.

## Nota

Si editas `*_ui.py` manualmente, esos cambios pueden perderse al regenerarlo.
