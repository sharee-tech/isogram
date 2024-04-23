def is_isogram(string):
  string = string.lower()
  newString = set()
  for char in string:
    if char == ' ' or char == '-':
      continue
    if char in newString:
      return False
    newString.add(char)

  return True


string = "ambidextrously"

print(is_isogram(string))
