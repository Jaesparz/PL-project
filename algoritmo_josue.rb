=begin
Simulador de operaciones y combate
Utiliza variables, condicionales y ciclos con diferentes operadores
=end

MAX_ROUNDS = 5
round_actual = 1
estamina = 100.0
peleador_listo = true
@error_intencional = nil # Dispara error lexico

puts "Iniciando combate..."

while round_actual <= MAX_ROUNDS do
    if estamina >= 20.0 && peleador_listo == true
        estamina = estamina - 15.5
        puts "Golpe conectado"
    else
        estamina = estamina + 10.0
    end
    round_actual = round_actual + 1
end