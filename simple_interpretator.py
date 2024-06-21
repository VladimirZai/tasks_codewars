import re

class SimpleInterpreter:
    def __init__(self):
        self.variables = {}

    def input(self, expression):
        try:
            expression = expression.strip()
            if not expression:
                return ""
            result = self.evaluate(expression)
            return result
        except Exception as e:
            return f"ERROR: {e}"

    def evaluate(self, expression):
        if '=' in expression:
            return self.handle_assignment(expression)
        else:
            return self.handle_expression(expression)

    def handle_assignment(self, expression):
        identifier, expr = map(str.strip, expression.split('=', 1))

        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', identifier):
            raise ValueError(f"Invalid identifier: {identifier}")

        value = self.handle_expression(expr)
        self.variables[identifier] = value
        return value

    def handle_expression(self, expression):
        expression = self.replace_variables(expression)
        return self.eval_expr(expression)

    def replace_variables(self, expression):
        def replacer(match):
            var_name = match.group(0)
            if var_name not in self.variables:
                raise ValueError(f"Invalid identifier. No variable with name '{var_name}' was found.")
            return str(self.variables[var_name])

        return re.sub(r'[a-zA-Z_][a-zA-Z0-9_]*', replacer, expression)

    def eval_expr(self, expression):
        try:
            return eval(expression, {"__builtins__": None}, {})
        except NameError as e:
            raise ValueError(f"Invalid identifier: {e}")
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

if __name__ == "__main__":
    interpreter = SimpleInterpreter()
    while True:
        try:
            user_input = input(">>> ")
            if user_input.lower() in ['exit', 'quit']:
                break
            result = interpreter.input(user_input)
            if result != "":
                print(result)
        except (EOFError, KeyboardInterrupt):
            break
