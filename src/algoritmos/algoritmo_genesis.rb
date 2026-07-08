# Sistema de control y diccionarios

nota_final = 85.5
estado = "Aprobado"
estudiante = {"nombre" => "Carlos", "edad" => 20}
?simbolo_invalido = false # Dispara error lexico

def calcular_promedio
    suma = 80 + 90
    promedio = suma / 2
    return promedio
end

if nota_final >= 60 || estado != "Reprobado"
    puts "Materia aprobada"
else
    puts "Necesita refuerzo"
end

