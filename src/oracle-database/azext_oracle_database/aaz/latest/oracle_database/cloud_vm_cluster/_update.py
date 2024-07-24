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
    "oracle-database cloud-vm-cluster update",
)
class Update(AAZCommand):
    """Update a CloudVmCluster

    :example: Update VM Cluster
        az oracle-database cloud-vm-cluster update --cloudvmclustername <vmclustername> --resource-group <Resource group> --tags {tagv1:tagk1}
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/oracle.database/cloudvmclusters/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.cloudvmclustername = AAZStrArg(
            options=["-n", "--name", "--cloudvmclustername"],
            help="CloudVmCluster name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern=".*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.compute_nodes = AAZListArg(
            options=["--compute-nodes"],
            arg_group="Properties",
            help="The list of compute servers to be added to the cloud VM cluster.",
            nullable=True,
        )
        _args_schema.cpu_core_count = AAZIntArg(
            options=["--cpu-core-count"],
            arg_group="Properties",
            help="The number of CPU cores enabled on the cloud VM cluster.",
        )
        _args_schema.data_collection_options = AAZObjectArg(
            options=["--collection-options", "--data-collection-options"],
            arg_group="Properties",
            help="Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.",
            nullable=True,
        )
        _args_schema.data_storage_size_in_tbs = AAZFloatArg(
            options=["--storage-tbs", "--data-storage-size-in-tbs"],
            arg_group="Properties",
            help="The data disk group size to be allocated in TBs.",
            nullable=True,
        )
        _args_schema.db_node_storage_size_in_gbs = AAZIntArg(
            options=["--node-storage-gbs", "--db-node-storage-size-in-gbs"],
            arg_group="Properties",
            help="The local node storage to be allocated in GBs.",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display Name",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        _args_schema.license_model = AAZStrArg(
            options=["--license-model"],
            arg_group="Properties",
            help="The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED. ",
            nullable=True,
            enum={"BringYourOwnLicense": "BringYourOwnLicense", "LicenseIncluded": "LicenseIncluded"},
        )
        _args_schema.memory_size_in_gbs = AAZIntArg(
            options=["--memory-size-in-gbs"],
            arg_group="Properties",
            help="The memory to be allocated in GBs.",
            nullable=True,
        )
        _args_schema.ocpu_count = AAZFloatArg(
            options=["--ocpu-count"],
            arg_group="Properties",
            help="The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.",
            nullable=True,
        )
        _args_schema.ssh_public_keys = AAZListArg(
            options=["--ssh-public-keys"],
            arg_group="Properties",
            help="The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.",
        )
        _args_schema.storage_size_in_gbs = AAZIntArg(
            options=["--storage-size-in-gbs"],
            arg_group="Properties",
            help="The data disk group size to be allocated in GBs per VM.",
            nullable=True,
        )

        compute_nodes = cls._args_schema.compute_nodes
        compute_nodes.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )

        data_collection_options = cls._args_schema.data_collection_options
        data_collection_options.is_diagnostics_events_enabled = AAZBoolArg(
            options=["is-diagnostics-events-enabled"],
            help="Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS.",
            nullable=True,
        )
        data_collection_options.is_health_monitoring_enabled = AAZBoolArg(
            options=["is-health-monitoring-enabled"],
            help="Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS.",
            nullable=True,
        )
        data_collection_options.is_incident_logs_enabled = AAZBoolArg(
            options=["is-incident-logs-enabled"],
            help="Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS.",
            nullable=True,
        )

        ssh_public_keys = cls._args_schema.ssh_public_keys
        ssh_public_keys.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CloudVmClustersGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CloudVmClustersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CloudVmClustersGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudVmClusters/{cloudvmclustername}",
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
                    "cloudvmclustername", self.ctx.args.cloudvmclustername,
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
                    "api-version", "2023-09-01",
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
            _UpdateHelper._build_schema_cloud_vm_cluster_read(cls._schema_on_200)

            return cls._schema_on_200

    class CloudVmClustersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudVmClusters/{cloudvmclustername}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "cloudvmclustername", self.ctx.args.cloudvmclustername,
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
                    "api-version", "2023-09-01",
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
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_cloud_vm_cluster_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("computeNodes", AAZListType, ".compute_nodes")
                properties.set_prop("cpuCoreCount", AAZIntType, ".cpu_core_count", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("dataCollectionOptions", AAZObjectType, ".data_collection_options")
                properties.set_prop("dataStorageSizeInTbs", AAZFloatType, ".data_storage_size_in_tbs")
                properties.set_prop("dbNodeStorageSizeInGbs", AAZIntType, ".db_node_storage_size_in_gbs")
                properties.set_prop("displayName", AAZStrType, ".display_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("licenseModel", AAZStrType, ".license_model")
                properties.set_prop("memorySizeInGbs", AAZIntType, ".memory_size_in_gbs")
                properties.set_prop("ocpuCount", AAZFloatType, ".ocpu_count")
                properties.set_prop("sshPublicKeys", AAZListType, ".ssh_public_keys", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("storageSizeInGbs", AAZIntType, ".storage_size_in_gbs")

            compute_nodes = _builder.get(".properties.computeNodes")
            if compute_nodes is not None:
                compute_nodes.set_elements(AAZStrType, ".")

            data_collection_options = _builder.get(".properties.dataCollectionOptions")
            if data_collection_options is not None:
                data_collection_options.set_prop("isDiagnosticsEventsEnabled", AAZBoolType, ".is_diagnostics_events_enabled")
                data_collection_options.set_prop("isHealthMonitoringEnabled", AAZBoolType, ".is_health_monitoring_enabled")
                data_collection_options.set_prop("isIncidentLogsEnabled", AAZBoolType, ".is_incident_logs_enabled")

            ssh_public_keys = _builder.get(".properties.sshPublicKeys")
            if ssh_public_keys is not None:
                ssh_public_keys.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_cloud_vm_cluster_read = None

    @classmethod
    def _build_schema_cloud_vm_cluster_read(cls, _schema):
        if cls._schema_cloud_vm_cluster_read is not None:
            _schema.id = cls._schema_cloud_vm_cluster_read.id
            _schema.location = cls._schema_cloud_vm_cluster_read.location
            _schema.name = cls._schema_cloud_vm_cluster_read.name
            _schema.properties = cls._schema_cloud_vm_cluster_read.properties
            _schema.system_data = cls._schema_cloud_vm_cluster_read.system_data
            _schema.tags = cls._schema_cloud_vm_cluster_read.tags
            _schema.type = cls._schema_cloud_vm_cluster_read.type
            return

        cls._schema_cloud_vm_cluster_read = _schema_cloud_vm_cluster_read = AAZObjectType()

        cloud_vm_cluster_read = _schema_cloud_vm_cluster_read
        cloud_vm_cluster_read.id = AAZStrType(
            flags={"read_only": True},
        )
        cloud_vm_cluster_read.location = AAZStrType(
            flags={"required": True},
        )
        cloud_vm_cluster_read.name = AAZStrType(
            flags={"read_only": True},
        )
        cloud_vm_cluster_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        cloud_vm_cluster_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cloud_vm_cluster_read.tags = AAZDictType()
        cloud_vm_cluster_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_cloud_vm_cluster_read.properties
        properties.backup_subnet_cidr = AAZStrType(
            serialized_name="backupSubnetCidr",
        )
        properties.cloud_exadata_infrastructure_id = AAZStrType(
            serialized_name="cloudExadataInfrastructureId",
            flags={"required": True},
        )
        properties.cluster_name = AAZStrType(
            serialized_name="clusterName",
        )
        properties.compartment_id = AAZStrType(
            serialized_name="compartmentId",
        )
        properties.cpu_core_count = AAZIntType(
            serialized_name="cpuCoreCount",
            flags={"required": True},
        )
        properties.data_collection_options = AAZObjectType(
            serialized_name="dataCollectionOptions",
        )
        properties.data_storage_percentage = AAZIntType(
            serialized_name="dataStoragePercentage",
        )
        properties.data_storage_size_in_tbs = AAZFloatType(
            serialized_name="dataStorageSizeInTbs",
        )
        properties.db_node_storage_size_in_gbs = AAZIntType(
            serialized_name="dbNodeStorageSizeInGbs",
        )
        properties.db_servers = AAZListType(
            serialized_name="dbServers",
        )
        properties.disk_redundancy = AAZStrType(
            serialized_name="diskRedundancy",
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
            flags={"required": True},
        )
        properties.domain = AAZStrType()
        properties.gi_version = AAZStrType(
            serialized_name="giVersion",
            flags={"required": True},
        )
        properties.hostname = AAZStrType(
            flags={"required": True},
        )
        properties.iorm_config_cache = AAZObjectType(
            serialized_name="iormConfigCache",
        )
        properties.is_local_backup_enabled = AAZBoolType(
            serialized_name="isLocalBackupEnabled",
        )
        properties.is_sparse_diskgroup_enabled = AAZBoolType(
            serialized_name="isSparseDiskgroupEnabled",
        )
        properties.last_update_history_entry_id = AAZStrType(
            serialized_name="lastUpdateHistoryEntryId",
        )
        properties.license_model = AAZStrType(
            serialized_name="licenseModel",
        )
        properties.lifecycle_details = AAZStrType(
            serialized_name="lifecycleDetails",
            flags={"read_only": True},
        )
        properties.lifecycle_state = AAZStrType(
            serialized_name="lifecycleState",
        )
        properties.listener_port = AAZIntType(
            serialized_name="listenerPort",
            flags={"read_only": True},
        )
        properties.memory_size_in_gbs = AAZIntType(
            serialized_name="memorySizeInGbs",
        )
        properties.node_count = AAZIntType(
            serialized_name="nodeCount",
            flags={"read_only": True},
        )
        properties.nsg_cidrs = AAZListType(
            serialized_name="nsgCidrs",
        )
        properties.nsg_url = AAZStrType(
            serialized_name="nsgUrl",
            flags={"read_only": True},
        )
        properties.oci_url = AAZStrType(
            serialized_name="ociUrl",
            flags={"read_only": True},
        )
        properties.ocid = AAZStrType()
        properties.ocpu_count = AAZFloatType(
            serialized_name="ocpuCount",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.scan_dns_name = AAZStrType(
            serialized_name="scanDnsName",
            flags={"read_only": True},
        )
        properties.scan_dns_record_id = AAZStrType(
            serialized_name="scanDnsRecordId",
        )
        properties.scan_ip_ids = AAZListType(
            serialized_name="scanIpIds",
            flags={"read_only": True},
        )
        properties.scan_listener_port_tcp = AAZIntType(
            serialized_name="scanListenerPortTcp",
        )
        properties.scan_listener_port_tcp_ssl = AAZIntType(
            serialized_name="scanListenerPortTcpSsl",
        )
        properties.shape = AAZStrType(
            flags={"read_only": True},
        )
        properties.ssh_public_keys = AAZListType(
            serialized_name="sshPublicKeys",
            flags={"required": True},
        )
        properties.storage_size_in_gbs = AAZIntType(
            serialized_name="storageSizeInGbs",
        )
        properties.subnet_id = AAZStrType(
            serialized_name="subnetId",
            flags={"required": True},
        )
        properties.subnet_ocid = AAZStrType(
            serialized_name="subnetOcid",
        )
        properties.system_version = AAZStrType(
            serialized_name="systemVersion",
        )
        properties.time_created = AAZStrType(
            serialized_name="timeCreated",
            flags={"read_only": True},
        )
        properties.time_zone = AAZStrType(
            serialized_name="timeZone",
        )
        properties.vip_ids = AAZListType(
            serialized_name="vipIds",
            flags={"read_only": True},
        )
        properties.vnet_id = AAZStrType(
            serialized_name="vnetId",
            flags={"required": True},
        )
        properties.zone_id = AAZStrType(
            serialized_name="zoneId",
        )

        data_collection_options = _schema_cloud_vm_cluster_read.properties.data_collection_options
        data_collection_options.is_diagnostics_events_enabled = AAZBoolType(
            serialized_name="isDiagnosticsEventsEnabled",
        )
        data_collection_options.is_health_monitoring_enabled = AAZBoolType(
            serialized_name="isHealthMonitoringEnabled",
        )
        data_collection_options.is_incident_logs_enabled = AAZBoolType(
            serialized_name="isIncidentLogsEnabled",
        )

        db_servers = _schema_cloud_vm_cluster_read.properties.db_servers
        db_servers.Element = AAZStrType()

        iorm_config_cache = _schema_cloud_vm_cluster_read.properties.iorm_config_cache
        iorm_config_cache.db_plans = AAZListType(
            serialized_name="dbPlans",
        )
        iorm_config_cache.lifecycle_details = AAZStrType(
            serialized_name="lifecycleDetails",
        )
        iorm_config_cache.lifecycle_state = AAZStrType(
            serialized_name="lifecycleState",
        )
        iorm_config_cache.objective = AAZStrType()

        db_plans = _schema_cloud_vm_cluster_read.properties.iorm_config_cache.db_plans
        db_plans.Element = AAZObjectType()

        _element = _schema_cloud_vm_cluster_read.properties.iorm_config_cache.db_plans.Element
        _element.db_name = AAZStrType(
            serialized_name="dbName",
        )
        _element.flash_cache_limit = AAZStrType(
            serialized_name="flashCacheLimit",
        )
        _element.share = AAZIntType()

        nsg_cidrs = _schema_cloud_vm_cluster_read.properties.nsg_cidrs
        nsg_cidrs.Element = AAZObjectType()

        _element = _schema_cloud_vm_cluster_read.properties.nsg_cidrs.Element
        _element.destination_port_range = AAZObjectType(
            serialized_name="destinationPortRange",
        )
        _element.source = AAZStrType(
            flags={"required": True},
        )

        destination_port_range = _schema_cloud_vm_cluster_read.properties.nsg_cidrs.Element.destination_port_range
        destination_port_range.max = AAZIntType(
            flags={"required": True},
        )
        destination_port_range.min = AAZIntType(
            flags={"required": True},
        )

        scan_ip_ids = _schema_cloud_vm_cluster_read.properties.scan_ip_ids
        scan_ip_ids.Element = AAZStrType()

        ssh_public_keys = _schema_cloud_vm_cluster_read.properties.ssh_public_keys
        ssh_public_keys.Element = AAZStrType()

        vip_ids = _schema_cloud_vm_cluster_read.properties.vip_ids
        vip_ids.Element = AAZStrType()

        system_data = _schema_cloud_vm_cluster_read.system_data
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

        tags = _schema_cloud_vm_cluster_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_cloud_vm_cluster_read.id
        _schema.location = cls._schema_cloud_vm_cluster_read.location
        _schema.name = cls._schema_cloud_vm_cluster_read.name
        _schema.properties = cls._schema_cloud_vm_cluster_read.properties
        _schema.system_data = cls._schema_cloud_vm_cluster_read.system_data
        _schema.tags = cls._schema_cloud_vm_cluster_read.tags
        _schema.type = cls._schema_cloud_vm_cluster_read.type


__all__ = ["Update"]