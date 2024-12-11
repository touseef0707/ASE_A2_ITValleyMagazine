# Advert Management System

This repository contains the implementation of an **Advert Management System**, designed to facilitate the creation, management, and assignment of advertisement requests. The project models a simplified workflow involving key roles and their respective functionalities, such as requestors, marketing managers, and editors.

## Project Structure

- **`advert_management.py`**: Contains the core implementation of the classes and methods for the system, including `User`, `Requestor`, `MarketingManager`, `Editor`, `Request`, and `Advert`.
- **`test.py`**: Includes test cases for various methods implemented in `advert_management.py`, utilizing the `evaluate_test_cases` function to validate functionality.

## Key Features

1. **User Management**:
   - Users can log in using a username and password.
   - Supports roles: `Requestor`, `MarketingManager`, and `Editor`.

2. **Request Management**:
   - Requestors can create and update advertisement requests with details such as content, size, and placement.
   - Marketing Managers can approve or reject advertisement requests.

3. **Advert Management**:
   - Editors can update adverts' content, size, placement, and associated dates.
   - Adverts can be assigned to editors by marketing managers.

4. **Validation**:
   - Includes helper functions for validating emails, roles, and statuses.

## Classes and Methods

### Classes

- **`User`**: Base class representing common user properties and behaviors.
- **`Requestor`**: Subclass for users who create advertisement requests.
- **`MarketingManager`**: Subclass for users who approve/reject requests and assign adverts.
- **`Editor`**: Subclass for users who update advert details.
- **`Request`**: Represents an advertisement request.
- **`Advert`**: Represents an advertisement.

### Key Methods

- **`login(username, password)`**: Verifies user credentials.
- **`create_request(request_id, advert_details)`**: Allows a requestor to create a new request.
- **`assign_ad_to_editor(advert, editor)`**: Assigns an advert to an editor (MarketingManager).
- **`update_request(updated_details)`**: Updates an existing request with new details.
- **`approve_request()`**: Marks a request as approved (MarketingManager).
- **`reject_request()`**: Marks a request as rejected (MarketingManager).
- **`update_advert(...)`**: Updates advert content, size, placement, or date (Editor).

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies (if any).

3. Run the test cases:
   ```bash
   python test.py
   ```

## Test Cases

Test cases in `test.py` validate the core functionalities:

1. **Login**:
   - Tests valid and invalid login attempts for different user roles.
2. **Create Request**:
   - Tests creating advertisement requests with complete and incomplete details.
3. **Assign Adverts**:
   - Verifies assigning adverts to valid editors and handling invalid inputs.
4. **Update Request and Approve/Reject**:
   - Tests updates to request details and the approval/rejection process.
5. **Advert Updates**:
   - Validates updates to adverts' properties by editors.

## Example Output

Sample output from running the test cases:

```
Testing `login` method
Test case 1 | Input: {...} | Output: True | Expected: True | PASSED
...

Testing `create_request` method
Test case 1 | Input: {...} | Output: None | Expected: None | PASSED
...
```


