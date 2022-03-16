MIPS_TYPES = {
    'int':'.word',
    'str':'.asciiz',
}

RESULT_REGISTER = '$t0'
LEFT_REGISTER = '$t1'
RIGHT_REGISTER = '$t2'


def printInti(n:int):
    printInstruction('li', ['$v0', 1])
    printInstruction('li', ['$a0', n])
    printInstruction('syscall')
    nuevaLinea()

def printTexto():  
    print('.text')

def printInt(name:str):
    printInstruction('li', ['$v0', 1])
    printInstruction('lw', ['$a0', name])
    printInstruction('syscall')
    nuevaLinea()

def generateAssignment(id, value=None, type='int'):
    generarLabel(id, value, type)

def generateReAssignment(id:str, newvalue:int):
    printInstruction('la', ['$a0', id])      
	# obtener dirección
    printInstruction('move', ['$a1', RESULT_REGISTER])
	# asignar val en v0
    printInstruction('sw', ['$a1', '0($a0)']) 
	# guardar nuevo valor
    

def Sum(left:int, right:int):
    cargarValores(left, right)
    printInstruction('addu', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])

def Rest(left:int, right:int):
    cargarValores(left, right)
    printInstruction('subu', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])

def Mult(left:int, right:int):
    cargarValores(left, right)
    printInstruction('mul', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])
    

def Div(left:int, right:int):
    cargarValores(left, right)
    printInstruction('div', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])


def DataSegment(memory):
    print('.data')
    generarLabel('newline', value='\\n', type='str')
    for key, val in memory.items():
        if val is not None:
            generarLabel(key, val)
        else:
            generarLabel(key)

def generarLabel(id, value=None, type='int'):
    if value is not None:
        if type=='str':
            value = '"'+str(value)+'"'
        else:
            value = str(value)
        line = '\t' + f'{id}:' + '\t' + MIPS_TYPES[type] + ' ' + value
    else:
        line = '\t' + f'{id}:'
    print(line)

def printInstruction(inst:str, args:list[str]=[], tabs:int=1):
    args = [str(x) for x in args]
    line = '\t'*tabs + inst + ' ' + ','.join(args)
    print(line)

def cargarValores(left, right):
    printInstruction('li', ['$t1', left])
    printInstruction('li', ['$t2', right])

def nuevaLinea():
    printInstruction('li', ['$v0', 4]) #li $v0, 4      
    printInstruction('la', ['$a0', 'newline'])
    printInstruction('syscall')

def Imprimir(s:str):
    raise NotImplementedError
    args = ['$a0', s]
    printInstruction('la', args)
    nuevaLinea()
    