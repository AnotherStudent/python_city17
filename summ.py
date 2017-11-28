def summ(count):
  assert(type(count) == int)
  assert(count >= 2)

  result = []

  for i in range(10**(count-1),10**count):
    sum = 0;
    for c in str(i):
      sum += int(c)**2

    if sum % 17 == 0:
      result.append(i)

  return result

def work():
  i = int(input())
  l = summ(i)
  print(l)

if __name__ == '__main__':
	work()
