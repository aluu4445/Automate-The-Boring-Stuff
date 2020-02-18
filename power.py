def power(number, exponent):

  if exponent == 0:
    return 1

  if exponent < 0:
    return 1 / number * power(number, exponent + 1)
  
  if exponent > 0:
    return number * power(number, exponent - 1)

print(power(2,1/2))
