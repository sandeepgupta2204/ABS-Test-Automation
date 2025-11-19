import requests
import pytest
import json
import os

# ============================================================
# CONFIGURATION
# ============================================================

BASE_URL = "https://input-backend.api.dehat.co/sale-management/order-requests/v2"
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
    "X-Request-ID": "2abe3c61-4186-4e9d-b8de-b55bdaccad66",
    "api-request-trace-id": "2abe3c61-4186-4e9d-b8de-b55bdaccad66",
    "DEVICE-ID": "b0742429-9bfb-4be9-bd44-3ce39b326a18",
    # ✅ Paste your fresh token here exactly (no truncation)
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWcnkxU3R2..."
}

PAYLOAD = {
    "cart_id": "908c69a8-a298-49ed-9398-7565c7ee9c31",
    "products": [
        {
            "product_id": "12000498",
            "total_order_quantity": 1,
            "product_type": "regular",
            "payment_modes": ["credit"],
            "is_bundle": False,
            "slots": [
                {"order_type": "confirmed", "id": None, "start_date": 1763490600, "end_date": 1763836199, "qty": 1},
                {"order_type": "virtual_order", "id": None, "start_date": None, "end_date": None},
                {"order_type": "preorder", "id": None, "start_date": None, "end_date": None}
            ],
            "unit_price": 1000,
            "untaxed_unit_price": "952.38"
        }
    ],
    "wallet_applied": True,
    "order_payment_mode": "prepaid",
    "ib_customer_id": "50034",
    "amount_details": {
        "cart_details": {
            "order_total": 1000,
            "delivery_fee": 0,
            "cart_breakup": {"sub_total": 952.38, "gst": 47.62}
        },
        "payment_details": {
            "amount_payable": 1000,
            "paid_using_credit_limit": 0,
            "discount_breakup": {},
            "overdue": 0,
            "total_applied_discount": 0,
            "wallet_balance_used": 0,
            "abs_balance_used": 40,
            "cashback_as_credit_note": 0
        },
        "payment_mode_breakup": {
            "credit": {
                "payable_amount": 1000,
                "net_payable": 960,
                "effective_amount": 1000,
                "abs_balance_used": 40,
                "remaining_used_advance_balance": 0,
                "paid_using_credit_limit": 0,
                "total_cashback_discount": 0,
                "instant_discount_breakup": [],
                "cashback_discount_breakup": [],
                "enabled": True
            },
            "prepaid": {
                "payable_amount": 1000,
                "net_payable": 960,
                "effective_amount": 1000,
                "paid_using_credit_limit": 0,
                "remaining_used_advance_balance": 0,
                "abs_balance_used": 40,
                "total_cashback_discount": 0,
                "instant_discount_breakup": [],
                "cashback_discount_breakup": [],
                "savings": 0,
                "enabled": True
            }
        }
    }
}

# ============================================================
# TEST FUNCTION
# ============================================================

@pytest.mark.api
def test_post_order_request():
    """
    Validate POST /sale-management/order-requests/v2
    Handles 200/201 success, 409 duplicates, and 401 unauthorized clearly
    """

    try:
        print("\n🚀 Sending Order Request API")
        print(f"Using cart_id: {PAYLOAD['cart_id']}\n")

        response = requests.post(BASE_URL, headers=HEADERS, params=PARAMS, json=PAYLOAD, timeout=20)
        print(f"HTTP Status: {response.status_code}")

        # --- Handle 401 Unauthorized ---
        if response.status_code == 401:
            pytest.fail("🔑 401 Unauthorized — token expired/invalid. Please update Authorization Bearer token.")

        # --- Accept 200/201/409 as business valid responses ---
        assert response.status_code in [200, 201, 409], f"Unexpected HTTP Status: {response.status_code}"

        try:
            json_data = response.json()
        except ValueError:
            pytest.fail("❌ Response is not valid JSON")

        print("Response JSON:", json.dumps(json_data, indent=2))

        # --- Handle Duplicate / Conflict ---
        if response.status_code == 409:
            msg = (json_data.get("message") or json_data.get("error") or "").lower()
            print("⚠️ 409 Conflict detected:", msg)
            if any(k in msg for k in ("already", "duplicate", "conflict", "exists")):
                print("✅ Duplicate cart/order handled successfully.")
                return
            pytest.fail("❌ 409 received but message not indicating duplicate/conflict")

        # --- Success response validation ---
        if "data" not in json_data:
            pytest.fail("❌ Missing 'data' in successful response")

        data = json_data["data"]
        order_id = data.get("order_id") or data.get("order_request_id") or data.get("id")
        assert order_id, "Missing order_id in response"
        status = data.get("status") or data.get("state") or ""
        assert status, "Missing status in response"
        assert status.lower() in ["success", "created", "completed"], f"Unexpected status: {status}"

        print(f"✅ Order created successfully — ID: {order_id}, Status: {status}")

    except requests.exceptions.Timeout:
        pytest.fail("⏰ Request timed out")
    except requests.exceptions.ConnectionError:
        pytest.fail("🚫 Connection error — check endpoint or VPN")
    except AssertionError as e:
        pytest.fail(f"❌ Assertion failed: {e}")
    except Exception as e:
        pytest.fail(f"⚠️ Unexpected error: {e}")