MIPS_TYPES = {
    'int':'.word',
    'str':'.asciiz',
}

RESULT_REGISTER = '$t0'
LEFT_REGISTER = '$t1'
RIGHT_REGISTER = '$t2'


def printInti(n:int):
    # immediate: n is a resolved value, labeled or not
    printInstruction('li', ['$v0', 1])
    printInstruction('li', ['$a0', n])
    printInstruction('syscall')
    _addNewLine()

def printTextSegment():  # called on start of Visitor
    print('.text')

def printInt(name:str):
    # labeled int
    printInstruction('li', ['$v0', 1])
    printInstruction('lw', ['$a0', name])
    printInstruction('syscall')
    _addNewLine()

def generateAssignment(id, value=None, type='int'):
    generateLabel(id, value, type)

def generateReAssignment(id:str, newvalue:int):
    # Assumes id points to an int (.word)
    # printInstruction('lw', ['$a0', id])  #get current value
    printInstruction('la', ['$a0', id])       # get address
    printInstruction('move', ['$a1', RESULT_REGISTER])    # new val in v0
    printInstruction('sw', ['$a1', '0($a0)'])    # save new value
    
    # lw $a2, globalVariable  #get new value
    # https://stackoverflow.com/questions/45686296/how-to-modify-data-values-inside-the-text-segment-in-mips

def generateMul(left:int, right:int):
    # left and right are evaluated ints
    # load immediates to t1 and t2
    loadValues(left, right)
    printInstruction('mul', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])
    

def generateDiv(left:int, right:int):
    loadValues(left, right)
    printInstruction('div', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])


def generateAdd(left:int, right:int):
    loadValues(left, right)
    printInstruction('addu', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])

def generateSub(left:int, right:int):
    loadValues(left, right)
    printInstruction('subu', [RESULT_REGISTER, LEFT_REGISTER, RIGHT_REGISTER])


def generateDataSegment(memory):
    print('.data')
    generateLabel('newline', value='\\n', type='str')
    for key, val in memory.items():
        if val is not None:
            generateLabel(key, val)
        else:
            generateLabel(key)

def generateLabel(id, value=None, type='int'):
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

def loadValues(left, right):
    # li versus move depends on whether we copy a value or load an immediate value
    printInstruction('li', ['$t1', left])
    printInstruction('li', ['$t2', right])

def _addNewLine():
    printInstruction('li', ['$v0', 4]) #li $v0, 4      
    printInstruction('la', ['$a0', 'newline'])
    printInstruction('syscall')

def printString(s:str):
    raise NotImplementedError
    args = ['$a0', s]
    printInstruction('la', args)
    _addNewLine()
    