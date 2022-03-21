# Manual de cricricri para NVDA

Pequeño complemento que nos ayudara a cambiar la fecha de los manifiestos.

Ahora según la última política de NVDA y hasta nuevos cambios, cada año en la primera versión de NVDA los programadores tendrán que cambiar la versión para hacer coincidir su manifiesto con la versión de NVDA.

Bien habrá programadores que lo hagan inmediatamente, otros que tarden y otros que simplemente no lo harán por abandono de complementos o por cualquier motivo.

En este ultimo caso nos tocara hacer el cambio de la propiedad lastTestedNVDAVersion a mano y si tenemos muchos complementos tendremos que perder el tiempo, además que no es una tarea para todos los usuarios ya que hay muchos niveles de usuarios.

También si queremos probar las betas y las RC tendremos que cambiar este parámetro en los manifiestos de lo contrario no podremos tener instalado el complemento.

Bien cricricri nos ayuda en esta tarea haciendo el proceso por nosotros y rápidamente.

## Uso de cricricri

Cricricri puede ser lanzado desde el menú Herramientas / Cambiador de fechas para los manifiestos o agregarle un atajo en Preferencias / Gestos de entrada y buscar la categoría cricricri.

Una vez abierto la ventana es sencilla tendremos una lista con nuestros complementos y su versión en el manifiesto.

Podremos elegir los que deseemos.

Si tabulamos tenemos dos botones, seleccionar todo o deseleccionar todo, poco que decir esto actuara sobre la lista de complementos.

Si tabulamos caeremos en tres cuadros combinados:

* Seleccione versión Mayor: Este cuadro combinado tiene que coincidir con la fecha de la versión que va a tener NVDA.

* Seleccione versión Menor: Aquí con dejarlo en 1 es suficiente no obstante e puesto las cuatro versiones que salen anuales por si hubiese cambios. (Cualquier cosa puede pasar)

* Seleccione una revisión: En este cuadro combinado con dejarlo a 0 es suficiente no obstante he puesto hasta 5 también por si acaso.

Si tabulamos caeremos en el botón Aplicar cambios a los manifiestos el cual empezara el proceso de modificar los manifiestos a aquellos complementos que tengamos seleccionados en la lista.

Si tabulamos otra vez caeremos en el botón cerrar que cerrara la ventana sin hacer ninguna acción.

## Teclas rápidas

* Alt+L: Nos lleva rápidamente a la lista de complementos.
* Alt+S: Nos selecciona todos los complementos.
* Alt+D: Nos deselecciona todos los complementos que estén marcados.
* Alt+A: Empezara la modificación de los manifiestos de aquellos complementos que tengamos seleccionados.
* Alt+C o Escape: Cerrara la ventana sin realizar ninguna acción.

## Observaciones del autor

Bien NVDA es un lector en constante evolución por lo que muchas veces hay complementos que se quedan en el camino por falta de desarrollo y por falta de adaptarlos a los cambios que NVDA en su evolución trae.

Esto quiere decir que el cambiar la fecha en los manifiestos soluciona un problema momentáneo para poder seguir usando esos complementos que no se actualizan o que el desarrollador tarda en actualizarlos. Pero habrá complementos que no solo sirva el cambiar el manifiesto y necesiten de cambios internos para adaptarse a las nuevas versiones, en ese caso el complemento se romperá y solo queda ponerse en contacto con el autor de dicho complemento.

Bien aconsejo actualizar los complementos que salgan ya con los cambios en los manifiestos aunque nosotros hallamos cambiado con cricricri la fecha ya que es posible que esos complementos traigan aparte de la adaptación del manifiesto otras modificaciones que el desarrollador haya hecho.

Decir igualmente que yo no me responsabilizo si algo se rompe por cambiar los manifiestos ya que hay cientos de complementos y puede haber alguna excepción no contemplada por mi parte.

El uso de este complemento y sus resultados queda exclusivamente bajo la responsabilidad del usuario final.
