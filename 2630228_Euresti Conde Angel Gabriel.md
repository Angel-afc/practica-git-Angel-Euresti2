# INVESTIGACION SOBRE TIPOS DE ROBOTS

## Configuraciones Mecánicas de Robots Móviles

## 1.Conceptos básicos

### ¿Qué es un robot móvil?
 Un robot móvil es un sistema automatizado capaz de desplazarse de manera autónoma o teleoperada a través de su entorno físico a diferencia de los robots estáticos, cuenta con un sistema de locomoción como ruedas, orugas o patas y sistemas de navegación que le permiten interactuar y cambiar de posición en espacios dinámicos.

### ¿Qué diferencia existe entre un robot móvil y un robot manipulador fijo?
 La principal diferencia radica en su movilidad y espacio de trabajo. Un robot manipulador fijo está anclado a una base o superficie y su área de alcance se limita al radio de su brazo robótico. En cambio, un robot móvil puede trasladarse grandes distancias, lo que expande significativamente su espacio de trabajo y su capacidad para realizar tareas en diferentes ubicaciones físicas.

### ¿Qué función cumple el sistema de locomoción de un robot?
 El sistema de locomoción es el conjunto de mecanismos físicos (ruedas, ejes, motores y transmisiones) encargados de transformar la energía eléctrica o mecánica en movimiento controlado. Su función es permitir que el robot venza la fricción y la gravedad para trasladarse de un punto a otro de forma precisa y estable.

### ¿Qué significa que un robot tenga movilidad omnidireccional?
 Significa que el robot puede desplazarse instantáneamente en cualquier dirección del plano horizontal (adelante, atrás, a los lados y en diagonal) sin necesidad de cambiar la orientación de su chasis o girar previamente sobre su propio eje.

### ¿Qué relación existe entre la disposición de las ruedas y los movimientos que puede realizar el robot?
 La disposición, tipo y orientación de las ruedas determinan las restricciones cinemáticas del robot. Por ejemplo, una configuración convencional limita el movimiento lateral inmediato debido a la fricción transversal de las llantas, mientras que las ruedas especiales (como las omnidireccionales o Mecanum) eliminan estas restricciones, permitiendo grados de libertad adicionales en el plano.

### Aplicaciones de los robots móviles:
 Logística y almacenes: Vehículos de guiado automático (AGV) y robots móviles autónomos (AMR) para transportar mercancías.

 Exploración espacial:
 Rovers planetarios que investigan terrenos difíciles en la Luna o Marte.

 Agricultura de precisión:
 Robots autónomos para siembra, monitoreo de cultivos y aplicación selectiva de fertilizantes.

 Sector médico y hospitalario: 
 Robots de entrega para trasladar medicamentos y suministros en pasillos clínicos.

## 2.Robot diferencial con rueda de castor
La configuración diferencial utiliza dos ruedas motrices independientes montadas sobre un mismo eje central, acompañadas de una o más ruedas de apoyo libres (rueda de castor).

### Descripción de la configuración:

Ruedas motrices: 
Están colocadas a los lados izquierdo y derecho del chasis, cada una impulsada por su propio motor de manera independiente.

Rueda de castor (o rueda loca): 
Es una rueda omnidireccional de soporte pasivo que gira libremente sobre un eje vertical desalineado. Su función es mantener el equilibrio y la estabilidad del chasis sin interferir en la dirección del movimiento impuesta por las ruedas motrices.

Avance en línea recta: 
Ambas ruedas motrices giran hacia adelante a la misma velocidad y sentido.

Giro a la izquierda o derecha: 
Una rueda gira más rápido que la otra, provocando una curvatura en la trayectoria hacia el lado de la rueda más lenta.

Diferencia de velocidades: 
Permite curvar la trayectoria de manera gradual según la relación de velocidad angular entre ambos motores.

Giro sobre su propio eje: 
Una rueda motriz avanza mientras la otra retrocede a la misma velocidad, haciendo que el robot gire en su lugar sin desplazarse linealmente.

### Ventajas y limitaciones:
|Ventajas  |Limitaciones | 
|:--------:|:-----------:|
| Mecánica sencilla, bajo costo, fácil construcción y control algorítmico directo.| No posee movilidad lateral directa y requiere maniobras complejas (como curvas en arco) para cambiar de orientación en espacios reducidos |

### Aplicaciones: 
Aspiradoras robot domésticas, plataformas educativas de iniciación y robots de exploración básica.

## 3.Robots omnidireccionales con ruedas Omni
​Una rueda omnidireccional (o rueda omni) es un componente mecánico diseñado para permitir que un robot se desplace en cualquier dirección sobre un plano sin necesidad de cambiar la orientación de su chasis.

Distribución y orientación
Distribución: Las tres ruedas se colocan a una distancia equidistante del centro del chasis, separadas simétricamente a 120 grados unas de otras (formando una estructura triangular o en "Y").

Orientación: Los ejes de las ruedas principales suelen apuntar tangencialmente hacia una circunferencia central (o radialmente dependiendo de la geometría exacta), de modo que la combinación de vectores de fuerza cubra los componentes en los ejes X e Y del plano.

¿Cómo está construida?

​Consta de dos elementos principales:

​Un disco o rueda central conectada directamente al eje del motor, la cual proporciona la tracción motriz principal.
​Una serie de pequeños rodillos pasivos montados libremente alrededor de la circunferencia exterior de la rueda principal. Sus ejes de rotación son perpendiculares al plano de la rueda principal y al eje del motor.
​
¿Para qué sirven los pequeños rodillos?

​Los rodillos periféricos actúan como puntos de contacto secundarios con el suelo. Su función principal es permitir el movimiento libre pasivo en una dirección transversal (lateral) al sentido de giro del motor, evitando que la rueda patine o se trabe al moverse de lado.

​¿En qué dirección puede generar fuerza la rueda?

​La rueda omni genera fuerza motriz activa únicamente en la dirección de rotación de su rueda principal (es decir, hacia adelante o hacia atrás según el sentido en que gire el motor).

​¿Por qué puede deslizarse libremente en otra dirección?

​Cuando el robot necesita moverse en un ángulo distinto al avance de la rueda, los rodillos periféricos giran libremente sobre sus propios ejes por fricción con el suelo. Esto permite que la rueda entera se deslice de manera pasiva y lateral (paralela al eje del motor) sin oponer resistencia mecánica al movimiento dictado por las demás ruedas.
​
Movimientos únicos que permite
​Gracias a este diseño, un sistema con ruedas omni es holonómico:
​Traslación en 360 grados: El robot puede moverse en línea recta hacia adelante, hacia atrás, hacia los lados o en cualquier diagonal de manera simultánea.

​Movimiento desacoplado: Permite girar sobre su propio eje (rotación) al mismo tiempo que se traslada en una dirección arbitraria, algo imposible para un sistema de dirección convencional tipo coche (diferencial o Ackerman).

### Configuración de tres ruedas (3WD)
​Un robot omnidireccional de tres ruedas utiliza una disposición simétrica para cubrir todo el plano de movimiento de 360 grados

## Modos de desplazamiento

Adelante y atrás: 
Se logra combinando las velocidades de los tres motores. Por ejemplo, para avanzar hacia adelante, la rueda trasera ejerce fuerza en una dirección mientras las dos ruedas delanteras ajustan sus velocidades angulares para cancelar las fuerzas laterales y sumar fuerzas hacia el frente.

Lateralmente: 
Modulando las velocidades de las tres ruedas de forma asimétrica, la componente vectorial neta de las fuerzas se desplaza horizontalmente hacia la izquierda o la derecha.

En diagonal: 
Se obtiene variando proporcionalmente la velocidad de cada motor para generar una resultante vectorial en el ángulo deseado.

Giro sobre su propio eje: 
Las tres ruedas giran en la misma dirección (todas en sentido horario o todas en antihorario) y a la misma velocidad. Esto crea un momento de torsión neto que hace rotar el robot sobre su centro geométrico sin cambiar su posición (coordenadas X, Y).

Diferentes velocidades: 
Cuando las tres ruedas giran a velocidades y sentidos distintos, el robot ejecuta un movimiento compuesto (translación y rotación simultáneas en una trayectoria curva u oblicua).

### Configuración de cuatro ruedas (4WD)

¿Cómo se colocan las ruedas?
En una configuración de cuatro ruedas omni, los motores se ubican generalmente en las cuatro esquinas de un chasis rectangular o cuadrado. Los ejes de las ruedas son paralelos a los lados del chasis (a diferencia de las ruedas Mecanum, que tienen rodillos a 45 grados).

¿Cómo se combinan sus velocidades?
Mediante la cinemática del sistema, las velocidades de los cuatro motores (v_1, v_2, v_3, v_4) se controlan de forma independiente para generar las velocidades deseadas en el plano ((V_x, V_y) y la velocidad angular \omega). El microcontrolador calcula en tiempo real las ecuaciones de transformación para cada rueda.
### Diferencias respecto al sistema de tres ruedas

Geometría del chasis: 
El sistema de 3 ruedas se adapta mejor a bases triangulares y circulares; el de 4 ruedas se adapta de manera natural a chasis rectangulares o cuadrados (muy comunes en aplicaciones industriales).

Distribución de carga: 
Cuatro puntos de contacto ofrecen mayor estabilidad estática y mejor reparto del peso del robot.

Redundancia: 
Al tener un motor extra, el sistema de 4 ruedas posee redundancia de fuerza, lo que facilita soportar cargas más pesadas.


|Ventajas | limitaciones|
|:-------:|:-----------:|
|Mayor capacidad de carga y estabilidad ante inclinaciones o superficies ligeramente irregulares.|Requiere un controlador y un canal de motor adicionales (mayor costo y complejidad de hardware)|
|Distrivucion uniforme de la traccion en las cuatro ruedas|Consumo energético ligeramente mayor debido al uso de cuatro motores en lugar de tres.|
||En superficies muy rígidas o irregulares, alguna de las cuatro ruedas podría perder contacto momentáneamente si el chasis carece de suspensión flexible.|


## 4.Un robot omnidireccional con ruedas Mecanum 
Es un sistema móvil capaz de desplazarse en cualquier dirección en un plano de dos dimensiones (adelante, atrás, de lado, en diagonal) y girar sobre su propio eje de manera simultánea (movimiento holonómico), sin necesidad de cambiar la orientación de su chasis.

### ​Construcción y Funcionamiento de las Ruedas Mecanum
​¿Cómo están construidas?

​Una rueda Mecanum consta de un cubo o llanta central rígido rodeado por una serie de rodillos periféricos (generalmente entre 6 y 12 o más) montados de forma libre sobre rodamientos alrededor de la circunferencia de la rueda.

​¿Cómo están colocados sus rodillos?

​Los ejes de rotación de los rodillos secundarios están montados en un ángulo de 45^\circ respecto al eje principal de rotación de la rueda y al plano de la llanta.

​Cuando la rueda gira impulsada por un motor, la fuerza de fricción entre los rodillos inclinados y el suelo descompone la fuerza resultante en dos vectores:

​Una fuerza perpendicular al eje de los rodillos.

​Una fuerza paralela al eje de los rodillos.

Al combinar las velocidades y sentidos de giro de las cuatro ruedas, estas fuerzas laterales y longitudinales se suman o se cancelan, permitiendo el movimiento en 
cualquier dirección.

​Diferencia entre rueda Mecanum y rueda Omni convencional

Rueda Omni convencional: 
Sus rodillos periféricos están orientados a 90^\circ respecto al eje principal de la rueda (es decir, giran en la dirección de la circunferencia). Una rueda omni transmite fuerza únicamente en la dirección en la que apunta la rueda y gira libremente hacia los lados. Para lograr movimiento omnidireccional, las ruedas omni requieren estar orientadas en ángulos distintos (por ejemplo, en disposición triangular o en ángulo de 45^\circ en el chasis).

​Rueda Mecanum: Sus rodillos están inclinados a 45^\circ. La rueda se monta con su eje principal paralelo al chasis (como una rueda normal), pero la inclinación de los rodillos permite generar empuje lateral directamente, sin necesidad de inclinar los ejes de los motores ni cambiar la orientación del chasis.

​¿Por qué generalmente se utilizan cuatro ruedas?
​Se utilizan cuatro ruedas independientes porque proporciona un sistema con 3 grados de libertad en el plano (X, Y y rotación \theta) completamente determinado y controlable. Con cuatro puntos de contacto y motores independientes para cada rueda, se pueden resolver las ecuaciones cinemáticas exactas para generar fuerza neta en cualquier dirección vectorial del plano. Menos de cuatro ruedas no permitirían un control holonómico completo de 3 DOF.

​Orientación de las ruedas respecto al chasis

​Las cuatro ruedas se montan en paralelo respecto al chasis (dos a la izquierda, dos a la derecha). Sin embargo, los rodillos de las ruedas deben formar un patrón en "X" (vistos desde arriba hacia el centro) o en "O". La configuración más común es la configuración en X, donde las diagonales tienen la misma orientación de inclinación en los rodillos:

​Delantera izquierda (DI) y Trasera derecha (TD): Tienen rodillos inclinados en una 
dirección.

​Delantera derecha (DD) y Trasera izquierda (TI): Tienen rodillos inclinados en la dirección opuesta.

### Combinación de Movimientos

​Para lograr los diferentes desplazamientos, las ruedas giran de las siguientes maneras (considerando la configuración en X estándar):

​Avance: 
Las cuatro ruedas giran en el mismo sentido hacia adelante. Las fuerzas laterales generadas por los rodillos inclinados se cancelan mutuamente, impulsando el robot en línea recta hacia adelante.

​Retroceso: 
Las cuatro ruedas giran en el mismo sentido hacia atrás.

​Movimiento hacia la izquierda: 
Las ruedas delanteras izquierda y trasera derecha giran hacia atrás, mientras que las delanteras derecha y trasera izquierda giran hacia adelante. Las fuerzas laterales se suman hacia la izquierda, mientras que las longitudinales se anulan.

​Movimiento hacia la derecha: 
Las ruedas delanteras izquierda y trasera derecha giran hacia adelante, mientras que las delanteras derecha y trasera izquierda giran hacia atrás. Las fuerzas laterales se suman hacia la derecha.

​Movimiento diagonal: 
Se combinan las velocidades de forma asimétrica (por ejemplo, haciendo girar únicamente una diagonal de ruedas o variando la velocidad relativa entre pares opuestos).

​Giro sobre el propio eje (Rotación): 
Las dos ruedas de un lado (izquierdo o derecho) giran en una dirección y las dos del lado opuesto giran en la dirección contraria, haciendo que el robot gire en su lugar sin desplazarse.

### Tabla de Sentido de Giro de las Ruedas

​Utilizamos las siguientes convenciones para los giros:

​Adelante (\uparrow): Giro del motor en sentido de avance.

​Atrás (\downarrow): Giro del motor en sentido de retroceso.

| Movimiento | Delantera Izquierda(DI) | Delantera Derecha(DD)|Trasera Izquierda(TI)| Trasera Derecha (TD)|
|:-----:|:------:|:---------:|:--------:|:---------:|
|Avanzar|delante|delante|delante|delante|
|retroceder| atras | atras | atras |atras|
|desplasarce a la izquierda|atras|delante|delante|atras|
|Desplazarse a la derecha|delante|atras|atras|delante|
|Girar a la izquierda(antihorario)|atras|delante|atras|delante|
|Girar a la derecha(horario)|delante|atras|delante|atras|

## 5.Robot con dirección Akermann

La geometría de dirección Ackermann es un arreglo cinemático diseñado para los ejes de dirección de un vehículo de cuatro ruedas, de modo que todas las ruedas giren sobre círculos con un centro común en un punto central de giro. Esto evita que los neumáticos derrapen lateralmente al tomar una curva.
### Funcionamiento y Arquitectura

​Cómo se distribuyen las ruedas

​Un vehículo o robot con dirección Ackermann cuenta típicamente con cuatro ruedas distribuidas en dos ejes principales: un eje delantero y un eje trasero, situados de forma simétrica a lo largo del chasis.

​¿Qué ruedas proporcionan la dirección?

​Normalmente, las ruedas delanteras son las encargadas de proporcionar la dirección. Están montadas sobre pivotes independientes y conectadas mediante un varillaje de dirección (o servomotores individuales) que ejecuta la geometría Ackermann para que giren en ángulos diferentes.

​¿Qué ruedas pueden proporcionar la tracción?

​La tracción puede ser proporcionada por:

1. ​Las ruedas traseras (tracción trasera o RWD).
2. Las ruedas delanteras (tracción delantera o FWD).
3. Las cuatro ruedas simultáneamente (tracción total o AWD/4WD).

En robótica móvil, el motor de tracción suele aplicarse al eje trasero, mientras que un motor independiente (como un servomotor) controla el ángulo de giro de las ruedas delanteras.

​¿Por qué las ruedas interiores y exteriores no giran con el mismo ángulo?

​Cuando un vehículo toma una curva, la rueda interior recorre un radio menor que la rueda exterior respecto al centro de giro. Si ambas ruedas giraran exactamente en el mismo ángulo paralelo, una de ellas se vería forzada a deslizarse o arrastrarse lateralmente sobre el suelo, generando fricción, desgaste prematuro y resistencia al avance. La geometría Ackermann compensa esto haciendo que la rueda interior gire un ángulo mayor que la rueda exterior.
¿​Qué es el radio de giro?

​Es el radio de la circunferencia más pequeña que describe el punto más exterior del vehículo (o su centro) al realizar un giro completo con el ángulo máximo de dirección permitido define la maniobrabilidad del robot en espacios reducidos.

​¿Por qué un vehículo Ackermann no puede desplazarse hacia un costado?

​A diferencia de los robots omnidireccionales (como los de ruedas Mecanum), los vehículos Ackermann tienen restricciones cinemáticas de movimiento (denominadas restricciones no holonómicas)Las ruedas solo pueden rodar en la dirección en la que apuntan. Por lo tanto, no pueden trasladarse lateralmente (cangrejo) sin antes avanzar o retroceder para reorientar el chasis.
​Semejanzas con la dirección de un automóvil convencional
​Tienen exactamente la misma arquitectura y cinemática, ya que la dirección Ackermann fue patentada originalmente en 1818 para carruajes de caballos y adaptada posteriormente a los automóviles modernos. Utilizan el principio de barras articuladas (trapecio de dirección) para lograr el diferencial de ángulo en las ruedas directrices.

Rueda interior: La rueda más cercana al centro de giro (en el diagrama, la del lado izquierdo del vehículo). Gira con un ángulo más pronunciado.

​Rueda exterior: La rueda más alejada del centro de giro (en el diagrama, la del lado derecho). Gira con un ángulo menor.

​Centro aproximado de giro: El punto geométrico imaginario en el plano donde convergen las líneas perpendiculares de los ejes de todas las ruedas (marcado como "Centre of turning circle").

​Dirección de desplazamiento: El sentido de avance tangencial al arco de la trayectoria circular que sigue el robot.

### Ejemplos de Robots y Vehículos Autónomos

​Coches autónomos a escala (Robots de investigación): Plataformas como F1TENTH o vehículos autónomos educativos que simulan la dinámica de conducción de un 
coche real.

​Vehículos autónomos de reparto (Last-mile delivery): Rovers de entrega en aceras y campus (como los de Starship Technologies) que emplean dirección 
Ackermann en el eje delantero para mayor estabilidad en exteriores.

​Automóviles comerciales y tractores autónomos: 
Vehículos agrícolas sin conductor (como los tractores autónomos de John Deere) que operan en campos abiertos y requieren alta precisión mecánica sin dañar el terreno por deslizamiento de neumáticos.

## 6.COMPARACION DE CONFIGURACIONES 
​Tabla Comparativa de Configuraciones de Robots Móviles
Configuración|Numero tipico de ruedas |Movimiento lateral |Giro sobre su eje |complejidad mecánica | complejidad de control |Aplicaciones típicas |
|:-------:|:---------:|:---------:|:----------:|:--------:|:------:|:------:| 
 |Diferencial+castor|2 tracción+ 1 o 2 locas (castor)|No(requiere girara para cambiar su rumbo)| si | Baja | Baja | Robots educativos, aspiradoras robot, robots de exploración básica |
 omni de 3 ruedas |3 ruedas(ruedas omnidirccionales con rodillos pasivos) | si (omnidireccional) | si |Media |Media-Alta |Robots de competición (tipo Robocup)plataformas móviles de interiores en espacios abiertos |
 Omni de 4 ruedas|4(ruedas omnidireccionales con rodillos pasivos)|si (omnidireccional)|si|Media-Alta |Media-Alta|Plataformas móviles industriales,robots de servicio con mayor capacidad de carga.|
 Mecanum|4(ruedas con rodillos angulares a 45 grados)|si|si|Alta|Alta|Almacenes automatizados sillas de ruedas|
 Ackerman|4|No|Si|Alta|Baja|Automóviles, vehículos autónomos viales|

### Selección de configuración por cada caso:
-Robot pequeño para aprender programación y control:Diferencial con ruedas de castor, debido a su simpliidad de circuiteria, control de motores DC basicos. 
-Robot que necesita desplazarse dentro de un almacén con espacios reducidos: Mecanum o Omni de 4 ruedas, ya que pueden girar y trasladarse de lado en pasillos angostos.
​-Plataforma que necesita moverse lateralmente sin cambiar su orientación: Mecanum, por su capacidad de traslación lateral pura manteniendo el frente fijo.
-​Vehículo autónomo que debe circular de manera similar a un automóvil: Ackermann, por cumplir con las normativas viales y adaptarse a la infraestructura urbana existente.
​-Robot para una competencia donde sea necesario cambiar rápidamente de dirección: Omni de 3 ruedas, por su excelente agilidad y menor inercia de giro.
​-Robot móvil sencillo que utilice únicamente dos motores: Diferencial con rueda de castor, el cual requiere exactamente dos actuadores independientes para su tracción y dirección
## 7.Análisis del movimiento
1. ​Diferencial: Para girar sobre su propio eje, las ruedas motrices deben girar a la misma velocidad pero en sentidos opuestos (una hacia adelante y otra hacia atrás). Esto genera un par de fuerzas neto que rota el chasis sobre su centro geométrico sin alterar su posición lineal.
2. Omni: Los pequeños rodillos permiten generar movimiento lateral porque al girar la rueda principal en una dirección donde el desplazamiento directo está bloqueado por el chasis, los rodillos pasivos giran libremente sobre su propio eje, descomponiendo la fuerza vectorial y permitiendo el avance ortogonal sin fricción indeseada.
3. ​Mecanum: El robot puede desplazarse lateralmente aunque ninguna rueda esté orientada hacia los costados porque la inclinación a 45^\circ de los rodillos descompone la fuerza rotacional de cada rueda en componentes vectoriales longitudinales y transversales. Al combinar las cuatro ruedas con sentidos específicos, las fuerzas longitudinales se anulan entre sí y las fuerzas transversales se suman, impulsando al robot de costado.
4. Ackermann: El vehículo necesita avanzar o retroceder para cambiar de posición lateral debido a que las ruedas convencionales generan una fuerza de fricción estática muy elevada en dirección transversal. Para trasladarse a un costado, el vehículo debe trazar una curva de avance o retroceso que modifique su orientación geométrica global.

# 8.Aplicación en un robot real

 - Aplicación en un robot real
 - ​Nombre del robot: KUKA iiwa / KMR iiwa (Mobile Robot).
 - Fabricante: KUKA AG.
 - Tipo de locomoción: Omnidireccional con ruedas Mecanum.
 - Número y tipo de ruedas: 4 ruedas Mecanum motrices independientes. 
 - Sensores principales: Escáneres láser de seguridad (LiDAR), cámaras de profundidad y sensores odométricos en las ruedas.
 - ​Actuadores utilizados para el movimiento: 4 servomotores de corriente alterna acoplados a engranajes de alta precisión.
 - ​Aplicación del robot: Logística industrial avanzada y ensamblaje flexible en fábricas inteligentes (Industria 4.0).

Justificación de la configuración: La disposición con ruedas Mecanum es ideal para este entorno industrial porque permite al robot maniobrar con total precisión milimétrica en espacios sumamente reducidos entre líneas de producción, acercándose lateralmente a las estaciones de trabajo sin necesidad de realizar curvas o giros amplios que obstaculizarían el paso de operarios y otros equipos

## Reflezion final
Analizando las diferente alternaticas mecánicas, la configuración que me pareció mas sencilla de comprender es la diferencial con rueda de castor, debido a que su lógica de control imita el movimiento intuitivo de caminar o girar mediante la variación de velocidad en dos puntos de tracción. Por otro lado, el sistema que ofrece mayor libertad de movimiento es el de ruedas Mecanum y Omni, ya que rompen con las restricciones cinemáticas tradicionales al introducir grados de libertad ortogonales en el plano.
Para construir mi primer robot móvil, elegiría sin duda una configuración diferencial, ya que reduce al mínimo la complejidad de programación, el costo de los componentes y facilita el diagnóstico de errores electrónicos. Finalmente, comprendo que no existe una única configuración de ruedas adecuada para todos los robots porque cada aplicación demanda un compromiso técnico específico entre capacidad de carga, eficiencia energética, complejidad de control, costo económico y las condiciones del terreno donde va a operar.
 
## Referencia 

 - Siciliano, B., & Khatib, O. (Eds.). (2016). Springer Handbook of Robotics. Springer Reference. https://doi.org/10.1007/978-3-319-32552-1
 - Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). Introduction to Autonomous Mobile Robots. MIT Press.
 - ​KUKA AG. (2024). KMR iiwa Technical Documentation and Datasheets. KUKA Robotics. https://www.kuka.com
 - Corke, P. (2017). Robotics, Vision and Control: Fundamental Algorithms in MATLAB (Vol. 118). Springer.