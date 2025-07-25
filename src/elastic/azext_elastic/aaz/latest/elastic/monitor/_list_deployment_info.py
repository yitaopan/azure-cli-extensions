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
    "elastic monitor list-deployment-info",
)
class ListDeploymentInfo(AAZCommand):
    """Fetch detailed information about Elastic cloud deployments corresponding to the Elastic monitor resource.

    :example: List deployment info
        az elastic monitor list-deployment-info --monitor-name name -g rg
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elastic/monitors/{}/listdeploymentinfo", "2024-06-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Monitor resource name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DeploymentInfoList(ctx=self.ctx)()
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

    class DeploymentInfoList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}/listDeploymentInfo",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
            _schema_on_200.deployment_url = AAZStrType(
                serialized_name="deploymentUrl",
                flags={"read_only": True},
            )
            _schema_on_200.disk_capacity = AAZStrType(
                serialized_name="diskCapacity",
                flags={"read_only": True},
            )
            _schema_on_200.elasticsearch_end_point = AAZStrType(
                serialized_name="elasticsearchEndPoint",
                flags={"read_only": True},
            )
            _schema_on_200.marketplace_saas_info = AAZObjectType(
                serialized_name="marketplaceSaasInfo",
                flags={"read_only": True},
            )
            _schema_on_200.memory_capacity = AAZStrType(
                serialized_name="memoryCapacity",
                flags={"read_only": True},
            )
            _schema_on_200.status = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.version = AAZStrType(
                flags={"read_only": True},
            )

            marketplace_saas_info = cls._schema_on_200.marketplace_saas_info
            marketplace_saas_info.billed_azure_subscription_id = AAZStrType(
                serialized_name="billedAzureSubscriptionId",
            )
            marketplace_saas_info.marketplace_name = AAZStrType(
                serialized_name="marketplaceName",
            )
            marketplace_saas_info.marketplace_resource_id = AAZStrType(
                serialized_name="marketplaceResourceId",
            )
            marketplace_saas_info.marketplace_status = AAZStrType(
                serialized_name="marketplaceStatus",
            )
            marketplace_saas_info.marketplace_subscription = AAZObjectType(
                serialized_name="marketplaceSubscription",
            )
            marketplace_saas_info.subscribed = AAZBoolType()

            marketplace_subscription = cls._schema_on_200.marketplace_saas_info.marketplace_subscription
            marketplace_subscription.id = AAZStrType()
            marketplace_subscription.offer_id = AAZStrType(
                serialized_name="offerId",
            )
            marketplace_subscription.publisher_id = AAZStrType(
                serialized_name="publisherId",
            )

            return cls._schema_on_200


class _ListDeploymentInfoHelper:
    """Helper class for ListDeploymentInfo"""


__all__ = ["ListDeploymentInfo"]
