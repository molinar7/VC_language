import typeChecker
import VCquadruples

#SemanticCube

cuboSemantico = [['int','int','+','int'],['int','int','-','int'],['int','int','*','int'],['int','int','/','int'],['int','int','and','error'], ['int','int','or','error'], ['int','int','<','boolean'], ['int','int','>','boolean'], ['int','int','<=','boolean'], ['int','int','>=','boolean'], ['int','int','==','boolean'], ['int','int','!=','error'],
                 ['int','float','+','int'],['int','float','-','int'],['int','float','*','int'],['int','float','/','int'],['int','float','and','error'], ['int','float','or','error'],  ['int','float','<','error'], ['int','float','>','error'], ['int','float','<=','error'], ['int','float','>=','error'], ['int','float','==','error'], ['int','float','!=','error'],
                 ['int','String','+','error'],['int','String','-','error'],['int','String','*','error'],['int','String','/','error'],['int','String','and','error'], ['int','String','or','error'], ['int','String','<','error'], ['int','String','>','error'], ['int','String','<=','error'], ['int','String','>=','error'], ['int','String','==','error'], ['int','String','!=','error'],
                 ['int','boolean','+','error'],['int','boolean','-','error'],['int','boolean','*','error'],['int','boolean','/','error'],['int','boolean','and','error'], ['int','boolean','or','error'], ['int','boolean','<','error'], ['int','boolean','>','error'], ['int','boolean','<=','error'], ['int','boolean','>=','error'], ['int','boolean','==','error'], ['int','boolean','!=','error'],

                 ['float','int','+','float'], ['float','int','-','float'], ['float','int','*','int'], ['float','int','/','int'], ['float','int','and','error'], ['float','int','or','error'], ['float','int','<','error'], ['float','int','>','error'], ['float','int','<=','error'], ['float','int','>=','error'], ['float','int','==','error'], ['float','int','!=','error'],
                 ['float','float','+','float'], ['float','float','-','float'], ['float','float','*','float'], ['float','float','/','float'], ['float','float','and','error'], ['float','float','or','error'], ['float','float','<','boolean'], ['float','float','>','boolean'], ['float','float','<=','boolean'], ['float','float','>=','boolean'], ['float','float','==','boolean'], ['float','float','!=','boolean'],
                 ['float','String','+','error'], ['float','String','-','error'], ['float','String','*','error'], ['float','String','/','error'], ['float','String','and','error'], ['float','String','or','error'], ['float','String','<','error'], ['float','String','>','error'], ['float','String','<=','error'], ['float','String','>=','error'], ['float','String','==','error'], ['float','String','!=','error'],
                 ['float','boolean','+','error'], ['float','boolean','-','error'], ['float','boolean','*','error'], ['float','boolean','/','error'], ['float','boolean','and','error'], ['float','boolean','or','error'], ['float','boolean','<','error'], ['float','boolean','>','error'], ['float','boolean','<=','error'], ['float','boolean','>=','error'], ['float','boolean','==','error'], ['float','boolean','!=','error'],

                 ['String','int','+','error'], ['String','int','-','error'], ['String','int','*','error'], ['String','int','/','error'], ['String','int','and','error'], ['String','int','or','error'], ['String','int','<','error'], ['String','int','>','error'], ['String','int','<=','error'], ['String','int','>=','error'], ['String','int','==','error'], ['String','int','!=','error'],
                 ['String','float','+','error'], ['String','float','-','error'], ['String','float','*','error'], ['String','float','/','error'], ['String','float','and','error'], ['String','float','or','error'], ['String','float','<','error'], ['String','float','>','error'], ['String','float','<=','error'], ['String','float','>=','error'], ['String','float','==','error'], ['String','float','!=','error'],
                 ['String','String','+','error'], ['String','String','-','error'], ['String','String','*','error'], ['String','String','/','error'], ['String','String','and','error'], ['String','String','or','error'], ['String','String','<','error'], ['String','String','>','error'], ['String','String','<=','error'], ['String','String','>=','error'], ['String','String','==','error'], ['String','String','!=','error'],
                 ['String','boolean','+','error'], ['String','boolean','-','error'], ['String','boolean','*','error'], ['String','boolean','/','error'], ['String','boolean','and','error'], ['String','boolean','or','error'], ['String','boolean','<','error'], ['String','boolean','>','error'], ['String','boolean','<=','error'], ['String','boolean','>=','error'], ['String','boolean','==','error'], ['String','boolean','!=','error'],
                #BRO OCUPAMOS VER SI PODREMOS SUMAR LOS STRINGS, POR EL MOMENTO LE PUSE error

                 ['boolean','int','+','error'], ['boolean','int','-','error'], ['boolean','int','*','error'], ['boolean','int','/','error'], ['boolean','int','and','error'], ['boolean','int','or','error'], ['boolean','int','<','error'], ['boolean','int','>','error'], ['boolean','int','<=','error'], ['boolean','int','>=','error'], ['boolean','int','==','error'], ['boolean','int','!=','error'],
                 ['boolean','float','+','error'], ['boolean','float','-','error'], ['boolean','float','*','error'], ['boolean','float','/','error'], ['boolean','float','and','error'], ['boolean','float','or','error'], ['boolean','float','<','error'], ['boolean','float','>','error'], ['boolean','float','<=','error'], ['boolean','float','>=','error'], ['boolean','float','==','error'], ['boolean','float','!=','error'],
                 ['boolean','String','+','error'], ['boolean','String','-','error'], ['boolean','String','*','error'], ['boolean','String','/','error'], ['boolean','String','and','error'], ['boolean','String','or','error'], ['boolean','String','<','error'], ['boolean','String','>','error'], ['boolean','String','<=','error'], ['boolean','String','>=','error'], ['boolean','String','==','error'], ['boolean','String','!=','error'],
                 ['boolean','boolean','+','error'], ['boolean','boolean','-','error'], ['boolean','boolean','*','error'], ['boolean','boolean','/','error'], ['boolean','boolean','and','boolean'], ['boolean','boolean','or','boolean'], ['boolean','boolean','<','error'], ['boolean','boolean','>','error'], ['boolean','boolean','<=','error'], ['boolean','boolean','>=','error'], ['boolean','boolean','==','boolean'], ['boolean','boolean','!=','boolean']

                ]

#len(functionDir) nos ayuda a saber en que scope nos ubicamos :)

functionDir = [[1,'global', None]] # El directorio de funciones
varsTable = [] #LA tabla de variables


indexGlobalInt = 100001 # index de la memoria virutal
indexGlobalFloat = 130001
indexGlobalString = 160001
indexGlobalBoolean = 180001

def validateSemanticCube(left_op, right_op, operator): # esta funcion comprueba las operaciones entre tipos
    for element in cuboSemantico:
        if element[0] == left_op and element [1] == right_op and element [2] == operator:
            return element[3] # Regresamos el tipo de dato de la operacion resultante


def pushTo_FunctionDir(n,t, lineno):
    if not checkIfFunctionExists(n):
        functionDir.append([ len(functionDir) + 1, n, t])
    else:
        print('ERROR:', 'The function',n, 'at line:', lineno, 'is already defined')


def pushTo_varsTable_WithCTE(n, t, v, lineno): #Append it to the varTable when defining a var with value
    if not checkIfVarIdExistsOnModule(n): # Checa que la vairable no este ya definida en el modulo actual

        if t == 'int':
            if typeChecker.isInt(v):
                if len(functionDir) == 1: # We know that is global if the index is 1
                    global indexGlobalInt
                    varsTable.append([len(functionDir), n, t, v, indexGlobalInt])
                    indexGlobalInt += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, '']) # no le he puesto un index de memoria virtual por dudas
            else:
                print('ERROOR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()


        if t == 'float':
            if typeChecker.isFloat(v):
                if len(functionDir) == 1:
                    global indexGlobalFloat
                    varsTable.append([len(functionDir), n, t, v, indexGlobalFloat])
                    indexGlobalFloat += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()


        if t == 'String':
            if typeChecker.isString(v):
                if len(functionDir) == 1:
                    global indexGlobalString
                    varsTable.append([len(functionDir), n, t, v, indexGlobalString])
                    indexGlobalString += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()


        if t == 'boolean':
            if typeChecker.isBoolean(v):
                if len(functionDir) == 1:
                    global indexGlobalBoolean
                    varsTable.append([len(functionDir), n, t, v, indexGlobalBoolean])
                    indexGlobalBoolean += 1
                else:
                    varsTable.append([len(functionDir), n, t, v, ''])
            else:
                print('ERROR:','The variable',n,'at line', lineno, 'is not a',t)
                quit()

    else:
        print('ERROR:', 'The variable',n, 'at line', lineno, 'is already defined')
        quit()


def pushTo_varsTable(n, t, lineno ): #Append it to the varTable when defining a var with NOT value

    if not checkIfVarIdExistsOnModule(n): # Checa que no exista en el modulo actual la variable

        if t == 'int':
            global indexGlobalInt
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t, '', indexGlobalInt])
                indexGlobalInt +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])

        if t == 'float':
            global indexGlobalFloat
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalFloat])
                indexGlobalFloat +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])

        if t == 'String':
            global indexGlobalString
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalString])
                indexGlobalString +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])

        if t == 'boolean':
            global indexGlobalBoolean
            if len(functionDir) == 1:
                varsTable.append([len(functionDir), n, t,'', indexGlobalBoolean])
                indexGlobalBoolean +=1
            else:
                varsTable.append([len(functionDir), n, t, '',''])


    else:
        print('ERROR:', 'The variable',n,'at line',  lineno, 'is already defined')
        quit()




def validateIDScope(v, lineno): # Esta funcion nos sirve para ver que scope tiene la id

    if checkIfVarIdExistsOnModule(v): # Se checa si existe primero en el modulo
        #print(v,'exist on module')
        for id in varsTable:
                if id[0] == len(functionDir): # si es igual a uno sabemos que es global
                    if id[1] == v:
                        return id[1], id[2],id[4] #  = varName, varType, varMemIndex

    else:
        if checkIfVarIdExistsOnGlobal(v):# Se checa si existe despues en las variables globales
           # print(v,'exist on global')
            for id in varsTable:
                if id[0] == 1: # si es igual a uno sabemos que es global
                    if id[1] == v:
                        return id[1], id[2],id[4] #  = varName, varType, varMemIndex




        else:# Si no existe en en modulo ni en las variavles globales pues no esta definida
            print('ERROR:', v, 'at line', lineno ,'does not exist, you need to define it')
            quit()





def checkIfFunctionExists(n): # check that functions do not repeat
    for nombre in functionDir:
       if n == nombre[1]:
           return True
    return False

def checkIfVarIdExistsOnModule(n): # check if Var ID exists on module
    for varID in varsTable:

        if len(functionDir) == varID[0]: # Unicamente queremos que busque en su modulo
            if varID[1] == n:
                return True
    return False

def checkIfVarIdExistsOnGlobal(n): # check if Var ID exists on global
    for varID in varsTable:
        if varID[0] == 1: # Unicamente queremos que busque en las variables globales
            if varID[1] == n:
                return True
    return False
