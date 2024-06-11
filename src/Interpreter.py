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
        elif node_type == 'if':
            self.visit_if(statement)
        elif node_type == 'while':
            self.visit_while(statement)
        elif node_type == 'for':
            self.visit_for(statement)
        elif node_type == 'do_while':
            self.visit_do_while(statement)
        elif node_type == 'function':
            self.visit_function(statement)
        elif node_type == 'function_call':
            self.visit_function_call(statement)
        else:
            raise Exception(f'Unknown statement type: {node_type}')

    def visit_assign(self, node):
        _, var_name, value_node = node
        value = self.visit_expression(value_node)
        self.variables[var_name] = value

    def visit_print(self, node):
        _, expr_node = node
        value = self.visit_expression(expr_node)
        print(value)

    def visit_if(self, node):
        _, condition_node, if_body, else_clause = node
        if self.visit_expression(condition_node):
            self.visit_program(('program', if_body))
        else:
            self.visit_else_clause(else_clause)

    def visit_else_clause(self, node):
        if node is None:
            return
        if node[0] == 'elif':
            _, condition_node, elif_body, else_clause = node
            if self.visit_expression(condition_node):
                self.visit_program(('program', elif_body))
            else:
                self.visit_else_clause(else_clause)
        elif node[0] == 'else':
            _, else_body = node
            self.visit_program(('program', else_body))

    def visit_while(self, node):
        _, condition_node, body_node = node
        while self.visit_expression(condition_node):
            self.visit_program(('program', body_node))

    def visit_for(self, node):
        _, init_stmt, condition_node, post_stmt, body_node = node
        self.interpret_statement(init_stmt)
        while self.visit_expression(condition_node):
            self.visit_program(('program', body_node))
            self.interpret_statement(post_stmt)

    def visit_do_while(self, node):
        _, body_node, condition_node = node
        while True:
            self.visit_program(('program', body_node))
            if not self.visit_expression(condition_node):
                break

    def visit_function(self, node):
        _, func_name, params, body = node
        self.functions[func_name] = (params, body)

    def visit_function_call(self, node):
        _, func_name, args = node
        if func_name not in self.functions:
            raise Exception(f'Function {func_name} not defined')
        params, body = self.functions[func_name]
        if len(params) != len(args):
            raise Exception(f'Argument count mismatch in function call {func_name}')
        old_vars = self.variables.copy()
        self.variables.update({param: self.visit_expression(arg) for param, arg in zip(params, args)})
        self.visit_program(('program', body))
        self.variables = old_vars

    def visit_expression(self, node):
        if isinstance(node, tuple):
            op = node[0]
            if op in ('+', '-', '*', '/'):
                _, left_node, right_node = node
                left_val = self.visit_expression(left_node)
                right_val = self.visit_expression(right_node)
                if op == '+':
                    return left_val + right_val
                elif op == '-':
                    return left_val - right_val
                elif op == '*':
                    return left_val * right_val
                elif op == '/':
                    return left_val / right_val
            elif op == 'Var':
                return self.visit_Var(node)
            elif op == 'Num':
                return self.visit_Number(node)
            elif op == '==':
                _, left_node, right_node = node
                return self.visit_expression(left_node) == self.visit_expression(right_node)
            elif op == 'function_call':
                return self.visit_function_call(node)
        elif isinstance(node, int) or isinstance(node, float):
            return node
        elif isinstance(node, str) and (node[0] == '"' and node[-1] == '"'):
            return node[1:-1]  # Remove quotes from string
        else:
            raise Exception(f'Unknown expression type: {node}')

    def visit_Var(self, node):
        _, var_name = node
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise Exception(f'Undefined variable {var_name}')

    def visit_Number(self, node):
        _, value = node
        return value