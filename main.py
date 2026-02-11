import os
from collections import Counter
from lexer import tokenize # Esto ahora funcionará porque ya guardaste lexer.py

def analizar_archivo_usuario():
    nombre_archivo = input("Introduce el nombre del archivo Docker: ")
    
    if not os.path.exists(nombre_archivo):
        print(f" El archivo {nombre_archivo} no existe.")
        return

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()

        tokens_encontrados = list(tokenize(contenido))
        

        conteos = Counter(tipo for tipo, valor in tokens_encontrados)

        with open("reporte_analisis.txt", "w", encoding="utf-8") as f_rep:
            f_rep.write(f"REPORTE PARA: {nombre_archivo}\n" + "="*40 + "\n")
            f_rep.write(f"{'TIPO':<15} | {'VALOR'}\n")
            f_rep.write("-" * 40 + "\n")
            
            for tipo, valor in tokens_encontrados:
                f_rep.write(f"{tipo:<15} | {valor}\n")
            
            f_rep.write("\n" + "="*40 + "\n")
            f_rep.write("RESUMEN DE INSTRUCCIONES:\n")
            for tipo, total in conteos.items():
                f_rep.write(f"{tipo}: {total}\n")

        print(f" Análisis exitoso. Revisa 'reporte_analisis.txt'")

    except Exception as e:
        print(f" Error durante el análisis: {e}")

if __name__ == "__main__":
    analizar_archivo_usuario()