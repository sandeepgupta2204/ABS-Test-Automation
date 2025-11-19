import requests
import pytest
import json

BASE_URL = "https://input-backend.api.dehat.co/sale-management/validate-cart/v3"
PARAMS = {
    "app_code": "dehaat_business",
    "lang": "en",
    "is_bundle_coupon_allowed": "true",
    "is_payment_page_exist": "true"
}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "APP-CODE": "dehaat_business",
    "X-AUTH-SCHEME": "keycloak",
    "X-APP-VERSION": "968",
    "X-LANGUAGE": "en",
    "X-Request-ID": "a32dc342-9f40-47f1-9c0b-8b1268cd282f",
    "api-request-trace-id": "a32dc342-9f40-47f1-9c0b-8b1268cd282f",
    "DEVICE-ID": "abf7cd7b-c000-4fd7-9e5c-7bb402cf8cda",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM5NjkyOTYsImlhdCI6MTc2MzUzNzI5NiwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiIwNWRhMGFhZS00NjFlLTQzYjktOTk3MC1iMDA2NWYwNjdmNzEiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IcPT9aqJUJ9vxLN9pHBaY1piLsZ5xhJAzZs6-GQpIPjryAmEXe-EIb4Qj1xr0p26Pv7d6c7Naz2vyVK2jrc_JRTEZMCYoUHhR9z-UOCWSSODEzxFzuPp9rKEh2eibxUcBF9N2Agk1Hkx2AztDw11uaZ0kA2vNBV1eVqsIEUN1iFfho3MVuTQH0mVnf35lhvjG4pUDw44R1PAPcCAz9Kn3jOxiCc0mN4z44YIAoL-W6fb1CWoHqRLWueft5kmzkC3avwyxNoM0CCzjhuMhYdtQtfOFVIpQI3_Dk9aD758lpaYNUe8QAFTTcu5LBY4YAEPc6fEAPkHJ8vmTZsF3iIY8Q"
}

PAYLOAD = {
    "products": [
        {
            "product_id": "12000498",
            "total_order_quantity": 1,
            "product_type": "regular",
            "payment_modes": ["credit"],
            "is_bundle": False,
            "unit_price": 1000,
            "untaxed_unit_price": "952.38"
        }
    ],
    "wallet_applied": True,
    "partner_id": "1000005292"
}

@pytest.mark.api
def test_post_validate_cart():
    """Test POST /sale-management/validate-cart/v3 API with updated structure validation"""

    try:
        response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=10)
        print(f"HTTP Status: {response.status_code}")
        assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"

        json_data = response.json()
        print("Response JSON:", json.dumps(json_data, indent=2))

        data = json_data.get("data", {})

        # ✅ Updated checks per real response
        assert "cart_id" in data, "Missing cart_id"
        assert "is_valid" in data, "Missing is_valid key"
        assert data["is_valid"] is True, "Cart not validated successfully"
        assert isinstance(data.get("products", []), list), "Products should be a list"
        assert "amount_details" in data, "Missing amount_details"
        assert "cart_details" in data["amount_details"], "Missing cart_details inside amount_details"
        assert "payment_details" in data["amount_details"], "Missing payment_details inside amount_details"

        cart_total = data["amount_details"]["cart_details"].get("order_total", 0)
        assert float(cart_total) > 0, "Order total should be positive"

        print(f"✅ Cart validated successfully. Total order value: ₹{cart_total}")

    except Exception as e:
        pytest.fail(f"❌ Test failed: {e}")