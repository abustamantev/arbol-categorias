# Árbol de Categorías RC v4

Visualización interactiva del árbol de taxonomía canónica v4 de RetailCompass.

## Categorías

- **147 categorías** en 14 dominios
- **Oro:** categorías con definición completa, alta cobertura y atributos validados
- **Plata:** categorías con definición y cobertura parcial
- **Bronce:** categorías de escape, nicho o baja frecuencia

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `index.html` | Visualización interactiva tipo mindmap (Markmap) |
| `arbol_v4_final.html` | Tabla detallada con tiers Oro/Plata/Bronce |
| `rc_tree.json` | Datos del árbol en formato JSON |

## Cómo actualizar

```bash
python3 update_tree.py
```

## Deploy

Este repositorio se publica automáticamente en GitHub Pages:
https://andresbustoscompass.github.io/taxonomia-rc-v4/
