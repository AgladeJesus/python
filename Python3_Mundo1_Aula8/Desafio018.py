import math

ang = float(input('Digite um ângulo: '))
sn = math.sin(ang)
csn = math.cos(ang)
tgt = math.tan(ang)

print('O ângulo de {}º tem Seno de {}'. format(ang, sn))
print('O ângulo de {}º tem Coseno de {}'. format(ang, csn))
print('O ângulo de {}º tem Tangente de {}'. format(ang, tgt))