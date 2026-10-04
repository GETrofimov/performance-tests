import time
import httpx

new_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=new_user_payload)
create_user_response_data = create_user_response.json()

user_id = create_user_response_data['user']['id']

print("User Data: ", create_user_response_data)
print("Status Code: ", create_user_response.status_code)
print("UserId: ", user_id)

open_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json={"userId":user_id})
open_deposit_account_response_data = open_deposit_account_response.json()

print("Deposit Data: ", open_deposit_account_response_data)
print("Status Code: ", open_deposit_account_response.status_code)

