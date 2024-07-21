from __future__ import print_function
import time
from swagger_client import (
    DomainsApi,
    DomainCreateRequest,
    DomainCreateRequestCommand,
    DomainCreateType,
    DomainAuthInfoType,
    DomainPeriodType,
    EppcomPwAuthInfoType,
    DomainCreateRequestCommandExtension,
    SecDNSDsOrKeyType,
    SecDNSDsDataType
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

repp_cltrid = 'cltrid_with_DNSSEC' # str | Client transaction identifier
repp_svcs = ','.join(['urn:ietf:params:xml:ns:secDNS-1.1', 'unknown']) # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

# Domain create request with DNSSEC
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
        ),
        extension=DomainCreateRequestCommandExtension(
            sec_dns={
                "maxSigLife": 604800,
                "dsData": [SecDNSDsDataType(
                    key_tag=12345,
                    alg=3,
                    digest_type=1,
                    digest="49FD46E6C4B45C55D4AC"
                )]
            }
        )
    )
)

try:
    # Domain create with DNSSEC
    api_response = api_instance.domains_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_post: %s\n" % e)

repp_cltrid = 'cltrid_without_DNSSEC' # str | Client transaction identifier
repp_svcs = "other-extension" # str | Namespace used

# Domain create request without DNSSEC
body = DomainCreateRequest(
    command={
        "create": DomainCreateType(
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
        ),
        "clTRID": repp_cltrid,
        "unknown": "knock, knock"
    }
)

try:
    # Domain create without DNSSEC
    api_response = api_instance.domains_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_post: %s\n" % e)

