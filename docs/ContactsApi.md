# swagger_client.ContactsApi

All URIs are relative to *http://localhost:8080/repp/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_id_delete**](ContactsApi.md#contacts_id_delete) | **DELETE** /contacts/{id} | Contact delete
[**contacts_id_get**](ContactsApi.md#contacts_id_get) | **GET** /contacts/{id} | Contact info
[**contacts_id_head**](ContactsApi.md#contacts_id_head) | **HEAD** /contacts/{id} | Contact check
[**contacts_id_patch**](ContactsApi.md#contacts_id_patch) | **PATCH** /contacts/{id} | Contact update
[**contacts_id_transfers_latest_delete**](ContactsApi.md#contacts_id_transfers_latest_delete) | **DELETE** /contacts/{id}/transfers/latest | Contact transfer cancel
[**contacts_id_transfers_latest_get**](ContactsApi.md#contacts_id_transfers_latest_get) | **GET** /contacts/{id}/transfers/latest | Contact transfer query
[**contacts_id_transfers_latest_put**](ContactsApi.md#contacts_id_transfers_latest_put) | **PUT** /contacts/{id}/transfers/latest | Contact transfer approve
[**contacts_id_transfers_post**](ContactsApi.md#contacts_id_transfers_post) | **POST** /contacts/{id}/transfers | Contact transfer request
[**contacts_post**](ContactsApi.md#contacts_post) | **POST** /contacts | Contact create

# **contacts_id_delete**
> str contacts_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Contact delete

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Contact delete
    api_response = api_instance.contacts_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_delete: %s\n" % e)
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

# **contacts_id_get**
> str contacts_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, filter=filter, val=val)

Contact info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)
filter = 'filter_example' # str |  (optional)
val = 'val_example' # str |  (optional)

try:
    # Contact info
    api_response = api_instance.contacts_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid, filter=filter, val=val)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_get: %s\n" % e)
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
 **filter** | **str**|  | [optional] 
 **val** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_id_head**
> contacts_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Contact check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Contact check
    api_instance.contacts_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_head: %s\n" % e)
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

# **contacts_id_patch**
> str contacts_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)

Contact update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
body = 'body_example' # str | Default request body for XML of JSON message
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Contact update
    api_response = api_instance.contacts_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_patch: %s\n" % e)
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

# **contacts_id_transfers_latest_delete**
> str contacts_id_transfers_latest_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)

Contact transfer cancel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)

try:
    # Contact transfer cancel
    api_response = api_instance.contacts_id_transfers_latest_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_transfers_latest_delete: %s\n" % e)
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

# **contacts_id_transfers_latest_get**
> str contacts_id_transfers_latest_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)

Contact transfer query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)

try:
    # Contact transfer query
    api_response = api_instance.contacts_id_transfers_latest_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_transfers_latest_get: %s\n" % e)
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

# **contacts_id_transfers_latest_put**
> str contacts_id_transfers_latest_put(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)

Contact transfer approve

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)

try:
    # Contact transfer approve
    api_response = api_instance.contacts_id_transfers_latest_put(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_transfers_latest_put: %s\n" % e)
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

# **contacts_id_transfers_post**
> str contacts_id_transfers_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)

Contact transfer request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
repp_auth_info = 'repp_auth_info_example' # str | Object authorization details (optional)
repp_roid = 'repp_roid_example' # str | Object linked to authorization (optional)

try:
    # Contact transfer request
    api_response = api_instance.contacts_id_transfers_post(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, repp_auth_info=repp_auth_info, repp_roid=repp_roid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_id_transfers_post: %s\n" % e)
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

# **contacts_post**
> str contacts_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)

Contact create

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactsApi()
body = 'body_example' # str | Default request body for XML of JSON message
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Contact create
    api_response = api_instance.contacts_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Default request body for XML of JSON message | 
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
 **repp_svcs_ext** | **str**| Extension namespace used | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/epp+json, application/epp+xml
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

