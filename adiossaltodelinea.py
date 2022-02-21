# -*- coding: utf-8 -*-
"""
¿Los archivos de texto con saltos de línea te tocan mucho la moral
porque tienes que ir borrándolos de uno en uno y poniendo un espacio
en su lugar? ¡No llores más! Aplícales este simpático script y
se acabaron tus problemas.
"""

orig = open("nombre_archivo_original.txt","r",encoding='utf-8') #Abrimos el archivo original, especificando la codificación.
arreglao = open("arreglao.txt","w+",encoding='utf-8') #Lo mismo, en modo escritura, con el archivo arreglao.
for line in orig.readlines(): #Para cada línea del archivo original...
    arreglao.writelines(line.replace("\n"," ")) #...reemplazamos el salto de línea \n por un espacio.
orig.close()
arreglao.close()
#Y ya está.
