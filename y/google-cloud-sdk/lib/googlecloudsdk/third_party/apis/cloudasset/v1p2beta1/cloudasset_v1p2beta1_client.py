"""Generated client library for cloudasset version v1p2beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1p2beta1 import cloudasset_v1p2beta1_messages as messages


class CloudassetV1p2beta1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1p2beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudasset.googleapis.com/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'cloudasset'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1p2beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudassetV1p2beta1'
  _URL_VERSION = 'v1p2beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1p2beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.feeds = self.FeedsService(self)
    self.v1p2beta1 = self.V1p2beta1Service(self)

  class FeedsService(base_api.BaseApiService):
    """Service class for the feeds resource."""

    _NAME = 'feeds'

    def __init__(self, client):
      super(CloudassetV1p2beta1.FeedsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a feed in a parent project/folder/organization to listen to its.
asset updates.

      Args:
        request: (CloudassetFeedsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}/feeds',
        http_method='POST',
        method_id='cloudasset.feeds.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1p2beta1/{+parent}/feeds',
        request_field='createFeedRequest',
        request_type_name='CloudassetFeedsCreateRequest',
        response_type_name='Feed',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an asset feed.

      Args:
        request: (CloudassetFeedsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}/feeds/{feedsId}',
        http_method='DELETE',
        method_id='cloudasset.feeds.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p2beta1/{+name}',
        request_field='',
        request_type_name='CloudassetFeedsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details about an asset feed.

      Args:
        request: (CloudassetFeedsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}/feeds/{feedsId}',
        http_method='GET',
        method_id='cloudasset.feeds.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p2beta1/{+name}',
        request_field='',
        request_type_name='CloudassetFeedsGetRequest',
        response_type_name='Feed',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all asset feeds in a parent project/folder/organization.

      Args:
        request: (CloudassetFeedsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListFeedsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}/feeds',
        http_method='GET',
        method_id='cloudasset.feeds.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1p2beta1/{+parent}/feeds',
        request_field='',
        request_type_name='CloudassetFeedsListRequest',
        response_type_name='ListFeedsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an asset feed configuration.

      Args:
        request: (CloudassetFeedsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}/feeds/{feedsId}',
        http_method='PATCH',
        method_id='cloudasset.feeds.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p2beta1/{+name}',
        request_field='updateFeedRequest',
        request_type_name='CloudassetFeedsPatchRequest',
        response_type_name='Feed',
        supports_download=False,
    )

  class V1p2beta1Service(base_api.BaseApiService):
    """Service class for the v1p2beta1 resource."""

    _NAME = 'v1p2beta1'

    def __init__(self, client):
      super(CloudassetV1p2beta1.V1p2beta1Service, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGetAssetsHistory(self, request, global_params=None):
      r"""Batch gets the update history of assets that overlap a time window.
For RESOURCE content, this API outputs history with asset in both
non-delete or deleted status.
For IAM_POLICY content, this API outputs history when the asset and its
attached IAM POLICY both exist. This can create gaps in the output history.

      Args:
        request: (CloudassetBatchGetAssetsHistoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetAssetsHistoryResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGetAssetsHistory')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGetAssetsHistory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}:batchGetAssetsHistory',
        http_method='GET',
        method_id='cloudasset.batchGetAssetsHistory',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['assetNames', 'contentType', 'readTimeWindow_endTime', 'readTimeWindow_startTime'],
        relative_path='v1p2beta1/{+parent}:batchGetAssetsHistory',
        request_field='',
        request_type_name='CloudassetBatchGetAssetsHistoryRequest',
        response_type_name='BatchGetAssetsHistoryResponse',
        supports_download=False,
    )

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage.
location. The output format is newline-delimited JSON.
This API implements the google.longrunning.Operation API allowing you
to keep track of the export.

      Args:
        request: (CloudassetExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p2beta1/{v1p2beta1Id}/{v1p2beta1Id1}:exportAssets',
        http_method='POST',
        method_id='cloudasset.exportAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1p2beta1/{+parent}:exportAssets',
        request_field='exportAssetsRequest',
        request_type_name='CloudassetExportAssetsRequest',
        response_type_name='Operation',
        supports_download=False,
    )
