"""Generated client library for serviceusage version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.serviceusage.v1alpha import serviceusage_v1alpha_messages as messages


class ServiceusageV1alpha(base_api.BaseApiClient):
  """Generated client library for service serviceusage version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://serviceusage.googleapis.com/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'serviceusage'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only', 'https://www.googleapis.com/auth/service.management']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ServiceusageV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new serviceusage handle."""
    url = url or self.BASE_URL
    super(ServiceusageV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.services = self.ServicesService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(ServiceusageV1alpha.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (ServiceusageOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/operations/{operationsId}',
        http_method='GET',
        method_id='serviceusage.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='ServiceusageOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ServicesService(base_api.BaseApiService):
    """Service class for the services resource."""

    _NAME = 'services'

    def __init__(self, client):
      super(ServiceusageV1alpha.ServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def GenerateIdentity(self, request, global_params=None):
      r"""Generate service identity for service.

      Args:
        request: (ServiceusageServicesGenerateIdentityRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('GenerateIdentity')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateIdentity.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/{v1alphaId}/{v1alphaId1}/services/{servicesId}:generateIdentity',
        http_method='POST',
        method_id='serviceusage.services.generateIdentity',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}:generateIdentity',
        request_field='',
        request_type_name='ServiceusageServicesGenerateIdentityRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def GetIdentity(self, request, global_params=None):
      r"""Get service identity for service.

      Args:
        request: (ServiceusageServicesGetIdentityRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceIdentity) The response message.
      """
      config = self.GetMethodConfig('GetIdentity')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIdentity.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/{v1alphaId}/{v1alphaId1}/services/{servicesId}:getIdentity',
        http_method='GET',
        method_id='serviceusage.services.getIdentity',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}:getIdentity',
        request_field='',
        request_type_name='ServiceusageServicesGetIdentityRequest',
        response_type_name='ServiceIdentity',
        supports_download=False,
    )