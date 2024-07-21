# swagger_client.DomainsApi

All URIs are relative to *http://localhost:8080/repp/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_id_delete**](DomainsApi.md#domains_id_delete) | **DELETE** /domains/{id} | Domain delete
[**domains_id_get**](DomainsApi.md#domains_id_get) | **GET** /domains/{id} | Domain info
[**domains_id_head**](DomainsApi.md#domains_id_head) | **HEAD** /domains/{id} | Domain check
[**domains_id_patch**](DomainsApi.md#domains_id_patch) | **PATCH** /domains/{id} | Domain update
[**domains_id_renewals_post**](DomainsApi.md#domains_id_renewals_post) | **POST** /domains/{id}/renewals | Domain renew
[**domains_id_transfers_latest_delete**](DomainsApi.md#domains_id_transfers_latest_delete) | **DELETE** /domains/{id}/transfers/latest | Domain transfer cancel
[**domains_id_transfers_latest_get**](DomainsApi.md#domains_id_transfers_latest_get) | **GET** /domains/{id}/transfers/latest | Domain transfer query
[**domains_id_transfers_latest_put**](DomainsApi.md#domains_id_transfers_latest_put) | **PUT** /domains/{id}/transfers/latest | Domain transfer approve
[**domains_id_transfers_post**](DomainsApi.md#domains_id_transfers_post) | **POST** /domains/{id}/transfers | Domain transfer request
[**domains_post**](DomainsApi.md#domains_post) | **POST** /domains | Domain create

# **domains_id_delete**
> str domains_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Domain delete

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain delete
    api_response = api_instance.domains_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_get**
> str domains_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, filter=filter, val=val)

Domain info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)
filter = 'filter_example' # str | Name of attibute to filter on (optional)
val = 'val_example' # str | Value to use for filter (optional)

try:
    # Domain info
    api_response = api_instance.domains_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, filter=filter, val=val)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 
 **repp_auth_info** | **str**| Object authorization details | [optional] 
 **repp_roid** | **str**| Object linked to authorization | [optional] 
 **filter** | **str**| Name of attibute to filter on | [optional] 
 **val** | **str**| Value to use for filter | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_head**
> domains_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Domain check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain check
    api_instance.domains_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_patch**
> str domains_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)

Domain update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = 'body_example' # str | Default request body for XML of JSON message
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain update
    api_response = api_instance.domains_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Default request body for XML of JSON message | 
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_renewals_post**
> str domains_id_renewals_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, unit=unit, value=value, current_date=current_date)

Domain renew

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
unit = 'unit_example' # str | Unit used for renewal value (e.g. y for year) (optional)
value = 56 # int | Value for renewal (optional)
current_date = 'current_date_example' # str | Date on which the current validity period ends (optional)

try:
    # Domain renew
    api_response = api_instance.domains_id_renewals_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, unit=unit, value=value, current_date=current_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_renewals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 
 **unit** | **str**| Unit used for renewal value (e.g. y for year) | [optional] 
 **value** | **int**| Value for renewal | [optional] 
 **current_date** | **str**| Date on which the current validity period ends | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_transfers_latest_delete**
> str domains_id_transfers_latest_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Domain transfer cancel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain transfer cancel
    api_response = api_instance.domains_id_transfers_latest_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_transfers_latest_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_transfers_latest_get**
> str domains_id_transfers_latest_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)

Domain transfer query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)

try:
    # Domain transfer query
    api_response = api_instance.domains_id_transfers_latest_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_transfers_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 
 **repp_auth_info** | **str**| Object authorization details | [optional] 
 **repp_roid** | **str**| Object linked to authorization | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_transfers_latest_put**
> str domains_id_transfers_latest_put(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Domain transfer approve

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Domain transfer approve
    api_response = api_instance.domains_id_transfers_latest_put(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_transfers_latest_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_id_transfers_post**
> str domains_id_transfers_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, unit=unit, value=value)

Domain transfer request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)
unit = 'unit_example' # str | Unit used for renewal value (e.g. y for year) (optional)
value = 56 # int | Value for renewal (optional)

try:
    # Domain transfer request
    api_response = api_instance.domains_id_transfers_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, unit=unit, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains_id_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **id** | **str**| Object identifier | 
 **body** | [**str**](str.md)| Default request body for XML of JSON message | [optional] 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 
 **repp_auth_info** | **str**| Object authorization details | [optional] 
 **repp_roid** | **str**| Object linked to authorization | [optional] 
 **unit** | **str**| Unit used for renewal value (e.g. y for year) | [optional] 
 **value** | **int**| Value for renewal | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains_post**
> str domains_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)

Domain create

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = swagger_client.DomainCreateRequest() # DomainCreateRequest | 
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainCreateRequest**](DomainCreateRequest.md)|  | 
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

