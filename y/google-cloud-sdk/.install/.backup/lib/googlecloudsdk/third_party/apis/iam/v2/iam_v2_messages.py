"""Generated message classes for iam version v2.

Manages identity and access control for Google Cloud Platform resources,
including the creation of service accounts, which you can use to authenticate
to Google and make API calls.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'iam'


class GoogleIamAdminV1AuditData(_messages.Message):
  r"""Audit log information specific to Cloud IAM admin APIs. This message is
  serialized as an `Any` type in the `ServiceData` message of an `AuditLog`
  message.

  Fields:
    permissionDelta: The permission_delta when when creating or updating a
      Role.
  """

  permissionDelta = _messages.MessageField('GoogleIamAdminV1AuditDataPermissionDelta', 1)


class GoogleIamAdminV1AuditDataPermissionDelta(_messages.Message):
  r"""A PermissionDelta message to record the added_permissions and
  removed_permissions inside a role.

  Fields:
    addedPermissions: Added permissions.
    removedPermissions: Removed permissions.
  """

  addedPermissions = _messages.StringField(1, repeated=True)
  removedPermissions = _messages.StringField(2, repeated=True)


class GoogleIamV1BindingDelta(_messages.Message):
  r"""One delta entry for Binding. Each individual change (only one member in
  each entry) to a binding will be a separate entry.

  Enums:
    ActionValueValuesEnum: The action that was performed on a Binding.
      Required

  Fields:
    action: The action that was performed on a Binding. Required
    condition: The condition that is associated with this binding.
    member: A single identity requesting access for a Google Cloud resource.
      Follows the same format of Binding.members. Required
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`. Required
  """

  class ActionValueValuesEnum(_messages.Enum):
    r"""The action that was performed on a Binding. Required

    Values:
      ACTION_UNSPECIFIED: Unspecified.
      ADD: Addition of a Binding.
      REMOVE: Removal of a Binding.
    """
    ACTION_UNSPECIFIED = 0
    ADD = 1
    REMOVE = 2

  action = _messages.EnumField('ActionValueValuesEnum', 1)
  condition = _messages.MessageField('GoogleTypeExpr', 2)
  member = _messages.StringField(3)
  role = _messages.StringField(4)


class GoogleIamV1LoggingAuditData(_messages.Message):
  r"""Audit log information specific to Cloud IAM. This message is serialized
  as an `Any` type in the `ServiceData` message of an `AuditLog` message.

  Fields:
    policyDelta: Policy delta between the original policy and the newly set
      policy.
  """

  policyDelta = _messages.MessageField('GoogleIamV1PolicyDelta', 1)


class GoogleIamV1PolicyDelta(_messages.Message):
  r"""The difference delta between two policies.

  Fields:
    bindingDeltas: The delta for Bindings between two policies.
  """

  bindingDeltas = _messages.MessageField('GoogleIamV1BindingDelta', 1, repeated=True)


class GoogleIamV1betaWorkloadIdentityPoolOperationMetadata(_messages.Message):
  r"""Metadata for long-running WorkloadIdentityPool operations."""


class GoogleIamV2DenyRule(_messages.Message):
  r"""A deny rule in an IAM deny policy.

  Fields:
    denialCondition: The condition that determines whether this deny rule
      applies to a request. If the condition expression evaluates to `true`,
      then the deny rule is applied; otherwise, the deny rule is not applied.
      Each deny rule is evaluated independently. If this deny rule does not
      apply to a request, other deny rules might still apply. The condition
      can use CEL functions that evaluate [resource
      tags](https://cloud.google.com/iam/help/conditions/resource-tags). Other
      functions and operators are not supported.
    deniedPermissions: The permissions that are explicitly denied by this
      rule. Each permission uses the format
      `{service_fqdn}/{resource}.{verb}`, where `{service_fqdn}` is the fully
      qualified domain name for the service. For example,
      `iam.googleapis.com/roles.list`.
    deniedPrincipals: The identities that are prevented from using one or more
      permissions on Google Cloud resources. This field can contain the
      following values: * `principalSet://goog/public:all`: A special
      identifier that represents any principal that is on the internet, even
      if they do not have a Google Account or are not logged in. *
      `principal://goog/subject/{email_id}`: A specific Google Account.
      Includes Gmail, Cloud Identity, and Google Workspace user accounts. For
      example, `principal://goog/subject/alice@example.com`. *
      `deleted:principal://goog/subject/{email_id}?uid={uid}`: A specific
      Google Account that was deleted recently. For example,
      `deleted:principal://goog/subject/alice@example.com?uid=1234567890`. If
      the Google Account is recovered, this identifier reverts to the standard
      identifier for a Google Account. *
      `principalSet://goog/group/{group_id}`: A Google group. For example,
      `principalSet://goog/group/admins@example.com`. *
      `deleted:principalSet://goog/group/{group_id}?uid={uid}`: A Google group
      that was deleted recently. For example,
      `deleted:principalSet://goog/group/admins@example.com?uid=1234567890`.
      If the Google group is restored, this identifier reverts to the standard
      identifier for a Google group. * `principal://iam.googleapis.com/project
      s/-/serviceAccounts/{service_account_id}`: A Google Cloud service
      account. For example,
      `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-
      account@iam.gserviceaccount.com`. * `deleted:principal://iam.googleapis.
      com/projects/-/serviceAccounts/{service_account_id}?uid={uid}`: A Google
      Cloud service account that was deleted recently. For example,
      `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-
      service-account@iam.gserviceaccount.com?uid=1234567890`. If the service
      account is undeleted, this identifier reverts to the standard identifier
      for a service account. *
      `principalSet://goog/cloudIdentityCustomerId/{customer_id}`: All of the
      principals associated with the specified Google Workspace or Cloud
      Identity customer ID. For example,
      `principalSet://goog/cloudIdentityCustomerId/C01Abc35`.
    exceptionPermissions: Specifies the permissions that this rule excludes
      from the set of denied permissions given by `denied_permissions`. If a
      permission appears in `denied_permissions` _and_ in
      `exception_permissions` then it will _not_ be denied. The excluded
      permissions can be specified using the same syntax as
      `denied_permissions`.
    exceptionPrincipals: The identities that are excluded from the deny rule,
      even if they are listed in the `denied_principals`. For example, you
      could add a Google group to the `denied_principals`, then exclude
      specific users who belong to that group. This field can contain the same
      values as the `denied_principals` field, excluding
      `principalSet://goog/public:all`, which represents all users on the
      internet.
  """

  denialCondition = _messages.MessageField('GoogleTypeExpr', 1)
  deniedPermissions = _messages.StringField(2, repeated=True)
  deniedPrincipals = _messages.StringField(3, repeated=True)
  exceptionPermissions = _messages.StringField(4, repeated=True)
  exceptionPrincipals = _messages.StringField(5, repeated=True)


class GoogleIamV2GetEffectivePoliciesResponse(_messages.Message):
  r"""A GoogleIamV2GetEffectivePoliciesResponse object.

  Fields:
    policiesPerResource: Ordered list starting from the resource on which this
      API was called, and walking up the hierarchy.
  """

  policiesPerResource = _messages.MessageField('GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResource', 1, repeated=True)


class GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResource(_messages.Message):
  r"""A GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResource object.

  Fields:
    attachmentPoint: Empty if the user doesn't have the "kind.list" permission
      for any of the policy kinds in the request.
    policiesPerResourcePerKind: One entry for each kind in the request.
  """

  attachmentPoint = _messages.StringField(1)
  policiesPerResourcePerKind = _messages.MessageField('GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerResourcePerKind', 2, repeated=True)


class GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerResourcePerKind(_messages.Message):
  r"""A GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerR
  esourcePerKind object.

  Fields:
    hasListPermission: Is false if "kind.list" permission is denied. If false,
      policies is empty.
    kind: A string attribute.
    policies: Includes policies for a specific kind for callers having
      'kind.list' permission (i.e. has_list_permission = true) and any such
      policies exist.
  """

  hasListPermission = _messages.BooleanField(1)
  kind = _messages.StringField(2)
  policies = _messages.MessageField('GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerResourcePerKindPolicyView', 3, repeated=True)


class GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerResourcePerKindPolicyView(_messages.Message):
  r"""A GoogleIamV2GetEffectivePoliciesResponsePoliciesPerResourcePoliciesPerR
  esourcePerKindPolicyView object.

  Fields:
    hasGetPermission: Is false if "kind.get" permission is denied. If false,
      policies.rules is empty.
    policy: A single policy. Includes policy.rules for callers having
      'kind.get' permission (i.e. has_get_permission = true) and rules exist
      in the policy.
  """

  hasGetPermission = _messages.BooleanField(1)
  policy = _messages.MessageField('GoogleIamV2Policy', 2)


class GoogleIamV2ListApplicablePoliciesResponse(_messages.Message):
  r"""Response message for ListApplicablePolicies method.

  Fields:
    inaccessible: A list of resources that the caller does not have permission
      to retrieve. List or Get can be used to get detailed error messages.
      Get: `policies/{attachment-point}/denypolicies/{policy-id}` List:
      `policies/{attachment-point}/denypolicies`
    nextPageToken: A page token that can be used in a
      ListApplicablePoliciesRequest to retrieve the next page. If this field
      is blank, there are no additional pages.
    policies: Ordered list starting from the resource on which this API was
      called then proceeding up the hierarchy. Policies for the same
      attachment point will be grouped, but no further ordering is guaranteed.
  """

  inaccessible = _messages.StringField(1, repeated=True)
  nextPageToken = _messages.StringField(2)
  policies = _messages.MessageField('GoogleIamV2Policy', 3, repeated=True)


class GoogleIamV2ListPoliciesResponse(_messages.Message):
  r"""Response message for `ListPolicies`.

  Fields:
    nextPageToken: A page token that you can use in a ListPoliciesRequest to
      retrieve the next page. If this field is omitted, there are no
      additional pages.
    policies: Metadata for the policies that are attached to the resource.
  """

  nextPageToken = _messages.StringField(1)
  policies = _messages.MessageField('GoogleIamV2Policy', 2, repeated=True)


class GoogleIamV2Policy(_messages.Message):
  r"""Data for an IAM policy.

  Messages:
    AnnotationsValue: A key-value map to store arbitrary metadata for the
      `Policy`. Keys can be up to 63 characters. Values can be up to 255
      characters.

  Fields:
    annotations: A key-value map to store arbitrary metadata for the `Policy`.
      Keys can be up to 63 characters. Values can be up to 255 characters.
    createTime: Output only. The time when the `Policy` was created.
    deleteTime: Output only. The time when the `Policy` was deleted. Empty if
      the policy is not deleted.
    displayName: A user-specified description of the `Policy`. This value can
      be up to 63 characters.
    etag: An opaque tag that identifies the current version of the `Policy`.
      IAM uses this value to help manage concurrent updates, so they do not
      cause one update to be overwritten by another. If this field is present
      in a CreatePolicy request, the value is ignored.
    kind: Output only. The kind of the `Policy`. Always contains the value
      `DenyPolicy`.
    managingAuthority: Immutable. Specifies that this policy is managed by an
      authority and can only be modified by that authority. Usage is
      restricted.
    name: Immutable. The resource name of the `Policy`, which must be unique.
      Format: `policies/{attachment_point}/denypolicies/{policy_id}` The
      attachment point is identified by its URL-encoded full resource name,
      which means that the forward-slash character, `/`, must be written as
      `%2F`. For example,
      `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-
      project/denypolicies/my-deny-policy`. For organizations and folders, use
      the numeric ID in the full resource name. For projects, requests can use
      the alphanumeric or the numeric ID. Responses always contain the numeric
      ID.
    rules: A list of rules that specify the behavior of the `Policy`. All of
      the rules should be of the `kind` specified in the `Policy`.
    uid: Immutable. The globally unique ID of the `Policy`. Assigned
      automatically when the `Policy` is created.
    updateTime: Output only. The time when the `Policy` was last updated.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AnnotationsValue(_messages.Message):
    r"""A key-value map to store arbitrary metadata for the `Policy`. Keys can
    be up to 63 characters. Values can be up to 255 characters.

    Messages:
      AdditionalProperty: An additional property for a AnnotationsValue
        object.

    Fields:
      additionalProperties: Additional properties of type AnnotationsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a AnnotationsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  annotations = _messages.MessageField('AnnotationsValue', 1)
  createTime = _messages.StringField(2)
  deleteTime = _messages.StringField(3)
  displayName = _messages.StringField(4)
  etag = _messages.StringField(5)
  kind = _messages.StringField(6)
  managingAuthority = _messages.StringField(7)
  name = _messages.StringField(8)
  rules = _messages.MessageField('GoogleIamV2PolicyRule', 9, repeated=True)
  uid = _messages.StringField(10)
  updateTime = _messages.StringField(11)


class GoogleIamV2PolicyOperationMetadata(_messages.Message):
  r"""Metadata for long-running `Policy` operations.

  Fields:
    createTime: Timestamp when the `google.longrunning.Operation` was created.
  """

  createTime = _messages.StringField(1)


class GoogleIamV2PolicyRule(_messages.Message):
  r"""A single rule in a `Policy`.

  Fields:
    denyRule: A rule for a deny policy.
    description: A user-specified description of the rule. This value can be
      up to 256 characters.
  """

  denyRule = _messages.MessageField('GoogleIamV2DenyRule', 1)
  description = _messages.StringField(2)


class GoogleLongrunningOperation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('GoogleRpcStatus', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class GoogleRpcStatus(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class GoogleTypeExpr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec. Example (Comparison):
  title: "Summary size limit" description: "Determines if a summary is less
  than 100 chars" expression: "document.summary.size() < 100" Example
  (Equality): title: "Requestor is owner" description: "Determines if
  requestor is the document owner" expression: "document.owner ==
  request.auth.claims.email" Example (Logic): title: "Public documents"
  description: "Determine whether the document should be publicly visible"
  expression: "document.type != 'private' && document.type != 'internal'"
  Example (Data Manipulation): title: "Notification string" description:
  "Create a notification string with a timestamp." expression: "'New message
  received at ' + string(document.create_time)" The exact variables and
  functions that may be referenced within an expression are determined by the
  service that evaluates it. See the service documentation for additional
  information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class IamGetEffectivePoliciesRequest(_messages.Message):
  r"""A IamGetEffectivePoliciesRequest object.

  Fields:
    attachmentPoint: Required. The Cloud resource at which the effective
      policies are to be retrieved.
    filter: Filtering currently only supports the kind of policies to return,
      and must be in the format "kind:[policyKind1],[policyKind2]". An empty
      value returns all policy kinds. Example Value: "" (empty),
      "kind:denyPolicies", "kind:denyPolicies,grantPolicies".
  """

  attachmentPoint = _messages.StringField(1, required=True)
  filter = _messages.StringField(2)


class IamListApplicablePoliciesRequest(_messages.Message):
  r"""A IamListApplicablePoliciesRequest object.

  Fields:
    attachmentPoint: Required. The Cloud resource at which the applicable
      policies are to be retrieved. Format: `{attachment-point}` Use the URL-
      encoded full resource name, which means that the forward-slash
      character, `/`, must be written as `%2F`. For example,
      `cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project`.
    filter: Filtering currently only supports the kind of policies to return,
      and must be in the format "kind:[policyKind1] OR kind:[policyKind2]".
      New policy kinds may be added in the future without notice. Example
      value: "kind:denyPolicies"
    pageSize: Limit on the number of policies to include in the response.
      Further policies can subsequently be obtained by including the
      ListApplicablePoliciesResponse.next_page_token in a subsequent request.
      The minimum is 25, and the maximum is 100.
    pageToken: If present, then retrieve the batch of results following the
      results from the preceding call to this method. `page_token` must be the
      value of `next_page_token`
      ListApplicablePoliciesResponse.next_page_token from the previous
      response. The values of other method parameters should be identical to
      those in the previous call.
  """

  attachmentPoint = _messages.StringField(1, required=True)
  filter = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class IamPoliciesCreatePolicyRequest(_messages.Message):
  r"""A IamPoliciesCreatePolicyRequest object.

  Fields:
    googleIamV2Policy: A GoogleIamV2Policy resource to be passed as the
      request body.
    parent: Required. The resource that the policy is attached to, along with
      the kind of policy to create. Format:
      `policies/{attachment_point}/denypolicies` The attachment point is
      identified by its URL-encoded full resource name, which means that the
      forward-slash character, `/`, must be written as `%2F`. For example,
      `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-
      project/denypolicies`. For organizations and folders, use the numeric ID
      in the full resource name. For projects, you can use the alphanumeric or
      the numeric ID.
    policyId: The ID to use for this policy, which will become the final
      component of the policy's resource name. The ID must contain 3 to 63
      characters. It can contain lowercase letters and numbers, as well as
      dashes (`-`) and periods (`.`). The first character must be a lowercase
      letter.
  """

  googleIamV2Policy = _messages.MessageField('GoogleIamV2Policy', 1)
  parent = _messages.StringField(2, required=True)
  policyId = _messages.StringField(3)


class IamPoliciesDeleteRequest(_messages.Message):
  r"""A IamPoliciesDeleteRequest object.

  Fields:
    etag: Optional. The expected `etag` of the policy to delete. If the value
      does not match the value that is stored in IAM, the request fails with a
      `409` error code and `ABORTED` status. If you omit this field, the
      policy is deleted regardless of its current `etag`.
    name: Required. The resource name of the policy to delete. Format:
      `policies/{attachment_point}/denypolicies/{policy_id}` Use the URL-
      encoded full resource name, which means that the forward-slash
      character, `/`, must be written as `%2F`. For example,
      `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-
      project/denypolicies/my-policy`. For organizations and folders, use the
      numeric ID in the full resource name. For projects, you can use the
      alphanumeric or the numeric ID.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class IamPoliciesGetRequest(_messages.Message):
  r"""A IamPoliciesGetRequest object.

  Fields:
    name: Required. The resource name of the policy to retrieve. Format:
      `policies/{attachment_point}/denypolicies/{policy_id}` Use the URL-
      encoded full resource name, which means that the forward-slash
      character, `/`, must be written as `%2F`. For example,
      `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-
      project/denypolicies/my-policy`. For organizations and folders, use the
      numeric ID in the full resource name. For projects, you can use the
      alphanumeric or the numeric ID.
  """

  name = _messages.StringField(1, required=True)


class IamPoliciesListPoliciesRequest(_messages.Message):
  r"""A IamPoliciesListPoliciesRequest object.

  Fields:
    pageSize: The maximum number of policies to return. IAM ignores this value
      and uses the value 1000.
    pageToken: A page token received in a ListPoliciesResponse. Provide this
      token to retrieve the next page.
    parent: Required. The resource that the policy is attached to, along with
      the kind of policy to list. Format:
      `policies/{attachment_point}/denypolicies` The attachment point is
      identified by its URL-encoded full resource name, which means that the
      forward-slash character, `/`, must be written as `%2F`. For example,
      `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-
      project/denypolicies`. For organizations and folders, use the numeric ID
      in the full resource name. For projects, you can use the alphanumeric or
      the numeric ID.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class IamPoliciesOperationsGetRequest(_messages.Message):
  r"""A IamPoliciesOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
