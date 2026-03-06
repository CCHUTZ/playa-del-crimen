# Playa del Crimen - Guía de Uso y Próximos Pasos

## ✅ Repositorio Creado Exitosamente

**URL del Repositorio:** https://github.com/CCHUTZ/playa-del-crimen

El repositorio ha sido creado y todos los archivos han sido subidos exitosamente. Ahora, necesitas habilitar GitHub Pages para que el sitio web sea accesible públicamente.

## 📋 Cómo Habilitar GitHub Pages

1. Ve a tu repositorio en GitHub: https://github.com/CCHUTZ/playa-del-crimen
2. Haz clic en **Settings** (Configuración) en la barra superior.
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En la sección **Source** (Fuente), selecciona:
   - **Branch:** `master`
   - **Folder:** `/docs`
5. Haz clic en **Save** (Guardar).
6. GitHub Pages comenzará a construir tu sitio. Esto puede tomar unos minutos.
7. Una vez completado, verás un mensaje que dice: **"Your site is published at https://cchutz.github.io/playa-del-crimen/"**

## 🌐 Acceso al Sitio Web

Una vez habilitado GitHub Pages, tu sitio estará disponible en:

**https://cchutz.github.io/playa-del-crimen/**

## 📁 Estructura del Repositorio

```
playa-del-crimen/
├── README.md                    # Descripción del proyecto
├── BLUEPRINT.md                 # Documento de diseño y estrategia
├── docs/                        # Sitio web (GitHub Pages)
│   ├── index.html               # Página principal
│   ├── style.css                # Estilos vaporwave
│   └── scenarios/
│       └── 00_la_estrella_del_terror.html
├── content/                     # Contenido en Markdown
│   └── scenarios/
│       └── 00_la_estrella_del_terror/
│           ├── README.md
│           ├── briefing.md
│           ├── team_structure/
│           ├── phases/
│           ├── exercises/
│           └── references.md
└── scripts/
    └── build.py                 # Script para generar HTML desde Markdown
```

## 🚀 Próximos Pasos

### 1. Crear Más Escenarios

El repositorio está diseñado para escalar fácilmente. Para agregar un nuevo escenario:

1. Crea un nuevo directorio en `content/scenarios/` (ej: `01_nuevo_escenario/`)
2. Copia la estructura de `00_la_estrella_del_terror/`
3. Escribe el contenido en Markdown
4. Actualiza el script `scripts/build.py` para incluir el nuevo escenario
5. Ejecuta `python3 scripts/build.py`
6. Haz commit y push de los cambios

### 2. Generar Material Gráfico

Para potenciar el impacto visual:

- Crea diagramas de flujo para las fases de ataque
- Diseña gráficos de redes sociales para el mapeo de relaciones
- Genera mockups de interfaces "del equipo hacker"
- Crea infografías para los conceptos clave

Guarda todos los gráficos en `content/scenarios/XX_nombre_escenario/assets/`

### 3. Enlazar desde el Curso Principal

Para integrar "Playa del Crimen" con tu programa de inteligencia estratégica:

1. Agrega una sección "Recursos Prácticos" en el README de los repositorios del curso
2. Enlaza directamente a https://cchutz.github.io/playa-del-crimen/
3. Menciona los escenarios en los módulos relevantes del curso

### 4. Promover el Proyecto

- Comparte el enlace en LinkedIn con un post sobre la importancia del entrenamiento OSINT
- Menciona el proyecto en tus presentaciones y talleres
- Considera escribir un artículo en Medium sobre la filosofía detrás de "Playa del Crimen"

## 🎨 Personalización Visual

Si quieres ajustar la paleta de colores o el diseño:

1. Edita el archivo `docs/style.css`
2. Modifica las variables CSS en la sección `:root`
3. Haz commit y push de los cambios
4. GitHub Pages se actualizará automáticamente

## 📝 Notas Importantes

- **Todos los escenarios son ficticios.** Asegúrate de que esto quede claro en todas las comunicaciones.
- **El objetivo es educativo.** El enfoque siempre debe ser en la defensa, no en el ataque.
- **Mantén la calidad.** Cada escenario debe ser técnicamente preciso y educativamente valioso.

## 🤝 Contribuciones Futuras

Si decides hacer el repositorio colaborativo en el futuro:

1. Crea un archivo `CONTRIBUTING.md` con las directrices para contribuir
2. Establece un proceso de revisión para nuevos escenarios
3. Considera crear un sistema de "badges" o certificados para quienes completen todos los escenarios

---

**¡El proyecto está listo para ser usado y compartido!**
