from theoretical import *
#import theoretical as theo (then use theo.calculation())

def my_fac(n):

  if n == 0:
    return 1
  else:
    return n * my_fac(n-1)

def my_choice(n,k):

  return my_fac(n) / (my_fac(n-k) * my_fac(k))

def main():

  n = int(input("Please enter the total number of items: "))
  k = int(input("Please enter how many items you want to choose from: "))

  if(k > n):
    
    print("The number of items you selected is greater than the total number of items.")
    return

  if(n == k):
    
    print(n,"choose",k,"=",1)

  else: 

    answer = my_choice(n,k)
    print(n,"choose",k,"=",answer)
    answer2 = calculation()
    print("The theoretical probablity of choosing 40 red and 20 white balls is:",answer2 * 100,"%")
    # | theo minus actual / theo |
    

if __name__ == '__main__':
  main()
