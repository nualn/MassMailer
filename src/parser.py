
class _Parser:

    def parse(self, text, variable_dict):
        result = text
        for key in variable_dict.keys():
            result = result.replace(f"[{key}]", str(variable_dict[key]))
        return result

parser = _Parser()