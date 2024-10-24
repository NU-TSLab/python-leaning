import itertools
import sys

def solve_equation(nums):

  operations = ['+', '-', '*', '/']
  for permutation in itertools.permutations(nums):
    for op_combination in itertools.product(operations, repeat=3):
      equation = f"{permutation[0]} {op_combination[0]} {permutation[1]} {op_combination[1]} {permutation[2]} {op_combination[2]} {permutation[3]}"
      try:
        result = eval(equation)
        if result == 10:
          return equation
      except ZeroDivisionError:
        pass  # Skip cases with division by zero
  return None

if __name__ == "__main__":
  if len(sys.argv) != 5:
    print("Please provide four integers from 1 to 9 as command line arguments.")
  else:
    nums = [int(arg) for arg in sys.argv[1:]]
    solution = solve_equation(nums)
    if solution:
      print(f"Solution found: {solution} = 10")
    else:
      print("No solution found.")