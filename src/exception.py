import sys

def error_message_detials(error,error_detials:sys):
    _,_,exc_tb=error_detials.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error Accoured in {file_name} at {exc_tb.tb_lineno} the error is {error} "
    return error_message

class CustomeException(Exception):
    def __init__(self, error_message,error_detials: sys):
        super().__init__(error_message)
        self.error_message=error_message_detials(error_message,error_detials)
        
    def __str__(self) :
        return self.error_message