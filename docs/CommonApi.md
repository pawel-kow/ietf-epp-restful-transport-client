# swagger_client.CommonApi

All URIs are relative to *http://localhost:8080/repp/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_get**](CommonApi.md#messages_get) | **GET** /messages | Poll request
[**messages_id_head**](CommonApi.md#messages_id_head) | **HEAD** /messages/{id} | Poll ack
[**root_get**](CommonApi.md#root_get) | **GET** / | Hello

# **messages_get**
> str messages_get(repp_cltrid, repp_svcs, accept_language, body=body, repp_svcs_ext=repp_svcs_ext)

Poll request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Poll request
    api_response = api_instance.messages_get(repp_cltrid, repp_svcs, accept_language, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repp_cltrid** | **str**| Client transaction identifier | 
 **repp_svcs** | **str**| Namespace used | 
 **accept_language** | **str**| Language used for response | 
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

# **messages_id_head**
> messages_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Poll ack

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Poll ack
    api_instance.messages_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
except ApiException as e:
    print("Exception when calling CommonApi->messages_id_head: %s\n" % e)
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

# **root_get**
> str root_get(accept_language)

Hello

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()
accept_language = 'accept_language_example' # str | Language used for response

try:
    # Hello
    api_response = api_instance.root_get(accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language used for response | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/epp+json, application/epp+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

