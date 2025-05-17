# Modelado
## Práctica 3:

### Gráfica de la posición de las ruedas:
![grafica_posicion](https://github.com/user-attachments/assets/e4a3ba79-91b7-44de-9d9a-5da35c1f7f27)

En esta gráfica podemos ver como varía la posición de cada una de las ruedas con respecto al tiempo, vemos que hay algunos picos debido a la inercia y a que me pasñe un poco de más en la teleoperación del robot y tuve que retroceder.


### Gráfica de la aceleración:
![grafica_aceleracion](https://github.com/user-attachments/assets/e646c075-fb7f-46a0-9efe-575795ca818f)

En esta gráfica podemos ver como varía la aceleración medida por el IMU con respecto al tiempo, se ve que la aceleración en el eje z es cercana a 9.8, es decir es la gravedad, y la aceleración en x e y es la del porpio robot que se ve que es bastante estable, excepto algún pico propio de cuando hay un cambio de velocidad brusco ya sea al commienzo de la teleoperación del robot, cuando tuve que retroceder o cuando paro por completo el robot, para empezar el pick and place.


### Gráfica del gasto:
![grafica_gasto](https://github.com/user-attachments/assets/d1f16bd7-587f-4368-ab39-ada51939deb8)

En esta gráfica podemos ver como varía el gasto de las articulaciones con respecto al tiempo, los picos son debidos a los períodos de tiempo donde decido a donde mover el brazo para hacer correcta la tarea de pick and place, así como ciando hay más de una articulación involucrada en el movimiento.


El rosbag está [aquí](https://urjc-my.sharepoint.com/:f:/g/personal/j_delatorre_2020_alumnos_urjc_es/Elf6rD7dyq5DkaHWPleVnyQBd2jt9Dj-LXH4SfpJGTLh3g?e=u0uat0)
