import math

ang = float(input('Digite um ângulo: '))
sn = math.sin(math.radians(ang))
csn = math.cos(math.radians(ang))
tgt = math.tan(math.radians(ang))

print('O ângulo de {}º tem Seno de {:.2f}'. format(ang, sn))
print('O ângulo de {}º tem Coseno de {:.2f}'. format(ang, csn))
print('O ângulo de {}º tem Tangente de {:.2f}'. format(ang, tgt))