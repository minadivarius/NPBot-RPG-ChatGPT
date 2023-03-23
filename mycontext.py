import docx2txt

# Lee el archivo de Word
prompt = docx2txt.process('prompt-npbot.docx')

# Reemplaza todas las ocurrencias de salto de línea por el carácter de escape \n
prompt = prompt.replace('\r', '').replace('\n', '\n')

# Asigna el texto al valor "content" del diccionario "context"
context = {"role": "system", "content": prompt}
