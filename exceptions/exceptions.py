class CustomException(Exception):

    def __init__(self, message, status):
        super.__init__(message)
        self.status = status
