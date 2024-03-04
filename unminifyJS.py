import os
def unminify(filename):
    with open(filename, 'r') as file:
        code = file.read()
        
    indentation = 0
    unminified = ""
    inside_block = False
    tab = "  "
    
    for char in code:
        if char == "{":
            inside_block = True
            unminified += char + "\n" + tab * indentation
            indentation += 1
        elif char == "}":
            inside_block = False
            indentation -= 1
            unminified += "\n" + tab * indentation + char
        elif char == ";":
            unminified += char + ("\n" + tab * indentation if not inside_block else "")
        else:
            unminified += char
    
    with open(filename, 'w') as file:
        file.write(unminified)

unminify('code.js')


