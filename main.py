from __future__ import print_function
import time
from swagger_client import (
    DomainsApi,
    DomainCreateRequest,
    DomainCreateRequestCommand,
    DomainCreateType,
    DomainAuthInfoType,
    DomainPeriodType,
    EppcomPwAuthInfoType
)
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

import secrets
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(letters) for _ in range(length))

# create an instance of the API class
api_instance = DomainsApi()
body = DomainCreateRequest(
    command=DomainCreateRequestCommand(
        create=DomainCreateType(
            name="foo.com",
            auth_info={
                "pw": EppcomPwAuthInfoType(
                    value=generate_random_string(8)
                )
            },
            period=DomainPeriodType(
                unit='y',
                value=1
            )
        )
    )
)
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain create
    api_response = api_instance.domains_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_post: %s\n" % e)