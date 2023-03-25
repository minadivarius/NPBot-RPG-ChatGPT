# NPBot - Versión local

![](https://storage.ko-fi.com/cdn/useruploads/display/994d8c2c-a36c-47f7-adec-47da169f5034_npbot.png)

Este bot permite interactuar con **Personajes No Jugadores (NPCs) para juegos de rol y larp**, a través de la API de ChatGPT (en principio, en su modelo GPT-3.5-turbo, ya que aún no he tenido acceso a GPT-4).

He podido desarrollarlo gracias a las explicaciones del genial [MoureDev](https://mouredev.com/) en su directo de Twich.

Los archivos que encontraréis aquí están configurados para interpretar a un personaje concreto de mi rol en vivo ***Project Dark.ia - La insurrección de los cautivos*** ("coescrito" junto a ChatGPT, por cierto), que podrás descargar [aquí](https://github.com/minadivarius/LARP-AI-Design).

La modificación y utilización del bot es muy sencilla, y voy a explicarlo todo paso a paso, por lo que **no son necesarios conocimientos de programación** para adaptarlo a vuestras necesidades.

Si eres desarrollador y encuentras algún fallo o posible mejora, estaré encantada de ampliar el proyecto. Yo tan solo estoy empezando con Python :)

Tienes más información sobre aplicaciones de **IA para larp** en mi repositorio [LARP-AI-Design](https://github.com/minadivarius/LARP-AI-Design), donde también puedes compartir tus experiencias.

### ¿Bot local o bot por Discord?
Ten en cuenta que, además de este bot, también existe una versión para utilizar el **bot a través de Discord**, disponible aquí: [NPBot-RPG-ChatGPT-vDiscord](https://github.com/minadivarius/NPBot-RPG-ChatGPT-vDiscord).

En general, el bot local es potencialmente más configurable, pero editarlo requiere más conocimientos, y ahora mismo no permite acceso a través de dispositivos móviles. El bot de Discord está más limitado en cuanto a estructura y diseño, pero al ser una aplicación real resulta más accesible desde cualquier dispositivo de forma online, aunque también dependes de ella.

En esta tabla os resumo algunas de las **diferencias** que he encontrado entre ellos:

| NPBot Local | NPBot Discord  |
|--|--|
| Instalación sencilla | Instalación compleja |
| - | Dependencia de Discord |
| En principio requiere de un PC | Permite utilizar dispositivos móviles |
| Requiere descargarlo en cada dispositivo | Una vez se ejecuta en PC, el resto puede acceder online |
| Permite solo una conversación individual | Varias personas pueden interactuar al mismo tiempo con el bot y ver las interacciones de los demás |
| Prompt visible en los archivos descargados | Prompt no accesible a través de Discord |
| Interfaz configurable | Interfaz de Discord |
| Fluidez de escritura | Necesidad de usar comandos |
| Posible funcionalidad futura | Facilidad de alternar entre prompts con los comandos |
| Hay que reiniciar el programa para ver cambios en el prompt inicial | Posibilidad de editar prompts sin reiniciar Discord |
| - | Puedes montar varios bots dentro de la misma aplicación |


# Instalación del bot local

## Obtener OpenAI API Keys

Accede a tu perfil para ver tus [OpenAI API Keys](https://platform.openai.com/account/api-keys). Tendrás que crear una cuenta gratuita si aún no la tienes.

Una vez allí, crea una nueva clave y cópiala en un lugar seguro.

**Nota:** Recuerda que a diferencia de ChatGPT, su API sí es de pago. Con tu cuenta tendrás acceso a unos 18$ de tokens gratuitos durante tres meses (para que os hagáis una idea, yo todavía no he gastado ni un tercio de los mismos, así que aunque finalmente tengáis que poner vuestra tarjeta, para este tipo de usos, no creo que lleguéis a gastar más de unos céntimos al mes).


## Configurar el bot
Descarga todos los **archivos** de este repositorio (puedes hacerlo fácilmente desde la pestaña *Code > Download Zip*).

**Instala** la última versión de [Python.org](http://python.org/).

Después tendrás que instalar algunos **requerimientos**. Para ello, ejecuta los siguientes comandos en la consola o terminal de tu PC (si usas windows, escribe "cmd" en la barra de búsqueda):
```shell
pip install openai
pip install typer[all]
pip install rich
```
**Nota**: Typer y Rich no son estrictamente necesarios, pero permiten darle un toque más visual a la interfaz.

Ahora tendrás que descargar los archivos de este **repositorio** y realizar algunos cambios.
- Edita el nombre del archivo `myconfig.py` para cambiarlo a `config.py`. Modifica su contenido para poner tu **API key** de OpenAI (si no tienes algún programa como Visual Studio Code, también puedes usar el bloc de notas para editarlo).
- Borra los contenidos del archivo `prompt-npbot.docx` y escribe el **prompt** que quieras utilizar para determinar el comportamiento de tu bot. Recuerda que si escribes un prompt demasiado largo, el bot llegará antes a su límite de memoria (actualmente de unas 3.000 palabras, entre prompts + respuestas) y tendrás que reiniciar su contexto para que pueda seguir funcionando.
- En el archivo `main` puedes añadir o modificar **parámetros** de ChatGPT, como la temperatura (un número entre el 0 y el 2, que permite disminuir o aumentar la creatividad de las respuestas). Tienes más información al respecto aquí: [Chat completion - OpenAI API](https://platform.openai.com/docs/guides/chat).


## Configurar la interfaz
Para cambiar los **textos y colores** de la interfaz, también tendrás que editar el archivo `main`:

- En la sección `# Imprimir respuesta del bot`, cambia "Ordenador" por el **nombre de tu personaje.**
- En la parte de `# Permitir al usuario escribir su input`, podrías sustituir "User input: " por el nombre del personaje del jugador que está escribiendo.
- Puedes eliminar la **barra de carga** si borras los trozos de código correspondiente (solo es una barra decorativa, que resultaba atractiva para mi proyecto de ciencia ficción).
- Puedes sustituir los **textos de introducción** de "Comunicación establecida..." y "SISTEMA GUBERNAMENTAL DE COMUNICACIÓN CON EL ORDENADOR" (y como ves, también puedes incluir emojis).
- Puedes cambiar el nombre y el texto de los **comandos**, e incluso borrar la tabla si lo prefieres.
- Puedes cambiar cualquier`[color]` y estilo (negrita, subrayado, parpadeo, tachado, etc.). Tienes más información al respecto [aquí](https://typer.tiangolo.com/tutorial/printing/).


## Usar el bot
Para usar el bot tan solo tienes que **ejecutar** el archivo `main`. También puedes crear un **acceso directo** con el nombre que prefieras.

Para interactuar con él, solo tienes que escribir y pulsar intro, al igual que con ChatGPT.

Existen dos **comandos** especiales
1. Cerrar la aplicación ("**exit**")
2. Resetear la memoria del contexto del bot e iniciar una nueva conversación ("**reset**")

En un determinado punto de la conversación probablemente alcanzarás el **límite de memoria**. En este caso, surgirá un error, que puedes solucionar sin necesidad de reiniciar el programa, tan solo utilizando el comando "reset" para vaciar la memoria.


## ¿Funcionalidades futuras?
Por último, si el tiempo y los conocimientos me lo permiten, o si alguien se anima a colaborar conmigo, estas son las funcionalidades que me gustaría explorar:
1. Conseguir que la **memoria** se reinicie sola automáticamente, sin necesidad de visualizar el error y tener que ejecutar el comando "reset"
2. Posibilidad de **cambiar prompts iniciales** a través de otros comandos
3. Utilizar el **modelo GPT-4** para mejorar los resultados y ampliar la cantidad de información que podemos dar al bot (aunque habría que ver si resulta rentable, ya que por ahora es unas seis veces más caro)
 2. Introducir prompts por **voz** y obtener respuestas sonoras del bot (para simular llamadas telefónicas con los personajes)
 3. Añadir un **avatar virtual de vídeo** (para simular videollamadas con los personajes)


## Support

Si te ha resultado útil, puedes invitarme a un café: [https://ko-fi.com/albadivarius](https://ko-fi.com/albadivarius)

¡Gracias!
