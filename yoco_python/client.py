import json
import requests


class YocoClient():
    """
    Yoco API SDK.
    
    :param secret_key: The secret key for the Yoco API.
    :param charge_token: The token generated by the Yoco card tokenizer plugin.
    :param amount: The amount to charge in cents.
    :param currency: The currency of the amount as an ISO 4217 currency code.

    https://developer.yoco.com/online/api-reference/charge-api
    
    https://developer.yoco.com/online/api-reference/refund-api
    """

    def __init__(self, secret_key: str, charge_token: str, amount_in_cents: int, currency: str='ZAR'):
        self.secret_key = secret_key
        self.charge_token = charge_token
        self.amount_in_cents = amount_in_cents
        self.currency = currency
        self.charge_success = False
        self.refund_success = False
        
    def charge(self):
        """
        Charge the card.

        :return: The response from the Yoco API.
        """

        url = 'https://online.yoco.com/v1/charges/'
        headers = {
            'X-Auth-Secret-Key': self.secret_key,
        }
        json = {
            'token': self.charge_token,
            'amountInCents': self.amount_in_cents,
            'currency': self.currency,
        }
        response = requests.post(url, headers=headers, json=json)
        json_response = response.json()
        if response.status_code == 201:
            self.charge_success = True
            self.charge_id = json_response['id']
        return json_response

    def refund(self):
        """
        Refund the charge.

        :return: The response from the Yoco API.
        """

        url = 'https://online.yoco.com/v1/refunds/',
        headers = {
            'X-Auth-Secret-Key': self.secret_key,
        }
        json = {
            'chargeId': self.charge_id,
        }
        response = requests.post(url, headers=headers, json=json)
        json_response = response.json()
        if response.status_code == 200:
            self.refund_success = True
            self.refund_id = json_response['id']
        return json_response