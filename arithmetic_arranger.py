def arithmetic_arranger(problems):
  
  collected_problems = []
  arranged_problems ="default arranged_problems"

  # If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
  if(len(problems) >5):
    return "Error: Too many problems."
    print(len(problems))
    exit()

  for item in problems:
    
    item_pieces = item.split(' ')
    first_operand = item_pieces[0]
    op = item_pieces[1] 
    second_operand = item_pieces[2]

    # Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.

    # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    
    # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    if op == "+":
      result = int(first_operand) + int(second_operand)
    elif op == "-":
      result = int(first_operand) - int(second_operand)
    else:
      return "Error: Operator must be '+' or '-'."
      exit()
      
    item_string = first_operand + '\n' + op + "\n" + second_operand + "\n" + str(result)
    print("Successful coding output per item: ", item_string)
    collected_problems.append(item_string)

  arranged_problems = collected_problems
  return arranged_problems