# Reglas de Learning Site (Quizzes & Readers)

0. **Dos Instancias con Usuario y Contraseña Inicial (`R` y `D`) y Nombre de la App (`Learning Site`):**
   - La aplicación se llama **`Learning Site`**. En la pantalla de `Acceso Privado`, el campo de usuario dice únicamente `Usuario...` (sin mencionar `R` ni `D`).
   - **Instancia `R`**: Usuario **`R`**, Contraseña **`Baerga`**. Contiene los quizzes de lectura de R (20 preguntas: 50% Multiple Choice, 25% Matching Columns, 25% True/False + Spelling Cipher).
   - **Instancia `D`**: Usuario **`D`**, Contraseña **`Lesish`**. Contiene quizzes de **5 preguntas** separados: un quiz independiente para **Multiple Choice (5 preguntas)** y otro quiz independiente para **Fill in the Blank (5 preguntas)** (20.0 puntos por pregunta = 100 puntos cada quiz).
   - El botón `👤 User: R/D (Switch)` en el encabezado permite cambiar de usuario/instancia en cualquier momento.

1. **Distribución Obligatoria de Preguntas en los Quizzes de `R`:**
   - **50% Multiple Choice (`mc`)** (ej. 10 de 20 preguntas)
   - **25% Matching Columns (`match`)** (ej. 5 de 20 preguntas)
   - **25% True or False (`tf`)** (ej. 5 de 20 preguntas)
   - Cada pregunta vale **5.0 puntos** (`4.0 pts` tarea de comprensión + `1.0 pt` deletreo `Spelling`). Con 20 preguntas el total es exactamente **100 puntos**.

2. **Reglas de Matching Columns (`match`):**
   - Cada vez que el usuario comete un error al emparejar las columnas, las parejas se reinician (`solvedPairs = []`), ambas columnas se reorganizan en un orden aleatorio garantizado diferente (`shuffleDifferentOrder`), y el contenido de la columna derecha cambia su redacción (`rightVariants`).

3. **Reglas de Deletreo (`Spelling`) y `Submit Answer`:**
   - El botón `Submit Answer` permanece deshabilitado hasta que se haya respondido la pregunta principal **y** se haya resuelto correctamente el `Spelling` o agotado sus 3 intentos.
   - Tanto la parte de comprensión como el `Spelling` cuentan para marcar la pregunta como correcta; si falla cualquiera de las dos, la pregunta pasa a `Review Missed`.

4. **Reglas de `Review Missed`, `Hint` y `Reread chapter to find answer`:**
   - `Review Missed` está bloqueado hasta que el usuario termine el quiz completo (`isQuizCompleted === true`).
   - Debajo de `Hint (-1.0 pt)` siempre debe existir el botón `📖 Reread chapter to find answer (-1.0 pt)` que muestra el texto específico de la página del capítulo donde está la respuesta y descuenta `1.0 pt`.

5. **Audio Feedback y Canciones Finales:**
   - Al presionar `Submit Answer`, suena uno de los 3 audios TTS para respuesta correcta o 3 para incorrecta.
   - Al terminar el quiz, suena automáticamente la canción de 30 segundos correspondiente al grado obtenido (**A**, **B**, **C** o **D y menor**) sin barra de progreso ni botones de Play/Replay.

6. **Contraseña de Reinicio (`Reset`), `AI Quiz Studio` y Acceso Privado:**
   - El botón `Reset` y el botón `✨ Crear / Quizzes (IA)` (`AI Quiz Studio`) solicitan la contraseña `admin123` en un modal con soporte para la tecla `Enter`.
   - Dentro de `AI Quiz Studio`, se pueden subir **imágenes/fotos de páginas**, **documentos (`PDF`, `.docx`, `.txt`, `.md`)** o **pegar texto directo** para que Gemini IA genere automáticamente nuevos quizzes cumpliendo todas las reglas (50% MC, 25% Match con 4 `rightVariants`, 25% T/F, `Spelling`, `Hint`, `Reread chapter` y lector HTML) y los sincronice en `quizzes-library.json`.
   - Mantener siempre la pantalla de `Acceso Privado` con soporte para tecla `Enter` y la etiqueta `Actualizado: [hora] - [mes/día/año]` visible en una esquina tanto en `Acceso Privado` como en la pantalla principal.
