# Sending SMS Using Twilio SMS with FastAPI

If you're looking to send SMS messages using the Twilio SMS along with FastAPI, follow these installation and setup steps:

## Installation Steps:

1. **Sign Up on Twilio and Create an Account:** Before getting started, make sure you have a Twilio account. If not, sign up for one.

2. **Configure Authentication Details:** Open the `AuthDetail.py` file and modify the `AuthKey`, `Phone Number`, and `Account SID` with your Twilio account's actual authentication details.

3. **Install Required Packages:** Install all the necessary dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Server:** After successfully installing the dependencies, use the following command to launch the server:

    ```bash
    uvicorn main:app --reload
    ```

    Alternatively, you can use the following command as well:

    ```bash
    python -m uvicorn main:app --reload
    ```

5. **Check Server Status:** Open your web browser and navigate to `http://localhost`. Ensure that the server status is displayed as "OK".

Please make sure to follow these steps carefully to set up the Twilio SMS API integration with FastAPI for sending SMS messages. If you encounter any issues, refer to the provided steps.
