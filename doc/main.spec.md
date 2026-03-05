# Modos de ejecucion (Comandos)

1. **one-dir**
```bash
uv run pyinstaller main.spec
```

2. **one-file**
```bash
POS_PYI_MODE=onefile uv run pyinstaller main.spec
```

3. Volver explicitamente a **one-dir**
```bash
POS_PYI_MODE=onedir uv run pyinstaller main.spec
```

## Notas:

- Si no defines POS_PYI_MODE, usa onedir.
- Si pones un valor inválido, el spec lanza error.