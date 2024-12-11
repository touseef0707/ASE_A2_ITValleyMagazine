from datetime import date
from advert_management import User, Requestor, MarketingManager, Editor, Request, Advert
from jovian.pythondsa import evaluate_test_cases

# ---------------------------
# Sample User Data
# ---------------------------
# Users
requestor = Requestor(1, "req_user", "pass123", "John Doe", "john@example.com")
manager = MarketingManager(2, "mgr_user", "pass456", "Jane Smith", "jane@example.com")
editor = Editor(3, "edit_user", "pass789", "Alice Johnson", "alice@example.com")


# Adverts and Requests
advert1 = Advert(101, "Ad Content 1", "Small", "Top", date.today())
advert2 = Advert(102, "Ad Content 2", "Medium", "Middle", date.today())
request1 = Request(201, {"content": "Ad Content 1", "size": "Small", "placement": "Top"}, date.today())
request2 = Request(202, {"content": "Ad Content 2", "size": "Medium", "placement": "Middle"}, date.today())

# Assign sample data
requestor.requests.extend([request1, request2])
editor.adverts.append(advert1)

# ---------------------------
# Test Cases for Methods
# ---------------------------

# 1. Testing `login`
login_test_cases = [
    {"input": {"instance": requestor, "username": "req_user", "password": "pass123"}, "output": True},
    {"input": {"instance": editor, "username": "edit_user", "password": "pass789"}, "output": True},
    {"input": {"instance": manager, "username": "mgr_user", "password": "wrongpass"}, "output": False},
]


# 2. Testing `create_request`
create_request_test_cases = [
    {"input": {"request_id": 203, "advert_details": {"content": "New Ad", "size": "Small", "placement": "Footer"}}, "output": None},  # Valid request
    {"input": {"request_id": 204, "advert_details": {}}, "output": None},  # Missing details in request
    {"input": {"request_id": 205, "advert_details": {"content": "Another Ad", "size": "Large", "placement": "Top"}}, "output": None},  # Another valid request
    {"input": {"request_id": 206, "advert_details": {"size": "Medium"}}, "output": None},  # Missing content
]

# 3. Testing `assign_ad_to_editor`
assign_ad_test_cases = [
    {"input": {"advert": advert2, "editor": editor}, "output": None},  # Valid assignment
    {"input": {"advert": advert1, "editor": None}, "output": None},  # Invalid editor
    {"input": {"advert": None, "editor": editor}, "output": None},  # Invalid advert
]

# 4. Testing `update_request`
update_request_test_cases = [
    {"input": {"updated_details": {"content": "Updated Ad Content", "placement": "Header"}}, "output": None},  # Valid update
    {"input": {"updated_details": {}}, "output": None},  # No updates provided
    {"input": {"updated_details": {"content": "Final Content", "placement": "Footer"}}, "output": None},  # Another valid update
]

# 5. Testing `approve_request`
approve_request_test_cases = [
    {"input": {}, "output": True},  # Approving request
    {"input": {}, "output": True},  # Approve again to check behavior
]

# 6. Testing `reject_request`
reject_request_test_cases = [
    {"input": {}, "output": False},  # Rejecting request
]

# 7. Testing `update_advert`
update_advert_test_cases = [
    {
        "input": {
            "updated_content": "Updated Content",
            "updated_size": "Large",
            "updated_placement": "Footer",
            "updated_date": date.today(),
        },
        "output": None,
    },  # Valid update
    {
        "input": {
            "updated_content": "",
            "updated_size": "",
            "updated_placement": "",
            "updated_date": date.today(),
        },
        "output": None,
    },  # Empty update
    {
        "input": {
            "updated_content": "New Ad Content",
            "updated_size": "Medium",
            "updated_placement": "Header",
            "updated_date": date.today(),
        },
        "output": None,
    },  # Another valid update
]

# ---------------------------
# Evaluate Test Cases
# ---------------------------

dashes = '-' * 40
print("Testing `login` method")

def test_login(instance, username, password):
    return instance.login(username, password)

evaluate_test_cases(test_login, login_test_cases)
print(dashes)

print("\nTesting `create_request` method:")
evaluate_test_cases(requestor.create_request, create_request_test_cases)
print(dashes)

print("\nTesting `assign_ad_to_editor` method:")
evaluate_test_cases(manager.assign_ad_to_editor, assign_ad_test_cases)
print(dashes)

print("\nTesting `update_request` method:")
evaluate_test_cases(request1.update_request, update_request_test_cases)
print(dashes)

print("\nTesting `approve_request` method:")
evaluate_test_cases(request1.approve_request, approve_request_test_cases)
print(dashes)

print("\nTesting `reject_request` method:")
evaluate_test_cases(request1.reject_request, reject_request_test_cases)
print(dashes)

print("\nTesting `update_advert` method:")
evaluate_test_cases(advert1.update_advert, update_advert_test_cases)
