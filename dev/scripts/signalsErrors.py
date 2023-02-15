class Error(Exception):
    '''Base class for exceptions in this module'''
    pass

class IDError(Error):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self:callable, message:str="Signals ID Error") -> None:
        self.message = f"\n \t--> {message}"
        super().__init__(self.message)
