# Investigacion sobre Censores y Actuadores
## conceptos básicos
 ### ¿Que es un sensor?
  Es un aparato fisico que detecta variaciones en distintos campos puede ser de temperatura, sonido, entre otros...
 ### ¿Que es un actuador? 
  Es un aparato que recive señales electricas que las transforma en movimientos mecanicos, como generar movimientos, fuerza, calor, etc.
 ### ¿Cual es la diferenci entre un sensor y un actuador?
  Los sensores mandan energia o señales que se interpretan como sentidos ya sea calor, peso, etc.
  Los actuadores sol reciben las señales mandadas por otros componentes 
 ### ¿Que funcion tiene dentro de un sistema mecatrónico
  Hayudan con la interacción de el robot con su entorno, el sensor manda señales electricas a otros componentes, los actuadores ayudan con el movimiento 
## Ejemplo en un sistema cotidiano: aire acondicionado
  sensor:termostato le indica la temperatura de el cuarto y manda señales cuando esta muy frio o muy caliente
  Actuadores: el compresor que manda a over el flujo de aire para modificar la temperatura del espacio
## 2.Investigación de sensores
|Tipo de sensor|Variable que emite|Principio de funcionamiento|Ejemplo|Aplicación|
|:---------:|:----------:|:----------:|:----------:|:----------:|
 |Temperatura|Temperatura|Varia su resistencia eléctrica o genera un voltaje diminuto en función de el calor recibido|LM3/Termopar Tipo k|Monitoreo térmico en motores industriales o control de clima|
 Luz|Intensidad Lumínica|Modifica su resistencia eléctrica de acuerdo con la cantidad de fotones que inciden sobre su superficie semiconductora|LDR(Fotorresistencia)|Sistema de encendido automático de alumbrado público al atardecer|
 Proximidad|Precencia u objeto cercano|Genera campos electromagnéticos o rayos infrarrojos que rebotan o se alteran al acercarse un objeto, sin requerir contacto fisico.|Sensor inductivo LJ12A3-4-Z/BX|Deteccion de piezas metálicas en lineas de ensamblaje automatizadas|
 Distancia |Distancia lineal a un objeto|Emite pulsos de ondas (ultrasonicos o laser) y mide el tiempo que tardan en rebotar contra el objetivo|HC-SR04(Ultrasonico)|Sistemas anticolisión en robots móviles autonomos |
 Presion |Fuerza por unidad de área |Utiliza elementos piezoelecrico o membranas deformables que convierten la presion de gases o liquidos en señales electricas|MPX5700AP|Monitoreo de presion en sistemas neumaticos o barometros|
 Humedad|Humedad relativa de el aire o suelo|Detecta cambios en la conductividad electrica o capacitancia de un material higroscopico al absorver vapor de agua|DHT11/DHT22|Invernadores automatizados para controlar el riego|
 Posición|Ubicacion angular o lineal|Emite pulsos obticos o magneticos a traves de discos ranurados para registrar el desplazamiento exacto de un eje |Codificador óptico|Control de posicionamiento en ejes de fresadoras CNC|
 Velocidad o movimiento|Velocidad de giro o desplazamiento|mide la frecuencia de pulsos generados por cambios magneticos u ópticos por unidad de tiempo|Sensor efector Hall|Medicion de la velocidad de giro en ruedas de vehiculos o motores|
 Fuerza o peso|Carga o fuerza aplicada|Emplea galgas extenciometricas que varian su resistencia eléctrica al estirarse o comprimirse bajo una carga mecánica|Celda de carga HX711|Basculas dijitales y plataformas de pesaje industrial|

## 3.Clasificasion de sensores
### Sensores analógos y digitales:
 - Caracteristica de clasificasion:la naturaleza de la señal de salida.
 - Dierencia:Los analógos entregan una señal eléctrica continua que varia de una forma proporsional de rango de la varable medida un ejemplo sera de 0-5 volts
### Sensores de contacto y sin contacto:
 - Caracteristica de clasificasión:La necesidad o falta de interaccion fisica directa con el objeto a medir
 - Diferencia:Los de contacto requieren tocar fisicamente el objeto para realizar la medicion, mientras que los sin contacto detactan la presencia o dimensiones de un objeto ´por medio de el sonido, magneticos,etc.
### Sensores activos y pasivos
 - Caracteristica de clasificación:Si requiere o no una fuente de alimentacion externa para generar señal
 - Diferencia:Los activos necesitan una alimentación eléctrica esterna para funcionar(como los censores ultrasónicos).Los pasivos no requieren energia externa, ya que su propia señal eléctrica directamente a partir de la energia de la variable fisica que miden
## 4.Investigación de actuadores
|Actuadores|Energia utilizada|Movimiento|Ventaja|Limitación|Aplicación|
 :-------:|:--------:|:-------:|:-------:|:------:|:-------:|
  Motor DC|Electrica (corrirnte directa|Rotatorio|Alto torque a altas velocidades y facilidad de control de velocidad|Requiere mantenimiento por desgaste de escobillas|Tracción de pequeños vehiculos robotizados y ventiladores|
  Servomotor|Eléctrica|Rotatorio limitado|Excelente precisión en el posicionamiento angular gracias a su lazo de retroalimentacion interna|Su angulo de giro suele estar limitado macánicamente|Control de direccion en autos a escala y articulaciones de brazos robóticos|
  Motor paso a paso|Eléctrica(pulsos digitales)|Rotatorio fraccionado en pasos discretos|Permite un control extremadamente preciso de la posición y velocidad sin requerir retroalimentacion externa|Puede perder un paso si se le exige un torque superior a su capacidad máxima|Impresoras 3D y maquinas de corte láser|
  Solenoide|Eléctrica|Lineal(puede empujar o atraer)|Respuesta muy rapida y diseño electromecánico sencillo y robusto|Su carrera de movimiento es corta y limitada|Cerrojos eléctricos de puertas y válvulas de paso de agua|
  Cilindro neumático|Neumática(Aire comprimido)|Lineal|Velocidad de operación alta y componentes limpios y seguros en entornos industriales|Requiere compresores y sistemas de filtrado de aire adicionales|Ecpulcion de piesas defectuosas en bandas transportadoras|
  Cilindro hidráulico|Hidraulica(Aceite a alta presión)|Lineal|Capacidad para desarrollar fuerzas y cargas extremadamente elevadas|Instalacion compleja y riesgo de fugas de fluido hidráulico|Maquinaria pesada|
## 5.Comparacion de actuadores
 - Motor DC vs. Servomotor
   - Diferencia:Un motor DC gira continuamente sin limitacion al aplicarle voltaje,mientras que el servomotor tiene una serie de limitadres que solo lo dejan girar 180 grados
   - Situacion de eleccion:En lo personal utilizaria un servomotor mas qu enada para un brazo robotico que es el que tiene que estar limitado el movimiento,y un motoe dc para el movimiento de las ruedas de un vehiculo
 - Servomotor vs.Motor paso a paso:
   - Diferencia:El servomotor utiliza un sistema de retroalimentacion para correguir errores de pocision continuamente,mientras que el motor paso a paso se mueve mediante pulsos discretos preestabecidos sin verificar si el paso se ejecuto de forma correcta bajo carga
   - Situacion de eleccion:Elegiria un motor paso a paso para una impresora 3D,ya que pede repetir una accion varias veces,tiene buen control de revoluciones por pulso abajo costo en comparacion con un servo de precision industrial
 - Actadores neumáticos vs. Actuadores hidráulico:
   - Diferencia:La neumática utiliza aire comprimido lo que le permite cargas moderada y altas velocidades,mientras que la hidráulica utiliza aceite lo que le permite mayor carga en pocas palabras para cargas mucho mas pesadas
   - Situacion de eleccion:elegiria un actuador hidraulico si se tratara de un brazo de una grúa excabadora porque gracias a que es aceite y no aire lepermite generar mayor potencia y mayor rigides

## 6.Sensores y actuadores en un sistema real
- sistema celeccionado:Aire acondicionado automático
 - sensores identificados:
    1. Sensor de temperatura ambiente:Mide la temperatura de el aire en la habitacion para saber si debe enfriar o calentar
    2. sensor de humedad:Monitorea la saturación de humedad en el ambiente para regular el nivel de confort
    3. Sensor de presencia(infrarrojo):Detecta si hay personas en la sala para activar el modo de ahorro de energético si el espacio esta vacio
 - Actuadore identificados:
    1. Motor compresor(Electrico):Comprime y circula el refrigerante para enfriar el serpentin del sistema
    2. Motor de persianas/louvers(servomotor/paso a paso):Modifica la dirección fisica hacia donde fluye el aire frio dentro de la habitación
### Diagrama funcional del sistema
[ Sensor de temperatura ] ----(Señal eléctrica)----->[ Microcontrolador / sistema de control ]
[ sensor de humedad ] ----(Señal eléctrica)----> [(Toma de decisiones)]                              
         |
         (Señal de control de potencia)
         /                           \
      [motor compresor]  [servomotor de percianas]
[ sensor de presencia ] ---(Señal electrica) ----

## 7.Seleccion de componentes
1. Detectar si una persona se encuentra frente a una puerta automática:
    - Componente: Sensor ultrasónico o sensor de presencia infrarrojo (PIR).
    - ​Razón: Permiten detectar el movimiento o la presencia de un cuerpo a distancia sin requerir contacto físico.
2. ​Medir la temperatura dentro de un salón:
    - ​Componente: Sensor de temperatura digital (ej. DHT22 o LM35).
    - ​Razón: Son precisos para rangos ambientales cotidianos y entregan lecturas sencillas para monitoreo continuo.
3. ​Detectar el nivel de agua de un depósito:
    - ​Componente: Sensor ultrasónico de distancia o sensor de nivel resistivo/capacitivo.
   - ​Razón: Miden sin contacto directo o mediante flotadores/conductividad la altura exacta del líquido disponible.
4. ​Mover una rueda de un robot móvil:
   - ​Componente: Motor de corriente directa (DC) con caja reductora.
   - Razón: Proporcionan tracción continua, alta velocidad y facilidad de control de giro por modulación de voltaje.
5. ​Controlar con precisión el ángulo de una pequeña articulación robótica:
   - ​Componente: Servomotor.
   - Razón: Posee un sistema interno de control que permite posicionar la articulación en un ángulo exacto de forma confiable. 
6. Empujar una pieza en una línea de producción:
   - Componente: Cilindro neumático.
   - Razón: Ofrece una acción lineal rápida, con alta frecuencia de ciclo y gran fuerza para tareas repetitivas de expulsión.
7. ​Medir la distancia entre un robot y una pared:
   - Componente: Sensor de distancia láser (LiDAR) o ultrasónico (ej. HC-SR04).
   - ​Razón: Permiten calcular distancias precisas mediante el tiempo de rebote de ondas o haces de luz.
8. ​Detectar si una habitación está iluminada:
   - ​Componente: Fotorresistencia (LDR) o sensor de luz ambiental (ej. BH1750).
   - ​Razón: Modifican sus propiedades eléctricas de manera proporcional a la cantidad de luz visible presente en el entorno.
## ​Reflexión final
​Medir una variable implica un proceso pasivo o de adquisición de información donde el sistema comprende el estado físico del mundo mediante señales eléctricas mientras que realizar una acción física requiere transformar energía para alterar mover o intervenir directamente en el entorno. Un sistema mecatrónico necesita ambos elementos porque la automatización inteligente es un ciclo cerrado: sin los sensores el sistema estaría "ciego" y sin los actuadores estaría "paralizado" siendo incapaz de responder o adaptarse a los cambios del medio. Entre los elementos investigados el servomotor me pareció el más interesante ya que combina un motor eléctrico convencional con un sistema de control en lazo cerrado capaz de otorgar precisión milimétrica en el posicionamiento angular mostrando cómo la electrónica y la mecánica se fusionan con elegancia.
## ​Referencias
 1. Ogata, K. (2010). Ingeniería de Control Moderna (5ª ed.). Pearson Educación.
 2. ​Bolton, W. (2016). Mecatrónica: Sistemas de control electrónico en la ingeniería mecánica y eléctrica (6ª ed.). Cengage Learning.
 3. National Instruments Corporation. (2023). Guía técnica sobre sensores y actuadores para sistemas de adquisición de datos. Disponible en recursos técnicos de instrumentación industrial.