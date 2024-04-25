lang = "05AB1E"
filename = "4"

codebase = open(lang+".codebase", "r").read()

code_utf8 = open(filename+"utf8."+lang, "r").read()

with open(filename+"."+lang, "wb") as code:
    for char in code_utf8:
        code.write(codebase.find(char).to_bytes(1, byteorder='big'))
    code.close()
