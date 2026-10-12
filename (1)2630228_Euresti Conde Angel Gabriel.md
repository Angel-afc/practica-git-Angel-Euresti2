# 1. Resumen Ejecutivo

 ​La agilidad surge como una respuesta a la rigidez y lentitud de los métodos tradicionales de gestión de proyectos (como Cascada o Waterfall), los cuales fallaban frecuentemente en entornos caracterizados por la alta incertidumbre, cambios constantes de requerimientos y la necesidad de entregar valor temprano a los usuarios.
 
 Ser “ágil” no es seguir una metodología estricta, sino adoptar una mentalidad (mindset) basada en la adaptabilidad, la colaboración estrecha con el cliente, la transparencia y la entrega iterativa e incremental de valor.
 
 Este documento cubre los fundamentos teóricos y prácticos de la gestión ágil, desglosando los marcos de trabajo más utilizados en la industria (Scrum, Kanban y Design Thinking), sus roles, artefactos, eventos, métricas clave, ventajas, riesgos y su articulación en el ciclo de vida del desarrollo de software.

## 2. Principios Ágiles
### ​Valores y Principios Clave
​Basados en el Manifiesto Ágil, los cuatro valores fundamentales priorizan:
 1. Individuos e interacciones sobre procesos y herramientas.

 2. ​Software funcionando sobre documentación exhaustiva.

 3. Colaboración con el cliente sobre negociación de contratos.
 
 4. Respuesta ante el cambio sobre seguir un plan rígido.

### ​Impacto en la Gestión del Trabajo

 - ​Mitigación temprana de riesgos: Al entregar incrementos funcionales frecuentemente, los errores o desalineaciones se detectan en semanas y no al final de meses de desarrollo.

 - ​Empoderamiento de los equipos: Se fomenta la auto-organización, lo que incrementa la motivación y la creatividad técnica.

 - ​Alineación continua con el negocio: Las prioridades pueden ajustarse ciclo a ciclo según el feedback real del mercado.

## 3. Panorama de Marcos Ágiles

 - Scrum: Marco iterativo e incremental estructurado en ciclos cortos llamados Sprints. Ideal para proyectos donde los requerimientos son complejos pero se pueden acotar en bloques de tiempo definidos.

 - Kanban: Sistema de gestión de flujo continuo basado en la visualización del trabajo y la limitación del WIP (Work in Progress). Ideal para entornos de soporte, mantenimiento o operaciones con alta variabilidad y llegada impredecible de tareas.

 - ​Design Thinking: Enfoque de innovación centrado en el usuario para resolver problemas complejos y mal definidos. Se usa al inicio de los proyectos para asegurar que se está construyendo el producto correcto (discovery).
 
|Marco|Cuando elegirlo|
|:---:|:-------------:|
|scrum|productos nuevos, equipos dedicados y cuando necesita estimar capacidad y velocidad|
Kanban|cuando el proceso es continuo, para el soporte técnico, flujos con cuello de botella frecuentes y tareas varadas que entran espontaniamente|
ScrumBan|Transiciones donde se requiere la estructura de eventos de Scrum limitación de flujo de Kanban|
## 4.Ventajas y riesgos 

|Beneficios|Limitaciones y Trade-offs|
|:--------:|:-----------------------:|
Mayor adaptabilidad a cambios del mercado|Requiere alta disciplina cultural y cambio organizasional|
Visibilidad constante del progreso del proyecto|Riesgo de "Scrum-fall"(hacer metodologias agiles con mentalidad rigida tradicional) |
Alta calidad técnica gracias a revisiones constantes|Posible resistencia al cambio por parte de mandos medios o stakeholders tradicionales|
foco en la entrega de valor real al usuario final|Dependencia critica de la disponibildad y compromiso de los roles|

## Contenido Mínimo (Scrum)
### Conceptos Base
 - Propósito: Gestionar proyectos complejos bajo un entorno empírico (transparencia, inspección y adaptación).
 - Cuándo usarlo: Cuando el alcance es incierto pero el equipo puede comprometerse a objetivos de corto plazo estables (Sprints de 1 a 4 semanas).
### ​Roles
 - ​Product Owner (PO): Maximiza el valor del producto y gestiona el Product Backlog.
     - ​Error frecuente: Actuar como un mero "pasador de requisitos" sin entender la rentabilidad de negocio o estar ausente para el equipo de desarrollo.
 - ​Scrum Master (SM): Facilita el proceso Scrum, elimina impedimentos y promueve la mejora continua.
     - Error frecuente: Confundirlo con un jefe de proyecto tradicional que asigna tareas y microgestiona.
 - ​Development Team: Profesionales auto-organizados que construyen el incremento de producto.
     - Error frecuente: Trabajar en silos funcionales (ej. solo diseño, solo desarrollo, solo pruebas) en lugar de colaborar de forma multidisciplinaria.
### Artefactos
 - ​Product Backlog: Lista priorizada de todo lo necesario en el producto.
 - ​Sprint Backlog: Selección del Product Backlog para el Sprint actual más el plan para entregarlo.
 - ​Increment: La suma de todos los elementos del Product Backlog completados durante un Sprint.
 - ​Definition of Done (DoD) vs. Criterios de Aceptación:
     - Definition of Done: Criterios de calidad globales aplicables a cualquier elemento del backlog (ej. código probado, documentado, revisado y desplegable).
     - ​Criterios de Aceptación: Condiciones específicas que debe cumplir una historia de usuario particular para considerarse satisfecha.
### Eventos
 - Sprint: Contenedor de todos los demás eventos (duración: 1 a 4 semanas). Antipatrón: Cambiar el objetivo del Sprint a mitad del ciclo.
 - ​Sprint Planning: Planificación del trabajo del Sprint (Duración sugerida: máx. 8 horas para un mes). Antipatrón: Planificar sin conocer la capacidad real del equipo.
 - Daily Scrum: Sincronización diaria de 15 minutos. Antipatrón: Convertirlo en un reporte de estatus dirigido al jefe o Scrum Master.
 - Sprint Review: Inspección del incremento con los stakeholders (Duración: máx. 4 horas). Antipatrón: Presentar diapositivas en lugar de software funcionando.
 - ​Sprint Retrospective: Inspección del proceso del equipo y plan de mejora (Duración: máx. 3 horas). Antipatrón: Quejarse sin generar acciones de mejora tangibles.

### Métricas
 - ​Velocity: Cantidad de historias de usuario completadas por Sprint. Cómo usarla: Para estimar la capacidad futura de planificación. Cómo NO usarla: Como métrica de productividad para comparar equipos o castigar desarrolladores.
 - Burndown Chart: Gráfica de trabajo restante frente al tiempo. Cómo usarla: Visualizar la tendencia de cumplimiento del objetivo del Sprint.
 - ​WIP (Work in Progress): Tareas iniciadas y no terminadas. Cómo interpretarla: Ayuda a detectar cuellos de botella por exceso de multitarea

## ​Contenido Mínimo (Kanban)
### Fundamentos
#### ​Se basa en 6 prácticas principales:
1. ​Visualizar el flujo de trabajo.
2. ​Limitar el WIP (Work in Progress).
3. ​Gestionar y medir el flujo.
4. Hacer las políticas de proceso explícitas
5. ​Implementar bucles de retroalimentación.
6. Mejorar colaborativamente (evolutivamente).

### ​Tablero Kanban y Límites WIP
 - Propuesta de columnas para desarrollo: Backlog -> Análisis -> En Desarrollo -> Code Review -> QA / Testing -> Listo para Producción -> Hecho.
 - ​Límites WIP razonados: Por ejemplo, restringir la columna En Desarrollo a un máximo de 3 elementos para obligar al equipo a terminar tareas antes de iniciar nuevas (stop starting, start finishing).

### Métricas de Flujo
 - Lead Time: Tiempo total desde que se solicita una tarea hasta que se entrega en producción.
 - ​Cycle Time: Tiempo que tarda el equipo en completar una tarea desde que comienza a trabajar activamente en ella.
 - ​Throughput: Cantidad de elementos completados por unidad de tiempo (ej. tareas por semana).
 - Diagrama de Flujo Acumulado (CFD): Gráfica que muestra el volumen de trabajo en cad

Políticas y Clases de Servicio
​Políticas explícitas: Reglas claras de cuándo un ticket puede pasar de una columna a otra (ej. "Para pasar a QA, el código debe tener al menos 80% de cobertura de pruebas unitarias").
​Clases de servicio: Categorización de tareas (ej. Expedite para errores críticos en producción que saltan restricciones de WIP; Standard para requerimientos normales).
​Cuándo Usar Kanban
​Ideal para departamentos de soporte técnico, mantenimiento de software, equipos de operaciones o proyectos con flujos constantes de solicitudes de diversa magnitud donde los Sprints fijos no aportan valor.
​Contenido Mínimo (Design Thinking)
​Visión General
​Design Thinking es un proceso iterativo de resolución de problemas enfocado en entender profundamente las necesidades humanas. Se acopla perfectamente en la fase de descubrimiento (Discovery) del desarrollo de software para evitar crear productos funcionales pero irrelevantes para el usuario.
​Fases
​Empatizar: Entender al usuario en su contexto real.
​Técnicas: Entrevistas en profundidad, observación, mapa de empatía.
​Entregable: Perfiles de usuario y hallazgos clave.
​Definir: Sintetizar los hallazgos para enfocar el problema real.
​Técnicas: Definición del punto de vista (POV), arquetipos (Personas), How Might We (HMW).
​Entregable: Declaración clara del problema a resolver.
​Idear: Generar un volumen alto de ideas creativas sin filtros iniciales.
​Técnicas: Brainstorming, Crazy Eights, Worst Possible Idea.
​Entregable: Selección de ideas principales a explorar.
​Prototipar: Construir versiones preliminares y tangibles de las soluciones.
​Técnicas: Bocetos en papel, wireframes de baja fidelidad, maquetas conceptuales.
​Entregable: Prototipo de baja fidelidad.
​Probar: Evaluar los prototipos con usuarios reales para iterar y refinar.
​Técnicas: Pruebas de usabilidad, malla receptora de información.
​Entregable: Feedback estructurado para ajustar la solución.
​Mini-Caso Práctico
​Problema: Los estudiantes universitarios abandonan una plataforma de tutorías en línea durante el proceso de inscripción por confusión en la interfaz.
​Fases aplicadas:
​Empatizar: Entrevistas breves a 5 alumnos revelan que el calendario de horarios es confuso.
​Definir: "¿Cómo podríamos simplificar la selección de horarios para reducir el abandono en un 30%?".
​Idear: Propuesta de selector de horarios basado en bloques visuales de colores y sincronización con Google Calendar.
​Prototipar: Boceto en papel (paper prototype) con pantallas secuenciales de selección.
​Probar: Se muestra el boceto a 3 estudiantes; se detecta que falta un botón claro de confirmación. Se ajusta el diseño antes de escribir código.
​Relación con SDLC y Ágil
​Design Thinking opera en el espacio del Problem Space (asegurar que construimos lo correcto), mientras que Scrum/Kanban operan en el Solution Space (construir la solución correctamente). Una vez validado el prototipo en Design Thinking, las soluciones se descomponen en historias de usuario que alimentan el Product Backlog de Scrum.
​Conclusiones
​La adopción de enfoques ágiles y de marcos como Scrum, Kanban y Design Thinking no representa una simple moda corporativa, sino un cambio estructural hacia la eficiencia y la centralidad en el usuario. En el ámbito académico y profesional, dominar estas herramientas permite enfrentar proyectos complejos reduciendo el desperdicio de recursos, fomentando la adaptabilidad ante escenarios cambiantes y garantizando que el desarrollo tecnológico genere un impacto real y medible.
​Referencias
​Beck, K., et al. (2001). Manifesto for Agile Software Development. [En línea].
​Schwaber, K., & Sutherland, J. (2020). La Guía de Scrum: La Guía Definitiva para Scrum: Las Reglas del Juego. Scrum.org.
​Anderson, D. J. (2010). Kanban: Successful Evolutionary Change for Your Technology Business. Blue Hole Press.
​Brown, T. (2008). Design Thinking. Harvard Business Review, 86(6), 84.
​Kniberg, H., & Skelton, M.