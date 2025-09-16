import requests
import json


def generate_otp(phone_number):
    generate_otp_url = "https://cerberus.ather.io/auth/v2/generate-login-otp"

    payload = {"email": "", "contact_no": phone_number, "country_code": "IN"}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Charset": "UTF-8",
        "User-Agent": "Ktor client",
        "Source": "ATHER_APP/11.3.0",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = requests.post(generate_otp_url, json=payload, headers=headers, allow_redirects=True)
        # print(f"Request URL: {generate_otp_url}")
        # print(f"Request Payload: {json.dumps(payload, indent=4)}")
        # print(f"Response Status Code: {response.status_code}")
        # print(f"Response Text: {response.text}")

        if response.status_code == 200:
            response_data = response.json()
            print("OTP generated successfully.")
            return True
            # return response_data['data']
        else:
            print("Failed to generate OTP. Please check the response above.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None


def verify_otp(phone_number, otp):
    verify_otp_url = "https://cerberus.ather.io/auth/v2/verify-login-otp"

    payload = {
        "email": "",
        "contact_no": phone_number,
        "userOtp": otp,
        "is_mobile_login": "true",
        "country_code": "IN",
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Charset": "UTF-8",
        "User-Agent": "Ktor client",
        "Source": "ATHER_APP/11.3.0",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = requests.post(verify_otp_url, json=payload, headers=headers, allow_redirects=True)
        # print(f"Request URL: {verify_otp_url}")
        # print(f"Request Payload: {json.dumps(payload, indent=4)}")
        # print(f"Response Status Code: {response.status_code}")
        # print(f"Response Text: {response.text}")

        if response.status_code == 200:
            response_data = response.json()
            return response_data["token"]
        else:
            print("Failed to verify OTP. Please check the response above.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None


def main():
    phone_number = input("Enter your phone number: ")

    # Generate OTP
    otp_data = generate_otp(phone_number)
    if not otp_data:
        return

    otp = input(f"Enter the OTP sent to {phone_number}: ")
    verification_data = verify_otp(phone_number, otp)

    if verification_data:
        print("OTP verified successfully.")
        print("Token:", json.dumps(verification_data, indent=4))


if __name__ == "__main__":
    main()