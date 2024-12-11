from datetime import date
from typing import List, Dict
import re

# Helper functions
def is_valid_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_role(role: str) -> bool:
    """Check if the role is valid."""
    return role in {'Editor', 'Requestor', 'Manager'}

def is_valid_status(status: str, valid_statuses: List[str]) -> bool:
    """Check if the status is valid."""
    return status in valid_statuses

# Base User class
class User:
    def __init__(self, user_id: int, role: str, username: str, password: str, name: str, email: str) -> None:
        if not user_id:
            raise ValueError("User ID must not be null.")  # OCL: User must have a valid ID
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")  # OCL: Username and password cannot be empty
        if not is_valid_email(email):
            raise ValueError("Invalid email format.")  # OCL: Email must follow a valid format
        if not is_valid_role(role):
            raise ValueError(f"Invalid role: {role}. Role must be one of 'Editor', 'Requestor', or 'Manager'.")  # OCL

        self.__user_id = user_id
        self.__role = role
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def role(self) -> str:
        return self.__role

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def login(self, username: str, password: str) -> bool:
        """Validates login credentials."""
        if not username or not password:
            print("Error: Username and password cannot be empty.")
            return False
        
        print(f"Attempting login for Username: {username}, Role: {self.role}")
        
        if self.__username == username and self.__password == password:
            print(f"Login successful for {self.__username} with Role: {self.role}.")
            return True
        
        print("Error: Invalid username or password.")
        return False

    def view_details(self) -> None:
        print(f"User ID: {self.__user_id}, Role: {self.__role}, Name: {self.__name}, Email: {self.__email}")

    def logout(self) -> bool:
        print(f"User {self.__username} logged out.")
        return True

# Requestor class
class Requestor(User):
    def __init__(self, user_id: int, username: str, password: str, name: str, email: str) -> None:
        super().__init__(user_id, "Requestor", username, password, name, email)
        self.__requests: List['Request'] = []

    @property
    def requests(self) -> List['Request']:
        return self.__requests

    def create_request(self, request_id: int, advert_details: Dict[str, object]) -> None:
        if not advert_details or "content" not in advert_details:
            print("Error: Advertisement details must include content.")
            return
        request = Request(request_id, advert_details, date.today())
        self.__requests.append(request)
        print(f"Request {request_id} created successfully.")

    def view_requests(self) -> None:
        if not self.__requests:
            print("No requests found.")
        else:
            for request in self.__requests:
                request.view_details()

# MarketingManager class
class MarketingManager(User):
    def __init__(self, user_id: int, username: str, password: str, name: str, email: str) -> None:
        super().__init__(user_id, "Manager", username, password, name, email)  # OCL: Role must be 'Manager'

    def assign_ad_to_editor(self, advert: 'Advert', editor: 'Editor') -> None:
        if not isinstance(editor, Editor):
            print("Error: Invalid editor.")
            return
        if not isinstance(advert, Advert):
            print("Error: Invalid advert.")
            return
        editor.adverts.append(advert)
        print(f"Advert {advert.advert_id} assigned to Editor {editor.user_id}.")

# Editor class
class Editor(User):
    def __init__(self, user_id: int, username: str, password: str, name: str, email: str) -> None:
        super().__init__(user_id, "Editor", username, password, name, email)  
        self.__adverts: List['Advert'] = []

    @property
    def adverts(self) -> List['Advert']:
        return self.__adverts

    def view_adverts(self) -> None:
        if not self.__adverts:
            print("No adverts found.")
        else:
            for advert in self.__adverts:
                advert.view_details()

# Request class
class Request:
    def __init__(self, request_id: int, advert_details: Dict[str, object], request_date: date) -> None:
        if not request_id:
            raise ValueError("Request must have a unique identifier.")  # OCL: Request must have a unique identifier
        if not advert_details:
            raise ValueError("Advertisement details must be provided.")  # OCL: Advertisement details must be provided
        if request_date > date.today():
            raise ValueError("Request date cannot be in the future.")  # OCL: Request date constraint

        self.__request_id = request_id
        self.__advert_details = advert_details
        self.__request_date = request_date
        self.__status = "Pending"  # OCL: Default status is 'Pending'

    @property
    def request_id(self) -> int:
        return self.__request_id

    @property
    def advert_details(self) -> Dict[str, object]:
        return self.__advert_details

    @property
    def request_date(self) -> date:
        return self.__request_date

    @property
    def status(self) -> str:
        return self.__status

    def update_request(self, updated_details: Dict[str, object]) -> None:
        if not updated_details:
            print("Error: Update details cannot be empty.")
            return
        self.__advert_details.update(updated_details)
        print(f"Request {self.__request_id} updated successfully.")

    def approve_request(self) -> bool:
        self.__status = "Approved"
        print(f"Request {self.__request_id} approved.")
        return True

    def reject_request(self) -> bool:
        self.__status = "Rejected"
        print(f"Request {self.__request_id} rejected.")
        return False

    def view_details(self) -> None:
        print(f"Request ID: {self.__request_id}, Status: {self.__status}, Details: {self.__advert_details}")

# Advert class
class Advert:
    def __init__(self, advert_id: int, content: str, size: str, placement: str, publish_date: date) -> None:
        if not advert_id:
            raise ValueError("Advert must have a unique identifier.")  # OCL
        if not content:
            raise ValueError("Advertisement content cannot be empty.")  # OCL
        if size not in {'Small', 'Medium', 'Large'}:
            raise ValueError("Invalid size. Must be 'Small', 'Medium', or 'Large'.")  # OCL
        if placement not in {'Top', 'Middle', 'Bottom'}:
            raise ValueError("Invalid placement. Must be 'Top', 'Middle', or 'Bottom'.")  # OCL
        if publish_date > date.today():
            raise ValueError("Publish date cannot be in the future.")  # OCL

        self.__advert_id = advert_id
        self.__content = content
        self.__size = size
        self.__placement = placement
        self.__publish_date = publish_date

    @property
    def advert_id(self) -> int:
        return self.__advert_id

    @property
    def content(self) -> str:
        return self.__content

    @property
    def size(self) -> str:
        return self.__size

    @property
    def placement(self) -> str:
        return self.__placement

    @property
    def publish_date(self) -> date:
        return self.__publish_date

    def update_advert(self, updated_content: str, updated_size: str, updated_placement: str, updated_date: date) -> None:
        if not updated_content or not updated_size or not updated_placement:
            print("Error: All fields must be provided for update.")
            return
        self.__content = updated_content
        self.__size = updated_size
        self.__placement = updated_placement
        self.__publish_date = updated_date
        print(f"Advert {self.__advert_id} updated successfully.")

    def view_details(self) -> None:
        print(f"Advert ID: {self.__advert_id}, Content: {self.__content}, Size: {self.__size}, Placement: {self.__placement}, Publish Date: {self.__publish_date}")

# Command Interface
class Command:
    """Command Interface."""
    def execute(self) -> None:
        """Execute the command."""
        pass

# Command for Requestor to create a request
class CreateRequestCommand(Command):
    def __init__(self, requestor: 'Requestor', request_id: int, advert_details: Dict[str, object]) -> None:
        self.requestor = requestor
        self.request_id = request_id
        self.advert_details = advert_details

    def execute(self) -> None:
        self.requestor.create_request(self.request_id, self.advert_details)

# Command for Marketing Manager to assign an advert to an editor
class AssignAdvertToEditorCommand(Command):
    def __init__(self, manager: 'MarketingManager', advert: 'Advert', editor: 'Editor') -> None:
        self.manager = manager
        self.advert = advert
        self.editor = editor

    def execute(self) -> None:
        self.manager.assign_ad_to_editor(self.advert, self.editor)

# Command for Editor to view adverts
class ViewAdvertsCommand(Command):
    def __init__(self, editor: 'Editor') -> None:
        self.editor = editor

    def execute(self) -> None:
        self.editor.view_adverts()

# Command for Requestor to approve a request
class ApproveRequestCommand(Command):
    def __init__(self, request: 'Request') -> None:
        self.request = request

    def execute(self) -> None:
        self.request.approve_request()

# Command for creating an advert
class CreateAdvertCommand(Command):
    def __init__(self, advert: 'Advert') -> None:
        self.advert = advert

    def execute(self) -> None:
        print(f"Advert {self.advert.advert_id} created successfully with content: {self.advert.content}.")

# Define an Invoker class that can execute any command
class CommandInvoker:
    def __init__(self) -> None:
        self.__commands = []

    def add_command(self, command: Command) -> None:
        """Adds a command to the invoker."""
        self.__commands.append(command)

    def execute_commands(self) -> None:
        """Executes all commands in the invoker."""
        for command in self.__commands:
            command.execute()

    def clear_commands(self) -> None:
        """Clears all commands."""
        self.__commands = []


if __name__ == "__main__":
    
    # Using CommandInvoker with Commands

    # Step 1: Create instances of the Requestor, Manager, Editor, Advert, and Request
    requestor = Requestor(user_id=1, username="john_doe", password="password123", name="John Doe", email="john.doe@example.com")
    manager = MarketingManager(user_id=2, username="alice_smith", password="password123", name="Alice Smith", email="alice.smith@example.com")
    editor = Editor(user_id=3, username="bob_jones", password="password123", name="Bob Jones", email="bob.jones@example.com")
    advert_details = {"content": "Summer Sale", "size": "Medium", "placement": "Top"}
    advert = Advert(advert_id=101, content="Summer Sale", size="Medium", placement="Top", publish_date=date.today())

    # Creating a request
    request = Request(request_id=101, advert_details=advert_details, request_date=date.today())

    # Step 2: Create command objects
    create_request_command = CreateRequestCommand(requestor, request_id=101, advert_details=advert_details)
    approve_request_command = ApproveRequestCommand(request)
    create_advert_command = CreateAdvertCommand(advert)
    assign_advert_command = AssignAdvertToEditorCommand(manager, advert, editor)
    view_adverts_command = ViewAdvertsCommand(editor)

    # Step 3: Instantiate the invoker and add commands
    invoker = CommandInvoker()
    invoker.add_command(create_request_command)
    invoker.add_command(approve_request_command)  # Added approve request command
    invoker.add_command(create_advert_command)    # Added create advert command
    invoker.add_command(assign_advert_command)
    invoker.add_command(view_adverts_command)

    # Step 4: Execute the commands
    invoker.execute_commands()

    # Optional: Clear commands if needed
    invoker.clear_commands()
