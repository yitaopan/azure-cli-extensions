# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "data-transfer connection list",
    is_preview=True,
)
class List(AAZCommand):
    """List all the connections.

    :example: Gets connections in a resource group
        az data-transfer connection list --resource-group testRG
    """

    _aaz_info = {
        "version": "2025-05-21",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azuredatatransfer/connections", "2025-05-21"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConnectionsListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ConnectionsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureDataTransfer/connections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2025-05-21",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZIdentityObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType(
                nullable=True,
            )

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.approver = AAZStrType(
                flags={"read_only": True},
            )
            properties.date_submitted = AAZStrType(
                serialized_name="dateSubmitted",
                flags={"read_only": True},
            )
            properties.direction = AAZStrType()
            properties.flow_types = AAZListType(
                serialized_name="flowTypes",
            )
            properties.force_disabled_status = AAZListType(
                serialized_name="forceDisabledStatus",
                flags={"read_only": True},
            )
            properties.justification = AAZStrType()
            properties.link_status = AAZStrType(
                serialized_name="linkStatus",
                flags={"read_only": True},
            )
            properties.linked_connection_id = AAZStrType(
                serialized_name="linkedConnectionId",
                flags={"read_only": True},
            )
            properties.pin = AAZStrType()
            properties.pipeline = AAZStrType(
                flags={"required": True},
            )
            properties.policies = AAZListType()
            properties.primary_contact = AAZStrType(
                serialized_name="primaryContact",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.remote_subscription_id = AAZStrType(
                serialized_name="remoteSubscriptionId",
            )
            properties.requirement_id = AAZStrType(
                serialized_name="requirementId",
            )
            properties.schema_uris = AAZListType(
                serialized_name="schemaUris",
            )
            properties.schemas = AAZListType()
            properties.secondary_contacts = AAZListType(
                serialized_name="secondaryContacts",
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.status_reason = AAZStrType(
                serialized_name="statusReason",
                flags={"read_only": True},
            )

            flow_types = cls._schema_on_200.value.Element.properties.flow_types
            flow_types.Element = AAZStrType()

            force_disabled_status = cls._schema_on_200.value.Element.properties.force_disabled_status
            force_disabled_status.Element = AAZStrType()

            policies = cls._schema_on_200.value.Element.properties.policies
            policies.Element = AAZStrType()

            schema_uris = cls._schema_on_200.value.Element.properties.schema_uris
            schema_uris.Element = AAZStrType()

            schemas = cls._schema_on_200.value.Element.properties.schemas
            schemas.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.schemas.Element
            _element.connection_id = AAZStrType(
                serialized_name="connectionId",
            )
            _element.content = AAZStrType()
            _element.direction = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.schema_type = AAZStrType(
                serialized_name="schemaType",
            )
            _element.schema_uri = AAZStrType(
                serialized_name="schemaUri",
            )
            _element.status = AAZStrType()

            secondary_contacts = cls._schema_on_200.value.Element.properties.secondary_contacts
            secondary_contacts.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
