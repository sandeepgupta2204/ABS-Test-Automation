import requests
import pytest
import json

BASE_URL = "https://input-backend.api.dehat.co/delivery/delivery-slots/v1"
PARAMS = {
    "app_code": "dehaat_business",
    "lang": "en"
}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "APP-CODE": "dehaat_business",
    "X-AUTH-SCHEME": "keycloak",
    "X-APP-VERSION": "968",
    "X-LANGUAGE": "en",
    "X-Request-ID": "7c7212d8-2cfc-4b6b-b54a-7e00ac3f7f9c",
    "api-request-trace-id": "7c7212d8-2cfc-4b6b-b54a-7e00ac3f7f9c",
    "DEVICE-ID": "d5c0186e-414c-4a94-9cb4-cd2069f75c24",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM5NjkyOTYsImlhdCI6MTc2MzUzNzI5NiwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiIwNWRhMGFhZS00NjFlLTQzYjktOTk3MC1iMDA2NWYwNjdmNzEiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IcPT9aqJUJ9vxLN9pHBaY1piLsZ5xhJAzZs6-GQpIPjryAmEXe-EIb4Qj1xr0p26Pv7d6c7Naz2vyVK2jrc_JRTEZMCYoUHhR9z-UOCWSSODEzxFzuPp9rKEh2eibxUcBF9N2Agk1Hkx2AztDw11uaZ0kA2vNBV1eVqsIEUN1iFfho3MVuTQH0mVnf35lhvjG4pUDw44R1PAPcCAz9Kn3jOxiCc0mN4z44YIAoL-W6fb1CWoHqRLWueft5kmzkC3avwyxNoM0CCzjhuMhYdtQtfOFVIpQI3_Dk9aD758lpaYNUe8QAFTTcu5LBY4YAEPc6fEAPkHJ8vmTZsF3iIY8Q"
}

PAYLOAD = {"data": [{"product_id": "12000498"}]}


@pytest.mark.api
def test_post_delivery_slots():
    """Test POST /delivery/delivery-slots/v1 API with correct structure validation"""

    try:
        response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=10)
        print(f"HTTP Status: {response.status_code}")
        assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"

        json_data = response.json()
        print("Response JSON:", json.dumps(json_data, indent=2))

        # ✅ Validate JSON structure
        assert "data" in json_data, "Missing 'data' in response"
        data = json_data["data"]
        assert isinstance(data, dict), f"Expected 'data' to be dict, got {type(data)}"

        # ✅ Check keys
        assert "default" in data, "Missing 'default' key in data"
        default_slots = data["default"]
        assert isinstance(default_slots, list), "'default' should be a list"

        # ✅ Validate slots for each product
        for product in default_slots:
            assert "product_id" in product, "Missing product_id"
            assert "slots" in product, f"Missing 'slots' for product {product.get('product_id')}"
            slots = product["slots"]
            assert isinstance(slots, list), "Slots should be a list"

            for slot in slots:
                assert "order_type" in slot, "Missing order_type"
                assert "start_date" in slot, "Missing start_date"
                assert "end_date" in slot, "Missing end_date"
                assert slot["order_type"] in ["confirmed", "virtual_order", "preorder"], f"Unexpected order_type: {slot['order_type']}"

        print(f"✅ Delivery slots validated successfully for product(s): {[p['product_id'] for p in default_slots]}")

    except Exception as e:
        pytest.fail(f"❌ Test failed: {e}")