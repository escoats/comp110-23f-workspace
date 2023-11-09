"""Class to store a message (operator overload, union types, default parameters)."""

class Email:
    
    to: str | int
    message: str
    important: bool

    def __init__(self, recipient: str | int, message_text: str = "", importance_flag: bool = False): # by default, importance_flag is False unless otherwise given
        """Constructor."""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag
    
    def __str__(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important} \n"
        m_string += f'"{self.message}"'
        return m_string

    def __mul__(self, factor: int):
        self.message *= factor

def add(x: int | float, y: int | float = 1) -> int | float: # by default, y is 1 unless otherwise stated
    return x + y        

email_to_chiara: Email = Email("chiara", "You're a great TA!", False)
email_to_chiara * 10
print(email_to_chiara)

email_to_lauren: Email = Email("lauren")
print(email_to_lauren)
email_to_lauren.message = "You're the best!"
print(email_to_lauren)