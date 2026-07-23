import sys

class CustomException(Exception):
    def __init__(self, message: str, errors: Exception = None):
       self.error_message = self.get_detailed_error_message(message, errors)
       super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message: str, errors: Exception = None) -> str:
           exc_type, exc_obj, exc_tb = sys.exc_info()
           file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
           line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
           error_details = f"Error Type: {exc_type.__name__}, File: {file_name}, Line: {line_number}"
           if errors:
               error_details += f", Original Error: {str(errors)}"
           return f"{message} | {error_details}"

    def __str__(self):
            return self.error_message