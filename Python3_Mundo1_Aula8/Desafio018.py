from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))
sn = sin(radians(ang))
csn = cos(radians(ang))
tgt = tan(radians(ang))

print('O ângulo de {}º tem Seno de {:.2f}'. format(ang, sn))
print('O ângulo de {}º tem Coseno de {:.2f}'. format(ang, csn))
print('O ângulo de {}º tem Tangente de {:.2f}'. format(ang, tgt))