def firstNotRepeatingCharacter(string):
  chars = {}
  for c in string:
    if chars.get(c):
      chars[c] += 1
    else:
      chars[c] = 1
  for c in string:
    if chars[c] == 1:
      return c
  return "_"
