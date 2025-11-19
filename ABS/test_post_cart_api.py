import requests
import pytest
import json

# --- API Config ---
BASE_URL = "https://input-backend.api.dehat.co/products/cart/v2"
PARAMS = {
    "app_code": "dehaat_business",
    "lang": "en",
    "is_bundle_coupon_allowed": "true"
}

# --- Headers from curl ---
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "APP-CODE": "dehaat_business",
    "X-AUTH-SCHEME": "keycloak",
    "X-APP-VERSION": "968",
    "X-LANGUAGE": "en",
    "X-Request-ID": "c3719a60-70aa-4afd-92b2-faf26d8655f0",
    "api-request-trace-id": "c3719a60-70aa-4afd-92b2-faf26d8655f0",
    "DEVICE-ID": "24881f8e-2639-4544-aaa3-7b9309a22b78",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2ZXFUMWswUGZpUWNhN0RLcWpKWjZEZ0NwWTAwanZIUHpwbk5ZIn0.eyJleHAiOjE3NjM5NjkyOTYsImlhdCI6MTc2MzUzNzI5NiwiYXV0aF90aW1lIjoxNzYzNDQ5MzkwLCJqdGkiOiIwNWRhMGFhZS00NjFlLTQzYjktOTk3MC1iMDA2NWYwNjdmNzEiLCJpc3MiOiJodHRwczovL29pZGMuZGVoYXQuY28vYXV0aC9yZWFsbXMvZGVoYWF0IiwiYXVkIjpbImNvcmUtYXBpIiwia2hldGkiLCJvZG9vIiwiaW5wdXQtYmFja2VuZC1kamFuZ28tYWRtaW4iLCJpZGVudGl0eS1tYXN0ZXIiLCJhY2NvdW50Il0sInN1YiI6ImFlZDQ0YTY2LTI5YzEtNDc5Ny04MmRmLTcyZmFmMjlmOWY2OCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJ1c2luZXNzYXBwIiwibm9uY2UiOiJFR2RjU1c1dTJwcWJCUVp0YjlOMXBnIiwic2Vzc2lvbl9zdGF0ZSI6ImFmZGVlYTU5LTAzYjMtNDE1OS04MTZlLWMzNTU1Yjk1NmM1ZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1kZWhhYXQiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyBtb2JpbGUgaWRlbnRpdHktbWFzdGVyLWF1ZGllbmNlIHByb2ZpbGUgZW1haWwgaW5wdXQtYmFja2VuZC1hdWRpZW5jZSBjc2MiLCJzaWQiOiJhZmRlZWE1OS0wM2IzLTQxNTktODE2ZS1jMzU1NWI5NTZjNWUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJBc2hvayBLdW1hciBNYW5kYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmNmEzY2Q4NS0yYjBmLTQxNWUtYTgwOC1mZWVmMjNkYTNlNDUiLCJnaXZlbl9uYW1lIjoiQXNob2sgS3VtYXIiLCJtb2JpbGVfbnVtYmVyIjoiNzc4Mjk0ODgzMCIsImZhbWlseV9uYW1lIjoiTWFuZGFsIiwiZW1haWwiOiJuYW5kdGVtcEBhZ3Jldm9sdXRpb24uaW4ifQ.IcPT9aqJUJ9vxLN9pHBaY1piLsZ5xhJAzZs6-GQpIPjryAmEXe-EIb4Qj1xr0p26Pv7d6c7Naz2vyVK2jrc_JRTEZMCYoUHhR9z-UOCWSSODEzxFzuPp9rKEh2eibxUcBF9N2Agk1Hkx2AztDw11uaZ0kA2vNBV1eVqsIEUN1iFfho3MVuTQH0mVnf35lhvjG4pUDw44R1PAPcCAz9Kn3jOxiCc0mN4z44YIAoL-W6fb1CWoHqRLWueft5kmzkC3avwyxNoM0CCzjhuMhYdtQtfOFVIpQI3_Dk9aD758lpaYNUe8QAFTTcu5LBY4YAEPc6fEAPkHJ8vmTZsF3iIY8Q"
}

# --- Payload from your cURL ---
PAYLOAD = {
    "scheme_id": None,
    "products": [
        {
            "id": "12000498",
            "total_order_quantity": 1,
            "product_type": "regular",
            "payment_modes": ["credit"],
            "is_bundle": False,
            "unit_price": "1000",
            "delivery_fee": "10",
            "slots": [
                {"order_type": "confirmed", "id": None, "start_date": 1763490600, "end_date": 1763836199, "qty": 1},
                {"order_type": "virtual_order", "id": None, "start_date": None, "end_date": None},
                {"order_type": "preorder", "id": None, "start_date": None, "end_date": None}
            ]
        }
    ]
}


@pytest.mark.api
def test_post_cart():
    """Test POST /products/cart/v2 API with validation and assertions"""

    try:
        response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=10)
        print(f"HTTP Status: {response.status_code}")

        # ✅ 1. Accept 200 or 201
        assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"

        json_data = response.json()
        print("Response JSON:", json.dumps(json_data, indent=2))

        # ✅ 2. Validate structure
        assert isinstance(json_data, dict), "Response is not a valid JSON object"
        assert "data" in json_data, "Missing 'data' key in response"

        data = json_data["data"]

        # ✅ 3. Validate core keys
        expected_keys = ["cart_id", "total_items", "total_amount", "products"]
        missing_keys = [k for k in expected_keys if k not in data]
        if missing_keys:
            print(f"⚠️ Missing expected keys: {missing_keys}")

        # ✅ 4. Logical validation
        if "products" in data:
            assert isinstance(data["products"], list), "Products should be a list"
            assert len(data["products"]) > 0, "Products list is empty"

        print(f"✅ Cart created successfully with {len(data.get('products', []))} product(s).")

    except requests.exceptions.Timeout:
        pytest.fail("⏰ Request timed out")
    except requests.exceptions.ConnectionError:
        pytest.fail("🚫 Connection error - check network or endpoint")
    except ValueError:
        pytest.fail("❌ Failed to parse JSON response")
    except AssertionError as e:
        pytest.fail(f"❌ Assertion failed: {e}")
    except Exception as e:
        pytest.fail(f"⚠️ Unexpected error: {e}")