
def arithmetic_arranger(*args):
  '''
    Takes arithmatic problem, check for out of scope conditions, returns formated
    problem with optional solution

    Args:
      args[0] Problems (string): The problems in the equation
      args[1] sol_flag (Bool): Optional tag (thus * in args) to signal including solution to problem in return value

    Raises:
      # Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
      # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
      # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.

    Returns:
      String: equalation formatted with optional solution  
  
  '''

  # args[0] Problems (string): The problems in the equation
  problems = args[0]
  #args[1] sol_flag (Bool): Optional tag (thus * in args) to signal including solution to problem in return value
  sol_flag = False
  if len(args)>1:
    if args[1] == True:
      sol_flag=True
  
  row1 = ""
  row2 = ""
  row3 = ""
  row4 = ""
  arranged_problems =""

  # If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
  if(len(problems) >5):
    return "Error: Too many problems."
    print(len(problems))
    exit()

  for idx, item in enumerate(problems):
    
    item_pieces = item.split(' ')
    first_operand = item_pieces[0]
    op = item_pieces[1] 
    second_operand = item_pieces[2]

    # Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
    try: 
      int(first_operand)
      int(second_operand)
    except:
      return("Error: Numbers must only contain digits.")
      exit()
      
    # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    if (len(first_operand)>4 or len(second_operand)>4):
      return("Error: Numbers cannot be more than four digits.")
      exit()
    
    # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    if op == "+":
      result = int(first_operand) + int(second_operand)
    elif op == "-":
      result = int(first_operand) - int(second_operand)
    else:
      return "Error: Operator must be '+' or '-'." 
      exit()
      
    #format_a_problem(first_operand, op, second_operand,result)
    num1 = first_operand
    num2 = second_operand

    #creating a spacer var for the 4 space min req
    spaces = ""
    if idx < len(problems)-1:
      spaces = "    "
    else:
      spaces = ""
      
    largest_digits = len(num1) if len(num1)>len(num2) else len(num2)
    block_width = largest_digits+2
    row1 = row1 + (" "*(block_width-len(str(num1)))) + num1 + spaces
    row2 = row2 + op + (" "*(block_width-(len(num2))-1)) + num2 + spaces
    row3 = row3 + ("-"*(block_width)) + spaces
    if sol_flag == True:
      row4 = row4 + (" "*(block_width-(len(str(result))))) + str(result) + spaces

    #Leaving my prior code in for future reference per a different way of completeing the task:
      
    #print("Updated rows: \n" + row1 + '\n'+ row2 + '\n' + row3 + '\n'+ row4)
  #   item_string = format_a_problem(first_operand, op, second_operand,result)
  #   collected_raw_data.append([first_operand, op, second_operand,result])
  #   #print("Successful coding output per item: ", item_string)
  #   collected_problems.append(item_string)
  # #arranged_problems = collected_problems
  # #for item in collected_problems:
  # # print(collected_problems[0].partition('\n')[0])  
  # # print(collected_problems[1].partition('\n')[0])  
  # #print("    ".join(collected_problems))
  # #arranged_problems = ("    ".join(collected_problems[0][0]))

  # # for idx, item in enumerate(collected_problems): 
  # #   arranged_problems = arranged_problems + item.partition('\n')[0]
  # #   print ("Item: " + item)
  # #   print("idx: " + str(idx))
  #   #print("item.partition('\\n')[0]: " + item.partition('\n')[0])
  # print(collected_problems[0])
  # print(tabulate(collected_raw_data))
  
  #arranged_problems = row1 + '\n'+ row2 + '\n' + row3 + '\n'+ row4  
  arranged_problems = row1 + '\n'+ row2 + '\n' + row3
  if sol_flag == True:
    arranged_problems = arranged_problems + '\n' + row4
  return arranged_problems

#Leaving my prior code in for future reference per a different way of completeing the task:

# def format_a_problem(num1,op,num2,result):
#   #output = ""
#   largest_digits = len(num1) if len(num1)>len(num2) else len(num2)
#   block_width = largest_digits+2
#   # output = ((" "*(block_width-len(str(num1)))) + num1 + '\n' 
#   #   + op + (" "*(block_width-(len(num2))-1)) + num2 + "\n" 
#   #   + ("-"*(block_width)) + "\n" 
#   #   + (" "*(block_width-(len(str(result))))) + str(result))
#   # return output
#   row1 = row1 + (" "*(block_width-len(str(num1)))) + num1 + "    "
#   row2 = row2 + op + (" "*(block_width-(len(num2))-1)) + num2 + "    "
#   row3 = row3 + ("-"*(block_width)) + "    " 
#   row4 = row4 + (" "*(block_width-(len(str(result))))) + str(result) + "    "
