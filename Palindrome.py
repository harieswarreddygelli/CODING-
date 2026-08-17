def palindrome(a):
  sum,temp=0,a
  while temp:
    digit=temp%10
    sum+=temp
    temp//=10
  if a==sum:
    return True
  else:
    return False
a=int(input("Enter a number"))
if palindrome(a):
  print("The entered number is a palindrome")
else:
  print("The entered number is not a palindrome")
  
    
    
  
