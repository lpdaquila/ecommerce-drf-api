
def load(file_path):
    """
    :file_path: -> Path
    return the query in an external file 
    """
    with open(file_path, 'r') as file:
        return file.read()