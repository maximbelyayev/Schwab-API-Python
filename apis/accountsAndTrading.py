"""
APIs for Accounts and Trading
https://developer.tdameritrade.com/account-access/apis
"""

import requests
from variables import globals


def cancelOrder(orderId):
    return requests.delete('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders/' + orderId,
                           headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def getOrder(orderId):
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders/' + orderId,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


"""
#Unfortunatley python doesn't support function overloading so if you prefer this method use this one.
def getOrdersByPath(maxResults, fromEnteredTime, toEnteredTime, status):  # times are entered as "yyyy-MM-dd"
    args = (inspect.signature(getOrdersByPath)).parameters.keys()
    params = {}
    for arg in args:
        var = locals()[arg]
        if var not in ["", "null", None]: params[arg] = var
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders',
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()
"""


def getOrdersByPath(**kwargs):  # times are entered as "yyyy-MM-dd"
    args = ["maxResults", "fromEnteredTime", "toEnteredTime", "status"]
    params = {}
    for key, value in kwargs.items():
        if key in args: params[key] = value
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders',
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()
# options for status "AWAITING_PARENT_ORDER", "AWAITING_CONDITION", "AWAITING_MANUAL_REVIEW", "ACCEPTED", "AWAITING_UR_OUT", "PENDING_ACTIVATION", "QUEUED", "WORKING", "REJECTED", "PENDING_CANCEL", "CANCELED", "PENDING_REPLACE", "REPLACED", "FILLED", "EXPIRED"


"""
def getOrdersByQuery(accountId, maxResults, fromEnteredTime, toEnteredTime, status):
    args = (inspect.signature(getOrdersByPath)).parameters.keys()
    params = {}
    for arg in args:
        var = locals()[arg]
        if var not in ["", "null", None]: params[arg] = var
    return requests.get('https://api.tdameritrade.com/v1/orders/',
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()
"""


def getOrdersByQuery(**kwargs):
    args = ["accountId", "maxResults", "fromEnteredTime", "toEnteredTime", "status"]
    params = {}
    for key, value in kwargs.items():
        if key in args: params[key] = value
    return requests.get('https://api.tdameritrade.com/v1/orders/',
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def placeOrder(data):
    return requests.post('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders',
                         json=data,
                         headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def replaceOrder(orderId, data):
    return requests.put('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/orders/' + orderId,
                        data=data,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def createSavedOrder(data):  # FIX
    return requests.post('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/savedorders',
                         json=data,
                         headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def deleteSavedOrder(savedOrderId):
    return requests.delete('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/savedorders/' + savedOrderId,
                           headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def getSavedOrder(savedOrderId):
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/savedorders/' + savedOrderId,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def getSavedOrdersByPath():
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/savedorders/',
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


# not tested
def replaceSavedOrder(savedOrderId, data):  # FIX
    return requests.put('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber + '/savedorders/' + savedOrderId,
                        params=data,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


# not tested
def getAccount(**kwargs):
    args = ["fields"]
    params = {}
    for key, value in kwargs.items():
        if key in args: params[key] = value
    return requests.get('https://api.tdameritrade.com/v1/accounts/' + globals.accountNumber,
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


# not tested
def getAccounts(**kwargs):
    args = ["fields"]
    params = {}
    for key, value in kwargs.items():
        if key in args: params[key] = value
    return requests.get('https://api.tdameritrade.com/v1/accounts/',
                        params=params,
                        headers={'Authorization': 'Bearer ' + globals.accessToken}).json()


def examples():
    print("------------------------------------")
    print("Examples for: api-accountsAndTrading")
    print("------------------------------------")
    print("No examples yet")
    print("------------------------------------")
    print("------------------------------------")
    print("------------------------------------")
    print("------------------------------------")
    return
