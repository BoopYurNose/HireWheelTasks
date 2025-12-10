#Remember in python arrays start at 0, it's only lua where the arrays start at 1 (For the most part)

room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]

def move(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col          
  direction = input()
  if direction == 'up':
    new_row -= 1
  elif direction == 'down':
    new_row += 1
  elif direction == 'left':
    new_col -= 1
  elif direction == 'right':
    new_col += 1


  return [new_row, new_col]

new_position = move(2, 2, 'up') # its saying we start at 2, 2 in the List




# At this point, new_position should be the list [1, 2]

print(new_position)