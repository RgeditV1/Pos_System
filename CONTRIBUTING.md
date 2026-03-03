# Contributing Guide

Gracias por contribuir a `Pos System`.

## Requisitos basicos

- Python 3.12+
- Entorno virtual recomendado
- Dependencias instaladas desde `pyproject.toml` / `uv.lock`

## Como contribuir

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio.
3. Implementa y prueba tu aporte.
4. Abre un Pull Request con una descripcion clara.

## Convenciones de ramas

Ejemplos recomendados:

- `feat/nombre-corto`
- `fix/nombre-corto`
- `docs/nombre-corto`

## Estandares de codigo (Python)

- Sigue PEP 8.
- Usa nombres claros para funciones y variables.
- Manten funciones pequenas y con una sola responsabilidad.
- Agrega docstrings en metodos o modulos no triviales.
- Usa logging en vez de `print` para trazas del sistema.

## Estructura UI (importante)

- `*.ui`: se editan en Qt Designer.
- `*_ui.py`: archivos generados, evita editar manualmente.
- `*_view.py`: aqui va la logica de interfaz, señales y validaciones.

## Calidad minima antes de PR

- El proyecto debe iniciar sin errores.
- No incluir codigo comentado sin uso.
- No romper flujos existentes (agregar, eliminar, calculo de totales).
- Si cambias comportamiento, explica el motivo en el PR.

## Commits

Usa mensajes simples y directos. Ejemplos:

- `feat: permitir editar solo la columna cantidad`
- `fix: recalcular totales al eliminar fila`
- `docs: agregar guia de contribucion`

## Pull Request checklist

- [ ] El cambio tiene un objetivo claro.
- [ ] El codigo fue probado manualmente.
- [ ] No se editaron archivos generados sin justificacion.
- [ ] Se actualizo documentacion si aplicaba.

## Licencia

Al contribuir, aceptas que tu codigo se distribuya bajo la licencia del proyecto: **GNU GPL v3**.
