
class _Parser:
    """Class for placing variables into text"""
    def parse(self, text, variable_dict):
        """Places variables into text
        
        Args: 
            text (String): A text with places for variables in the form "[{key_to_replace}]"
            variable_dict (dict): A dictionary of variables to be placed in the text in the form { key_to_replace: value_to_place }
        
        Returns: 
            The text string with the variables replaced with the values in variable_dict
        """
        result = text
        for key in variable_dict.keys():
            result = result.replace(f"[{key}]", str(variable_dict[key]))
        return result


parser = _Parser()
