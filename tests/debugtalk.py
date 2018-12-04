import os
import random
import string
import time
import re 
import hmac
import hashlib
import requests
import json


BASE_URL = "http://127.0.0.1:5000"

demo_default_request = {
    "base_url": "$BASE_URL",
    "headers": {
        "content-type": "application/json"
    }
}

def sum_two(m, n):
    return m + n

def sum_status_code(status_code, expect_sum):
    """ sum status code digits
        e.g. 400 => 4, 201 => 3
    """
    sum_value = 0
    for digit in str(status_code):
        sum_value += int(digit)

    assert sum_value == expect_sum

def is_status_code_200(status_code):
    return status_code == 200

os.environ["TEST_ENV"] = "PRODUCTION"

def skip_test_in_production_env():
    """ skip this test in production environment
    """
    return os.environ["TEST_ENV"] == "PRODUCTION"

def gen_app_version():
    return [
        {"app_version": "2.8.5"},
        {"app_version": "2.8.6"}
    ]

def get_account():
    return [
        {"username": "user1", "password": "111111"},
        {"username": "user2", "password": "222222"}
    ]

def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

def setup_hook_add_kwargs(request):
    request["key"] = "value"

def setup_hook_remove_kwargs(request):
    request.pop("key")

def teardown_hook_sleep_N_secs(response, n_secs):
    """ sleep n seconds after request
    """
    if response.status_code == 200:
        time.sleep(0.1)
    else:
        time.sleep(n_secs)

def hook_print(msg):
    print(msg)

def modify_headers_os_platform(request, os_platform):
    request["headers"]["os_platform"] = os_platform

def setup_hook_httpntlmauth(request):
    if "httpntlmauth" in request:
        from requests_ntlm import HttpNtlmAuth
        auth_account = request.pop("httpntlmauth")
        request["auth"] = HttpNtlmAuth(
            auth_account["username"], auth_account["password"])

def alter_response(response):
    response.status_code = 500
    response.headers["Content-Type"] = "html/text"
    response.json["headers"]["Host"] = "127.0.0.1:8888"
    response.new_attribute = "new_attribute_value"
    response.new_attribute_dict = {
        "key": 123
    }

def get_param_url(url):
    res = re.findall(r"param=(.*)",url)
    return res
    
# def alter_response_error(response):
    # NameError
    # not_defined_variable

def gen_random_number(num_len):
    random_num_list = []
    for _ in range(num_len):
        random_num = random.choice(range(0,9))
        random_num_list.append(random_num)

    random_number = ''.join(random_num_list)
    return random_number

def sleep_secs(n):
    time.sleep(n)

secret = "753b9f6acafcbba300315838be3374c1"

def signature(*args):
        content = bytes(json.dumps(*args), encoding='utf8')
        secret_key = bytes(secret, encoding='utf8')
        signature = hmac.new(secret_key, content, digestmod=hashlib.sha256).hexdigest();
        return signature

#变量的定义
name = os.environ["name"]
idno = os.environ["idno"]
mobile = os.environ["mobile"]
cardno = os.environ["cardno"]
base_url = os.environ["base_url"]
c_name = os.environ["c_name"]
codeORG = os.environ["codeORG"]
codeREG = os.environ["codeREG"]
codeUSC = os.environ["codeUSC"]
legalName = os.environ["legalName"]
authcode = os.environ["authcode"]
isfrom = os.environ["isfrom"]
callbackUrl = os.environ["callbackUrl"]
bank = os.environ["bank"]
cardno_org = os.environ["cardno_org"]
subbranch = os.environ["subbranch"]
cash = os.environ["cash"]
oid = os.environ["oid"]
orgOid = os.environ["orgOid"]
projectId = os.environ["projectId"]









    
