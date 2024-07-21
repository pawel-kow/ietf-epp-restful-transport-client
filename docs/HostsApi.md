# swagger_client.HostsApi

All URIs are relative to *http://localhost:8080/repp/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosts_id_delete**](HostsApi.md#hosts_id_delete) | **DELETE** /hosts/{id} | Host delete
[**hosts_id_get**](HostsApi.md#hosts_id_get) | **GET** /hosts/{id} | Host info
[**hosts_id_head**](HostsApi.md#hosts_id_head) | **HEAD** /hosts/{id} | Host check
[**hosts_id_patch**](HostsApi.md#hosts_id_patch) | **PATCH** /hosts/{id} | Host update
[**hosts_post**](HostsApi.md#hosts_post) | **POST** /hosts | Host create

# **hosts_id_delete**
> str hosts_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Host delete

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Host delete
    api_response = api_instance.hosts_id_delete(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_id_delete: %s\n" % e)
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

# **hosts_id_get**
> str hosts_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, filter=filter, val=val)

Host info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)
filter = 'filter_example' # str |  (optional)
val = 'val_example' # str |  (optional)

try:
    # Host info
    api_response = api_instance.hosts_id_get(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext, filter=filter, val=val)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_id_get: %s\n" % e)
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

# **hosts_id_head**
> hosts_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)

Host check

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
body = 'body_example' # str | Default request body for XML of JSON message (optional)
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Host check
    api_instance.hosts_id_head(repp_cltrid, repp_svcs, accept_language, id, body=body, repp_svcs_ext=repp_svcs_ext)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_id_head: %s\n" % e)
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

# **hosts_id_patch**
> str hosts_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)

Host update

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
body = 'body_example' # str | Default request body for XML of JSON message
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
id = 'id_example' # str | Object identifier
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Host update
    api_response = api_instance.hosts_id_patch(body, repp_cltrid, repp_svcs, accept_language, id, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_id_patch: %s\n" % e)
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

# **hosts_post**
> str hosts_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)

Host create

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
body = 'body_example' # str | Default request body for XML of JSON message
repp_cltrid = 'repp_cltrid_example' # str | Client transaction identifier
repp_svcs = 'repp_svcs_example' # str | Namespace used
accept_language = 'accept_language_example' # str | Language used for response
repp_svcs_ext = 'repp_svcs_ext_example' # str | Extension namespace used (optional)

try:
    # Host create
    api_response = api_instance.hosts_post(body, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext=repp_svcs_ext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_post: %s\n" % e)
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

