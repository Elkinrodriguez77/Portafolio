## Fuga de clientes

La Dirección de Inteligencia de Negocios de Carvajal tiene a su cargo liderar estrategias analíticas que le permitan a la compañía mejorar sus indicadores estratégicos. Una de las variables con mayor relevancia para nosotros es la fuga de los clientes, la cual ha ido creciendo sostenidamente durante los últimos años.

Teniendo en cuenta lo anterior, la Dirección considera pertinente desarrollar modelos de propensión de fuga de cada uno de sus clientes, a fin de enfocar los esfuerzos de retención. 

En su rol de científico de datos del área, se le han asignado las siguientes responsabilidades:
1.	Desarrollar un modelo de propensión de fuga que permita enfocar los esfuerzos de retención de la compañía.
2.	Diseñar una estrategia de uso de la información provista por el modelo.
3.	Proponer un diseño de experimento que permita testear tanto el modelo como la estrategia propuesta.

Para llevar a cabo esta tarea usted dispone de la siguiente información: 

* Afiliados Activos: Contiene información histórica (2017-2020) de afiliados activos. Los afiliados activos son aquellos que sostienen una relación contractual con la compañía.

* Afiliados Fugados: Contiene información histórica (2017-2020) de afiliados fugados. Los afiliados fugados son aquellos que han sido trasladados a otra administradora de fondos de pensiones (AFP), es decir, dichas personas no tienen una relación contractual con la compañía.

Glosario de Campos relacionados con las bases de datos a utilizar:

- ID: código de identificación único del afiliado o cliente
- Periodo: Periodo mensual para identificar si el cliente y/o afiliados se encuentra activo o fugado.
- Año: Periodo anual para identificar si el cliente y/o afiliados se encuentra activo o fugado.
- Estado: Denota el estado del afiliado con la compañía. Para este caso solo existirán 2 estados, activos y fugados. Un cliente solo puede tener un estado.
- Género: Clase o tipo a que pertenece una persona.
- Edad: Tiempo que ha vivido una persona desde su nacimiento
- IBC: El IBC significa Ingreso Base de Cotización y es el valor que se debe tomar como base para calcular la seguridad social y los aportes parafiscales de una persona, sea dependiente o independiente. Comúnmente se identifica como el salario de una persona.
- Ciudad: Corresponde a la ciudad de residencia del cliente o afiliado.
- Origen Afiliado: Corresponde a la procedencia del afiliado, es decir, si un afiliado tiene la marca “Vinculación Inicial” indica que el cliente fue ingresado por primera vez a una administradora de fondo de pensiones (AFP) por efecto de su primer trabajo. Si un cliente tiene la marca “Traslado de AFP” indica que el cliente fue trasladado de una AFP a otra AFP.
- Origen AFP: Denota a que AFP pertenecía el afiliado luego de haberse traslado de una AFP a otra AFP.
- Nivel de Satisfacción: Calificación sobre la percepción de servicios recibidos por parte del afiliado o cliente. La calificación varia de 1 a 10, siendo 10 la máxima calificación y 1 la mínima calificación.
- PQR: Denota si el afiliado ha realizado alguna Petición, Queja o Reclamo.


* Entregables: 

1.	Una presentación en la que se muestre lo siguiente:
a.	Análisis previo de variables.
b.	Modelo desarrollado, validación de supuestos y una breve discusión del porqué eligió este modelo. 
c.	Estrategia de uso del modelo.
d.	Diseño experimental propuesto.
2.	Código en R o Python con el procesamiento previo de la información y el modelo. Este código debe correr y los resultados deben coincidir con los expuestos en el punto anterior.
3.	Exposición de los resultados.


# Pasos para abordar la solución del caso

Para desarrollar un modelo de propensión de fuga necesitarás un conjunto de datos históricos que contengan tanto clientes que se quedaron como los que se fueron. Necesitarás definir una variable objetivo (una variable binaria que indique si un cliente se fue o no) y un conjunto de características que utilizarás para predecir esa variable objetivo. En este caso, parece que tienes una gran cantidad de características posibles, como la Edad, Género, Ciudad, Origen_Afiliado, Origen_AFP, Nivel_de_Satisfacción, etc.

1. Desarrollo del modelo de propensión de fuga:
Primero, necesitarás procesar tus datos. Es posible que necesites convertir algunas de tus características categóricas en numéricas mediante el one-hot encoding, y es posible que necesites normalizar algunas de tus características numéricas. También debes manejar los valores nulos, ya sea eliminándolos o imputándolos.

Una vez que hayas procesado tus datos, puedes dividirlos en conjuntos de entrenamiento y prueba. Luego puedes elegir un modelo para usar. Hay muchos modelos posibles para la predicción de churn, como la regresión logística, los árboles de decisión, el boosting de gradiente, las redes neuronales, etc. Puedes entrenar varios modelos y ver cuál funciona mejor en tu conjunto de prueba.

2. Estrategia de uso de la información provista por el modelo:
Una vez que tienes un modelo, puedes usarlo para predecir la propensión de fuga de tus clientes actuales. Puedes entonces enfocar tus esfuerzos de retención en los clientes que tu modelo predice que tienen un alto riesgo de churn.

Además, puedes examinar las características más importantes de tu modelo para entender qué factores están impulsando la fuga. Esto puede ayudarte a diseñar intervenciones más efectivas. Por ejemplo, si descubres que los clientes con un bajo Nivel_de_Satisfacción tienen un alto riesgo de churn, puedes centrarte en mejorar la satisfacción del cliente.

3. Diseño de un experimento para testear el modelo y la estrategia:
Para probar tu modelo y tu estrategia de retención, puedes diseñar un experimento controlado. Por ejemplo, puedes dividir a tus clientes de alto riesgo en dos grupos. En el grupo de tratamiento, implementas tu estrategia de retención, mientras que en el grupo de control, no haces nada. Luego puedes observar durante un periodo de tiempo (por ejemplo, seis meses) y ver si la tasa de churn es significativamente más baja en el grupo de tratamiento en comparación con el grupo de control.

Por último, recuerda que el desarrollo de un modelo y una estrategia de retención son procesos iterativos. Es probable que necesites revisar y ajustar tu modelo y tu estrategia con el tiempo a medida que recoges más datos y aprendes más sobre qué funciona y qué no.