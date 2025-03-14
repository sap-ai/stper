import func
i = 0
state = []
memory = []
file = open(input())
it = []
s = ""
l = 0
active = ""
for line in file:
   l = len(line)
   s = line[0:l]
   it.append(s)
while True:
   try:
      if state[0] == "var" and state[1] == "name added to memory" and active != "y":
         func.var(memory, 0)
         state = []
         memory = []
         active = "y"
   except:
      pass
   try:
      if state[0] == "var" and active != "y":
         state.append("name added to memory")
         memory.append(it[i])
         active = "y"
   except:
      pass
   try:
      if state[0] == "prin":
         state = []
         func.prin(exec(it[i]))
         active = "y"
   except:
      pass
   try:
      if it[i] == "print" and active != "y":
         state.append("prin")
         active = "y"
   except:
      pass
   try:
      if it[i] == "stop" and active != "y":
         active = "y"
         break
   except:
      pass
   try:
      if it[i] == "var" and active != "y":
         state.append("var")
         active = "y"
   except:
      pass
   i += 1
   active = ""
