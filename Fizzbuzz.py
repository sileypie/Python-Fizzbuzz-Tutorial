def fakefunction_so_the_code_works_at_the_end():


  # How to write Fizzbuzz

  # First start off by writing a loop to print 1 - 100


  for f in range(1,101):
    print(f)

  # Then you are going to figure out fizz. You want to write fizz everytime a number is divisable by 3.

  for f in range(1,101):
    if (f % 3 == 0):
      print("Fizz")
    
    else:
      print(f)

  # Then you are going to figure out buzz. You want to write buzz everytime a number is divisable by 5.

  for f in range(1,101):
    if (f % 3 == 0):
      print("Fizz")
    
    elif(f % 5 == 0):
      print("Buzz")


    else:
      print(f)
  

  # Then you are going to figure out Fizzbuzz. You want to write Fizzbuzz everytime a number is divisable by 3 and 5.


  for f in range(1,101):
    if (f % 3 == 0):
      if (f % 5 == 0):
        print("Fizzbuzz")
      else:
        print("Fizz")

    elif (f % 5 == 0):
      print("Buzz")

    else:
      print(f)




def put_code_you_want_to_test_in_here():
  # Final code
  for f in range(1,101):
    if (f % 3 == 0):
      if (f % 5 == 0):
        print("Fizzbuzz")
      else:
        print("Fizz")

    elif (f % 5 == 0):
      print("Buzz")

    else:
      print(f)







def end():
  input("Press enter to close.")
put_code_you_want_to_test_in_here()
end()