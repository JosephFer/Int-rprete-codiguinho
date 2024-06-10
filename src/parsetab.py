
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftT_SUMAT_RESTAleftT_MULTIPLICACIONT_DIVISIONleftT_MAYORQUET_MENORQUET_MAYOROIGUALT_MENOROIGUALT_IGUALT_DIFERENTEleftT_ANDT_ORrightT_NOTT_AND T_ASIGNACION T_BOOL T_BREAK T_CADENA T_COMA T_DIFERENTE T_DIVISION T_DO T_ELIF T_ELSE T_ENTERO T_FALSE T_FINDELINEA T_FLOTANTE T_FOR T_FUNCION T_IF T_IGUAL T_IN T_LLAVEDERECHA T_LLAVEIZQUIERDA T_MAYOROIGUAL T_MAYORQUE T_MENOROIGUAL T_MENORQUE T_MULTIPLICACION T_NOT T_NUMERO T_OR T_PDERECHA T_PIZQUIERDA T_PRINT T_RANK T_RESTA T_RETURN T_STRING T_SUMA T_TRUE T_VARIABLE T_WHILEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : expression T_FINDELINEA\n                 | assignment T_FINDELINEA\n                 | declaration T_FINDELINEA\n                 | conditional T_FINDELINEA\n                 | loop_while T_FINDELINEA\n                 | loop_for T_FINDELINEA\n                 | loop_do_while T_FINDELINEA\n                 | function_declaration T_FINDELINEA\n                 | return_statement T_FINDELINEA\n                 | break_statement T_FINDELINEA\n                 | statement_print T_FINDELINEAexpression : term\n                  | expression T_SUMA term\n                  | expression T_PDERECHA term\n                  | expression T_PIZQUIERDA term\n                  | expression T_RESTA term\n                  | expression T_MULTIPLICACION term\n                  | expression T_DIVISION term\n                  | expression T_MAYORQUE expression\n                  | expression T_MENORQUE expression\n                  | expression T_MAYOROIGUAL expression\n                  | expression T_MENOROIGUAL expression\n                  | expression T_IGUAL expression\n                  | expression T_DIFERENTE expression\n                  | T_NOT expression\n                  | expression T_AND expression\n                  | expression T_OR expressionterm : T_NUMERO\n            | T_VARIABLE\n            | T_TRUE\n            | T_FALSE\n            | T_STRING\n            | rank_functionassignment : T_VARIABLE T_ASIGNACION expressiondeclaration : T_ENTERO assignment\n                   | T_FLOTANTE assignment\n                   | T_BOOL assignment\n                   | T_CADENA assignment\n                   | T_ENTERO T_VARIABLE\n                   | T_FLOTANTE T_VARIABLE\n                   | T_BOOL T_VARIABLE\n                   | T_CADENA T_VARIABLEconditional : T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA\n                   | T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_ELSE T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHAloop_while : T_WHILE T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHArank_function : T_RANK T_PDERECHA expression T_COMA expression T_COMA expression T_PIZQUIERDAloop_for : T_FOR T_VARIABLE T_IN rank_function T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHAloop_do_while : T_DO T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_WHILE T_PDERECHA expression T_PIZQUIERDAparameter_list : T_VARIABLE\n                      | parameter_list T_COMA T_VARIABLEfunction_declaration : T_FUNCION T_PDERECHA parameter_list T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHAreturn_statement : T_RETURN expression\n                        | T_RETURNstatement_print : T_PRINT T_PDERECHA expression T_PIZQUIERDAbreak_statement : T_BREAK'
    
_lr_action_items = {'T_NOT':([0,2,3,16,28,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,99,111,112,113,114,116,119,120,121,122,123,124,134,135,],[16,16,-3,16,16,-2,-4,16,16,16,16,16,16,16,16,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'T_VARIABLE':([0,2,3,16,18,19,20,21,24,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,77,79,80,99,104,105,109,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[17,17,-3,63,66,68,70,72,75,63,-2,-4,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,63,63,63,17,101,63,63,17,63,63,117,63,63,17,17,17,17,17,17,17,63,17,63,63,63,17,17,]),'T_ENTERO':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[18,18,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,18,18,18,18,18,18,18,18,18,18,18,18,]),'T_FLOTANTE':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[19,19,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,19,19,19,19,19,19,19,19,19,19,19,19,]),'T_BOOL':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[20,20,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,20,20,20,20,20,20,20,20,20,20,20,20,]),'T_CADENA':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[21,21,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,21,21,21,21,21,21,21,21,21,21,21,21,]),'T_IF':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[22,22,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,22,22,22,22,22,22,22,22,22,22,22,22,]),'T_WHILE':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,107,112,113,114,116,119,120,121,123,134,135,],[23,23,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,23,23,115,23,23,23,23,23,23,23,23,23,23,]),'T_FOR':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[24,24,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,24,24,24,24,24,24,24,24,24,24,24,24,]),'T_DO':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[26,26,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,26,26,26,26,26,26,26,26,26,26,26,26,]),'T_FUNCION':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[27,27,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,27,27,27,27,27,27,27,27,27,27,27,27,]),'T_RETURN':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[28,28,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,28,28,28,28,28,28,28,28,28,28,28,28,]),'T_BREAK':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[29,29,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,29,29,29,29,29,29,29,29,29,29,29,29,]),'T_PRINT':([0,2,3,36,37,52,53,54,55,56,57,58,59,60,61,76,99,112,113,114,116,119,120,121,123,134,135,],[30,30,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,30,30,30,30,30,30,30,30,30,30,30,30,]),'T_NUMERO':([0,2,3,16,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[31,31,-3,31,31,-2,-4,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'T_TRUE':([0,2,3,16,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[32,32,-3,32,32,-2,-4,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'T_FALSE':([0,2,3,16,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[33,33,-3,33,33,-2,-4,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'T_STRING':([0,2,3,16,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[34,34,-3,34,34,-2,-4,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'T_RANK':([0,2,3,16,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,73,74,76,79,80,98,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[35,35,-3,35,35,-2,-4,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'$end':([1,2,3,36,37,52,53,54,55,56,57,58,59,60,61,],[0,-1,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,]),'T_LLAVEDERECHA':([3,36,37,52,53,54,55,56,57,58,59,60,61,99,119,120,121,123,135,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,107,125,126,127,129,136,]),'T_FINDELINEA':([4,5,6,7,8,9,10,11,12,13,14,15,17,25,28,29,31,32,33,34,62,63,65,66,67,68,69,70,71,72,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,110,125,126,127,129,132,133,136,],[37,52,53,54,55,56,57,58,59,60,61,-15,-32,-36,-56,-58,-31,-33,-34,-35,-28,-32,-38,-42,-39,-43,-40,-44,-41,-45,-55,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,-37,-57,-46,-48,-50,-54,-51,-49,-47,]),'T_SUMA':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[38,-15,-32,-36,-31,-33,-34,-35,-28,-32,38,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,38,38,38,38,38,38,38,38,-49,]),'T_PDERECHA':([4,15,17,22,23,25,27,30,31,32,33,34,35,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,115,118,128,130,133,],[39,-15,-32,73,74,-36,77,79,-31,-33,-34,-35,80,-28,-32,39,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,39,39,39,39,39,122,39,39,39,-49,]),'T_PIZQUIERDA':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,101,102,103,117,118,128,130,133,],[40,-15,-32,-36,-31,-33,-34,-35,-28,-32,40,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,40,104,105,108,-52,110,40,-53,40,132,133,-49,]),'T_RESTA':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[41,-15,-32,-36,-31,-33,-34,-35,-28,-32,41,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,41,41,41,41,41,41,41,41,-49,]),'T_MULTIPLICACION':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[42,-15,-32,-36,-31,-33,-34,-35,-28,-32,42,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,42,42,42,42,42,42,42,42,-49,]),'T_DIVISION':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[43,-15,-32,-36,-31,-33,-34,-35,-28,-32,43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,43,43,43,43,43,43,43,43,-49,]),'T_MAYORQUE':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[44,-15,-32,-36,-31,-33,-34,-35,-28,-32,44,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,44,44,44,44,44,44,44,44,-49,]),'T_MENORQUE':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[45,-15,-32,-36,-31,-33,-34,-35,-28,-32,45,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,45,45,45,45,45,45,45,45,-49,]),'T_MAYOROIGUAL':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[46,-15,-32,-36,-31,-33,-34,-35,-28,-32,46,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,46,46,46,46,46,46,46,46,-49,]),'T_MENOROIGUAL':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[47,-15,-32,-36,-31,-33,-34,-35,-28,-32,47,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,47,47,47,47,47,47,47,47,-49,]),'T_IGUAL':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[48,-15,-32,-36,-31,-33,-34,-35,-28,-32,48,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,48,48,48,48,48,48,48,48,-49,]),'T_DIFERENTE':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[49,-15,-32,-36,-31,-33,-34,-35,-28,-32,49,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,49,49,49,49,49,49,49,49,-49,]),'T_AND':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[50,-15,-32,-36,-31,-33,-34,-35,-28,-32,50,-16,-17,-18,-19,-20,-21,50,50,50,50,50,50,-29,-30,50,50,50,50,50,50,50,50,-49,]),'T_OR':([4,15,17,25,31,32,33,34,62,63,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,118,128,130,133,],[51,-15,-32,-36,-31,-33,-34,-35,-28,-32,51,-16,-17,-18,-19,-20,-21,51,51,51,51,51,51,-29,-30,51,51,51,51,51,51,51,51,-49,]),'T_COMA':([15,25,31,32,33,34,62,63,81,82,83,84,85,86,87,88,89,90,91,92,93,94,100,101,103,117,118,133,],[-15,-36,-31,-33,-34,-35,-28,-32,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-29,-30,109,-52,111,-53,124,-49,]),'T_ASIGNACION':([17,66,68,70,72,],[64,64,64,64,64,]),'T_LLAVEIZQUIERDA':([26,104,105,106,108,131,133,],[76,112,113,114,116,134,-49,]),'T_IN':([75,],[98,]),'T_ELSE':([125,],[131,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,76,112,113,114,116,134,],[2,99,119,120,121,123,135,]),'statement':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[3,36,3,36,3,3,3,3,36,36,36,36,3,36,]),'expression':([0,2,16,28,44,45,46,47,48,49,50,51,64,73,74,76,79,80,99,111,112,113,114,116,119,120,121,122,123,124,134,135,],[4,4,62,78,87,88,89,90,91,92,93,94,95,96,97,4,102,103,4,118,4,4,4,4,4,4,4,128,4,130,4,4,]),'assignment':([0,2,18,19,20,21,76,99,112,113,114,116,119,120,121,123,134,135,],[5,5,65,67,69,71,5,5,5,5,5,5,5,5,5,5,5,5,]),'declaration':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'conditional':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'loop_while':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'loop_for':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'loop_do_while':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'function_declaration':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'return_statement':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'break_statement':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'statement_print':([0,2,76,99,112,113,114,116,119,120,121,123,134,135,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'term':([0,2,16,28,38,39,40,41,42,43,44,45,46,47,48,49,50,51,64,73,74,76,79,80,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[15,15,15,15,81,82,83,84,85,86,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,83,83,83,15,15,15,15,15,15,15,15,15,15,15,83,83,15,15,]),'rank_function':([0,2,16,28,38,39,40,41,42,43,44,45,46,47,48,49,50,51,64,73,74,76,79,80,98,99,104,105,110,111,112,113,114,116,119,120,121,122,123,124,132,133,134,135,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,106,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'parameter_list':([77,],[100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser_1.py',16),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser_1.py',20),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser_1.py',21),
  ('statement -> expression T_FINDELINEA','statement',2,'p_statement','parser_1.py',28),
  ('statement -> assignment T_FINDELINEA','statement',2,'p_statement','parser_1.py',29),
  ('statement -> declaration T_FINDELINEA','statement',2,'p_statement','parser_1.py',30),
  ('statement -> conditional T_FINDELINEA','statement',2,'p_statement','parser_1.py',31),
  ('statement -> loop_while T_FINDELINEA','statement',2,'p_statement','parser_1.py',32),
  ('statement -> loop_for T_FINDELINEA','statement',2,'p_statement','parser_1.py',33),
  ('statement -> loop_do_while T_FINDELINEA','statement',2,'p_statement','parser_1.py',34),
  ('statement -> function_declaration T_FINDELINEA','statement',2,'p_statement','parser_1.py',35),
  ('statement -> return_statement T_FINDELINEA','statement',2,'p_statement','parser_1.py',36),
  ('statement -> break_statement T_FINDELINEA','statement',2,'p_statement','parser_1.py',37),
  ('statement -> statement_print T_FINDELINEA','statement',2,'p_statement','parser_1.py',38),
  ('expression -> term','expression',1,'p_expression','parser_1.py',42),
  ('expression -> expression T_SUMA term','expression',3,'p_expression','parser_1.py',43),
  ('expression -> expression T_PDERECHA term','expression',3,'p_expression','parser_1.py',44),
  ('expression -> expression T_PIZQUIERDA term','expression',3,'p_expression','parser_1.py',45),
  ('expression -> expression T_RESTA term','expression',3,'p_expression','parser_1.py',46),
  ('expression -> expression T_MULTIPLICACION term','expression',3,'p_expression','parser_1.py',47),
  ('expression -> expression T_DIVISION term','expression',3,'p_expression','parser_1.py',48),
  ('expression -> expression T_MAYORQUE expression','expression',3,'p_expression','parser_1.py',49),
  ('expression -> expression T_MENORQUE expression','expression',3,'p_expression','parser_1.py',50),
  ('expression -> expression T_MAYOROIGUAL expression','expression',3,'p_expression','parser_1.py',51),
  ('expression -> expression T_MENOROIGUAL expression','expression',3,'p_expression','parser_1.py',52),
  ('expression -> expression T_IGUAL expression','expression',3,'p_expression','parser_1.py',53),
  ('expression -> expression T_DIFERENTE expression','expression',3,'p_expression','parser_1.py',54),
  ('expression -> T_NOT expression','expression',2,'p_expression','parser_1.py',55),
  ('expression -> expression T_AND expression','expression',3,'p_expression','parser_1.py',56),
  ('expression -> expression T_OR expression','expression',3,'p_expression','parser_1.py',57),
  ('term -> T_NUMERO','term',1,'p_term','parser_1.py',64),
  ('term -> T_VARIABLE','term',1,'p_term','parser_1.py',65),
  ('term -> T_TRUE','term',1,'p_term','parser_1.py',66),
  ('term -> T_FALSE','term',1,'p_term','parser_1.py',67),
  ('term -> T_STRING','term',1,'p_term','parser_1.py',68),
  ('term -> rank_function','term',1,'p_term','parser_1.py',69),
  ('assignment -> T_VARIABLE T_ASIGNACION expression','assignment',3,'p_assignment','parser_1.py',73),
  ('declaration -> T_ENTERO assignment','declaration',2,'p_declaration','parser_1.py',77),
  ('declaration -> T_FLOTANTE assignment','declaration',2,'p_declaration','parser_1.py',78),
  ('declaration -> T_BOOL assignment','declaration',2,'p_declaration','parser_1.py',79),
  ('declaration -> T_CADENA assignment','declaration',2,'p_declaration','parser_1.py',80),
  ('declaration -> T_ENTERO T_VARIABLE','declaration',2,'p_declaration','parser_1.py',81),
  ('declaration -> T_FLOTANTE T_VARIABLE','declaration',2,'p_declaration','parser_1.py',82),
  ('declaration -> T_BOOL T_VARIABLE','declaration',2,'p_declaration','parser_1.py',83),
  ('declaration -> T_CADENA T_VARIABLE','declaration',2,'p_declaration','parser_1.py',84),
  ('conditional -> T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA','conditional',7,'p_conditional','parser_1.py',88),
  ('conditional -> T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_ELSE T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA','conditional',11,'p_conditional','parser_1.py',89),
  ('loop_while -> T_WHILE T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA','loop_while',7,'p_loop_while','parser_1.py',97),
  ('rank_function -> T_RANK T_PDERECHA expression T_COMA expression T_COMA expression T_PIZQUIERDA','rank_function',8,'p_rank_function','parser_1.py',101),
  ('loop_for -> T_FOR T_VARIABLE T_IN rank_function T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA','loop_for',7,'p_loop_for','parser_1.py',105),
  ('loop_do_while -> T_DO T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_WHILE T_PDERECHA expression T_PIZQUIERDA','loop_do_while',8,'p_loop_do_while','parser_1.py',109),
  ('parameter_list -> T_VARIABLE','parameter_list',1,'p_parameter_list','parser_1.py',113),
  ('parameter_list -> parameter_list T_COMA T_VARIABLE','parameter_list',3,'p_parameter_list','parser_1.py',114),
  ('function_declaration -> T_FUNCION T_PDERECHA parameter_list T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA','function_declaration',7,'p_function_declaration','parser_1.py',122),
  ('return_statement -> T_RETURN expression','return_statement',2,'p_return_statement','parser_1.py',127),
  ('return_statement -> T_RETURN','return_statement',1,'p_return_statement','parser_1.py',128),
  ('statement_print -> T_PRINT T_PDERECHA expression T_PIZQUIERDA','statement_print',4,'p_statement_print','parser_1.py',135),
  ('break_statement -> T_BREAK','break_statement',1,'p_break_statement','parser_1.py',140),
]