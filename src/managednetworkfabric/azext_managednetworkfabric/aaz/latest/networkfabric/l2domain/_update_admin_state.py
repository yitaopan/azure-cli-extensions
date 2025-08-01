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
    "networkfabric l2domain update-admin-state",
)
class UpdateAdminState(AAZCommand):
    """Enables isolation domain across the fabric or on specified racks.

    :example: Update admin state of L2 Isolation Domain
        az networkfabric l2domain update-admin-state --resource-group "example-rg" --resource-name "example-l2domain" --state "Enable"
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/l2isolationdomains/{}/updateadministrativestate", "2024-06-15-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the L2 Isolation Domain.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z]{1}[a-zA-Z0-9-_]{2,127}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.resource_ids = AAZListArg(
            options=["--resource-ids"],
            arg_group="Body",
            help="Network Fabrics or Network Rack resource Id.",
        )
        _args_schema.state = AAZStrArg(
            options=["--state"],
            arg_group="Body",
            help="Administrative state.",
            enum={"Disable": "Disable", "Enable": "Enable", "UnderMaintenance": "UnderMaintenance"},
        )

        resource_ids = cls._args_schema.resource_ids
        resource_ids.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.L2IsolationDomainsUpdateAdministrativeState(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class L2IsolationDomainsUpdateAdministrativeState(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l2IsolationDomains/{l2IsolationDomainName}/updateAdministrativeState",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "l2IsolationDomainName", self.ctx.args.resource_name,
                    required=True,
                ),
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
                    "api-version", "2024-06-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("resourceIds", AAZListType, ".resource_ids")
            _builder.set_prop("state", AAZStrType, ".state")

            resource_ids = _builder.get(".resourceIds")
            if resource_ids is not None:
                resource_ids.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _schema_on_200.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            _schema_on_200.error = AAZObjectType()
            _UpdateAdminStateHelper._build_schema_error_detail_read(_schema_on_200.error)
            _schema_on_200.failed_devices = AAZListType(
                serialized_name="failedDevices",
            )
            _schema_on_200.successful_devices = AAZListType(
                serialized_name="successfulDevices",
            )

            failed_devices = cls._schema_on_200.failed_devices
            failed_devices.Element = AAZStrType()

            successful_devices = cls._schema_on_200.successful_devices
            successful_devices.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateAdminStateHelper:
    """Helper class for UpdateAdminState"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.info = AAZDictType(
            flags={"read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        info = _schema_error_detail_read.additional_info.Element.info
        info.Element = AAZAnyType()

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target


__all__ = ["UpdateAdminState"]
