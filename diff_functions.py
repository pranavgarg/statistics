import mul

def fact(k):
  return reduce(mul,[1]+range(1,k+1))
  
  
def binomial_distribution(p):
  n = 15
  dict = {}
  heads_range = range(0,16)
  for i in heads_range:
    dict[i] = (fact(n)/(fact(i)*fact(n-i))) * (p**i)*((1-p)**(n-i))
    print i
    print dict[i]


binomial_distribution( 0.9)   
   

def variance(data, mu):
    data.sort
    square = lambda x:x**2
    return float(sum(map(square, [(i-mu) for i in data]))/len(data))

def create_data(no, times):
    data = []
    cnt = 0
    for time in times:
      for i in range(time):
        data.append(no[cnt])
      cnt +=1 
    return data

create_data([21,24,26,29,40],[4,6,7,11,2]) 
