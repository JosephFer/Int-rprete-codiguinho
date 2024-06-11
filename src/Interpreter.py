import re
class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def interpret(self, node):
        if node[0] == 'program':
            self.visit_program(node)
        else:
            raise Exception(f'Unknown node type: {node[0]}')

    def visit_program(self, node):
        _, statements = node
        for statement in statements:
            self.interpret_statement(statement)

    def interpret_statement(self, statement):
        node_type = statement[0]
        if node_type == 'assign':
            self.visit_assign(statement)
        elif node_type == 'Imprimir':
            self.visit_print(statement)
        else:
            raise Exception(f'Unknown statement type: {node_type}')

    def visit_assign(self, node):
        _, var_name, value = node
        self.variables[var_name] = value

    def visit_print(self, node):
        _, var_name = node
        if var_name in self.variables:
            print(self.variables[var_name])
        elif isinstance(var_name, str):
            # Elimina las comillas dobles que rodean la cadena
            var_name = var_name[1:-1]
            print(var_name)
        elif isinstance(var_name, int):
            print(var_name)
        else:
            raise NameError(f'Variable {var_name} not defined')

    def visit_expression(self, node):
        if isinstance(node, tuple):
            op, left, right = node
            left_val = self.visit_expression(left)
            right_val = self.visit_expression(right)
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                return left_val / right_val
        elif isinstance(node, str):  # Si es una variable, devolver su valor
            return self.visit_Var(('Var', node))
        else:
            return node  # Si es un número, devolver el número tal cual

    def visit_Var(self, node):
        _, var_name = node
        if var_name in self.variables:
            return self.variables[var_name]
        raise NameError(f'Variable {var_name} not defined')

    def visit_Number(self, node):
        _, value = node
        return value

    def visit_function_call(self, node):
        _, func_name, args = node
        params, body = self.functions[func_name]
        old_vars = self.variables.copy()
        self.variables.update(zip(params, [self.visit_expression(arg) for arg in args]))
        self.interpret(body)
        self.variables = old_vars

    def visit_Function(self, node):
        _, func_name, params, body = node
        self.functions[func_name] = (params, body)

    def visit_Return(self, node):
        _, value = node
        return self.visit_expression(value)
