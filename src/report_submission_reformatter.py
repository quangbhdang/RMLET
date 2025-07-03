"""
This function is to take the notebook file and output it according to the report requirement by the university
"""
import nbformat
import ast

class reformatter:
    def __init__(self, path):
        self.path_ = path

    def format(self, name:str, new_path) -> object:
        """
        return new notebook with the name and new_path

        input:
        - name: name of the new notebook
        - new_path: where the new notebook will be store

        output:
        - notebook
        """
        #TODO: Return the notebook as formatted formatted string
        return name, new_path