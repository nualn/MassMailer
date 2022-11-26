
class _Parser:

    def parse(self, text, variable_keys, variable_values):
        result = text
        for i, key in enumerate(variable_keys):
            if i >= len(variable_values):
                break
            result = result.replace(f"[{key}]", str(variable_values[i]))
        return result

parser = _Parser()