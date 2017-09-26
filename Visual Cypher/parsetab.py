
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAM ID VAR_INT VAR_FLOAT VAR_STRING VAR_BOOLEAN FLOAT INT STRING BOOLEAN CARET POINT COMA OP_PLUS OP_MINUS OP_TIMES OP_DIVISION OP_EQUALS_TWO OP_NOT_EQUALS OP_LPAREN OP_RPAREN OP_EQUALS OP_LESS_THAN OP_LESS_EQUALS_THAN OP_GREATER_THAN OP_GREATER_EQUALS_THAN AND OR PRINT QUOT_MARK SEMICOLON LCURLY_BRACKET RCURLY_BRACKET VAR IF ELSE OP_PLUS_EQUALS OP_MINUS_EQUALS RETURN FUNCTION MAIN FOR VOID\n\tprogram\t\t:\tPROGRAM  ID  LCURLY_BRACKET  vars   function \tmain_function\t RCURLY_BRACKET\t\n\n\t\n\tvars\t:\t\tINT\t \t ID\t\tOP_EQUALS\tVAR_INT\t \tSEMICOLON\tvars\n\t\t\t|\t\tFLOAT\t ID\t\tOP_EQUALS\tVAR_FLOAT \tSEMICOLON\tvars\n\t\t\t|\t\tSTRING\t ID\t\tOP_EQUALS\tVAR_STRING\tSEMICOLON\tvars\n\t\t\t|\t\tBOOLEAN\t ID\t\tOP_EQUALS\tVAR_BOOLEAN\tSEMICOLON\tvars\n\t\t\t|\t\tepsilon\n\t\n\tfunction\t:\tFUNCTION\ttype\tID\t\tOP_LPAREN\tparameters OP_RPAREN\tbloque\tfunction\n\t\t\t\t|\tepsilon\n\t\n\tmain_function\t:\tMAIN\tOP_LPAREN\tOP_RPAREN\tbloque\t\n\t\n\ttype\t:\tINT\n\t\t\t|\tFLOAT\n\t\t\t|\tSTRING\n\t\t\t|\tBOOLEAN\n\t\t\t|\tVOID\n\t\n\tparameters\t:\ttype\tID\tparameters\n\t\t\t\t|\tCOMA\ttype\tID\t\tparameters\n\t\t\t\t|\tepsilon\n\t\n\tbloque\t:\tLCURLY_BRACKET\tbloque_primo\tRCURLY_BRACKET\t\n\t\n\t\n\tbloque_primo\t:\tbloque_primo\tstatement \n\t\t\t\t\t|\tepsilon\n\t\t\t\n\t\n\tstatement\t:\tassigment\n\t\t\t\t|\tif\n\t\t\t\t|\tprinter\n\t\t\t\t|\tincrement\n\t\t\t\t|\tvars\n\t\t\t\t|\tfor\n\t\t\t\t|\treturn\n\t\t\t\t|\tfunction_call\n\t\t\t\t\n\t\n\tassigment\t:\tID\tOP_EQUALS\tmega_expression\t\tSEMICOLON\n\n\t\n\tif\t:\tIF\tOP_LPAREN\tmega_expression\tOP_RPAREN\tbloque\n\t\t|\tIF\tOP_LPAREN\tmega_expression\tOP_RPAREN\tbloque\tELSE\tbloque\t\n\t\t\t\n\t\n\tprinter\t:\tPRINT\tOP_LPAREN\timpression\tOP_RPAREN\t SEMICOLON\n\n\t\n\timpression\t:\tvar_cte\n\t\t\t\t|\tvar_cte\t\tOP_PLUS\t\timpression\n\t\n\t\n\tincrement\t:\tID\tOP_PLUS_EQUALS mega_expression\tSEMICOLON\n\t\t\t\t|\tID\tOP_MINUS_EQUALS mega_expression\tSEMICOLON\n\t\t\t\t|\tID\tOP_PLUS\t\tOP_PLUS\t\tSEMICOLON\n\t\t\t\t|\tID\tOP_MINUS\tOP_MINUS\tSEMICOLON\n\t\n\tfor\t:\tFOR\t\tOP_LPAREN\tvars\tmega_expression\t\tSEMICOLON\tincrement\tOP_RPAREN\tbloque\t\n\t\n\treturn\t:\tRETURN\tID SEMICOLON\n\t\t\t|\tRETURN mega_expression SEMICOLON\n\t\n\tfunction_call :\tID\tOP_LPAREN\tfunction_call_prime\t\tOP_RPAREN\tSEMICOLON\n\t\n\tfunction_call_prime\t:\tID\tfunction_call_prime\n\t\t\t\t\t\t|\tCOMA\tID\tfunction_call_prime\n\t\t\t\t\t\t|\tepsilon\n\t\n\tmega_expression\t:\tsuper_expression\n\t\t\t\t\t|\tsuper_expression\tAND\t\tsuper_expression\n\t\t\t\t\t|\tsuper_expression\tOR\t\tsuper_expression\n\t\n\tsuper_expression\t:\texpression\n\t\t\t\t\t\t|\texpression\tOP_GREATER_THAN\t\t\t expression\n\t\t\t\t\t\t|\texpression\tOP_LESS_THAN\t\t\t expression\n\t\t\t\t\t\t|\texpression\tOP_GREATER_EQUALS_THAN\t expression\n\t\t\t\t\t\t|\texpression\tOP_LESS_EQUALS_THAN\t\t expression\n\t\t\t\t\t\t|\texpression\tOP_EQUALS_TWO\t\t\t expression\n\t\t\t\t\t\t|\texpression\tOP_NOT_EQUALS\t\t\t expression\n\n\t\n\texpression :\tterm\n\t\t\t\t|\tterm\tOP_PLUS\t\texpression\t\n\t\t\t\t|\tterm\tOP_MINUS\texpression\t\n\t\t\t\t\n\t\n\tterm\t:\tfact\n\t\t\t|\tfact\tOP_DIVISION\t\tterm\t\n\t\t\t|\tfact\tOP_TIMES\t\tterm\t\n\n\t\n\tfact\t:\tvar_cte\n\t\t\t|\tOP_LPAREN\tmega_expression\tOP_RPAREN\t\n\t\n\tvar_cte : \tID\n\t\t\t| \tVAR_INT\n\t\t\t|\tVAR_FLOAT\n\t\t\t|\tVAR_STRING\n\tepsilon : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,30,],[0,-1,]),'ID':([2,6,7,8,9,10,20,21,22,23,24,25,39,40,41,42,44,45,49,50,51,52,53,54,57,58,59,60,61,62,63,64,65,66,67,72,76,77,78,81,82,83,84,92,104,106,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,128,129,130,131,134,137,152,154,155,157,161,163,],[3,14,15,16,17,-6,32,-10,-11,-12,-13,-14,-68,-68,-68,-68,-68,55,-2,-3,-4,-5,68,-20,75,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,85,98,98,98,104,98,98,-68,98,104,134,98,-40,-41,98,98,98,98,98,98,98,98,98,98,98,98,-29,-35,-36,-37,-38,104,98,-42,-30,-32,160,-31,-39,]),'LCURLY_BRACKET':([3,37,56,135,158,162,],[4,44,44,44,44,44,]),'INT':([4,10,12,38,39,40,41,42,44,47,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,75,84,112,113,127,128,129,130,131,152,154,155,161,163,],[6,-6,21,21,6,6,6,6,-68,21,-2,-3,-4,-5,6,-20,21,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,21,6,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'FLOAT':([4,10,12,38,39,40,41,42,44,47,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,75,84,112,113,127,128,129,130,131,152,154,155,161,163,],[7,-6,22,22,7,7,7,7,-68,22,-2,-3,-4,-5,7,-20,22,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,22,7,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'STRING':([4,10,12,38,39,40,41,42,44,47,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,75,84,112,113,127,128,129,130,131,152,154,155,161,163,],[8,-6,23,23,8,8,8,8,-68,23,-2,-3,-4,-5,8,-20,23,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,23,8,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'BOOLEAN':([4,10,12,38,39,40,41,42,44,47,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,75,84,112,113,127,128,129,130,131,152,154,155,161,163,],[9,-6,24,24,9,9,9,9,-68,24,-2,-3,-4,-5,9,-20,24,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,24,9,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'FUNCTION':([4,5,10,39,40,41,42,49,50,51,52,58,74,],[-68,12,-6,-68,-68,-68,-68,-2,-3,-4,-5,-18,12,]),'MAIN':([4,5,10,11,13,39,40,41,42,49,50,51,52,58,74,96,],[-68,-68,-6,19,-8,-68,-68,-68,-68,-2,-3,-4,-5,-18,-68,-7,]),'RCURLY_BRACKET':([10,18,39,40,41,42,43,44,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,112,113,127,128,129,130,131,152,154,155,161,163,],[-6,30,-68,-68,-68,-68,-9,-68,-2,-3,-4,-5,58,-20,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'IF':([10,39,40,41,42,44,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,112,113,127,128,129,130,131,152,154,155,161,163,],[-6,-68,-68,-68,-68,-68,-2,-3,-4,-5,69,-20,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'PRINT':([10,39,40,41,42,44,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,112,113,127,128,129,130,131,152,154,155,161,163,],[-6,-68,-68,-68,-68,-68,-2,-3,-4,-5,70,-20,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'FOR':([10,39,40,41,42,44,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,112,113,127,128,129,130,131,152,154,155,161,163,],[-6,-68,-68,-68,-68,-68,-2,-3,-4,-5,71,-20,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'RETURN':([10,39,40,41,42,44,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,112,113,127,128,129,130,131,152,154,155,161,163,],[-6,-68,-68,-68,-68,-68,-2,-3,-4,-5,72,-20,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-40,-41,-29,-35,-36,-37,-38,-42,-30,-32,-31,-39,]),'OP_LPAREN':([10,19,32,39,40,41,42,49,50,51,52,68,69,70,71,72,76,77,78,82,84,92,111,114,115,116,117,118,119,120,121,122,123,124,125,],[-6,31,38,-68,-68,-68,-68,-2,-3,-4,-5,81,82,83,84,92,92,92,92,92,-68,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'VAR_INT':([10,26,39,40,41,42,49,50,51,52,72,76,77,78,82,83,84,92,111,114,115,116,117,118,119,120,121,122,123,124,125,137,],[-6,33,-68,-68,-68,-68,-2,-3,-4,-5,93,93,93,93,93,93,-68,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'VAR_FLOAT':([10,27,39,40,41,42,49,50,51,52,72,76,77,78,82,83,84,92,111,114,115,116,117,118,119,120,121,122,123,124,125,137,],[-6,34,-68,-68,-68,-68,-2,-3,-4,-5,94,94,94,94,94,94,-68,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'VAR_STRING':([10,28,39,40,41,42,49,50,51,52,72,76,77,78,82,83,84,92,111,114,115,116,117,118,119,120,121,122,123,124,125,137,],[-6,35,-68,-68,-68,-68,-2,-3,-4,-5,95,95,95,95,95,95,-68,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'VOID':([12,38,47,55,75,],[25,25,25,25,25,]),'OP_EQUALS':([14,15,16,17,68,],[26,27,28,29,76,]),'VAR_BOOLEAN':([29,],[36,]),'OP_RPAREN':([31,38,46,48,55,73,75,81,87,88,89,90,91,93,94,95,97,98,104,105,107,108,109,110,126,128,129,130,131,132,134,139,140,141,142,143,144,145,146,147,148,149,150,151,153,156,159,],[37,-68,56,-17,-68,-15,-68,-68,-46,-49,-56,-59,-62,-65,-66,-67,-16,-64,-68,133,-45,135,136,-33,151,-35,-36,-37,-38,-43,-68,-47,-48,-50,-51,-52,-53,-54,-55,-57,-58,-60,-61,-63,-44,-34,162,]),'SEMICOLON':([33,34,35,36,85,86,87,88,89,90,91,93,94,95,98,99,100,101,102,103,133,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,],[39,40,41,42,112,113,-46,-49,-56,-59,-62,-65,-66,-67,-64,127,128,129,130,131,152,155,157,-47,-48,-50,-51,-52,-53,-54,-55,-57,-58,-60,-61,-63,]),'COMA':([38,55,75,81,104,134,],[47,47,47,106,106,106,]),'ELSE':([58,154,],[-18,158,]),'OP_PLUS_EQUALS':([68,160,],[77,77,]),'OP_MINUS_EQUALS':([68,160,],[78,78,]),'OP_PLUS':([68,79,85,89,90,91,93,94,95,98,110,149,150,151,160,],[79,102,-64,122,-59,-62,-65,-66,-67,-64,137,-60,-61,-63,79,]),'OP_MINUS':([68,80,85,89,90,91,93,94,95,98,149,150,151,160,],[80,103,-64,123,-59,-62,-65,-66,-67,-64,-60,-61,-63,80,]),'OP_DIVISION':([85,90,91,93,94,95,98,151,],[-64,124,-62,-65,-66,-67,-64,-63,]),'OP_TIMES':([85,90,91,93,94,95,98,151,],[-64,125,-62,-65,-66,-67,-64,-63,]),'OP_GREATER_THAN':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,116,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'OP_LESS_THAN':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,117,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'OP_GREATER_EQUALS_THAN':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,118,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'OP_LESS_EQUALS_THAN':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,119,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'OP_EQUALS_TWO':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,120,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'OP_NOT_EQUALS':([85,88,89,90,91,93,94,95,98,147,148,149,150,151,],[-64,121,-56,-59,-62,-65,-66,-67,-64,-57,-58,-60,-61,-63,]),'AND':([85,87,88,89,90,91,93,94,95,98,141,142,143,144,145,146,147,148,149,150,151,],[-64,114,-49,-56,-59,-62,-65,-66,-67,-64,-50,-51,-52,-53,-54,-55,-57,-58,-60,-61,-63,]),'OR':([85,87,88,89,90,91,93,94,95,98,141,142,143,144,145,146,147,148,149,150,151,],[-64,115,-49,-56,-59,-62,-65,-66,-67,-64,-50,-51,-52,-53,-54,-55,-57,-58,-60,-61,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,39,40,41,42,53,84,],[5,49,50,51,52,64,111,]),'epsilon':([4,5,38,39,40,41,42,44,53,55,74,75,81,84,104,134,],[10,13,48,10,10,10,10,54,10,48,13,48,107,10,107,107,]),'function':([5,74,],[11,96,]),'main_function':([11,],[18,]),'type':([12,38,47,55,75,],[20,45,57,45,45,]),'bloque':([37,56,135,158,162,],[43,74,154,161,163,]),'parameters':([38,55,75,],[46,73,97,]),'bloque_primo':([44,],[53,]),'statement':([53,],[59,]),'assigment':([53,],[60,]),'if':([53,],[61,]),'printer':([53,],[62,]),'increment':([53,157,],[63,159,]),'for':([53,],[65,]),'return':([53,],[66,]),'function_call':([53,],[67,]),'mega_expression':([72,76,77,78,82,92,111,],[86,99,100,101,108,126,138,]),'super_expression':([72,76,77,78,82,92,111,114,115,],[87,87,87,87,87,87,87,139,140,]),'expression':([72,76,77,78,82,92,111,114,115,116,117,118,119,120,121,122,123,],[88,88,88,88,88,88,88,88,88,141,142,143,144,145,146,147,148,]),'term':([72,76,77,78,82,92,111,114,115,116,117,118,119,120,121,122,123,124,125,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,149,150,]),'fact':([72,76,77,78,82,92,111,114,115,116,117,118,119,120,121,122,123,124,125,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'var_cte':([72,76,77,78,82,83,92,111,114,115,116,117,118,119,120,121,122,123,124,125,137,],[91,91,91,91,91,110,91,91,91,91,91,91,91,91,91,91,91,91,91,91,110,]),'function_call_prime':([81,104,134,],[105,132,153,]),'impression':([83,137,],[109,156,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LCURLY_BRACKET vars function main_function RCURLY_BRACKET','program',7,'p_program','vcparser.py',9),
  ('vars -> INT ID OP_EQUALS VAR_INT SEMICOLON vars','vars',6,'p_vars','vcparser.py',16),
  ('vars -> FLOAT ID OP_EQUALS VAR_FLOAT SEMICOLON vars','vars',6,'p_vars','vcparser.py',17),
  ('vars -> STRING ID OP_EQUALS VAR_STRING SEMICOLON vars','vars',6,'p_vars','vcparser.py',18),
  ('vars -> BOOLEAN ID OP_EQUALS VAR_BOOLEAN SEMICOLON vars','vars',6,'p_vars','vcparser.py',19),
  ('vars -> epsilon','vars',1,'p_vars','vcparser.py',20),
  ('function -> FUNCTION type ID OP_LPAREN parameters OP_RPAREN bloque function','function',8,'p_function','vcparser.py',24),
  ('function -> epsilon','function',1,'p_function','vcparser.py',25),
  ('main_function -> MAIN OP_LPAREN OP_RPAREN bloque','main_function',4,'p_main_function','vcparser.py',29),
  ('type -> INT','type',1,'p_type','vcparser.py',33),
  ('type -> FLOAT','type',1,'p_type','vcparser.py',34),
  ('type -> STRING','type',1,'p_type','vcparser.py',35),
  ('type -> BOOLEAN','type',1,'p_type','vcparser.py',36),
  ('type -> VOID','type',1,'p_type','vcparser.py',37),
  ('parameters -> type ID parameters','parameters',3,'p_parameters','vcparser.py',41),
  ('parameters -> COMA type ID parameters','parameters',4,'p_parameters','vcparser.py',42),
  ('parameters -> epsilon','parameters',1,'p_parameters','vcparser.py',43),
  ('bloque -> LCURLY_BRACKET bloque_primo RCURLY_BRACKET','bloque',3,'p_bloque','vcparser.py',49),
  ('bloque_primo -> bloque_primo statement','bloque_primo',2,'p_bloque_primo','vcparser.py',55),
  ('bloque_primo -> epsilon','bloque_primo',1,'p_bloque_primo','vcparser.py',56),
  ('statement -> assigment','statement',1,'p_statement','vcparser.py',61),
  ('statement -> if','statement',1,'p_statement','vcparser.py',62),
  ('statement -> printer','statement',1,'p_statement','vcparser.py',63),
  ('statement -> increment','statement',1,'p_statement','vcparser.py',64),
  ('statement -> vars','statement',1,'p_statement','vcparser.py',65),
  ('statement -> for','statement',1,'p_statement','vcparser.py',66),
  ('statement -> return','statement',1,'p_statement','vcparser.py',67),
  ('statement -> function_call','statement',1,'p_statement','vcparser.py',68),
  ('assigment -> ID OP_EQUALS mega_expression SEMICOLON','assigment',4,'p_assigment','vcparser.py',74),
  ('if -> IF OP_LPAREN mega_expression OP_RPAREN bloque','if',5,'p_if','vcparser.py',79),
  ('if -> IF OP_LPAREN mega_expression OP_RPAREN bloque ELSE bloque','if',7,'p_if','vcparser.py',80),
  ('printer -> PRINT OP_LPAREN impression OP_RPAREN SEMICOLON','printer',5,'p_printer','vcparser.py',87),
  ('impression -> var_cte','impression',1,'p_impression','vcparser.py',92),
  ('impression -> var_cte OP_PLUS impression','impression',3,'p_impression','vcparser.py',93),
  ('increment -> ID OP_PLUS_EQUALS mega_expression SEMICOLON','increment',4,'p_increment','vcparser.py',98),
  ('increment -> ID OP_MINUS_EQUALS mega_expression SEMICOLON','increment',4,'p_increment','vcparser.py',99),
  ('increment -> ID OP_PLUS OP_PLUS SEMICOLON','increment',4,'p_increment','vcparser.py',100),
  ('increment -> ID OP_MINUS OP_MINUS SEMICOLON','increment',4,'p_increment','vcparser.py',101),
  ('for -> FOR OP_LPAREN vars mega_expression SEMICOLON increment OP_RPAREN bloque','for',8,'p_for','vcparser.py',105),
  ('return -> RETURN ID SEMICOLON','return',3,'p_return','vcparser.py',110),
  ('return -> RETURN mega_expression SEMICOLON','return',3,'p_return','vcparser.py',111),
  ('function_call -> ID OP_LPAREN function_call_prime OP_RPAREN SEMICOLON','function_call',5,'p_function_call','vcparser.py',115),
  ('function_call_prime -> ID function_call_prime','function_call_prime',2,'p_function_call_prime','vcparser.py',119),
  ('function_call_prime -> COMA ID function_call_prime','function_call_prime',3,'p_function_call_prime','vcparser.py',120),
  ('function_call_prime -> epsilon','function_call_prime',1,'p_function_call_prime','vcparser.py',121),
  ('mega_expression -> super_expression','mega_expression',1,'p_mega_expression','vcparser.py',125),
  ('mega_expression -> super_expression AND super_expression','mega_expression',3,'p_mega_expression','vcparser.py',126),
  ('mega_expression -> super_expression OR super_expression','mega_expression',3,'p_mega_expression','vcparser.py',127),
  ('super_expression -> expression','super_expression',1,'p_super_expression','vcparser.py',132),
  ('super_expression -> expression OP_GREATER_THAN expression','super_expression',3,'p_super_expression','vcparser.py',133),
  ('super_expression -> expression OP_LESS_THAN expression','super_expression',3,'p_super_expression','vcparser.py',134),
  ('super_expression -> expression OP_GREATER_EQUALS_THAN expression','super_expression',3,'p_super_expression','vcparser.py',135),
  ('super_expression -> expression OP_LESS_EQUALS_THAN expression','super_expression',3,'p_super_expression','vcparser.py',136),
  ('super_expression -> expression OP_EQUALS_TWO expression','super_expression',3,'p_super_expression','vcparser.py',137),
  ('super_expression -> expression OP_NOT_EQUALS expression','super_expression',3,'p_super_expression','vcparser.py',138),
  ('expression -> term','expression',1,'p_expression','vcparser.py',143),
  ('expression -> term OP_PLUS expression','expression',3,'p_expression','vcparser.py',144),
  ('expression -> term OP_MINUS expression','expression',3,'p_expression','vcparser.py',145),
  ('term -> fact','term',1,'p_term','vcparser.py',151),
  ('term -> fact OP_DIVISION term','term',3,'p_term','vcparser.py',152),
  ('term -> fact OP_TIMES term','term',3,'p_term','vcparser.py',153),
  ('fact -> var_cte','fact',1,'p_fact','vcparser.py',158),
  ('fact -> OP_LPAREN mega_expression OP_RPAREN','fact',3,'p_fact','vcparser.py',159),
  ('var_cte -> ID','var_cte',1,'p_var_cte','vcparser.py',163),
  ('var_cte -> VAR_INT','var_cte',1,'p_var_cte','vcparser.py',164),
  ('var_cte -> VAR_FLOAT','var_cte',1,'p_var_cte','vcparser.py',165),
  ('var_cte -> VAR_STRING','var_cte',1,'p_var_cte','vcparser.py',166),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','vcparser.py',170),
]
