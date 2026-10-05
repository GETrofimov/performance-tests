import time
import httpx

# Создаем пользователя
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

# Открываем пользователю новый счет
new_credit_card_account_payload = {
    "userId": user_id
}

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=new_credit_card_account_payload)
open_credit_card_account_response_data = open_credit_card_account_response.json()

account_id = open_credit_card_account_response_data["account"]["id"]
card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]

print("Credit Account Data: ", open_credit_card_account_response_data)
print("Status Code: ", open_credit_card_account_response.status_code)
print("AccountId: ", account_id)
print("CardId: ", card_id)

# Делаем покупку
purchase_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": card_id,
    "accountId": account_id
}

make_purchase_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=purchase_payload)
make_purchase_response_data = make_purchase_response.json()

operation_id = make_purchase_response_data["operation"]["id"]

# Получаем чек операции
get_opearation_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
get_opearation_response_data = get_opearation_response.json()

print("Operation Data: ", get_opearation_response_data)
print("Status Code: ", get_opearation_response.status_code)