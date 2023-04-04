from rich.table import Table  # pip install rich // Crear tabla de comandos
from rich import print  # Mejorar la impresión de forma más visual
import typer  # pip install "typer[all]" // Interactividad en terminal
import openai  # pip install openai // Librería de OpenAI
import math  # Para la barra de progreso
import config  # Importar configuración con la key personal
import mycontext  # Importar el prompt inicial del sistema del otro archivo
import traceback  # Detectar errores
from datetime import datetime


# Función principal de la aplicación

def main():

    openai.api_key = config.api_key  # Establecer key personal

    log_file = open("conversation_log.txt", "a")  # Abrir archivo de registro

    # Imprimir barra de progreso ficticia con la función definida más abajo
    numbers = [x * 5 for x in range(2000, 3000)]
    results = []
    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i + 1, len(numbers))

    print("\n\n[green blink]Comunicacion establecida...[/green blink]")

    print("[bold cyan]\n\n\n 🌐 SISTEMA GUBERNAMENTAL DE COMUNICACIÓN CON EL ORDENADOR (SGCEO) 🌐[/bold cyan]\n")

    # Crear tabla de comandos
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de SGCEO")
    table.add_row("reset", "Nueva comunicación / Depuración de errores")
    print(table)
    print("[bright_black]\nIntroduzca su petición o comando para continuar. \n\n[Identificación biométrica requerida][/bright_black]\n")

    # Contexto del asistente
    context = mycontext.context
    messages = [context]

    # Crear bucle para que nos permita seguir preguntando más de una vez
    while True:

        # Permitir al usuario escribir su input llamando a la función definida más abajo
        content = __prompt()

        # Habilitar comando para empezar un nuevo chat
        if content == "reset":
            print("[bright_cyan]\n🔄️ Nueva comunicación generada[/bright_cyan]")
            messages = [context]
            content = __prompt()

        # Añadir preguntas previas al contexto
        messages.append({"role": "user", "content": content})

        # Añadir excepción para controlar errores
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=1.1,
                messages=messages)
        except Exception:
            print("Ha ocurrido un error")
            print(traceback.format_exc())
            continue

        # Variable para almacenar únicamente la respuesta del chatbot
        response_content = response.choices[0].message.content

        # Añadir su respuesta previa al contexto
        messages.append({"role": "assistant", "content": response_content})

        # Imprimir únicamente la respuesta del chatbot
        if response_content:
            print(
                f"[cyan bold]\n\nOrdenador:[/cyan bold] [bright_cyan]{response_content}\n[/bright_cyan]")

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual

        # Crea una cadena con el mensaje y la marca de tiempo
        log_entry = f"[{timestamp}] User: {content}\n Ordenador: {response_content}\n"

        # Escribe la entrada de registro en el archivo
        log_file.write(log_entry)

    log_file.close()  # Cierra el archivo de registro al salir del bucle principal


# Función de la barra de progreso ficticia
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def __prompt():
    # Permitir al usuario escribir su input
    prompt = typer.prompt("\nUser input")

    # Habilitar comando para interrumpir el programa
    if prompt == "exit":
        print("\r")
        salir = typer.confirm(
            "⚠️ ¿Seguro que quieres salir de SGCEO? Se perderán los datos de contexto de su comunicación ⚠️")
        if salir:
            raise typer.Abort()
        return __prompt()

    return prompt


# Ejecutar la función principal de la aplicación con typer
if __name__ == "__main__":
    typer.run(main)
