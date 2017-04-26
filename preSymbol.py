import os
import numpy

sy = ['dots', 'tan', ')', '(', '+', '-', 'sqrt', '1', '0', '3', '2', '4', '6', 'mul', 'pi', '=', 'sin', 'pm', 'A',
'frac', 'cos', 'delta', 'a', 'c', 'b', 'bar', 'd', 'f', 'i', 'h', 'k', 'm', 'o', 'n', 'p', 's', 't', 'y', 'x', 'div']
rules = {}

for i in range(0,len(sy)-1):
    rules[sy[i]] = i

#later we can do some merge rules: 0 and o, frac and bar and -, x and mul
#rules['o'] = rules['0']
#rules['frac'] = rules['-']
#rules['bar'] = rules['-']
#rules['x'] = rules['mul']

pp = pprint.PrettyPrinter(indent=4)
symbol = {}

def marklabel(f):
   ins = f.split('.')[0].split('_')
   if len(ins) > 3: # exclude the equation png only individual symbol
    #    symbol[f] = ins[3]
         symbol[f] = rules[ins[3]]
         



def main():
    dataroot = os.getcwd() + "/annotated"
    total = 0
    for f in os.listdir(dataroot):
        if f.endswith(".png"):
            marklabel(f)
            total = total + 1
    # print total
    # print (set(symbol.values()))


if __name__ == "__main__":
    main()
