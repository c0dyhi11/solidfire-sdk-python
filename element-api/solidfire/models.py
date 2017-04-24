#!/usr/bin/python
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.

from __future__ import unicode_literals
from __future__ import absolute_import
from solidfire.common import model as data_model
from uuid import UUID
from solidfire.custom.models import CHAPSecret as UserDefinedCHAPSecret
from solidfire.custom.models import Frequency as UserDefinedFrequency

class Frequency(UserDefinedFrequency):
    def __init__(self, **kwargs):
        self = UserDefinedFrequency()
        data_model.DataObject.__init__(self, **kwargs)

class CHAPSecret(UserDefinedCHAPSecret):
    def __init__(self, **kwargs):
        self = UserDefinedCHAPSecret()
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterAdminRequest(data_model.DataObject):
    """RemoveClusterAdminRequest  
    You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account.

    :param cluster_admin_id: [required] ClusterAdminID for the cluster admin to remove. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="[&#x27;ClusterAdminID for the cluster admin to remove.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesResult(data_model.DataObject):
    """TestDrivesResult  

    :param details: [required]  
    :type details: str

    :param duration: [required]  
    :type duration: str

    :param result: [required]  
    :type result: str

    """
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeHost(data_model.DataObject):
    """VirtualVolumeHost  

    :param virtual_volume_host_id: [required]  
    :type virtual_volume_host_id: UUID

    :param cluster_id: [required]  
    :type cluster_id: UUID

    :param visible_protocol_endpoint_ids: [required]  
    :type visible_protocol_endpoint_ids: UUID

    :param bindings: [required]  
    :type bindings: int

    :param initiator_names: [required]  
    :type initiator_names: str

    :param host_address: [required]  
    :type host_address: str

    """
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_id = data_model.property(
        "clusterID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    visible_protocol_endpoint_ids = data_model.property(
        "visibleProtocolEndpointIDs", UUID,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_names = data_model.property(
        "initiatorNames", str,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    host_address = data_model.property(
        "hostAddress", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsResult(data_model.DataObject):
    """ListVirtualVolumeHostsResult  

    :param hosts: [required] List of known ESX hosts. 
    :type hosts: VirtualVolumeHost

    """
    hosts = data_model.property(
        "hosts", VirtualVolumeHost,
        array=True, optional=False,
        documentation="[&#x27;List of known ESX hosts.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVolumesToVolumeAccessGroupRequest(data_model.DataObject):
    """AddVolumesToVolumeAccessGroupRequest  
    AddVolumesToVolumeAccessGroup enables you to add
    volumes to a specified volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to which volumes are added. 
    :type volume_access_group_id: int

    :param volumes: [required] The list of volumes to add to the volume access group. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group to which volumes are added.&#x27;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;The list of volumes to add to the volume access&#x27;, &#x27;group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotRequest(data_model.DataObject):
    """CreateGroupSnapshotRequest  
    CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot.
    Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volumes: [required] Unique ID of the volume image from which to copy. 
    :type volumes: int

    :param name:  Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param retention:  Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. 
    :type retention: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;Unique ID of the volume image from which to copy.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Replicates the snapshot created to remote storage.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: The snapshot is replicated to remote storage.&#x27;, &#x27;false: Default. The snapshot is not replicated.&#x27;]",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterConfig(data_model.DataObject):
    """ClusterConfig  
    Cluster Config object returns information the node uses to communicate with the cluster.

    :param cipi:  Network interface used for cluster communication. 
    :type cipi: str

    :param cluster:  Unique cluster name. 
    :type cluster: str

    :param ensemble:  Nodes that are participating in the cluster. 
    :type ensemble: str

    :param mipi:  Network interface used for node management. 
    :type mipi: str

    :param name:  Unique cluster name. 
    :type name: str

    :param node_id:   
    :type node_id: int

    :param pending_node_id:   
    :type pending_node_id: int

    :param role:  Identifies the role of the node 
    :type role: str

    :param sipi:  Network interface used for storage. 
    :type sipi: str

    :param state:   
    :type state: str

    :param encryption_capable:   
    :type encryption_capable: bool

    :param has_local_admin:   
    :type has_local_admin: bool

    :param version:   
    :type version: str

    """
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=True,
        documentation="[&#x27;Network interface used for cluster communication.&#x27;]",
        dictionaryType=None
    )
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=True,
        documentation="[&#x27;Unique cluster name.&#x27;]",
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=True,
        documentation="[&#x27;Nodes that are participating in the cluster.&#x27;]",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=True,
        documentation="[&#x27;Network interface used for node management.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Unique cluster name.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    role = data_model.property(
        "role", str,
        array=False, optional=True,
        documentation="[&#x27;Identifies the role of the node&#x27;]",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=True,
        documentation="[&#x27;Network interface used for storage.&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    encryption_capable = data_model.property(
        "encryptionCapable", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    has_local_admin = data_model.property(
        "hasLocalAdmin", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PhysicalAdapter(data_model.DataObject):
    """PhysicalAdapter  

    :param address:   
    :type address: str

    :param mac_address:   
    :type mac_address: str

    :param mac_address_permanent:   
    :type mac_address_permanent: str

    :param mtu:   
    :type mtu: str

    :param netmask:   
    :type netmask: str

    :param network:   
    :type network: str

    :param up_and_running:   
    :type up_and_running: bool

    """
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkConfigParams(data_model.DataObject):
    """NetworkConfigParams  

    :param _default:   
    :type _default: bool

    :param bond_master:   
    :type bond_master: str

    :param virtual_network_tag:   
    :type virtual_network_tag: str

    :param address:   
    :type address: str

    :param auto:   
    :type auto: bool

    :param bond_downdelay:   
    :type bond_downdelay: str

    :param bond_fail_over_mac:   
    :type bond_fail_over_mac: str

    :param bond_primary_reselect:   
    :type bond_primary_reselect: str

    :param bond_lacp_rate:   
    :type bond_lacp_rate: str

    :param bond_miimon:   
    :type bond_miimon: str

    :param bond_mode:   
    :type bond_mode: str

    :param bond_slaves:   
    :type bond_slaves: str

    :param bond_updelay:   
    :type bond_updelay: str

    :param dns_nameservers:   
    :type dns_nameservers: str

    :param dns_search:   
    :type dns_search: str

    :param family:   
    :type family: str

    :param gateway:   
    :type gateway: str

    :param mac_address:   
    :type mac_address: str

    :param mac_address_permanent:   
    :type mac_address_permanent: str

    :param method:   
    :type method: str

    :param mtu:   
    :type mtu: str

    :param netmask:   
    :type netmask: str

    :param network:   
    :type network: str

    :param physical:   
    :type physical: PhysicalAdapter

    :param routes:   
    :type routes: dict

    :param status:   
    :type status: str

    :param symmetric_route_rules:   
    :type symmetric_route_rules: str

    :param up_and_running:   
    :type up_and_running: bool

    """
    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_master = data_model.property(
        "bond-master", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_downdelay = data_model.property(
        "bond-downdelay", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond-miimon", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond-updelay", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    routes = data_model.property(
        "routes", dict,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkParams(data_model.DataObject):
    """NetworkParams  

    :param bond10_g:   
    :type bond10_g: NetworkConfigParams

    :param bond1_g:   
    :type bond1_g: NetworkConfigParams

    :param eth0:   
    :type eth0: NetworkConfigParams

    :param eth1:   
    :type eth1: NetworkConfigParams

    :param eth2:   
    :type eth2: NetworkConfigParams

    :param eth3:   
    :type eth3: NetworkConfigParams

    :param lo:   
    :type lo: NetworkConfigParams

    """
    bond10_g = data_model.property(
        "Bond10G", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond1_g = data_model.property(
        "Bond1G", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth0 = data_model.property(
        "eth0", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth1 = data_model.property(
        "eth1", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth2 = data_model.property(
        "eth2", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth3 = data_model.property(
        "eth3", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lo = data_model.property(
        "lo", NetworkConfigParams,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Config(data_model.DataObject):
    """Config  

    :param cluster: [required]  
    :type cluster: ClusterConfig

    :param network: [required]  
    :type network: NetworkParams

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", NetworkParams,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetConfigResult(data_model.DataObject):
    """GetConfigResult  

    :param config: [required] The details of the cluster. Values returned in "config": cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object) 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="[&#x27;The details of the cluster. Values returned in &quot;config&quot;: cluster- Cluster information that identifies how the node communicates with the cluster it is associated with. (Object) network - Network information for bonding and Ethernet connections. (Object)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingResult(data_model.DataObject):
    """StartVolumePairingResult  

    :param volume_pairing_key: [required] A string of characters that is used by the "CompleteVolumePairing" API method. 
    :type volume_pairing_key: str

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="[&#x27;A string of characters that is used by the &quot;CompleteVolumePairing&quot; API method.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class UpdateBulkVolumeStatusRequest(data_model.DataObject):
    """UpdateBulkVolumeStatusRequest  
    You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the
    StartBulkVolumeRead or StartBulkVolumeWrite methods.

    :param key: [required] The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. 
    :type key: str

    :param status: [required] The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. 
    :type status: str

    :param percent_complete:  The completed progress of the bulk volume job as a percentage value. 
    :type percent_complete: str

    :param message:  The message returned indicating the status of the bulk volume job after the job is complete. 
    :type message: str

    :param attributes:  JSON attributes; updates what is on the bulk volume job. 
    :type attributes: dict

    """
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="[&#x27;The key assigned during initialization of a&#x27;, &#x27;StartBulkVolumeRead or StartBulkVolumeWrite session.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;The status of the given bulk volume job. The system sets the status. Possible values are: &#x27;, &#x27;running: Jobs that are still active.&#x27;, &#x27;complete: Jobs that are done.&#x27;, &#x27;failed: Jobs that failed.&#x27;]",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", str,
        array=False, optional=True,
        documentation="[&#x27;The completed progress of the bulk volume job as a&#x27;, &#x27;percentage value.&#x27;]",
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=True,
        documentation="[&#x27;The message returned indicating the status of the bulk volume job after the job is complete.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes; updates what is on the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountEfficiencyRequest(data_model.DataObject):
    """GetAccountEfficiencyRequest  
    GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information
    only for the account you specify as a parameter.

    :param account_id: [required] Specifies the volume account for which efficiency statistics are returned. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the volume account for which efficiency&#x27;, &#x27;statistics are returned.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Platform(data_model.DataObject):
    """Platform  

    :param node_type: [required] SolidFire's name for this platform. 
    :type node_type: str

    :param chassis_type: [required] Name of the chassis (example: "R620"). 
    :type chassis_type: str

    :param cpu_model: [required] The model of CPU used on this platform. 
    :type cpu_model: str

    :param node_memory_gb: [required] The amount of memory on this platform in GiB. 
    :type node_memory_gb: int

    :param platform_config_version:   
    :type platform_config_version: str

    """
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=False,
        documentation="[&quot;SolidFire&#x27;s name for this platform.&quot;]",
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the chassis (example: &quot;R620&quot;).&#x27;]",
        dictionaryType=None
    )
    cpu_model = data_model.property(
        "cpuModel", str,
        array=False, optional=False,
        documentation="[&#x27;The model of CPU used on this platform.&#x27;]",
        dictionaryType=None
    )
    node_memory_gb = data_model.property(
        "nodeMemoryGB", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of memory on this platform in GiB.&#x27;]",
        dictionaryType=None
    )
    platform_config_version = data_model.property(
        "platformConfigVersion", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualNetworkAddress(data_model.DataObject):
    """VirtualNetworkAddress  

    :param virtual_network_id: [required] SolidFire unique identifier for a virtual network. 
    :type virtual_network_id: int

    :param address: [required] Virtual Network Address. 
    :type address: str

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="[&#x27;SolidFire unique identifier for a virtual network.&#x27;]",
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="[&#x27;Virtual Network Address.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Node(data_model.DataObject):
    """Node  
    A node refers to an individual machine in a cluster.
    Each active node hosts a master service, which is responsible for managing the drives and other services on its node.
    After a node is made active, its drives will become available for addition to the cluster.

    :param node_id: [required] The unique identifier for this node. 
    :type node_id: int

    :param associated_master_service_id: [required] The master service responsible for controlling other services on this node. 
    :type associated_master_service_id: int

    :param associated_fservice_id: [required]  
    :type associated_fservice_id: int

    :param fibre_channel_target_port_group:   
    :type fibre_channel_target_port_group: str

    :param name: [required]  
    :type name: str

    :param platform_info: [required] Information about the platform this node is. 
    :type platform_info: Platform

    :param software_version: [required] The version of SolidFire software this node is currently running. 
    :type software_version: str

    :param cip: [required] IP address used for both intra- and inter-cluster communication. 
    :type cip: str

    :param cipi: [required] The machine's name for the "cip" interface. 
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the API and web site). 
    :type mip: str

    :param mipi: [required] The machine's name for the "mip" interface. 
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic. 
    :type sip: str

    :param sipi: [required] The machine's name for the "sip" interface. 
    :type sipi: str

    :param uuid: [required] UUID of node. 
    :type uuid: UUID

    :param virtual_networks: [required]  
    :type virtual_networks: VirtualNetworkAddress

    :param attributes: [required]  
    :type attributes: dict

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique identifier for this node.&#x27;]",
        dictionaryType=None
    )
    associated_master_service_id = data_model.property(
        "associatedMasterServiceID", int,
        array=False, optional=False,
        documentation="[&#x27;The master service responsible for controlling other services on this node.&#x27;]",
        dictionaryType=None
    )
    associated_fservice_id = data_model.property(
        "associatedFServiceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    fibre_channel_target_port_group = data_model.property(
        "fibreChannelTargetPortGroup", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="[&#x27;Information about the platform this node is.&#x27;]",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="[&#x27;The version of SolidFire software this node is currently running.&#x27;]",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for both intra- and inter-cluster communication.&#x27;]",
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;cip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;mip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for iSCSI traffic.&#x27;]",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;sip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[&#x27;UUID of node.&#x27;]",
        dictionaryType=None
    )
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetworkAddress,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingNode(data_model.DataObject):
    """PendingNode  
    A "pending node" is one that has not yet joined the cluster.
    It can be added to a cluster using the AddNode method.

    :param pending_node_id: [required]  
    :type pending_node_id: int

    :param assigned_node_id: [required]  
    :type assigned_node_id: int

    :param name: [required] The host name for this node. 
    :type name: str

    :param compatible: [required]  
    :type compatible: bool

    :param platform_info: [required] Information about the platform this node is. 
    :type platform_info: Platform

    :param cip: [required] IP address used for both intra- and inter-cluster communication. 
    :type cip: str

    :param cipi: [required] The machine's name for the "cip" interface. 
    :type cipi: str

    :param mip: [required] IP address used for cluster management (hosting the API and web site). 
    :type mip: str

    :param mipi: [required] The machine's name for the "mip" interface. 
    :type mipi: str

    :param sip: [required] IP address used for iSCSI traffic. 
    :type sip: str

    :param sipi: [required] The machine's name for the "sip" interface. 
    :type sipi: str

    :param software_version: [required] The version of SolidFire software this node is currently running. 
    :type software_version: str

    :param uuid: [required] UUID of node. 
    :type uuid: UUID

    """
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The host name for this node.&#x27;]",
        dictionaryType=None
    )
    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="[&#x27;Information about the platform this node is.&#x27;]",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for both intra- and inter-cluster communication.&#x27;]",
        dictionaryType=None
    )
    cipi = data_model.property(
        "cipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;cip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for cluster management (hosting the API and web site).&#x27;]",
        dictionaryType=None
    )
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;mip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="[&#x27;IP address used for iSCSI traffic.&#x27;]",
        dictionaryType=None
    )
    sipi = data_model.property(
        "sipi", str,
        array=False, optional=False,
        documentation="[&#x27;The machine\&#x27;s name for the &quot;sip&quot; interface.&#x27;]",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="[&#x27;The version of SolidFire software this node is currently running.&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[&#x27;UUID of node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingActiveNode(data_model.DataObject):
    """PendingActiveNode  

    :param active_node_key: [required]  
    :type active_node_key: str

    :param assigned_node_id: [required]  
    :type assigned_node_id: int

    :param async_handle: [required]  
    :type async_handle: int

    :param cip: [required]  
    :type cip: str

    :param mip: [required]  
    :type mip: str

    :param pending_node_id: [required]  
    :type pending_node_id: int

    :param platform_info: [required]  
    :type platform_info: Platform

    :param sip: [required]  
    :type sip: str

    :param software_version: [required]  
    :type software_version: str

    """
    active_node_key = data_model.property(
        "activeNodeKey", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAllNodesResult(data_model.DataObject):
    """ListAllNodesResult  

    :param nodes: [required]  
    :type nodes: Node

    :param pending_nodes: [required]  
    :type pending_nodes: PendingNode

    :param pending_active_nodes:  List of objects detailing information about all PendingActive nodes in the system. 
    :type pending_active_nodes: PendingActiveNode

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_active_nodes = data_model.property(
        "pendingActiveNodes", PendingActiveNode,
        array=True, optional=True,
        documentation="[&#x27;List of objects detailing information about all PendingActive nodes in the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ShutdownResult(data_model.DataObject):
    """ShutdownResult  

    :param failed: [required]  
    :type failed: int

    :param successful: [required]  
    :type successful: int

    """
    failed = data_model.property(
        "failed", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    successful = data_model.property(
        "successful", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAPIResult(data_model.DataObject):
    """GetAPIResult  

    :param supported_versions: [required]  
    :type supported_versions: float

    :param current_version: [required]  
    :type current_version: float

    """
    supported_versions = data_model.property(
        "supportedVersions", float,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    current_version = data_model.property(
        "currentVersion", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LunAssignment(data_model.DataObject):
    """LunAssignment  
    VolumeID and Lun assignment.

    :param volume_id: [required] The volume ID assigned to the Lun. 
    :type volume_id: int

    :param lun: [required] Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. 
    :type lun: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The volume ID assigned to the Lun.&#x27;]",
        dictionaryType=None
    )
    lun = data_model.property(
        "lun", int,
        array=False, optional=False,
        documentation="[&#x27;Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeAccessGroupLunAssignments(data_model.DataObject):
    """VolumeAccessGroupLunAssignments  
    VolumeAccessGroup ID and Lun to be assigned to all volumes within it.

    :param volume_access_group_id: [required] Unique volume access group ID for which the LUN assignments will be modified. 
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume IDs with assigned LUN values. 
    :type lun_assignments: LunAssignment

    :param deleted_lun_assignments: [required] The volume IDs with deleted LUN values. 
    :type deleted_lun_assignments: LunAssignment

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique volume access group ID for which the LUN assignments will be modified.&#x27;]",
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="[&#x27;The volume IDs with assigned LUN values.&#x27;]",
        dictionaryType=None
    )
    deleted_lun_assignments = data_model.property(
        "deletedLunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="[&#x27;The volume IDs with deleted LUN values.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsResult  

    :param volume_access_group_lun_assignments: [required] List of all physical Fibre Channel ports, or a port for a single node. 
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments

    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="[&#x27;List of all physical Fibre Channel ports, or a port for a single node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class MetadataHosts(data_model.DataObject):
    """MetadataHosts  
    The volume services on which the volume metadata resides.

    :param dead_secondaries: [required] Secondary metadata (slice) services that are in a dead state. 
    :type dead_secondaries: int

    :param live_secondaries: [required] Secondary metadata (slice) services that are currently in a "live" state. 
    :type live_secondaries: int

    :param primary: [required] The primary metadata (slice) services hosting the volume. 
    :type primary: int

    """
    dead_secondaries = data_model.property(
        "deadSecondaries", int,
        array=True, optional=False,
        documentation="[&#x27;Secondary metadata (slice) services that are in a dead state.&#x27;]",
        dictionaryType=None
    )
    live_secondaries = data_model.property(
        "liveSecondaries", int,
        array=True, optional=False,
        documentation="[&#x27;Secondary metadata (slice) services that are currently in a &quot;live&quot; state.&#x27;]",
        dictionaryType=None
    )
    primary = data_model.property(
        "primary", int,
        array=False, optional=False,
        documentation="[&#x27;The primary metadata (slice) services hosting the volume.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeStats(data_model.DataObject):
    """VolumeStats  
    Contains statistical data for an individual volume.

    :param account_id: [required] AccountID of the volume owner. 
    :type account_id: int

    :param actual_iops:  Current actual IOPS to the volume in the last 500 milliseconds. 
    :type actual_iops: int

    :param average_iopsize:  Average size in bytes of recent I/O to the volume in the last 500 milliseconds. 
    :type average_iopsize: int

    :param burst_iopscredit:  The total number of IOP credits available to the user. When users are not using up to the max IOPS, credits are accrued. 
    :type burst_iopscredit: int

    :param client_queue_depth:  The number of outstanding read and write operations to the cluster. 
    :type client_queue_depth: int

    :param latency_usec:  The observed latency time, in microseconds, to complete operations to a volume. A "0" (zero) value means there is no I/O to the volume. 
    :type latency_usec: int

    :param metadata_hosts:  The volume services on which the volume metadata resides. 
    :type metadata_hosts: MetadataHosts

    :param non_zero_blocks: [required] The number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_latency_usec:  The average time, in microseconds, to complete read operations. 
    :type read_latency_usec: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param throttle:  A floating value between 0 and 1 that represents how much the system is throttling clients below their max IOPS because of re-replication of data, transient errors and snapshots taken. 
    :type throttle: float

    :param timestamp: [required] The current time in UTC. 
    :type timestamp: str

    :param total_latency_usec:  The average time, in microseconds, to complete read and write operations to a volume. 
    :type total_latency_usec: int

    :param unaligned_reads: [required] For 512e volumes, the number of read operations that were not on a 4k sector boundary. High numbers of unaligned reads may indicate improper partition alignment. 
    :type unaligned_reads: int

    :param unaligned_writes: [required] For 512e volumes, the number of write operations that were not on a 4k sector boundary. High numbers of unaligned writes may indicate improper partition alignment. 
    :type unaligned_writes: int

    :param volume_access_groups: [required] List of volume access group(s) to which a volume beintegers. 
    :type volume_access_groups: int

    :param volume_id: [required] Volume ID of the volume. 
    :type volume_id: int

    :param volume_size: [required] Total provisioned capacity in bytes. 
    :type volume_size: int

    :param volume_utilization:  A floating value that describes how much the client is using the volume.  Values:  0 = Client is not using the volume 1 = Client is using their max >1 = Client is using their burst 
    :type volume_utilization: float

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_latency_usec:  The average time, in microseconds, to complete write operations. 
    :type write_latency_usec: int

    :param write_ops: [required] Total write operations occurring on the volume. 
    :type write_ops: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garbage collection operation has completed. 
    :type zero_blocks: int

    :param write_bytes_last_sample:  The total number of bytes written to the volume during the last sample period. 
    :type write_bytes_last_sample: int

    :param sample_period_msec:  The length of the sample period in milliseconds. 
    :type sample_period_msec: int

    :param read_bytes_last_sample:  The total number of bytes read from the volume during the last sample period. 
    :type read_bytes_last_sample: int

    :param read_ops_last_sample:  The total number of read operations durin gth elast sample period. 
    :type read_ops_last_sample: int

    :param write_ops_last_sample:  The total number of write operations during the last sample period. 
    :type write_ops_last_sample: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;AccountID of the volume owner.&#x27;]",
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Current actual IOPS to the volume in the last 500 milliseconds.&#x27;]",
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=True,
        documentation="[&#x27;Average size in bytes of recent I/O to the volume in the last 500 milliseconds.&#x27;]",
        dictionaryType=None
    )
    burst_iopscredit = data_model.property(
        "burstIOPSCredit", int,
        array=False, optional=True,
        documentation="[&#x27;The total number of IOP credits available to the user.&#x27;, &#x27;When users are not using up to the max IOPS, credits are accrued.&#x27;]",
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=True,
        documentation="[&#x27;The number of outstanding read and write operations to the cluster.&#x27;]",
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=True,
        documentation="[&#x27;The observed latency time, in microseconds, to complete operations to a volume.&#x27;, &#x27;A &quot;0&quot; (zero) value means there is no I/O to the volume.&#x27;]",
        dictionaryType=None
    )
    metadata_hosts = data_model.property(
        "metadataHosts", MetadataHosts,
        array=False, optional=True,
        documentation="[&#x27;The volume services on which the volume metadata resides.&#x27;]",
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;The number of 4KiB blocks with data after the last garbage collection operation has completed.&#x27;]",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total bytes read by clients.&#x27;]",
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=True,
        documentation="[&#x27;The average time, in microseconds, to complete read operations.&#x27;]",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="[&#x27;Total read operations.&#x27;]",
        dictionaryType=None
    )
    throttle = data_model.property(
        "throttle", float,
        array=False, optional=True,
        documentation="[&#x27;A floating value between 0 and 1 that represents how much the system is throttling clients&#x27;, &#x27;below their max IOPS because of re-replication of data, transient errors and snapshots taken.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;The current time in UTC.&#x27;]",
        dictionaryType=None
    )
    total_latency_usec = data_model.property(
        "totalLatencyUSec", int,
        array=False, optional=True,
        documentation="[&#x27;The average time, in microseconds, to complete read and write operations to a volume.&#x27;]",
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=False,
        documentation="[&#x27;For 512e volumes, the number of read operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned reads may indicate improper partition alignment.&#x27;]",
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=False,
        documentation="[&#x27;For 512e volumes, the number of write operations that were not on a 4k sector boundary.&#x27;, &#x27;High numbers of unaligned writes may indicate improper partition alignment.&#x27;]",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="[&#x27;List of volume access group(s) to which a volume beintegers.&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Volume ID of the volume.&#x27;]",
        dictionaryType=None
    )
    volume_size = data_model.property(
        "volumeSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total provisioned capacity in bytes.&#x27;]",
        dictionaryType=None
    )
    volume_utilization = data_model.property(
        "volumeUtilization", float,
        array=False, optional=True,
        documentation="[&#x27;A floating value that describes how much the client is using the volume.&#x27;, u&#x27;&#x27;, &#x27;Values:&#x27;, &#x27; 0 = Client is not using the volume&#x27;, &#x27;1 = Client is using their max&#x27;, &#x27;&gt;1 = Client is using their burst&#x27;]",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total bytes written by clients.&#x27;]",
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=True,
        documentation="[&#x27;The average time, in microseconds, to complete write operations.&#x27;]",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="[&#x27;Total write operations occurring on the volume.&#x27;]",
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;Total number of 4KiB blocks without data after the last round of garbage collection operation has completed.&#x27;]",
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=True,
        documentation="[&#x27;The total number of bytes written to the volume during the last sample period.&#x27;]",
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMSec", int,
        array=False, optional=True,
        documentation="[&#x27;The length of the sample period in milliseconds.&#x27;]",
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=True,
        documentation="[&#x27;The total number of bytes read from the volume during the last sample period.&#x27;]",
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=True,
        documentation="[&#x27;The total number of read operations durin gth elast sample period.&#x27;]",
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=True,
        documentation="[&#x27;The total number of write operations during the last sample period.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByAccountResult(data_model.DataObject):
    """ListVolumeStatsByAccountResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotRequest(data_model.DataObject):
    """ModifyGroupSnapshotRequest  
    ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.

    :param group_snapshot_id: [required] Specifies the ID of the group of snapshots. 
    :type group_snapshot_id: int

    :param expiration_time:  Sets the time when the snapshot should be removed. If unspecified, the current time is used. 
    :type expiration_time: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the ID of the group of snapshots.&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="[&#x27;Sets the time when the snapshot should be&#x27;, &#x27;removed. If unspecified, the current time is used.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Replicates the snapshot created to a remote cluster.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: The snapshot is replicated to remote storage.&#x27;, &#x27;false: Default. The snapshot is not replicated.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotRequest(data_model.DataObject):
    """DeleteSnapshotRequest  
    DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must
    rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot.

    :param snapshot_id: [required] The ID of the snapshot to be deleted. 
    :type snapshot_id: int

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the snapshot to be deleted.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ScheduleInfo(data_model.DataObject):
    """ScheduleInfo  

    :param snapshot_name:  The snapshot name to be used.  
    :type snapshot_name: str

    :param enable_remote_replication:  Indicates if the snapshot should be included in remote replication. 
    :type enable_remote_replication: bool

    :param volume_ids:  A list of volume IDs to be included in the group snapshot. 
    :type volume_ids: int

    :param retention:  The amount of time the snapshot will be retained in HH:mm:ss. 
    :type retention: str

    """
    snapshot_name = data_model.property(
        "snapshotName", str,
        array=False, optional=True,
        documentation="[&#x27;The snapshot name to be used. &#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates if the snapshot should be included in remote replication.&#x27;]",
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volume IDs to be included in the group snapshot.&#x27;]",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="[&#x27;The amount of time the snapshot will be retained in HH:mm:ss.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Schedule(data_model.DataObject):
    """Schedule  
    Schedule is an object containing information about each schedule created to autonomously make a snapshot of a volume. The return object includes information for all schedules. If scheduleID is used to identify a specific schedule then only information for that scheduleID is returned. Schedules information is returned with the API method, see ListSchedules on the SolidFire API guide page 245.

    :param last_run_time_started:  Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed 
    :type last_run_time_started: str

    :param has_error:  Indicates whether or not the schedule has errors. 
    :type has_error: bool

    :param schedule_info: [required] Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created. 
    :type schedule_info: ScheduleInfo

    :param run_next_interval:  Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false". 
    :type run_next_interval: bool

    :param name: [required] Unique name assigned to the schedule. 
    :type name: str

    :param last_run_status:  Indicates the status of the last scheduled snapshot. Valid values are: Success Failed 
    :type last_run_status: str

    :param schedule_id:  Unique ID of the schedule 
    :type schedule_id: int

    :param paused:  Indicates whether or not the schedule is paused. 
    :type paused: bool

    :param to_be_deleted:  Indicates if the schedule is marked for deletion. 
    :type to_be_deleted: bool

    :param frequency: [required] Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency. Valid types are: DayOfWeekFrequency DayOfMonthFrequency TimeIntervalFrequency 
    :type frequency: Frequency

    :param starting_date:  Indicates the date the first time the schedule began of will begin. Formatted in UTC time. 
    :type starting_date: str

    :param recurring:  Indicates whether or not the schedule is recurring. 
    :type recurring: bool

    """
    last_run_time_started = data_model.property(
        "lastRunTimeStarted", str,
        array=False, optional=True,
        documentation="[&#x27;Indicates the last time the schedule started n ISO 8601 date string.&#x27;, &#x27;Valid values are:&#x27;, &#x27;Success&#x27;, &#x27;Failed&#x27;]",
        dictionaryType=None
    )
    has_error = data_model.property(
        "hasError", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule has errors.&#x27;]",
        dictionaryType=None
    )
    schedule_info = data_model.property(
        "scheduleInfo", ScheduleInfo,
        array=False, optional=False,
        documentation="[&#x27;Includes the unique name given to the schedule, the retention period for the snapshot that was created, and the volume ID of the volume from which the snapshot was created.&#x27;]",
        dictionaryType=None
    )
    run_next_interval = data_model.property(
        "runNextInterval", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule will run the next time the scheduler is active. When set to &quot;true&quot;, the schedule will run the next time the scheduler is active and then reset back to &quot;false&quot;.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Unique name assigned to the schedule.&#x27;]",
        dictionaryType=None
    )
    last_run_status = data_model.property(
        "lastRunStatus", str,
        array=False, optional=True,
        documentation="[&#x27;Indicates the status of the last scheduled snapshot.&#x27;, &#x27;Valid values are:&#x27;, &#x27;Success&#x27;, &#x27;Failed&#x27;]",
        dictionaryType=None
    )
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=True,
        documentation="[&#x27;Unique ID of the schedule&#x27;]",
        dictionaryType=None
    )
    paused = data_model.property(
        "paused", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule is paused.&#x27;]",
        dictionaryType=None
    )
    to_be_deleted = data_model.property(
        "toBeDeleted", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates if the schedule is marked for deletion.&#x27;]",
        dictionaryType=None
    )
    frequency = data_model.property(
        "frequency", Frequency,
        array=False, optional=False,
        documentation="[&#x27;Indicates the frequency of the schedule occurrence. Set this to a type that inherits from Frequency.&#x27;, &#x27;Valid types are:&#x27;, &#x27;DayOfWeekFrequency&#x27;, &#x27;DayOfMonthFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )
    starting_date = data_model.property(
        "startingDate", str,
        array=False, optional=True,
        documentation="[&#x27;Indicates the date the first time the schedule began of will begin. Formatted in UTC time.&#x27;]",
        dictionaryType=None
    )
    recurring = data_model.property(
        "recurring", bool,
        array=False, optional=True,
        documentation="[&#x27;Indicates whether or not the schedule is recurring.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleResult(data_model.DataObject):
    """GetScheduleResult  

    :param schedule: [required] The schedule attributes. 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[&#x27;The schedule attributes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiator(data_model.DataObject):
    """ModifyInitiator  
    Object containing characteristics of each initiator to modify

    :param initiator_id: [required] (Required) The numeric ID of the initiator to modify. (Integer) 
    :type initiator_id: int

    :param alias:  (Optional) A new friendly name to assign to the initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="[&#x27;(Required) The numeric ID of the initiator to modify. (Integer)&#x27;]",
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="[&#x27;(Optional) A new friendly name to assign to the initiator. (String)&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="[&#x27;(Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer)&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsRequest(data_model.DataObject):
    """ModifyInitiatorsRequest  
    ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing
    initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with
    CreateInitiators.
    If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify
    any initiators (no partial completion is possible).

    :param initiators: [required] A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 
    :type initiators: ModifyInitiator

    """
    initiators = data_model.property(
        "initiators", ModifyInitiator,
        array=True, optional=False,
        documentation="[&#x27;A list of objects containing characteristics of each initiator to modify. Values are:&#x27;, &#x27;initiatorID: (Required) The ID of the initiator to modify. (Integer)&#x27;, &#x27;alias: (Optional) A new friendly name to assign to the initiator.&#x27;, &#x27;(String)&#x27;, &#x27;attributes: (Optional) A new set of JSON attributes to assign to the&#x27;, &#x27;initiator. (JSON Object)&#x27;, &#x27;volumeAccessGroupID: (Optional) The ID of the volume access&#x27;, &#x27;group into to which the initiator should be added. If the initiator was&#x27;, &#x27;previously in a different volume access group, it is removed from the&#x27;, &#x27;old volume access group. If this key is present but null, the initiator is&#x27;, &#x27;removed from its current volume access group, but not placed in any&#x27;, &#x27;new volume access group. (Integer)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesRequest(data_model.DataObject):
    """ListVolumesRequest  
    The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to
    return in the list by using the available parameters.

    :param start_volume_id:  Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. 
    :type start_volume_id: int

    :param limit:  Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. 
    :type limit: int

    :param volume_status:  Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted 
    :type volume_status: str

    :param accounts:  Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. 
    :type accounts: int

    :param is_paired:  Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. 
    :type is_paired: bool

    :param volume_ids:  A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. 
    :type volume_ids: int

    :param volume_name:  Only volume object information matching the volume name is returned. 
    :type volume_name: str

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;Only volumes with an ID greater than or equal to this&#x27;, &#x27;value are returned. Mutually exclusive with the&#x27;, &#x27;volumeIDs parameter.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the maximum number of volume&#x27;, &#x27;results that are returned. Mutually exclusive with the&#x27;, &#x27;volumeIDs parameter.&#x27;]",
        dictionaryType=None
    )
    volume_status = data_model.property(
        "volumeStatus", str,
        array=False, optional=True,
        documentation="[&#x27;Only volumes with a status equal to the status value are&#x27;, &#x27;returned.&#x27;, &#x27;Possible values are:&#x27;, &#x27;creating&#x27;, &#x27;snapshotting&#x27;, &#x27;active&#x27;, &#x27;deleted&#x27;]",
        dictionaryType=None
    )
    accounts = data_model.property(
        "accounts", int,
        array=True, optional=True,
        documentation="[&#x27;Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter.&#x27;]",
        dictionaryType=None
    )
    is_paired = data_model.property(
        "isPaired", bool,
        array=False, optional=True,
        documentation="[&#x27;Returns volumes that are paired or not paired.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: Returns all paired volumes.&#x27;, &#x27;false: Returns all volumes that are not paired.&#x27;]",
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volume IDs. If you supply this parameter, other&#x27;, &#x27;parameters operate only on this set of volumes. Mutually&#x27;, &#x27;exclusive with the accounts, startVolumeID, and limit&#x27;, &#x27;parameters.&#x27;]",
        dictionaryType=None
    )
    volume_name = data_model.property(
        "volumeName", str,
        array=False, optional=True,
        documentation="[&#x27;Only volume object information matching the volume&#x27;, &#x27;name is returned.&#x27;]",
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleResult(data_model.DataObject):
    """ModifyScheduleResult  

    :param schedule: [required]  
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsRequest(data_model.DataObject):
    """ClearClusterFaultsRequest  
    You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved
    and unresolved faults can be cleared.

    :param fault_types:  Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. 
    :type fault_types: str

    """
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="[&#x27;Determines the types of faults cleared. Possible values are:&#x27;, &#x27;current: Faults that are currently detected and have&#x27;, &#x27;not been resolved.&#x27;, &#x27;resolved: (Default) Faults that were previously&#x27;, &#x27;detected and resolved.&#x27;, &#x27;all: Both current and resolved faults are cleared. The&#x27;, &#x27;fault status can be determined by the resolved field of&#x27;, &#x27;the fault object.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterAdminResult(data_model.DataObject):
    """RemoveClusterAdminResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AsyncHandle(data_model.DataObject):
    """AsyncHandle  

    :param async_result_id: [required] The ID of the result. 
    :type async_result_id: int

    :param completed: [required] Returns true if it is completed and false if it isn't. 
    :type completed: bool

    :param create_time: [required] The time at which the asyncronous result was created 
    :type create_time: str

    :param last_update_time: [required] Time at which the result was last updated 
    :type last_update_time: str

    :param result_type: [required] The type of result. Could be Clone, DriveAdd, etc. 
    :type result_type: str

    :param success: [required] Returns whether the result was a success or failure. 
    :type success: bool

    :param data: [required] Attributes related to the result 
    :type data: dict

    """
    async_result_id = data_model.property(
        "asyncResultID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the result.&#x27;]",
        dictionaryType=None
    )
    completed = data_model.property(
        "completed", bool,
        array=False, optional=False,
        documentation="[&quot;Returns true if it is completed and false if it isn&#x27;t.&quot;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[&#x27;The time at which the asyncronous result was created&#x27;]",
        dictionaryType=None
    )
    last_update_time = data_model.property(
        "lastUpdateTime", str,
        array=False, optional=False,
        documentation="[&#x27;Time at which the result was last updated&#x27;]",
        dictionaryType=None
    )
    result_type = data_model.property(
        "resultType", str,
        array=False, optional=False,
        documentation="[&#x27;The type of result. Could be Clone, DriveAdd, etc.&#x27;]",
        dictionaryType=None
    )
    success = data_model.property(
        "success", bool,
        array=False, optional=False,
        documentation="[&#x27;Returns whether the result was a success or failure.&#x27;]",
        dictionaryType=None
    )
    data = data_model.property(
        "data", dict,
        array=False, optional=False,
        documentation="[&#x27;Attributes related to the result&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsResult(data_model.DataObject):
    """ListAsyncResultsResult  

    :param async_handles: [required] An array of serialized asynchronous method results. 
    :type async_handles: AsyncHandle

    """
    async_handles = data_model.property(
        "asyncHandles", AsyncHandle,
        array=True, optional=False,
        documentation="[&#x27;An array of serialized asynchronous method results.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Account(data_model.DataObject):
    """Account  
    The object containing information about an account.
    This object only includes "configured" information about the account, not any runtime or usage information.

    :param account_id: [required] Unique AccountID for the account. 
    :type account_id: int

    :param username: [required] User name for the account. 
    :type username: str

    :param status: [required] Current status of the account. 
    :type status: str

    :param volumes: [required] List of VolumeIDs for Volumes owned by this account. 
    :type volumes: int

    :param initiator_secret:  CHAP secret to use for the initiator. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  CHAP secret to use for the target (mutual CHAP authentication). 
    :type target_secret: CHAPSecret

    :param storage_container_id:  The id of the storage container associated with the account 
    :type storage_container_id: UUID

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique AccountID for the account.&#x27;]",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;User name for the account.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the account.&#x27;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;List of VolumeIDs for Volumes owned by this account.&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the initiator.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;CHAP secret to use for the target (mutual CHAP authentication).&#x27;]",
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=True,
        documentation="[&#x27;The id of the storage container associated with the account&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountResult(data_model.DataObject):
    """AddAccountResult  

    :param account_id: [required] AccountID for the newly created Account. 
    :type account_id: int

    :param account:  The full account object 
    :type account: Account

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;AccountID for the newly created Account.&#x27;]",
        dictionaryType=None
    )
    account = data_model.property(
        "account", Account,
        array=False, optional=True,
        documentation="[&#x27;The full account object&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusRequest(data_model.DataObject):
    """GetFeatureStatusRequest  
    GetFeatureStatus enables you to retrieve the status of a cluster feature.

    :param feature:  Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the feature for which the status is returned. Valid value is:&#x27;, &#x27;vvols: Retrieve status for the NetApp SolidFire VVols&#x27;, &#x27;cluster feature.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigRequest(data_model.DataObject):
    """GetIpmiConfigRequest  
    GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node.

    :param chassis_type:  Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. 
    :type chassis_type: str

    """
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=True,
        documentation="[&#x27;Displays information for each node chassis type.&#x27;, &#x27;Valid values are:&#x27;, &#x27;all: Returns sensor information for each chassis type.&#x27;, &#x27;{chassis type}: Returns sensor information for a specified chassis type.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotRequest(data_model.DataObject):
    """ModifySnapshotRequest  
    ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on
    the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.

    :param snapshot_id: [required] Specifies the ID of the snapshot. 
    :type snapshot_id: int

    :param expiration_time:  Sets the time when the snapshot should be removed. 
    :type expiration_time: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the ID of the snapshot.&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="[&#x27;Sets the time when the snapshot should be&#x27;, &#x27;removed.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Replicates the snapshot created to a remote cluster.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: The snapshot is replicated to remote storage.&#x27;, &#x27;false: Default. The snapshot is not replicated.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterFullThresholdResult(data_model.DataObject):
    """ModifyClusterFullThresholdResult  

    :param block_fullness: [required] Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. 
    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between "blockFullness" and "metadataFullness". 
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata fullness of the cluster. 
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. 
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that is set for "Stage 2" cluster threshold level. 
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist. 
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist. 
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. 
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is getting low. 
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is critically low. 
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist. 
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist. 
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster measured in bytes. 
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space that can be used to store metadata. 
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the cluster. 
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on volume drives to store metadata. 
    :type sum_used_metadata_cluster_bytes: int

    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="[&#x27;Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.&#x27;]",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="[&#x27;A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.&#x27;]",
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of metadata fullness of the cluster.&#x27;]",
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.&#x27;]",
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.&#x27;]",
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage2 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage3 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="[&#x27;The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.&#x27;]",
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.&#x27;]",
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.&#x27;]",
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage4 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage5 condition will exist.&#x27;]",
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Physical capacity of the cluster measured in bytes.&#x27;]",
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total amount of space that can be used to store metadata.&#x27;]",
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes used on the cluster.&#x27;]",
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Amount of space used on volume drives to store metadata.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyScheduleRequest(data_model.DataObject):
    """ModifyScheduleRequest  
    ModifySchedule enables you to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.

    :param schedule: [required] The "Schedule" object will be used to modify an existing schedule. The ScheduleID property is required. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[&#x27;The &quot;Schedule&quot; object will be used to modify an existing schedule.&#x27;, &#x27;The ScheduleID property is required.&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&#x27;, &#x27;DaysOfMonthFrequency&#x27;, &#x27;DaysOrWeekFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NewDrive(data_model.DataObject):
    """NewDrive  

    :param drive_id: [required] A unique identifier for this drive. 
    :type drive_id: int

    :param type:  block or slice 
    :type type: str

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;A unique identifier for this drive.&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=True,
        documentation="[&#x27;block or slice&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterStats(data_model.DataObject):
    """ClusterStats  

    :param cluster_utilization: [required] The amount of cluster capacity being utilized. 
    :type cluster_utilization: float

    :param client_queue_depth: [required]  
    :type client_queue_depth: int

    :param read_bytes: [required] Total bytes read by clients. 
    :type read_bytes: int

    :param read_ops: [required] Total read operations. 
    :type read_ops: int

    :param timestamp: [required] Current time in UTC format. ISO 8601 date string. 
    :type timestamp: str

    :param write_bytes: [required] Total bytes written by clients. 
    :type write_bytes: int

    :param write_ops: [required] Total write operations. 
    :type write_ops: int

    :param actual_iops:   
    :type actual_iops: int

    :param average_iopsize:   
    :type average_iopsize: int

    :param latency_usec:   
    :type latency_usec: int

    :param read_bytes_last_sample:   
    :type read_bytes_last_sample: int

    :param read_latency_usec:   
    :type read_latency_usec: int

    :param read_ops_last_sample:   
    :type read_ops_last_sample: int

    :param sample_period_msec:   
    :type sample_period_msec: int

    :param unaligned_reads:   
    :type unaligned_reads: int

    :param unaligned_writes:   
    :type unaligned_writes: int

    :param write_bytes_last_sample:   
    :type write_bytes_last_sample: int

    :param write_latency_usec:   
    :type write_latency_usec: int

    :param write_ops_last_sample:   
    :type write_ops_last_sample: int

    """
    cluster_utilization = data_model.property(
        "clusterUtilization", float,
        array=False, optional=False,
        documentation="[&#x27;The amount of cluster capacity being utilized.&#x27;]",
        dictionaryType=None
    )
    client_queue_depth = data_model.property(
        "clientQueueDepth", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total bytes read by clients.&#x27;]",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="[&#x27;Total read operations.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;Current time in UTC format. ISO 8601 date string.&#x27;]",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total bytes written by clients.&#x27;]",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="[&#x27;Total write operations.&#x27;]",
        dictionaryType=None
    )
    actual_iops = data_model.property(
        "actualIOPS", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    average_iopsize = data_model.property(
        "averageIOPSize", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    latency_usec = data_model.property(
        "latencyUSec", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_bytes_last_sample = data_model.property(
        "readBytesLastSample", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_latency_usec = data_model.property(
        "readLatencyUSec", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_ops_last_sample = data_model.property(
        "readOpsLastSample", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    sample_period_msec = data_model.property(
        "samplePeriodMsec", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    unaligned_reads = data_model.property(
        "unalignedReads", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    unaligned_writes = data_model.property(
        "unalignedWrites", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    write_bytes_last_sample = data_model.property(
        "writeBytesLastSample", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    write_latency_usec = data_model.property(
        "writeLatencyUSec", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    write_ops_last_sample = data_model.property(
        "writeOpsLastSample", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStatsResult(data_model.DataObject):
    """GetClusterStatsResult  

    :param cluster_stats: [required]  
    :type cluster_stats: ClusterStats

    """
    cluster_stats = data_model.property(
        "clusterStats", ClusterStats,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupRequest  
    You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed.

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param virtual_network_id:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_tags: int

    :param name:  The new name for this volume access group. Not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
    :type volumes: int

    :param delete_orphan_initiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
    :type delete_orphan_initiators: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group to modify.&#x27;]",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="[&#x27;The ID of the SolidFire virtual network to associate the volume access group with.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="[&#x27;The ID of the SolidFire virtual network to associate the volume access group with.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;The new name for this volume access group. Not required to be unique, but recommended.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="[&quot;List of initiators to include in the volume access group. If unspecified, the access group&#x27;s configured initiators are not modified.&quot;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="[&quot;List of volumes to initially include in the volume access group. If unspecified, the access group&#x27;s volumes are not modified.&quot;]",
        dictionaryType=None
    )
    delete_orphan_initiators = data_model.property(
        "deleteOrphanInitiators", bool,
        array=False, optional=True,
        documentation="[&#x27;true: Delete initiator objects after they are removed from a volume access group.&#x27;, &#x27;false: Do not delete initiator objects after they are removed from a volume access group.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeQOS(data_model.DataObject):
    """VolumeQOS  
    Quality of Service (QoS) Result values are used on SolidFire volumes to provision performance expectations.

    :param min_iops: [required] Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their min IOPS value and there is still insufficient performance capacity. 
    :type min_iops: int

    :param max_iops: [required] Desired maximum 4KB IOPS allowed over an extended period of time. 
    :type max_iops: int

    :param burst_iops: [required] Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 
    :type burst_iops: int

    :param burst_time: [required] The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 
    :type burst_time: int

    :param curve: [required] The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their min IOPS value and there is still insufficient performance capacity.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]",
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=False,
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;Note: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="[&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]",
        dictionaryType=int
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnapshotReplication(data_model.DataObject):
    """SnapshotReplication  

    :param state: [required] The state of the snapshot replication. 
    :type state: str

    :param state_details: [required] Reserved for future use. 
    :type state_details: str

    """
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="[&#x27;The state of the snapshot replication.&#x27;]",
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="[&#x27;Reserved for future use.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoteReplication(data_model.DataObject):
    """RemoteReplication  
    Details on the volume replication.

    :param mode: [required] Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. 
    :type mode: str

    :param pause_limit: [required] The number of occurring write ops before auto-pausing, on a per volume pair level. 
    :type pause_limit: int

    :param remote_service_id: [required] The remote slice service ID. 
    :type remote_service_id: int

    :param resume_details: [required] Reserved for future use. 
    :type resume_details: str

    :param snapshot_replication: [required] The details of snapshot replication. 
    :type snapshot_replication: SnapshotReplication

    :param state: [required] The state of the volume replication. 
    :type state: str

    :param state_details: [required] Reserved for future use. 
    :type state_details: str

    """
    mode = data_model.property(
        "mode", str,
        array=False, optional=False,
        documentation="[&#x27;Volume replication mode.&#x27;, &#x27;Possible values:&#x27;, &#x27;Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&#x27;, &#x27;Sync: Source acknowledges write when the data is stored locally and on the remote cluster.&#x27;, &#x27;SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.&#x27;]",
        dictionaryType=None
    )
    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=False,
        documentation="[&#x27;The number of occurring write ops before auto-pausing, on a per volume pair level.&#x27;]",
        dictionaryType=None
    )
    remote_service_id = data_model.property(
        "remoteServiceID", int,
        array=False, optional=False,
        documentation="[&#x27;The remote slice service ID.&#x27;]",
        dictionaryType=None
    )
    resume_details = data_model.property(
        "resumeDetails", str,
        array=False, optional=False,
        documentation="[&#x27;Reserved for future use.&#x27;]",
        dictionaryType=None
    )
    snapshot_replication = data_model.property(
        "snapshotReplication", SnapshotReplication,
        array=False, optional=False,
        documentation="[&#x27;The details of snapshot replication.&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="[&#x27;The state of the volume replication.&#x27;]",
        dictionaryType=None
    )
    state_details = data_model.property(
        "stateDetails", str,
        array=False, optional=False,
        documentation="[&#x27;Reserved for future use.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumePair(data_model.DataObject):
    """VolumePair  
    The Volume Pair Info is an object containing information about a volume that is paired on a remote cluster.
    If the volume is not paired, this object is null.

    :param cluster_pair_id: [required] The remote cluster a volume is paired with. 
    :type cluster_pair_id: int

    :param remote_volume_id: [required] The VolumeID on the remote cluster a volume is paired with. 
    :type remote_volume_id: int

    :param remote_slice_id: [required] The SliceID on the remote cluster a volume is paired with. 
    :type remote_slice_id: int

    :param remote_volume_name: [required] The last-observed name of the volume on the remote cluster a volume is paired with. 
    :type remote_volume_name: str

    :param volume_pair_uuid: [required] A UUID in canonical form. 
    :type volume_pair_uuid: UUID

    :param remote_replication: [required] Details about the replication configuration for this volume pair. 
    :type remote_replication: RemoteReplication

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="[&#x27;The remote cluster a volume is paired with.&#x27;]",
        dictionaryType=None
    )
    remote_volume_id = data_model.property(
        "remoteVolumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The VolumeID on the remote cluster a volume is paired with.&#x27;]",
        dictionaryType=None
    )
    remote_slice_id = data_model.property(
        "remoteSliceID", int,
        array=False, optional=False,
        documentation="[&#x27;The SliceID on the remote cluster a volume is paired with.&#x27;]",
        dictionaryType=None
    )
    remote_volume_name = data_model.property(
        "remoteVolumeName", str,
        array=False, optional=False,
        documentation="[&#x27;The last-observed name of the volume on the remote cluster a volume is paired with.&#x27;]",
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;A UUID in canonical form.&#x27;]",
        dictionaryType=None
    )
    remote_replication = data_model.property(
        "remoteReplication", RemoteReplication,
        array=False, optional=False,
        documentation="[&#x27;Details about the replication configuration for this volume pair.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Volume(data_model.DataObject):
    """Volume  
    Volumes Info is an object containing information about a volume.
    The return objects only include "configured" information about the volume and not runtime or usage information.
    Information about paired volumes will also be returned.

    :param volume_id: [required] Unique VolumeID for the volume. 
    :type volume_id: int

    :param name: [required] Name of the volume as provided at creation time. 
    :type name: str

    :param account_id: [required] Unique AccountID for the account. 
    :type account_id: int

    :param create_time: [required] UTC formatted time the volume was created. 
    :type create_time: str

    :param status: [required] Current status of the volume init: A volume that is being initialized and is not ready for connections. active: An active volume ready for connections. 
    :type status: str

    :param access: [required] Access allowed for the volume readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Designated as a target volume in a replicated volume pair. 
    :type access: str

    :param enable512e: [required] If "true", the volume provides 512 byte sector emulation. 
    :type enable512e: bool

    :param iqn:  Volume iSCSI Qualified Name. 
    :type iqn: str

    :param scsi_euidevice_id: [required] Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format. 
    :type scsi_euidevice_id: str

    :param scsi_naadevice_id: [required] Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format. 
    :type scsi_naadevice_id: str

    :param qos: [required] Quality of service settings for this volume. 
    :type qos: VolumeQOS

    :param volume_access_groups: [required] List of volume access groups to which a volume beintegers. 
    :type volume_access_groups: int

    :param volume_pairs: [required] Information about a paired volume. Available only if a volume is paired. @see VolumePairs for return values. 
    :type volume_pairs: VolumePair

    :param delete_time:  The time this volume was deleted. If this has no value, the volume has not yet been deleted. 
    :type delete_time: str

    :param purge_time:  The time this volume will be purged from the system. If this has no value, the volume has not yet been deleted (and is not scheduled for purging). 
    :type purge_time: str

    :param slice_count: [required] The number of slices backing this volume. In the current software, this value will always be 1. 
    :type slice_count: int

    :param total_size: [required] Total size of this volume in bytes. 
    :type total_size: int

    :param block_size: [required] Size of the blocks on the volume. 
    :type block_size: int

    :param virtual_volume_id:  Virtual volume ID this volume backs. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique VolumeID for the volume.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the volume as provided at creation time.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique AccountID for the account.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[&#x27;UTC formatted time the volume was created.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the volume&#x27;, &#x27;init: A volume that is being initialized and is not ready for connections.&#x27;, &#x27;active: An active volume ready for connections.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;Access allowed for the volume&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Designated as a target volume in a replicated volume pair.&#x27;]",
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="[&#x27;If &quot;true&quot;, the volume provides 512 byte sector emulation.&#x27;]",
        dictionaryType=None
    )
    iqn = data_model.property(
        "iqn", str,
        array=False, optional=True,
        documentation="[&#x27;Volume iSCSI Qualified Name.&#x27;]",
        dictionaryType=None
    )
    scsi_euidevice_id = data_model.property(
        "scsiEUIDeviceID", str,
        array=False, optional=False,
        documentation="[&#x27;Globally unique SCSI device identifier for the volume in EUI-64 based 16-byte format.&#x27;]",
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="[&#x27;Globally unique SCSI device identifier for the volume in NAA IEEE Registered Extended format.&#x27;]",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", VolumeQOS,
        array=False, optional=False,
        documentation="[&#x27;Quality of service settings for this volume.&#x27;]",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="[&#x27;List of volume access groups to which a volume beintegers.&#x27;]",
        dictionaryType=None
    )
    volume_pairs = data_model.property(
        "volumePairs", VolumePair,
        array=True, optional=False,
        documentation="[&#x27;Information about a paired volume.&#x27;, &#x27;Available only if a volume is paired.&#x27;, &#x27;@see VolumePairs for return values.&#x27;]",
        dictionaryType=None
    )
    delete_time = data_model.property(
        "deleteTime", str,
        array=False, optional=True,
        documentation="[&#x27;The time this volume was deleted.&#x27;, &#x27;If this has no value, the volume has not yet been deleted.&#x27;]",
        dictionaryType=None
    )
    purge_time = data_model.property(
        "purgeTime", str,
        array=False, optional=True,
        documentation="[&#x27;The time this volume will be purged from the system.&#x27;, &#x27;If this has no value, the volume has not yet been deleted (and is not scheduled for purging).&#x27;]",
        dictionaryType=None
    )
    slice_count = data_model.property(
        "sliceCount", int,
        array=False, optional=False,
        documentation="[&#x27;The number of slices backing this volume.&#x27;, &#x27;In the current software, this value will always be 1.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total size of this volume in bytes.&#x27;]",
        dictionaryType=None
    )
    block_size = data_model.property(
        "blockSize", int,
        array=False, optional=False,
        documentation="[&#x27;Size of the blocks on the volume.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=True,
        documentation="[&#x27;Virtual volume ID this volume backs.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeResult(data_model.DataObject):
    """CloneVolumeResult  

    :param volume:  The resulting volume 
    :type volume: Volume

    :param clone_id: [required] The ID of the newly-created clone. 
    :type clone_id: int

    :param volume_id: [required] The volume ID of the newly-created clone. 
    :type volume_id: int

    :param async_handle: [required] Handle value used to track the progress of the clone. 
    :type async_handle: int

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="[&#x27;The resulting volume&#x27;]",
        dictionaryType=None
    )
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the newly-created clone.&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The volume ID of the newly-created clone.&#x27;]",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;Handle value used to track the progress of the clone.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsRequest(data_model.DataObject):
    """GetVolumeStatsRequest  
    GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume.

    :param volume_id: [required] Specifies the volume for which statistics are gathered. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the volume for which statistics are gathered.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsRequest(data_model.DataObject):
    """GetDriveStatsRequest  
    GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the
    cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you
    run this method. 

    :param drive_id: [required] Specifies the drive for which statistics are gathered. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the drive for which statistics are gathered.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """GetVolumeAccessGroupLunAssignmentsRequest  
    The GetVolumeAccessGroupLunAssignments
    method enables you to retrieve details on LUN mappings
    of a specified volume access group.

    :param volume_access_group_id: [required] The unique volume access group ID used to return information. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique volume access group ID used to return information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsRequest(data_model.DataObject):
    """ListVolumeStatsRequest  
    ListVolumeStats returns high-level activity measurements for a single volume, list of volumes, or all volumes (if you omit the volumeIDs parameter). Measurement values are cumulative from the creation of the volume.

    :param volume_ids:  A list of volume IDs of volumes from which to retrieve activity information. 
    :type volume_ids: int

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volume IDs of volumes from which to retrieve activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddAccountRequest(data_model.DataObject):
    """AddAccountRequest  
    You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account.

    :param username: [required] Specifies the username for this account. (Might be 1 to 64 characters in length). 
    :type username: str

    :param initiator_secret:  The CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. If unspecified, a random secret is created. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  The CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. If unspecified, a random secret is created. 
    :type target_secret: CHAPSecret

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;Specifies the username for this account. (Might be 1 to 64 characters in length).&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;The CHAP secret to use for the initiator. This secret must&#x27;, &#x27;be 12-16 characters in length and should be&#x27;, &#x27;impenetrable. The initiator CHAP secret must be unique&#x27;, &#x27;and cannot be the same as the target CHAP secret. If unspecified, a random secret is created.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;The CHAP secret to use for the target (mutual CHAP&#x27;, &#x27;authentication). This secret must be 12-16 characters in&#x27;, &#x27;length and should be impenetrable. The target CHAP&#x27;, &#x27;secret must be unique and cannot be the same as the&#x27;, &#x27;initiator CHAP secret. If unspecified, a random secret is&#x27;, &#x27;created.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByNameRequest(data_model.DataObject):
    """GetAccountByNameRequest  
    GetAccountByName enables you to retrieve details about a specific account, given its username.

    :param username: [required] Username for the account. 
    :type username: str

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;Username for the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupResult(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupResult  

    :param volume_stats: [required] List of account activity information. Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;, &#x27;Note: The volumeID member is 0 for each entry, as the values represent the summation of all volumes owned by the account.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetResult(data_model.DataObject):
    """CreateBackupTargetResult  

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeHostsRequest(data_model.DataObject):
    """ListVirtualVolumeHostsRequest  
    ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host
    that has initiated a session with the VASA API provider.

    :param virtual_volume_host_ids:  A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. 
    :type virtual_volume_host_ids: UUID

    """
    virtual_volume_host_ids = data_model.property(
        "virtualVolumeHostIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveDrivesRequest(data_model.DataObject):
    """RemoveDrivesRequest  
    You can use RemoveDrives to proactively remove drives that are part of the cluster. You might want to use this method when
    reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and
    migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on
    the total capacity of the drives being removed, it might take several minutes to migrate all of the data. Use the GetAsyncResult
    method to check the status of the remove operation.
    When removing multiple drives, use a single RemoveDrives method call rather than multiple individual methods with a single drive
    each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.
    You can also remove drives with a "failed" status using RemoveDrives. When you remove a drive with a "failed" status it is not
    returned to an "available" or active status. The drive is unavailable for use in the cluster.
    Use the ListDrives method to obtain the driveIDs for the drives you want to remove.

    :param drives: [required] List of driveIDs to remove from the cluster. 
    :type drives: int

    :param force_during_upgrade:  If you want to remove a drive during upgrade, this must be set to true. 
    :type force_during_upgrade: bool

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="[&#x27;List of driveIDs to remove from the cluster.&#x27;]",
        dictionaryType=None
    )
    force_during_upgrade = data_model.property(
        "forceDuringUpgrade", bool,
        array=False, optional=True,
        documentation="[&#x27;If you want to remove a drive during upgrade, this must be set to true.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneResult(data_model.DataObject):
    """CancelCloneResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LdapConfiguration(data_model.DataObject):
    """LdapConfiguration  
    LDAP Configuration object returns information about the LDAP configuration on SolidFire storage. LDAP information is returned with the API method GetLdapConfiguration.

    :param auth_type: [required] Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind 
    :type auth_type: str

    :param enabled: [required] Identifies whether or not the system is enabled for LDAP.  Valid values: true false 
    :type enabled: bool

    :param group_search_base_dn: [required] The base DN of the tree to start the group search (will do a subtree search from here). 
    :type group_search_base_dn: str

    :param group_search_custom_filter: [required] The custom search filter used. 
    :type group_search_custom_filter: str

    :param group_search_type: [required] Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). 
    :type group_search_type: str

    :param search_bind_dn: [required] A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
    :type search_bind_dn: str

    :param server_uris: [required] A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
    :type server_uris: str

    :param user_dntemplate: [required] A string that is used to form a fully qualified user DN. 
    :type user_dntemplate: str

    :param user_search_base_dn: [required] The base DN of the tree used to start the search (will do a subtree search from here). 
    :type user_search_base_dn: str

    :param user_search_filter: [required] The LDAP filter used. 
    :type user_search_filter: str

    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=False,
        documentation="[&#x27;Identifies which user authentcation method will be used. &#x27;, &#x27;Valid values:&#x27;, &#x27;DirectBind&#x27;, &#x27;SearchAndBind&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;Identifies whether or not the system is enabled for LDAP. &#x27;, &#x27;Valid values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]",
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=False,
        documentation="[&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=False,
        documentation="[&#x27;The custom search filter used.&#x27;]",
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=False,
        documentation="[&#x27;Controls the default group search filter used, can be one of the following:&#x27;, &#x27;NoGroups: No group support.&#x27;, &quot;ActiveDirectory: Nested membership of all of a user&#x27;s AD groups.&quot;, &#x27;MemberDN: MemberDN style groups (single-level).&#x27;]",
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=False,
        documentation="[&#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]",
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="[&#x27;A comma-separated list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]",
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=False,
        documentation="[&#x27;A string that is used to form a fully qualified user DN.&#x27;]",
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=False,
        documentation="[&#x27;The base DN of the tree used to start the search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=False,
        documentation="[&#x27;The LDAP filter used.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestLdapAuthenticationRequest(data_model.DataObject):
    """TestLdapAuthenticationRequest  
    The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is
    correct, the API call returns the group membership of the tested user.

    :param username: [required] The username to be tested. 
    :type username: str

    :param password: [required] The password for the username to be tested. 
    :type password: str

    :param ldap_configuration:  An ldapConfiguration object to be tested. If specified, the API call tests the provided configuration even if LDAP authentication is disabled. 
    :type ldap_configuration: LdapConfiguration

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;The username to be tested.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="[&#x27;The password for the username to be tested.&#x27;]",
        dictionaryType=None
    )
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=True,
        documentation="[&#x27;An ldapConfiguration object to be tested. If specified, the API call tests the provided&#x27;, &#x27;configuration even if LDAP authentication is disabled.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveConfigInfo(data_model.DataObject):
    """DriveConfigInfo  

    :param canonical_name: [required]  
    :type canonical_name: str

    :param connected: [required]  
    :type connected: bool

    :param dev: [required]  
    :type dev: int

    :param dev_path: [required]  
    :type dev_path: str

    :param drive_type: [required]  
    :type drive_type: str

    :param product: [required]  
    :type product: str

    :param name: [required]  
    :type name: str

    :param path: [required]  
    :type path: str

    :param path_link: [required]  
    :type path_link: str

    :param scsi_compat_id: [required]  
    :type scsi_compat_id: str

    :param smart_ssd_write_capable:   
    :type smart_ssd_write_capable: bool

    :param security_enabled: [required]  
    :type security_enabled: bool

    :param security_frozen: [required]  
    :type security_frozen: bool

    :param security_locked: [required]  
    :type security_locked: bool

    :param security_supported: [required]  
    :type security_supported: bool

    :param size: [required]  
    :type size: int

    :param slot: [required]  
    :type slot: int

    :param uuid: [required]  
    :type uuid: UUID

    :param vendor: [required]  
    :type vendor: str

    :param version: [required]  
    :type version: str

    :param security_at_maximum: [required]  
    :type security_at_maximum: bool

    :param serial: [required]  
    :type serial: str

    :param scsi_state: [required]  
    :type scsi_state: str

    """
    canonical_name = data_model.property(
        "canonicalName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DrivesConfigInfo(data_model.DataObject):
    """DrivesConfigInfo  

    :param drives: [required]  
    :type drives: DriveConfigInfo

    :param num_block_actual: [required]  
    :type num_block_actual: int

    :param num_block_expected: [required]  
    :type num_block_expected: int

    :param num_slice_actual: [required]  
    :type num_slice_actual: int

    :param num_slice_expected: [required]  
    :type num_slice_expected: int

    :param num_total_actual: [required]  
    :type num_total_actual: int

    :param num_total_expected: [required]  
    :type num_total_expected: int

    """
    drives = data_model.property(
        "drives", DriveConfigInfo,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_block_actual = data_model.property(
        "numBlockActual", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_block_expected = data_model.property(
        "numBlockExpected", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_slice_actual = data_model.property(
        "numSliceActual", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_slice_expected = data_model.property(
        "numSliceExpected", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_total_actual = data_model.property(
        "numTotalActual", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    num_total_expected = data_model.property(
        "numTotalExpected", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveConfigResult(data_model.DataObject):
    """GetDriveConfigResult  

    :param drive_config: [required] Configuration information for the drives that are connected to the cluster 
    :type drive_config: DrivesConfigInfo

    """
    drive_config = data_model.property(
        "driveConfig", DrivesConfigInfo,
        array=False, optional=False,
        documentation="[&#x27;Configuration information for the drives that are connected to the cluster&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsRequest(data_model.DataObject):
    """GetNodeStatsRequest  
    GetNodeStats enables you to retrieve the high-level activity measurements for a single node.

    :param node_id: [required] Specifies the node for which statistics are gathered. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the node for which statistics are gathered.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesRequest(data_model.DataObject):
    """ResetDrivesRequest  
    ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused
    in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call.

    :param drives: [required] List of device names (not driveIDs) to reset. 
    :type drives: str

    :param force: [required] Required parameter to successfully reset a drive. 
    :type force: bool

    """
    drives = data_model.property(
        "drives", str,
        array=False, optional=False,
        documentation="[&#x27;List of device names (not driveIDs) to reset.&#x27;]",
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;Required parameter to successfully reset a drive.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EventInfo(data_model.DataObject):
    """EventInfo  

    :param event_id: [required]  
    :type event_id: int

    :param severity: [required]  
    :type severity: int

    :param event_info_type: [required]  
    :type event_info_type: str

    :param message: [required]  
    :type message: str

    :param service_id: [required]  
    :type service_id: int

    :param node_id: [required]  
    :type node_id: int

    :param drive_id: [required]  
    :type drive_id: int

    :param drive_ids: [required]  
    :type drive_ids: int

    :param time_of_report: [required]  
    :type time_of_report: str

    :param time_of_publish: [required]  
    :type time_of_publish: str

    :param details:   
    :type details: str

    """
    event_id = data_model.property(
        "eventID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    severity = data_model.property(
        "severity", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    event_info_type = data_model.property(
        "eventInfoType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    message = data_model.property(
        "message", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    time_of_report = data_model.property(
        "timeOfReport", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    time_of_publish = data_model.property(
        "timeOfPublish", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListEventsResult(data_model.DataObject):
    """ListEventsResult  

    :param event_queue_type: [required]  
    :type event_queue_type: str

    :param events: [required]  
    :type events: EventInfo

    """
    event_queue_type = data_model.property(
        "eventQueueType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    events = data_model.property(
        "events", EventInfo,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetRequest(data_model.DataObject):
    """ModifyBackupTargetRequest  
    ModifyBackupTarget enables you to change attributes of a backup target.

    :param backup_target_id: [required] The unique target ID for the target to modify. 
    :type backup_target_id: int

    :param name:  The new name for the backup target. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique target ID for the target to modify.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;The new name for the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PairedCluster(data_model.DataObject):
    """PairedCluster  

    :param cluster_name: [required] Name of the other cluster in the pair 
    :type cluster_name: str

    :param cluster_pair_id: [required] Unique ID given to each cluster in the pair. 
    :type cluster_pair_id: int

    :param cluster_pair_uuid: [required] Universally unique identifier. 
    :type cluster_pair_uuid: UUID

    :param latency: [required] Number, in milliseconds, of latency between clusters. 
    :type latency: int

    :param mvip: [required] IP of the management connection for paired clusters. 
    :type mvip: str

    :param status: [required] Can be one of the following: Connected Misconfigured Disconnected 
    :type status: str

    :param version: [required] The Element OS version of the other cluster in the pair. 
    :type version: str

    """
    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the other cluster in the pair&#x27;]",
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID given to each cluster in the pair.&#x27;]",
        dictionaryType=None
    )
    cluster_pair_uuid = data_model.property(
        "clusterPairUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;Universally unique identifier.&#x27;]",
        dictionaryType=None
    )
    latency = data_model.property(
        "latency", int,
        array=False, optional=False,
        documentation="[&#x27;Number, in milliseconds, of latency between clusters.&#x27;]",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="[&#x27;IP of the management connection for paired clusters.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;Connected&#x27;, &#x27;Misconfigured&#x27;, &#x27;Disconnected&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[&#x27;The Element OS version of the other cluster in the pair.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterPairsResult(data_model.DataObject):
    """ListClusterPairsResult  

    :param cluster_pairs: [required] Information about each paired cluster. 
    :type cluster_pairs: PairedCluster

    """
    cluster_pairs = data_model.property(
        "clusterPairs", PairedCluster,
        array=True, optional=False,
        documentation="[&#x27;Information about each paired cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterVersionInfo(data_model.DataObject):
    """ClusterVersionInfo  
    Version information for a node in the cluster.

    :param node_id: [required]  
    :type node_id: int

    :param node_version: [required]  
    :type node_version: str

    :param node_internal_revision: [required]  
    :type node_internal_revision: str

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_version = data_model.property(
        "nodeVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_internal_revision = data_model.property(
        "nodeInternalRevision", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SoftwareVersionInfo(data_model.DataObject):
    """SoftwareVersionInfo  

    :param current_version: [required]  
    :type current_version: str

    :param node_id: [required]  
    :type node_id: int

    :param package_name: [required]  
    :type package_name: str

    :param pending_version: [required]  
    :type pending_version: str

    :param start_time: [required]  
    :type start_time: str

    """
    current_version = data_model.property(
        "currentVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    package_name = data_model.property(
        "packageName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_version = data_model.property(
        "pendingVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    start_time = data_model.property(
        "startTime", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterVersionInfoResult(data_model.DataObject):
    """GetClusterVersionInfoResult  

    :param cluster_apiversion: [required]  
    :type cluster_apiversion: str

    :param cluster_version: [required]  
    :type cluster_version: str

    :param cluster_version_info: [required]  
    :type cluster_version_info: ClusterVersionInfo

    :param software_version_info: [required]  
    :type software_version_info: SoftwareVersionInfo

    """
    cluster_apiversion = data_model.property(
        "clusterAPIVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_version = data_model.property(
        "clusterVersion", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_version_info = data_model.property(
        "clusterVersionInfo", ClusterVersionInfo,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    software_version_info = data_model.property(
        "softwareVersionInfo", SoftwareVersionInfo,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CopyVolumeRequest(data_model.DataObject):
    """CopyVolumeRequest  
    CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or
    snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are
    not changed. The destination volume must already exist and must be the same size as the source volume.
    NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the
    destination volume is modified during the copy operation, the changes will be lost.
    This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to
    determine when the process has finished, and ListSyncJobs to see the progress of the copy.

    :param volume_id: [required] VolumeID of the volume to be read from. 
    :type volume_id: int

    :param dst_volume_id: [required] VolumeID of the volume to be overwritten. 
    :type dst_volume_id: int

    :param snapshot_id:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
    :type snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID of the volume to be read from.&#x27;]",
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID of the volume to be overwritten.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the snapshot that is used as the source of the clone.&#x27;, &#x27;If no ID is provided, the current active volume is used.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkInterface(data_model.DataObject):
    """NetworkInterface  

    :param address: [required] IP address of the network. 
    :type address: str

    :param broadcast: [required] Address of NTP broadcast. 
    :type broadcast: str

    :param mac_address: [required] Address used to configure the interface. 
    :type mac_address: str

    :param mtu: [required] Packet size on the network interface. 
    :type mtu: int

    :param name: [required] Name of the network interface. 
    :type name: str

    :param netmask: [required] Netmask for the network interface. 
    :type netmask: str

    :param status: [required] Status of the network. 
    :type status: str

    :param type: [required] The type of network, ie, BondMaster. 
    :type type: str

    :param virtual_network_tag: [required] Virtual Network Tag if on virtual network. 
    :type virtual_network_tag: int

    :param namespace:   
    :type namespace: bool

    """
    address = data_model.property(
        "address", str,
        array=False, optional=False,
        documentation="[&#x27;IP address of the network.&#x27;]",
        dictionaryType=None
    )
    broadcast = data_model.property(
        "broadcast", str,
        array=False, optional=False,
        documentation="[&#x27;Address of NTP broadcast.&#x27;]",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=False,
        documentation="[&#x27;Address used to configure the interface.&#x27;]",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", int,
        array=False, optional=False,
        documentation="[&#x27;Packet size on the network interface.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the network interface.&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="[&#x27;Netmask for the network interface.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the network.&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[&#x27;The type of network, ie, BondMaster.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="[&#x27;Virtual Network Tag if on virtual network.&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNetworkInterfacesResult(data_model.DataObject):
    """ListNetworkInterfacesResult  

    :param interfaces: [required]  
    :type interfaces: NetworkInterface

    """
    interfaces = data_model.property(
        "interfaces", NetworkInterface,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupRequest(data_model.DataObject):
    """CreateVolumeAccessGroupRequest  
    You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication.

    :param name: [required] The name for this volume access group. Not required to be unique, but recommended. 
    :type name: str

    :param initiators:  List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 
    :type initiators: str

    :param volumes:  List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 
    :type volumes: int

    :param virtual_network_id:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_id: int

    :param virtual_network_tags:  The ID of the SolidFire virtual network to associate the volume access group with. 
    :type virtual_network_tags: int

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name for this volume access group. Not required to be unique, but recommended.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=True,
        documentation="[&quot;List of initiators to include in the volume access group. If unspecified, the access group&#x27;s configured initiators are not modified.&quot;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=True,
        documentation="[&quot;List of volumes to initially include in the volume access group. If unspecified, the access group&#x27;s volumes are not modified.&quot;]",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=True, optional=True,
        documentation="[&#x27;The ID of the SolidFire virtual network to associate the volume access group with.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="[&#x27;The ID of the SolidFire virtual network to associate the volume access group with.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotRequest(data_model.DataObject):
    """CreateSnapshotRequest  
    CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch.
    If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication.
    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volume_id: [required] Specifies the unique ID of the volume image from which to copy. 
    :type volume_id: int

    :param snapshot_id:  Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
    :type snapshot_id: int

    :param name:  Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. 
    :type name: str

    :param enable_remote_replication:  Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 
    :type enable_remote_replication: bool

    :param retention:  Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. 
    :type retention: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the unique ID of the volume image from which to copy.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the unique ID of a snapshot from which the new snapshot&#x27;, &#x27;is made. The snapshotID passed must be a snapshot on the given volume.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[&#x27;Replicates the snapshot created to a remote cluster.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: The snapshot is replicated to remote storage.&#x27;, &#x27;false: Default. The snapshot is not replicated.&#x27;]",
        dictionaryType=None
    )
    retention = data_model.property(
        "retention", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesRequest(data_model.DataObject):
    """DeleteVolumesRequest  
    DeleteVolumes marks multiple (up to 500) active volumes for deletion. Once marked, the volumes are purged (permanently deleted) after the cleanup interval elapses.The cleanup interval can be set in the SetClusterSettings method. For more information on using this method, see SetClusterSettings on page 1. After making a request to delete volumes, any active iSCSI connections to the volumes are immediately terminated and no further connections are allowed while the volumes are in this state. A marked volume is not returned in target discovery requests. Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from the system. If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or write operation is stopped. If the volumes you delete are paired with a volume, replication between the paired volumes is suspended and no data is transferred to them or from them while in a deleted state. The remote volumes the deleted volumes were paired with enter into a PausedMisconfigured state and data is no integerer sent to them or from the deleted volumes. Until the deleted volumes are purged, they can be restored and data transfers resume. If the deleted volumes are purged from the system, the volumes they were paired with enter into a StoppedMisconfigured state and the volume pairing status is removed. The purged volumes become permanently unavailable.

    :param account_ids:  A list of account IDs. All volumes from these accounts are deleted from the system.  
    :type account_ids: int

    :param volume_access_group_ids:  A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system. 
    :type volume_access_group_ids: int

    :param volume_ids:  The list of IDs of the volumes to delete from the system. 
    :type volume_ids: int

    """
    account_ids = data_model.property(
        "accountIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of account IDs. All volumes from these accounts are deleted from the system. &#x27;]",
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volume access group IDs. All of the volumes from all of the volume access groups you specify in this list are deleted from the system.&#x27;]",
        dictionaryType=None
    )
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;The list of IDs of the volumes to delete from the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CopyVolumeResult(data_model.DataObject):
    """CopyVolumeResult  

    :param clone_id: [required]  
    :type clone_id: int

    :param async_handle: [required] Handle value used to track the progress of the volume copy. 
    :type async_handle: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;Handle value used to track the progress of the volume copy.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestartServicesRequest(data_model.DataObject):
    """RestartServicesRequest  
    The RestartServices API method enables you to restart the services on a node.
    Caution: This method causes temporary node services interruption. Exercise caution when using this method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param force: [required] Required parameter to successfully restart services on a node. 
    :type force: bool

    :param service:  Service name to be restarted. 
    :type service: str

    :param action:  Action to perform on the service (start, stop, restart). 
    :type action: str

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;Required parameter to successfully restart services on a node.&#x27;]",
        dictionaryType=None
    )
    service = data_model.property(
        "service", str,
        array=False, optional=True,
        documentation="[&#x27;Service name to be restarted.&#x27;]",
        dictionaryType=None
    )
    action = data_model.property(
        "action", str,
        array=False, optional=True,
        documentation="[&#x27;Action to perform on the service (start, stop, restart).&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNvramInfoResult(data_model.DataObject):
    """GetNvramInfoResult  

    :param nvram_info: [required] Arrays of events and errors detected on the NVRAM card. 
    :type nvram_info: dict

    """
    nvram_info = data_model.property(
        "nvramInfo", dict,
        array=False, optional=False,
        documentation="[&#x27;Arrays of events and errors detected on the NVRAM card.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterMasterNodeIDResult(data_model.DataObject):
    """GetClusterMasterNodeIDResult  

    :param node_id: [required] ID of the master node. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;ID of the master node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareRequest(data_model.DataObject):
    """ListDriveHardwareRequest  
    ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware
    information or use this method on the cluster master node MVIP to see information for all the drives on all nodes.
    Note: The "securitySupported": true line of the method response does not imply that the drives are capable of
    encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE",
    commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information.

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;To run this command, the force parameter must be set to true.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeResult(data_model.DataObject):
    """DeleteVolumeResult  

    :param volume:   
    :type volume: Volume

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeWaitingToJoin(data_model.DataObject):
    """NodeWaitingToJoin  

    :param name:   
    :type name: str

    :param version: [required]  
    :type version: str

    :param node_id:   
    :type node_id: int

    :param pending_node_id:   
    :type pending_node_id: int

    :param mip:   
    :type mip: str

    :param cip:   
    :type cip: str

    :param sip:   
    :type sip: str

    :param compatible: [required]  
    :type compatible: bool

    :param chassis_type:   
    :type chassis_type: str

    :param hostname:   
    :type hostname: str

    :param node_type:   
    :type node_type: str

    """
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    compatible = data_model.property(
        "compatible", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    chassis_type = data_model.property(
        "chassisType", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    hostname = data_model.property(
        "hostname", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_type = data_model.property(
        "nodeType", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBootstrapConfigResult(data_model.DataObject):
    """GetBootstrapConfigResult  

    :param cluster_name: [required] Name of the cluster. 
    :type cluster_name: str

    :param node_name: [required] Name of the node. 
    :type node_name: str

    :param nodes: [required] List of descriptions for each node that is actively waiting to join this cluster: compatible - Indicates if the listed node is compatible with the node the API call was executed against. name - IP address of each node. version - version of SolidFire Element software currently installed on the node. 
    :type nodes: NodeWaitingToJoin

    :param version: [required] Version of the SolidFire Element software currently installed. 
    :type version: str

    """
    cluster_name = data_model.property(
        "clusterName", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the cluster.&#x27;]",
        dictionaryType=None
    )
    node_name = data_model.property(
        "nodeName", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the node.&#x27;]",
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", NodeWaitingToJoin,
        array=True, optional=False,
        documentation="[&#x27;List of descriptions for each node that is actively waiting to join this cluster: compatible - Indicates if the listed node is compatible with the node the API call was executed against. name - IP address of each node. version - version of SolidFire Element software currently installed on the node.&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[&#x27;Version of the SolidFire Element software currently installed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListTestsResult(data_model.DataObject):
    """ListTestsResult  

    :param tests: [required] List of tests that can be performed on the node. 
    :type tests: str

    """
    tests = data_model.property(
        "tests", str,
        array=False, optional=False,
        documentation="[&#x27;List of tests that can be performed on the node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LoggingServer(data_model.DataObject):
    """LoggingServer  

    :param host: [required] Hostname or IP address of the log server. 
    :type host: str

    :param port: [required] Port number that the log server is listening on. 
    :type port: int

    """
    host = data_model.property(
        "host", str,
        array=False, optional=False,
        documentation="[&#x27;Hostname or IP address of the log server.&#x27;]",
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="[&#x27;Port number that the log server is listening on.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsRequest(data_model.DataObject):
    """SetRemoteLoggingHostsRequest  
    SetRemoteLoggingHosts enables you to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use GetRemoteLoggingHosts to determine what the current logging hosts are, and then use SetRemoteLoggingHosts to set the desired list of current and new logging hosts.

    :param remote_hosts: [required] A list of hosts to send log messages to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="[&#x27;A list of hosts to send log messages to.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigNodesResult(data_model.DataObject):
    """GetIpmiConfigNodesResult  

    :param node_id: [required]  
    :type node_id: int

    :param result: [required]  
    :type result: dict

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiConfigResult(data_model.DataObject):
    """GetIpmiConfigResult  

    :param nodes: [required]  
    :type nodes: GetIpmiConfigNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiConfigNodesResult,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetScheduleRequest(data_model.DataObject):
    """GetScheduleRequest  
    You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific
    schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this
    method by specifying additional scheduleIDs in the parameter.

    :param schedule_id: [required] Specifies the unique ID of the schedule or multiple schedules to display. 
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the unique ID of the schedule or multiple schedules to display.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminResult(data_model.DataObject):
    """AddLdapClusterAdminResult  

    :param cluster_admin_id:   
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddedNode(data_model.DataObject):
    """AddedNode  

    :param node_id:   
    :type node_id: int

    :param pending_node_id: [required]  
    :type pending_node_id: int

    :param active_node_key:   
    :type active_node_key: str

    :param assigned_node_id:   
    :type assigned_node_id: int

    :param async_handle:   
    :type async_handle: int

    :param cip:   
    :type cip: str

    :param mip:   
    :type mip: str

    :param platform_info:   
    :type platform_info: Platform

    :param sip:   
    :type sip: str

    :param software_version:   
    :type software_version: str

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pending_node_id = data_model.property(
        "pendingNodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    active_node_key = data_model.property(
        "activeNodeKey", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    assigned_node_id = data_model.property(
        "assignedNodeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cip = data_model.property(
        "cip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    platform_info = data_model.property(
        "platformInfo", Platform,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    sip = data_model.property(
        "sip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    software_version = data_model.property(
        "softwareVersion", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesResult(data_model.DataObject):
    """AddNodesResult  

    :param auto_install:   
    :type auto_install: bool

    :param nodes: [required] An array of objects mapping the previous "pendingNodeID" to the "nodeID". 
    :type nodes: AddedNode

    """
    auto_install = data_model.property(
        "autoInstall", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", AddedNode,
        array=True, optional=False,
        documentation="[&#x27;An array of objects mapping the previous &quot;pendingNodeID&quot; to the &quot;nodeID&quot;.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpTrapRecipient(data_model.DataObject):
    """SnmpTrapRecipient  
    Host that is to receive the traps generated by the cluster.

    :param host: [required] The IP address or host name of the target network management station. 
    :type host: str

    :param community: [required] SNMP community string. 
    :type community: str

    :param port: [required] The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. 
    :type port: int

    """
    host = data_model.property(
        "host", str,
        array=False, optional=False,
        documentation="[&#x27;The IP address or host name of the target network management station.&#x27;]",
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="[&#x27;SNMP community string.&#x27;]",
        dictionaryType=None
    )
    port = data_model.property(
        "port", int,
        array=False, optional=False,
        documentation="[&#x27;The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminResult(data_model.DataObject):
    """AddClusterAdminResult  

    :param cluster_admin_id: [required] ClusterAdminID for the newly created Cluster Admin. 
    :type cluster_admin_id: int

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="[&#x27;ClusterAdminID for the newly created Cluster Admin.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingRequest(data_model.DataObject):
    """CompleteClusterPairingRequest  
    You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process. 

    :param cluster_pairing_key: [required] A string of characters that is returned from the "StartClusterPairing" API method. 
    :type cluster_pairing_key: str

    """
    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="[&#x27;A string of characters that is returned from the &quot;StartClusterPairing&quot; API method.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveHardwareInfo(data_model.DataObject):
    """DriveHardwareInfo  

    :param description: [required]  
    :type description: str

    :param dev: [required]  
    :type dev: str

    :param devpath: [required]  
    :type devpath: str

    :param drive_security_at_maximum: [required]  
    :type drive_security_at_maximum: bool

    :param drive_security_frozen: [required]  
    :type drive_security_frozen: bool

    :param drive_security_locked: [required]  
    :type drive_security_locked: bool

    :param logicalname: [required]  
    :type logicalname: str

    :param product: [required]  
    :type product: str

    :param scsi_compat_id: [required]  
    :type scsi_compat_id: str

    :param security_feature_enabled: [required]  
    :type security_feature_enabled: bool

    :param security_feature_supported: [required]  
    :type security_feature_supported: bool

    :param serial: [required]  
    :type serial: str

    :param size: [required]  
    :type size: int

    :param uuid: [required]  
    :type uuid: UUID

    :param version: [required]  
    :type version: str

    """
    description = data_model.property(
        "description", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    devpath = data_model.property(
        "devpath", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_security_at_maximum = data_model.property(
        "driveSecurityAtMaximum", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_security_frozen = data_model.property(
        "driveSecurityFrozen", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_security_locked = data_model.property(
        "driveSecurityLocked", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    logicalname = data_model.property(
        "logicalname", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatID", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_feature_enabled = data_model.property(
        "securityFeatureEnabled", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_feature_supported = data_model.property(
        "securityFeatureSupported", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoResult(data_model.DataObject):
    """GetDriveHardwareInfoResult  

    :param drive_hardware_info: [required]  
    :type drive_hardware_info: DriveHardwareInfo

    """
    drive_hardware_info = data_model.property(
        "driveHardwareInfo", DriveHardwareInfo,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsRequest(data_model.DataObject):
    """DeleteInitiatorsRequest  
    DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access
    groups).
    If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any
    initiators (no partial completion is possible).

    :param initiators: [required] An array of IDs of initiators to delete. 
    :type initiators: int

    """
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=False,
        documentation="[&#x27;An array of IDs of initiators to delete.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoRequest(data_model.DataObject):
    """SetSnmpTrapInfoRequest  
    You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo.

    :param trap_recipients: [required] List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 
    :type trap_recipients: SnmpTrapRecipient

    :param cluster_fault_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. 
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. 
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. 
    :type cluster_event_traps_enabled: bool

    """
    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="[&#x27;List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.&#x27;]",
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false.&#x27;]",
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false.&#x27;]",
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkRequest(data_model.DataObject):
    """RemoveVirtualNetworkRequest  
    RemoveVirtualNetwork enables you to remove a previously added virtual network.
    Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both.

    :param virtual_network_id:  Network ID that identifies the virtual network to remove. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network tag that identifies the virtual network to remove. 
    :type virtual_network_tag: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="[&#x27;Network ID that identifies the virtual network to remove.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="[&#x27;Network tag that identifies the virtual network to remove.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsResult(data_model.DataObject):
    """ListVolumeStatsResult  

    :param volume_stats: [required] List of volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of volume activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigResult(data_model.DataObject):
    """SetClusterConfigResult  

    :param cluster: [required] Settings for the cluster. All new and current settings are returned. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="[&#x27;Settings for the cluster. All new and current settings are returned.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneRequest(data_model.DataObject):
    """CancelGroupCloneRequest  
    CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel
    a group clone operation, the system completes and removes the operation's associated asyncHandle.

    :param group_clone_id: [required] The cloneID for the ongoing clone process. 
    :type group_clone_id: int

    """
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="[&#x27;The cloneID for the ongoing clone process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesRequest(data_model.DataObject):
    """ListActiveVolumesRequest  
    ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in
    VolumeID order and can be returned in multiple parts (pages).

    :param start_volume_id:  Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. 
    :type start_volume_id: int

    :param limit:  Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). 
    :type limit: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;Starting VolumeID to return. If no volume exists with this&#x27;, &#x27;VolumeID, the next volume by VolumeID order is used as&#x27;, &#x27;the start of the list. To page through the list, pass the&#x27;, &#x27;VolumeID of the last volume in the previous response +&#x27;, &#x27;1.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;Maximum number of Volume Info objects to return. A value of 0&#x27;, &#x27;(zero) returns all volumes (unlimited).&#x27;]",
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleRequest(data_model.DataObject):
    """CreateScheduleRequest  
    CreateSchedule enables you to schedule an automatic snapshot of a volume at a defined interval.
    You can use the created snapshot later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for
    the point in time in which the snapshot was created.
    If you schedule a snapshot to run at a time period that is not divisible by 5 minutes, the snapshot runs at the next time period
    that is divisible by 5 minutes. For example, if you schedule a snapshot to run at 12:42:00 UTC, it runs at 12:45:00 UTC.
    Note: You can create snapshots if cluster fullness is at stage 1, 2 or 3. You cannot create snapshots after cluster fullness reaches stage 4 or 5.

    :param schedule: [required] The "Schedule" object will be used to create a new schedule. Do not set ScheduleID property, it will be ignored. Frequency property must be of type that inherits from Frequency. Valid types are: DaysOfMonthFrequency DaysOrWeekFrequency TimeIntervalFrequency 
    :type schedule: Schedule

    """
    schedule = data_model.property(
        "schedule", Schedule,
        array=False, optional=False,
        documentation="[&#x27;The &quot;Schedule&quot; object will be used to create a new schedule.&#x27;, &#x27;Do not set ScheduleID property, it will be ignored.&#x27;, &#x27;Frequency property must be of type that inherits from Frequency. Valid types are:&#x27;, &#x27;DaysOfMonthFrequency&#x27;, &#x27;DaysOrWeekFrequency&#x27;, &#x27;TimeIntervalFrequency&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteAllSupportBundlesResult(data_model.DataObject):
    """DeleteAllSupportBundlesResult  

    :param duration: [required]  
    :type duration: str

    :param details: [required]  
    :type details: dict

    :param result: [required]  
    :type result: str

    """
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveHardwareInfoRequest(data_model.DataObject):
    """GetDriveHardwareInfoRequest  
    GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and
    other associated hardware identification information.

    :param drive_id: [required] DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. 
    :type drive_id: int

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StorageContainer(data_model.DataObject):
    """StorageContainer  

    :param name: [required]  
    :type name: str

    :param storage_container_id: [required]  
    :type storage_container_id: UUID

    :param account_id: [required]  
    :type account_id: int

    :param protocol_endpoint_type: [required]  
    :type protocol_endpoint_type: str

    :param initiator_secret: [required]  
    :type initiator_secret: str

    :param target_secret: [required]  
    :type target_secret: str

    :param status: [required]  
    :type status: str

    :param virtual_volumes:   
    :type virtual_volumes: UUID

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volumes = data_model.property(
        "virtualVolumes", UUID,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerResult(data_model.DataObject):
    """ModifyStorageContainerResult  

    :param storage_container: [required]  
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class InvokeSFApiRequest(data_model.DataObject):
    """InvokeSFApiRequest  
    This will invoke any API method supported by the SolidFire API for the version and port the connection is using.
    Returns a nested hashtable of key/value pairs that contain the result of the invoked method.

    :param method: [required] The name of the method to invoke. This is case sensitive. 
    :type method: str

    :param parameters:  An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. 
    :type parameters: str

    """
    method = data_model.property(
        "method", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the method to invoke. This is case sensitive.&#x27;]",
        dictionaryType=None
    )
    parameters = data_model.property(
        "parameters", str,
        array=False, optional=True,
        documentation="[&#x27;An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesResult(data_model.DataObject):
    """RemoveNodesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountResult(data_model.DataObject):
    """RemoveAccountResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeCountResult(data_model.DataObject):
    """GetVolumeCountResult  

    :param count: [required] The number of volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="[&#x27;The number of volumes currently in the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetStorageContainerEfficiencyRequest(data_model.DataObject):
    """GetStorageContainerEfficiencyRequest  
    GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.

    :param storage_container_id: [required] The ID of the storage container for which to retrieve efficiency information. 
    :type storage_container_id: UUID

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The ID of the storage container for which to retrieve efficiency information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Initiator(data_model.DataObject):
    """Initiator  
    Object containing characteristics of each initiator

    :param alias: [required] The friendly name assigned to this initiator. (String) 
    :type alias: str

    :param initiator_id: [required] The numeric ID of the initiator that has been created. (Integer) 
    :type initiator_id: int

    :param initiator_name: [required] The name of the initiator that has been created. (String) 
    :type initiator_name: str

    :param volume_access_groups: [required] A list of volumeAccessGroupIDs to which this initiator beintegers. (Array of Integers) 
    :type volume_access_groups: int

    :param attributes: [required] A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    alias = data_model.property(
        "alias", str,
        array=False, optional=False,
        documentation="[&#x27;The friendly name assigned to this initiator. (String)&#x27;]",
        dictionaryType=None
    )
    initiator_id = data_model.property(
        "initiatorID", int,
        array=False, optional=False,
        documentation="[&#x27;The numeric ID of the initiator that has been created. (Integer)&#x27;]",
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the initiator that has been created. (String)&#x27;]",
        dictionaryType=None
    )
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=False,
        documentation="[&#x27;A list of volumeAccessGroupIDs to which this initiator beintegers. (Array of Integers)&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;A set of JSON attributes assigned to this initiator. (JSON Object)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ISCSISession(data_model.DataObject):
    """ISCSISession  

    :param drive_ids:   
    :type drive_ids: int

    :param account_id: [required]  
    :type account_id: int

    :param initiator:   
    :type initiator: Initiator

    :param account_name: [required]  
    :type account_name: str

    :param drive_id: [required]  
    :type drive_id: int

    :param initiator_ip: [required]  
    :type initiator_ip: str

    :param initiator_port_name: [required]  
    :type initiator_port_name: str

    :param target_port_name: [required]  
    :type target_port_name: str

    :param initiator_name: [required]  
    :type initiator_name: str

    :param node_id: [required]  
    :type node_id: int

    :param service_id: [required]  
    :type service_id: int

    :param session_id: [required]  
    :type session_id: int

    :param target_name: [required]  
    :type target_name: str

    :param target_ip: [required]  
    :type target_ip: str

    :param virtual_network_id: [required]  
    :type virtual_network_id: int

    :param volume_id: [required]  
    :type volume_id: int

    :param create_time: [required]  
    :type create_time: str

    :param volume_instance: [required]  
    :type volume_instance: int

    :param initiator_session_id: [required]  
    :type initiator_session_id: int

    """
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator = data_model.property(
        "initiator", Initiator,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    account_name = data_model.property(
        "accountName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_ip = data_model.property(
        "initiatorIP", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_port_name = data_model.property(
        "initiatorPortName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    target_port_name = data_model.property(
        "targetPortName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_name = data_model.property(
        "initiatorName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    session_id = data_model.property(
        "sessionID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    target_name = data_model.property(
        "targetName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    target_ip = data_model.property(
        "targetIP", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_instance = data_model.property(
        "volumeInstance", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_session_id = data_model.property(
        "initiatorSessionID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListISCSISessionsResult(data_model.DataObject):
    """ListISCSISessionsResult  

    :param sessions: [required]  
    :type sessions: ISCSISession

    """
    sessions = data_model.property(
        "sessions", ISCSISession,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesRequest(data_model.DataObject):
    """ListVirtualVolumesRequest  
    ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes,
    or only list a subset.

    :param details:  Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. 
    :type details: bool

    :param limit:  The maximum number of virtual volumes to list. 
    :type limit: int

    :param recursive:  Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. 
    :type recursive: bool

    :param start_virtual_volume_id:  The ID of the virtual volume at which to begin the list. 
    :type start_virtual_volume_id: UUID

    :param virtual_volume_ids:  A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    details = data_model.property(
        "details", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies the level of detail about each virtual volume that is returned. Possible values are:&#x27;, &#x27;true: Include more details about each virtual volume in the response.&#x27;, &#x27;false: Include the standard level of detail about each virtual volume in&#x27;, &#x27;the response.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of virtual volumes to list.&#x27;]",
        dictionaryType=None
    )
    recursive = data_model.property(
        "recursive", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies whether to include information about the children of each virtual volume in the response.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true: Include information about the children of each virtual volume in&#x27;, &#x27;the response.&#x27;, &#x27;false: Do not include information about the children of each&#x27;, &#x27;virtual volume in the response.&#x27;]",
        dictionaryType=None
    )
    start_virtual_volume_id = data_model.property(
        "startVirtualVolumeID", UUID,
        array=False, optional=True,
        documentation="[&#x27;The ID of the virtual volume at which to begin the list.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of virtual volume IDs for which to retrieve information. If&#x27;, &#x27;you specify this parameter, the method returns information&#x27;, &#x27;about only these virtual volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingResult(data_model.DataObject):
    """CompleteVolumePairingResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDeletedVolumesRequest(data_model.DataObject):
    """ListDeletedVolumesRequest  
    ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system.

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersResult(data_model.DataObject):
    """ListStorageContainersResult  

    :param storage_containers: [required]  
    :type storage_containers: StorageContainer

    """
    storage_containers = data_model.property(
        "storageContainers", StorageContainer,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLdapConfigurationResult(data_model.DataObject):
    """GetLdapConfigurationResult  

    :param ldap_configuration: [required] List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.  Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of "authType", and "groupSearchType" which are set to "SearchAndBind" and "ActiveDirectory" respectively. 
    :type ldap_configuration: LdapConfiguration

    """
    ldap_configuration = data_model.property(
        "ldapConfiguration", LdapConfiguration,
        array=False, optional=False,
        documentation="[&#x27;List of the current LDAP configuration settings. This API call will not return the plain text of the search account password.&#x27;, u&#x27;&#x27;, &#x27;Note: If LDAP authentication is currently disabled, all the returned settings will be empty with the exception of &quot;authType&quot;, and &quot;groupSearchType&quot; which are set to &quot;SearchAndBind&quot; and &quot;ActiveDirectory&quot; respectively.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupSnapshotMembers(data_model.DataObject):
    """GroupSnapshotMembers  
    List of checksum, volumeIDs and snapshotIDs for each member of the group.

    :param volume_id: [required] The source volume ID for the snapshot. 
    :type volume_id: int

    :param snapshot_id: [required] Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 
    :type snapshot_id: int

    :param snapshot_uuid: [required] Universal Unique ID of an existing snapshot. 
    :type snapshot_uuid: str

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    :param attributes:   
    :type attributes: dict

    :param create_time:   
    :type create_time: str

    :param enable_remote_replication:   
    :type enable_remote_replication: bool

    :param expiration_reason:   
    :type expiration_reason: str

    :param expiration_time:   
    :type expiration_time: str

    :param group_id:   
    :type group_id: int

    :param group_snapshot_uuid:   
    :type group_snapshot_uuid: UUID

    :param name:   
    :type name: str

    :param remote_status:   
    :type remote_status: str

    :param remote_statuses:   
    :type remote_statuses: dict

    :param status:   
    :type status: str

    :param total_size:   
    :type total_size: int

    :param virtual_volume_id:   
    :type virtual_volume_id: int

    :param volume_pair_uuid:   
    :type volume_pair_uuid: UUID

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The source volume ID for the snapshot.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of a snapshot from which the new snapshot is made.&#x27;, &#x27;The snapshotID passed must be a snapshot on the given volume.&#x27;]",
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", str,
        array=False, optional=False,
        documentation="[&#x27;Universal Unique ID of an existing snapshot.&#x27;]",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    remote_status = data_model.property(
        "remoteStatus", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", dict,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupSnapshot(data_model.DataObject):
    """GroupSnapshot  
    Group Snapshot object represents a point-in-time copy of a group of volumes.

    :param group_snapshot_id: [required] Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param group_snapshot_uuid: [required] UUID of the group snapshot. 
    :type group_snapshot_uuid: UUID

    :param members: [required] List of volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    :param name: [required] Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created. 
    :type name: str

    :param create_time: [required] The UTC formatted day and time on which the snapshot was created. 
    :type create_time: str

    :param status: [required] Status of the snapshot. Possible values: Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable 
    :type status: str

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of the new group snapshot.&#x27;]",
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;UUID of the group snapshot.&#x27;]",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="[&#x27;List of volumeIDs and snapshotIDs for each member of the group.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the group snapshot, or, if none was given, the UTC formatted day and time on which the snapshot was created.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[&#x27;The UTC formatted day and time on which the snapshot was created.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the snapshot.&#x27;, &#x27;Possible values:&#x27;, &#x27;Preparing: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;Done: A snapshot that has finished being prepared and is now usable&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyGroupSnapshotResult(data_model.DataObject):
    """ModifyGroupSnapshotResult  

    :param group_snapshot: [required]  
    :type group_snapshot: GroupSnapshot

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveStatsRequest(data_model.DataObject):
    """ListDriveStatsRequest  
    ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives.

    :param drives:  Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=True,
        documentation="[&#x27;Optional list of DriveIDs for which to return drive&#x27;, &#x27;statistics. If you omit this parameter, measurements for&#x27;, &#x27;all drives are returned.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsRequest(data_model.DataObject):
    """ListInitiatorsRequest  
    ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs).

    :param start_initiator_id:  The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. 
    :type start_initiator_id: int

    :param limit:  The maximum number of initiator objects to return. 
    :type limit: int

    :param initiators:  A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. 
    :type initiators: int

    """
    start_initiator_id = data_model.property(
        "startInitiatorID", int,
        array=False, optional=True,
        documentation="[&#x27;The initiator ID at which to begin the listing. You can supply this&#x27;, &#x27;parameter or the &quot;initiators&quot; parameter, but not both.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of initiator objects to return.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", int,
        array=True, optional=True,
        documentation="[&#x27;A list of initiator IDs to retrieve. You can provide a value for this parameter or&#x27;, &#x27;the &quot;startInitiatorID&quot; parameter, but not both.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListInitiatorsResult(data_model.DataObject):
    """ListInitiatorsResult  

    :param initiators: [required] List of the initiator information. 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="[&#x27;List of the initiator information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddressBlock(data_model.DataObject):
    """AddressBlock  
    Unique Range of IP addresses to include in the virtual network.

    :param start: [required] Start of the IP address range. 
    :type start: str

    :param size: [required] Number of IP addresses to include in the block. 
    :type size: int

    :param available: [required] Nuber of available blocks 
    :type available: str

    """
    start = data_model.property(
        "start", str,
        array=False, optional=False,
        documentation="[&#x27;Start of the IP address range.&#x27;]",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="[&#x27;Number of IP addresses to include in the block.&#x27;]",
        dictionaryType=None
    )
    available = data_model.property(
        "available", str,
        array=False, optional=False,
        documentation="[&#x27;Nuber of available blocks&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualNetwork(data_model.DataObject):
    """VirtualNetwork  

    :param virtual_network_id: [required] SolidFire unique identifier for a virtual network. 
    :type virtual_network_id: int

    :param virtual_network_tag: [required] VLAN Tag identifier. 
    :type virtual_network_tag: int

    :param address_blocks: [required] Range of address blocks currently assigned to the virtual network. available: Binary string in "1"s and "0"s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks. size: the size of this block of addresses. start: first IP address in the block. 
    :type address_blocks: AddressBlock

    :param name: [required] The name assigned to the virtual network. 
    :type name: str

    :param netmask: [required] IP address of the netmask for the virtual network. 
    :type netmask: str

    :param svip: [required] Storage IP address for the virtual network. 
    :type svip: str

    :param gateway:   
    :type gateway: str

    :param namespace:   
    :type namespace: bool

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=False,
        documentation="[&#x27;SolidFire unique identifier for a virtual network.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="[&#x27;VLAN Tag identifier.&#x27;]",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="[&#x27;Range of address blocks currently assigned to the virtual network.&#x27;, &#x27;available: Binary string in &quot;1&quot;s and &quot;0&quot;s. 1 equals the IP is available and 0 equals the IP is not available. The string is read from right to left with the digit to the far right being the first IP address in the list of addressBlocks.&#x27;, &#x27;size: the size of this block of addresses.&#x27;, &#x27;start: first IP address in the block.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name assigned to the virtual network.&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="[&#x27;IP address of the netmask for the virtual network.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Storage IP address for the virtual network.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksResult(data_model.DataObject):
    """ListVirtualNetworksResult  

    :param virtual_networks: [required] Object containing virtual network IP addresses. 
    :type virtual_networks: VirtualNetwork

    """
    virtual_networks = data_model.property(
        "virtualNetworks", VirtualNetwork,
        array=True, optional=False,
        documentation="[&#x27;Object containing virtual network IP addresses.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartVolumePairingRequest(data_model.DataObject):
    """StartVolumePairingRequest  
    StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this
    method creates is used in the CompleteVolumePairing API method to establish a volume pairing.

    :param volume_id: [required] The ID of the volume on which to start the pairing process. 
    :type volume_id: int

    :param mode:  The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 
    :type mode: str

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume on which to start the pairing process.&#x27;]",
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="[&#x27;The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableSnmpResult(data_model.DataObject):
    """DisableSnmpResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class QoS(data_model.DataObject):
    """QoS  
    Quality of Service (QoS) values are used on SolidFire volumes to provision performance expectations.
    Minimum, maximum and burst QoS values can be set within the ranges specified in the QoS table below.
    
    Volumes created without specified QoS values are created with the Default values listed below.
    Default values can be found by running the GetDefaultQoS method.
    
    minIOPS Min: 100/50 (v7.0/v8.0), Default: 100, Max: 15,000
    maxIOPS Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000
    burstIOPS Min: 100/50 (v7.0/v8.0), Default: 15,000, Max: 100,000

    :param min_iops:  Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. 
    :type min_iops: int

    :param max_iops:  Desired maximum 4KB IOPS allowed over an extended period of time. 
    :type max_iops: int

    :param burst_iops:  Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 
    :type burst_iops: int

    :param burst_time:  The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 
    :type burst_time: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Desired minimum 4KB IOPS to guarantee.&#x27;, &#x27;The allowed IOPS will only drop below this level if all volumes have been capped&#x27;, &#x27;at their minimum IOPS value and there is still insufficient performance capacity.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Desired maximum 4KB IOPS allowed over an extended period of time.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;Maximum &quot;peak&quot; 4KB IOPS allowed for short periods of time.&#x27;, &#x27;Allows for bursts of I/O activity over the normal max IOPS value.&#x27;]",
        dictionaryType=None
    )
    burst_time = data_model.property(
        "burstTime", int,
        array=False, optional=True,
        documentation="[&#x27;The length of time burst IOPS is allowed.&#x27;, &#x27;The value returned is represented in time units of seconds.&#x27;, &#x27;Note: this value is calculated by the system based on IOPS set for QoS.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NetworkConfig(data_model.DataObject):
    """NetworkConfig  

    :param _default:   
    :type _default: bool

    :param bond_master:   
    :type bond_master: str

    :param virtual_network_tag:   
    :type virtual_network_tag: str

    :param address:   
    :type address: str

    :param auto:   
    :type auto: bool

    :param bond_downdelay:   
    :type bond_downdelay: str

    :param bond_fail_over_mac:   
    :type bond_fail_over_mac: str

    :param bond_primary_reselect:   
    :type bond_primary_reselect: str

    :param bond_lacp_rate:   
    :type bond_lacp_rate: str

    :param bond_miimon:   
    :type bond_miimon: str

    :param bond_mode:   
    :type bond_mode: str

    :param bond_slaves:   
    :type bond_slaves: str

    :param bond_updelay:   
    :type bond_updelay: str

    :param dns_nameservers:   
    :type dns_nameservers: str

    :param dns_search:   
    :type dns_search: str

    :param family:   
    :type family: str

    :param gateway:   
    :type gateway: str

    :param mac_address:   
    :type mac_address: str

    :param mac_address_permanent:   
    :type mac_address_permanent: str

    :param method:   
    :type method: str

    :param mtu:   
    :type mtu: str

    :param netmask:   
    :type netmask: str

    :param network:   
    :type network: str

    :param physical:   
    :type physical: PhysicalAdapter

    :param routes:   
    :type routes: dict

    :param status:   
    :type status: str

    :param symmetric_route_rules:   
    :type symmetric_route_rules: str

    :param up_and_running:   
    :type up_and_running: bool

    :param bond_xmit_hash_policy:   
    :type bond_xmit_hash_policy: str

    :param bond_ad_num_ports:   
    :type bond_ad_num_ports: str

    """
    _default = data_model.property(
        "#default", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_master = data_model.property(
        "bond-master", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    address = data_model.property(
        "address", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    auto = data_model.property(
        "auto", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_downdelay = data_model.property(
        "bond-downdelay", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_fail_over_mac = data_model.property(
        "bond-fail_over_mac", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_primary_reselect = data_model.property(
        "bond-primary_reselect", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_lacp_rate = data_model.property(
        "bond-lacp_rate", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_miimon = data_model.property(
        "bond-miimon", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_mode = data_model.property(
        "bond-mode", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_slaves = data_model.property(
        "bond-slaves", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_updelay = data_model.property(
        "bond-updelay", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dns_nameservers = data_model.property(
        "dns-nameservers", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dns_search = data_model.property(
        "dns-search", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    family = data_model.property(
        "family", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address = data_model.property(
        "macAddress", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mac_address_permanent = data_model.property(
        "macAddressPermanent", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    method = data_model.property(
        "method", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mtu = data_model.property(
        "mtu", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    physical = data_model.property(
        "physical", PhysicalAdapter,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    routes = data_model.property(
        "routes", dict,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    symmetric_route_rules = data_model.property(
        "symmetricRouteRules", str,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    up_and_running = data_model.property(
        "upAndRunning", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_xmit_hash_policy = data_model.property(
        "bond-xmit_hash_policy", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond_ad_num_ports = data_model.property(
        "bond-ad_num_ports", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Network(data_model.DataObject):
    """Network  

    :param bond10_g:   
    :type bond10_g: NetworkConfig

    :param bond1_g:   
    :type bond1_g: NetworkConfig

    :param eth0:   
    :type eth0: NetworkConfig

    :param eth1:   
    :type eth1: NetworkConfig

    :param eth2:   
    :type eth2: NetworkConfig

    :param eth3:   
    :type eth3: NetworkConfig

    :param lo:   
    :type lo: NetworkConfig

    """
    bond10_g = data_model.property(
        "Bond10G", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bond1_g = data_model.property(
        "Bond1G", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth0 = data_model.property(
        "eth0", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth1 = data_model.property(
        "eth1", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth2 = data_model.property(
        "eth2", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    eth3 = data_model.property(
        "eth3", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lo = data_model.property(
        "lo", NetworkConfig,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigResult(data_model.DataObject):
    """SetNetworkConfigResult  

    :param network: [required]  
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkRequest(data_model.DataObject):
    """AddVirtualNetworkRequest  
    You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network,
    an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you
    specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk
    provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual
    network addresses to nodes manually.
    Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an
    existing virtual network, use ModifyVirtualNetwork.
    Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false.

    :param virtual_network_tag: [required] A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. 
    :type virtual_network_tag: int

    :param name: [required] A user-defined name for the new virtual network. 
    :type name: str

    :param address_blocks: [required] Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlock

    :param netmask: [required] Unique network mask for the virtual network being created. 
    :type netmask: str

    :param svip: [required] Unique storage IP address for the virtual network being created. 
    :type svip: str

    :param gateway:  The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 
    :type gateway: str

    :param namespace:  When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it. 
    :type namespace: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=False,
        documentation="[&#x27;A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;A user-defined name for the new virtual network.&#x27;]",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=False,
        documentation="[&#x27;Unique range of IP addresses to include in the virtual network.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;start: The start of the IP address range. (String)&#x27;, &#x27;size: The number of IP addresses to include in the block. (Integer)&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=False,
        documentation="[&#x27;Unique network mask for the virtual network being created.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Unique storage IP address for the virtual network being created.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[&#x27;The IP address of a gateway of the virtual network. This parameter is only valid if the &quot;namespace&quot; parameter is set to true.&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[&#x27;When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsRequest(data_model.DataObject):
    """ListClusterFaultsRequest  
    ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds.

    :param best_practices:  Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false 
    :type best_practices: bool

    :param fault_types:  Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. 
    :type fault_types: str

    """
    best_practices = data_model.property(
        "bestPractices", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies whether to include faults triggered by suboptimal system configuration.&#x27;, &#x27;Possible values are:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]",
        dictionaryType=None
    )
    fault_types = data_model.property(
        "faultTypes", str,
        array=False, optional=True,
        documentation="[&#x27;Determines the types of faults returned. Possible values are:&#x27;, &#x27;current: List active, unresolved faults.&#x27;, &#x27;resolved: List faults that were previously detected and&#x27;, &#x27;resolved.&#x27;, &#x27;all: (Default) List both current and resolved faults. You can&#x27;, &#x27;see the fault status in the resolved field of the Cluster Fault&#x27;, &#x27;object.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestPingResult(data_model.DataObject):
    """TestPingResult  

    :param result: [required] Result of the ping test. 
    :type result: str

    :param duration: [required] The total duration of the ping test. 
    :type duration: str

    :param details: [required] List of each IP the node was able to communicate with. 
    :type details: dict

    """
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;Result of the ping test.&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The total duration of the ping test.&#x27;]",
        dictionaryType=None
    )
    details = data_model.property(
        "details", dict,
        array=False, optional=False,
        documentation="[&#x27;List of each IP the node was able to communicate with.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class BackupTarget(data_model.DataObject):
    """BackupTarget  
    The object containing information about a backup target.

    :param name: [required] Name for the backup target. 
    :type name: str

    :param backup_target_id: [required] Unique identifier assigned to the backup target. 
    :type backup_target_id: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name for the backup target.&#x27;]",
        dictionaryType=None
    )
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetResult(data_model.DataObject):
    """GetBackupTargetResult  

    :param backup_target: [required] Object returned for backup target. 
    :type backup_target: BackupTarget

    """
    backup_target = data_model.property(
        "backupTarget", BackupTarget,
        array=False, optional=False,
        documentation="[&#x27;Object returned for backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesResult(data_model.DataObject):
    """AddDrivesResult  

    :param async_handle:   
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeRequest(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeRequest  
    ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume.

    :param virtual_volume_ids:  A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 
    :type virtual_volume_ids: UUID

    """
    virtual_volume_ids = data_model.property(
        "virtualVolumeIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigResult(data_model.DataObject):
    """SetConfigResult  

    :param config: [required] The new and current configuration for the node. 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="[&#x27;The new and current configuration for the node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeWriteRequest(data_model.DataObject):
    """StartBulkVolumeWriteRequest  
    StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server
    interaction information for external data access is passed by a script running on the storage system.

    :param volume_id: [required] The ID of the volume to be written to. 
    :type volume_id: int

    :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
    :type format: str

    :param script:  The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: dict

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume to be written to.&#x27;]",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="[&#x27;The format of the volume data. It can be either of the following formats:&#x27;, &#x27;uncompressed: Every byte of the volume is returned without any compression.&#x27;, &#x27;native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk&#x27;, &#x27;volume write.&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="[&#x27;The executable name of a script. If unspecified,&#x27;, &#x27;the key and URL are necessary to access SF-series&#x27;, &#x27;nodes. The script runs on the primary node and the key&#x27;, &#x27;and URL is returned to the script, so the local web server&#x27;, &#x27;can be contacted.&#x27;]",
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON parameters to pass to the script.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes for the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeResult(data_model.DataObject):
    """ModifyVolumeResult  

    :param volume:  Object containing information about the newly modified volume. 
    :type volume: Volume

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="[&#x27;Object containing information about the newly modified volume.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeResult(data_model.DataObject):
    """PurgeDeletedVolumeResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnapshotRemoteStatus(data_model.DataObject):
    """SnapshotRemoteStatus  

    :param remote_status: [required]  
    :type remote_status: str

    :param volume_pair_uuid: [required] The snapshot is done and is writable (the active branch of the slice). 
    :type volume_pair_uuid: UUID

    """
    remote_status = data_model.property(
        "remoteStatus", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_pair_uuid = data_model.property(
        "volumePairUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The snapshot is done and is writable (the active branch of the slice).&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Snapshot(data_model.DataObject):
    """Snapshot  
    Snapshots is an object containing information about each snapshot made for a volume.
    The return object includes information for the active snapshot as well as each snapshot created for the volume.

    :param snapshot_id: [required] Unique ID for this snapshot. 
    :type snapshot_id: int

    :param volume_id: [required] The volume this snapshot was taken of. 
    :type volume_id: int

    :param name: [required] A name for this snapshot. It is not necessarily unique. 
    :type name: str

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    :param enable_remote_replication: [required] Identifies if snapshot is enabled for remote replication. 
    :type enable_remote_replication: bool

    :param expiration_reason: [required] Indicates how the snapshot expiration was set. Possible values: api: expiration time was set by using the API. none: there is no expiration time set. test: expiration time was set for testing. 
    :type expiration_reason: str

    :param expiration_time:  The time at which this snapshot will expire and be purged from the cluster. 
    :type expiration_time: str

    :param remote_statuses:  Current remote status of the snapshot remoteStatus: Possible values: Present: Snapshot exists on a remote cluster Not Present: Snapshot does not exist on remote cluster Syncing: This is a target cluster and it is currently replicating the snapshot Deleted: This is a target cluster, the snapshot has been deleted, and it still exists on the source. volumePairUUID: universal identifier of the volume pair 
    :type remote_statuses: SnapshotRemoteStatus

    :param status: [required] Current status of the snapshot Preparing: A snapshot that is being prepared for use and is not yet writable. Done: A snapshot that has finished being prepared and is now usable. Active: This snapshot is the active branch. 
    :type status: str

    :param snapshot_uuid: [required] Universal Unique ID of an existing snapshot. 
    :type snapshot_uuid: UUID

    :param total_size: [required] Total size of this snapshot in bytes. It is equivalent to totalSize of the volume when this snapshot was taken. 
    :type total_size: int

    :param group_id:  If present, the ID of the group this snapshot is a part of. If not present, this snapshot is not part of a group. 
    :type group_id: int

    :param group_snapshot_uuid: [required] The current "members" results contains information about each snapshot in the group. Each of these members will have a "uuid" parameter for the snapshot's UUID. 
    :type group_snapshot_uuid: UUID

    :param create_time: [required] The time this snapshot was taken. 
    :type create_time: str

    :param virtual_volume_id:  The ID of the virtual volume with which the snapshot is associated. 
    :type virtual_volume_id: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID for this snapshot.&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The volume this snapshot was taken of.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;A name for this snapshot.&#x27;, &#x27;It is not necessarily unique.&#x27;]",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )
    enable_remote_replication = data_model.property(
        "enableRemoteReplication", bool,
        array=False, optional=False,
        documentation="[&#x27;Identifies if snapshot is enabled for remote replication.&#x27;]",
        dictionaryType=None
    )
    expiration_reason = data_model.property(
        "expirationReason", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates how the snapshot expiration was set. Possible values:&#x27;, &#x27;api: expiration time was set by using the API.&#x27;, &#x27;none: there is no expiration time set.&#x27;, &#x27;test: expiration time was set for testing.&#x27;]",
        dictionaryType=None
    )
    expiration_time = data_model.property(
        "expirationTime", str,
        array=False, optional=True,
        documentation="[&#x27;The time at which this snapshot will expire and be purged from the cluster.&#x27;]",
        dictionaryType=None
    )
    remote_statuses = data_model.property(
        "remoteStatuses", SnapshotRemoteStatus,
        array=True, optional=True,
        documentation="[&#x27;Current remote status of the snapshot remoteStatus: Possible values:&#x27;, &#x27;Present: Snapshot exists on a remote cluster&#x27;, &#x27;Not Present: Snapshot does not exist on remote cluster&#x27;, &#x27;Syncing: This is a target cluster and it is currently replicating the snapshot&#x27;, &#x27;Deleted: This is a target cluster, the snapshot has been deleted, and it still exists on the source.&#x27;, &#x27;volumePairUUID: universal identifier of the volume pair&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Current status of the snapshot&#x27;, &#x27;Preparing: A snapshot that is being prepared for use and is not yet writable.&#x27;, &#x27;Done: A snapshot that has finished being prepared and is now usable.&#x27;, &#x27;Active: This snapshot is the active branch.&#x27;]",
        dictionaryType=None
    )
    snapshot_uuid = data_model.property(
        "snapshotUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;Universal Unique ID of an existing snapshot.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total size of this snapshot in bytes.&#x27;, &#x27;It is equivalent to totalSize of the volume when this snapshot was taken.&#x27;]",
        dictionaryType=None
    )
    group_id = data_model.property(
        "groupID", int,
        array=False, optional=True,
        documentation="[&#x27;If present, the ID of the group this snapshot is a part of.&#x27;, &#x27;If not present, this snapshot is not part of a group.&#x27;]",
        dictionaryType=None
    )
    group_snapshot_uuid = data_model.property(
        "groupSnapshotUUID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The current &quot;members&quot; results contains information about each snapshot in the group.&#x27;, &#x27;Each of these members will have a &quot;uuid&quot; parameter for the snapshot\&#x27;s UUID.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[&#x27;The time this snapshot was taken.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=True,
        documentation="[&#x27;The ID of the virtual volume with which the snapshot is associated.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeInfo(data_model.DataObject):
    """VirtualVolumeInfo  

    :param virtual_volume_id: [required]  
    :type virtual_volume_id: UUID

    :param parent_virtual_volume_id: [required]  
    :type parent_virtual_volume_id: UUID

    :param storage_container: [required]  
    :type storage_container: StorageContainer

    :param volume_id: [required]  
    :type volume_id: int

    :param snapshot_id: [required]  
    :type snapshot_id: int

    :param virtual_volume_type: [required]  
    :type virtual_volume_type: str

    :param status: [required]  
    :type status: str

    :param bindings: [required]  
    :type bindings: int

    :param children: [required]  
    :type children: UUID

    :param metadata: [required]  
    :type metadata: dict

    :param snapshot_info:   
    :type snapshot_info: Snapshot

    :param volume_info:   
    :type volume_info: Volume

    :param descendants:   
    :type descendants: int

    """
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    parent_virtual_volume_id = data_model.property(
        "parentVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volume_type = data_model.property(
        "virtualVolumeType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bindings = data_model.property(
        "bindings", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    children = data_model.property(
        "children", UUID,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    metadata = data_model.property(
        "metadata", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_info = data_model.property(
        "snapshotInfo", Snapshot,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_info = data_model.property(
        "volumeInfo", Volume,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    descendants = data_model.property(
        "descendants", int,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumesResult(data_model.DataObject):
    """ListVirtualVolumesResult  

    :param virtual_volumes: [required]  
    :type virtual_volumes: VirtualVolumeInfo

    :param next_virtual_volume_id:   
    :type next_virtual_volume_id: UUID

    """
    virtual_volumes = data_model.property(
        "virtualVolumes", VirtualVolumeInfo,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    next_virtual_volume_id = data_model.property(
        "nextVirtualVolumeID", UUID,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumesResult(data_model.DataObject):
    """DeleteVolumesResult  

    :param volumes: [required] Information about the newly deleted volume. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;Information about the newly deleted volume.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterCapacity(data_model.DataObject):
    """ClusterCapacity  
    High level capacity measurements for the entire cluster.

    :param active_block_space: [required] The amount of space on the block drives. This includes additional information such as metadata entries and space which can be cleaned up. 
    :type active_block_space: int

    :param active_sessions: [required] Number of active iSCSI sessions communicating with the cluster 
    :type active_sessions: int

    :param average_iops: [required] Average IPS for the cluster since midnight Coordinated Universal Time (UTC). 
    :type average_iops: int

    :param cluster_recent_iosize: [required] The average size of IOPS to all volumes in the cluster. 
    :type cluster_recent_iosize: int

    :param current_iops: [required] Average IOPS for all volumes in the cluster over the last 5 seconds. 
    :type current_iops: int

    :param max_iops: [required] Estimated maximum IOPS capability of the current cluster. 
    :type max_iops: int

    :param max_over_provisionable_space: [required] The maximum amount of provisionable space. This is a computed value. You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number: maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull 
    :type max_over_provisionable_space: int

    :param max_provisioned_space: [required] The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata). 
    :type max_provisioned_space: int

    :param max_used_metadata_space: [required] The amount of bytes on volume drives used to store metadata. 
    :type max_used_metadata_space: int

    :param max_used_space: [required] The total amount of space on all active block drives. 
    :type max_used_space: int

    :param non_zero_blocks: [required] Total number of 4KiB blocks with data after the last garbage collection operation has completed. 
    :type non_zero_blocks: int

    :param peak_active_sessions: [required] Peak number of iSCSI connections since midnight UTC. 
    :type peak_active_sessions: int

    :param peak_iops: [required] The highest value for currentIOPS since midnight UTC. 
    :type peak_iops: int

    :param provisioned_space: [required] Total amount of space provisioned in all volumes on the cluster. 
    :type provisioned_space: int

    :param snapshot_non_zero_blocks: [required] Total number of 4KiB blocks in snapshots with data. 
    :type snapshot_non_zero_blocks: int

    :param timestamp: [required] The date and time this cluster capacity sample was taken. 
    :type timestamp: str

    :param total_ops: [required] The total number of I/O operations performed throughout the lifetime of the cluster 
    :type total_ops: int

    :param unique_blocks: [required] The total number of blocks stored on the block drives. The value includes replicated blocks. 
    :type unique_blocks: int

    :param unique_blocks_used_space: [required] The total amount of data the uniqueBlocks take up on the block drives. This number is always consistent with the uniqueBlocks value. 
    :type unique_blocks_used_space: int

    :param used_metadata_space: [required] The total amount of bytes on volume drives used to store metadata 
    :type used_metadata_space: int

    :param used_metadata_space_in_snapshots: [required] The amount of bytes on volume drives used for storing unique data in snapshots. This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system. 
    :type used_metadata_space_in_snapshots: int

    :param used_space: [required] Total amount of space used by all block drives in the system. 
    :type used_space: int

    :param zero_blocks: [required] Total number of 4KiB blocks without data after the last round of garabage collection operation has completed. 
    :type zero_blocks: int

    """
    active_block_space = data_model.property(
        "activeBlockSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of space on the block drives.&#x27;, &#x27;This includes additional information such as metadata entries and space which can be cleaned up.&#x27;]",
        dictionaryType=None
    )
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=False,
        documentation="[&#x27;Number of active iSCSI sessions communicating with the cluster&#x27;]",
        dictionaryType=None
    )
    average_iops = data_model.property(
        "averageIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Average IPS for the cluster since midnight Coordinated Universal Time (UTC).&#x27;]",
        dictionaryType=None
    )
    cluster_recent_iosize = data_model.property(
        "clusterRecentIOSize", int,
        array=False, optional=False,
        documentation="[&#x27;The average size of IOPS to all volumes in the cluster.&#x27;]",
        dictionaryType=None
    )
    current_iops = data_model.property(
        "currentIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Average IOPS for all volumes in the cluster over the last 5 seconds.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;Estimated maximum IOPS capability of the current cluster.&#x27;]",
        dictionaryType=None
    )
    max_over_provisionable_space = data_model.property(
        "maxOverProvisionableSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The maximum amount of provisionable space.&#x27;, &#x27;This is a computed value.&#x27;, &#x27;You cannot create new volumes if the current provisioned space plus the new volume size would exceed this number:&#x27;, &#x27;maxOverProvisionableSpace = maxProvisionedSpace * GetClusterFull&#x27;]",
        dictionaryType=None
    )
    max_provisioned_space = data_model.property(
        "maxProvisionedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The total amount of provisionable space if all volumes are 100% filled (no thin provisioned metadata).&#x27;]",
        dictionaryType=None
    )
    max_used_metadata_space = data_model.property(
        "maxUsedMetadataSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of bytes on volume drives used to store metadata.&#x27;]",
        dictionaryType=None
    )
    max_used_space = data_model.property(
        "maxUsedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The total amount of space on all active block drives.&#x27;]",
        dictionaryType=None
    )
    non_zero_blocks = data_model.property(
        "nonZeroBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;Total number of 4KiB blocks with data after the last garbage collection operation has completed.&#x27;]",
        dictionaryType=None
    )
    peak_active_sessions = data_model.property(
        "peakActiveSessions", int,
        array=False, optional=False,
        documentation="[&#x27;Peak number of iSCSI connections since midnight UTC.&#x27;]",
        dictionaryType=None
    )
    peak_iops = data_model.property(
        "peakIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;The highest value for currentIOPS since midnight UTC.&#x27;]",
        dictionaryType=None
    )
    provisioned_space = data_model.property(
        "provisionedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;Total amount of space provisioned in all volumes on the cluster.&#x27;]",
        dictionaryType=None
    )
    snapshot_non_zero_blocks = data_model.property(
        "snapshotNonZeroBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;Total number of 4KiB blocks in snapshots with data.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;The date and time this cluster capacity sample was taken.&#x27;]",
        dictionaryType=None
    )
    total_ops = data_model.property(
        "totalOps", int,
        array=False, optional=False,
        documentation="[&#x27;The total number of I/O operations performed throughout the lifetime of the cluster&#x27;]",
        dictionaryType=None
    )
    unique_blocks = data_model.property(
        "uniqueBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;The total number of blocks stored on the block drives.&#x27;, &#x27;The value includes replicated blocks.&#x27;]",
        dictionaryType=None
    )
    unique_blocks_used_space = data_model.property(
        "uniqueBlocksUsedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The total amount of data the uniqueBlocks take up on the block drives.&#x27;, &#x27;This number is always consistent with the uniqueBlocks value.&#x27;]",
        dictionaryType=None
    )
    used_metadata_space = data_model.property(
        "usedMetadataSpace", int,
        array=False, optional=False,
        documentation="[&#x27;The total amount of bytes on volume drives used to store metadata&#x27;]",
        dictionaryType=None
    )
    used_metadata_space_in_snapshots = data_model.property(
        "usedMetadataSpaceInSnapshots", int,
        array=False, optional=False,
        documentation="[&#x27;The amount of bytes on volume drives used for storing unique data in snapshots.&#x27;, &#x27;This number provides an estimate of how much metadata space would be regained by deleting all snapshots on the system.&#x27;]",
        dictionaryType=None
    )
    used_space = data_model.property(
        "usedSpace", int,
        array=False, optional=False,
        documentation="[&#x27;Total amount of space used by all block drives in the system.&#x27;]",
        dictionaryType=None
    )
    zero_blocks = data_model.property(
        "zeroBlocks", int,
        array=False, optional=False,
        documentation="[&#x27;Total number of 4KiB blocks without data after the last round of garabage collection operation has completed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterCapacityResult(data_model.DataObject):
    """GetClusterCapacityResult  

    :param cluster_capacity: [required]  
    :type cluster_capacity: ClusterCapacity

    """
    cluster_capacity = data_model.property(
        "clusterCapacity", ClusterCapacity,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareConfigResult(data_model.DataObject):
    """GetHardwareConfigResult  

    :param hardware_config: [required] List of hardware information and current settings. 
    :type hardware_config: dict

    """
    hardware_config = data_model.property(
        "hardwareConfig", dict,
        array=False, optional=False,
        documentation="[&#x27;List of hardware information and current settings.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipRequest(data_model.DataObject):
    """TestConnectSvipRequest  
    The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param svip:  If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
    :type svip: str

    """
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="[&#x27;If specified, tests the storage connection of a&#x27;, &#x27;different SVIP. You do not need to use this value when&#x27;, &#x27;testing the connection to the target cluster. This parameter is optional.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestPingRequest(data_model.DataObject):
    """TestPingRequest  
    You can use the TestPing API method to validate the
    connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param attempts:  Specifies the number of times the system should repeat the test ping. The default value is 5. 
    :type attempts: int

    :param hosts:  Specifies a comma-separated list of addresses or hostnames of devices to ping. 
    :type hosts: str

    :param total_timeout_sec:  Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 
    :type total_timeout_sec: int

    :param packet_size:  Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. 
    :type packet_size: int

    :param ping_timeout_msec:  Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. 
    :type ping_timeout_msec: int

    :param prohibit_fragmentation:  Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. 
    :type prohibit_fragmentation: bool

    """
    attempts = data_model.property(
        "attempts", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the number of times the system&#x27;, &#x27;should repeat the test ping. The default value is 5.&#x27;]",
        dictionaryType=None
    )
    hosts = data_model.property(
        "hosts", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies a comma-separated list of addresses or hostnames of devices to ping.&#x27;]",
        dictionaryType=None
    )
    total_timeout_sec = data_model.property(
        "totalTimeoutSec", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process.&#x27;]",
        dictionaryType=None
    )
    packet_size = data_model.property(
        "packetSize", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration.&#x27;]",
        dictionaryType=None
    )
    ping_timeout_msec = data_model.property(
        "pingTimeoutMsec", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms.&#x27;]",
        dictionaryType=None
    )
    prohibit_fragmentation = data_model.property(
        "prohibitFragmentation", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsInfo(data_model.DataObject):
    """NodeStatsInfo  

    :param c_bytes_in: [required] Bytes in on the cluster interface. 
    :type c_bytes_in: int

    :param c_bytes_out: [required] Bytes out on the cluster interface. 
    :type c_bytes_out: int

    :param cpu: [required] CPU Usage % 
    :type cpu: int

    :param m_bytes_in: [required] Bytes in on the management interface. 
    :type m_bytes_in: int

    :param m_bytes_out: [required] Bytes out on the management interface. 
    :type m_bytes_out: int

    :param network_utilization_cluster: [required] Network interface utilization (in %) for the cluster network interface. 
    :type network_utilization_cluster: int

    :param network_utilization_storage: [required] Network interface utilization (in %) for the storage network interface. 
    :type network_utilization_storage: int

    :param node_id: [required]  
    :type node_id: int

    :param s_bytes_in: [required] Bytes in on the storage interface. 
    :type s_bytes_in: int

    :param s_bytes_out: [required] Bytes out on the storage interface. 
    :type s_bytes_out: int

    :param timestamp: [required] Current time in UTC format ISO 8691 date string. 
    :type timestamp: str

    :param used_memory: [required] Total memory usage in bytes. 
    :type used_memory: int

    """
    c_bytes_in = data_model.property(
        "cBytesIn", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes in on the cluster interface.&#x27;]",
        dictionaryType=None
    )
    c_bytes_out = data_model.property(
        "cBytesOut", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes out on the cluster interface.&#x27;]",
        dictionaryType=None
    )
    cpu = data_model.property(
        "cpu", int,
        array=False, optional=False,
        documentation="[&#x27;CPU Usage %&#x27;]",
        dictionaryType=None
    )
    m_bytes_in = data_model.property(
        "mBytesIn", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes in on the management interface.&#x27;]",
        dictionaryType=None
    )
    m_bytes_out = data_model.property(
        "mBytesOut", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes out on the management interface.&#x27;]",
        dictionaryType=None
    )
    network_utilization_cluster = data_model.property(
        "networkUtilizationCluster", int,
        array=False, optional=False,
        documentation="[&#x27;Network interface utilization (in %) for the cluster network interface.&#x27;]",
        dictionaryType=None
    )
    network_utilization_storage = data_model.property(
        "networkUtilizationStorage", int,
        array=False, optional=False,
        documentation="[&#x27;Network interface utilization (in %) for the storage network interface.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    s_bytes_in = data_model.property(
        "sBytesIn", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes in on the storage interface.&#x27;]",
        dictionaryType=None
    )
    s_bytes_out = data_model.property(
        "sBytesOut", int,
        array=False, optional=False,
        documentation="[&#x27;Bytes out on the storage interface.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;Current time in UTC format ISO 8691 date string.&#x27;]",
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="[&#x27;Total memory usage in bytes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStatsNodes(data_model.DataObject):
    """NodeStatsNodes  

    :param nodes: [required] Node activity information for a single node. 
    :type nodes: NodeStatsInfo

    """
    nodes = data_model.property(
        "nodes", NodeStatsInfo,
        array=True, optional=False,
        documentation="[&#x27;Node activity information for a single node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeStatsResult(data_model.DataObject):
    """ListNodeStatsResult  

    :param node_stats: [required] Node activity information for all nodes. 
    :type node_stats: NodeStatsNodes

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsNodes,
        array=False, optional=False,
        documentation="[&#x27;Node activity information for all nodes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupResult(data_model.DataObject):
    """DeleteVolumeAccessGroupResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteInitiatorsResult(data_model.DataObject):
    """DeleteInitiatorsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddInitiatorsToVolumeAccessGroupRequest(data_model.DataObject):
    """AddInitiatorsToVolumeAccessGroupRequest  
    AddInitiatorsToVolumeAccessGroup enables you
    to add initiators to a specified volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to modify. 
    :type volume_access_group_id: int

    :param initiators: [required] The list of initiators to add to the volume access group. 
    :type initiators: str

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group&#x27;, &#x27;to modify.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="[&#x27;The list of initiators to add to the volume access&#x27;, &#x27;group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeAccessGroupRequest(data_model.DataObject):
    """DeleteVolumeAccessGroupRequest  
    DeleteVolumeAccessGroup enables you to delete a
    volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to be deleted. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group&#x27;, &#x27;to be deleted.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FeatureObject(data_model.DataObject):
    """FeatureObject  

    :param enabled: [required] True if the feature is enabled, otherwise false. 
    :type enabled: bool

    :param feature: [required] The name of the feature. 
    :type feature: str

    """
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;True if the feature is enabled, otherwise false.&#x27;]",
        dictionaryType=None
    )
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the feature.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetFeatureStatusResult(data_model.DataObject):
    """GetFeatureStatusResult  

    :param features: [required] An array of feature objects indicating the feature name and its status. 
    :type features: FeatureObject

    """
    features = data_model.property(
        "features", FeatureObject,
        array=True, optional=False,
        documentation="[&#x27;An array of feature objects indicating the feature name and its status.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualNetworksRequest(data_model.DataObject):
    """ListVirtualNetworksRequest  
    ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual
    network settings in the cluster.
    There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or
    VirtualNetworkTag values.

    :param virtual_network_id:  Network ID to filter the list for a single virtual network. 
    :type virtual_network_id: int

    :param virtual_network_tag:  Network tag to filter the list for a single virtual network. 
    :type virtual_network_tag: int

    :param virtual_network_ids:  Network IDs to include in the list. 
    :type virtual_network_ids: int

    :param virtual_network_tags:  Network tag to include in the list. 
    :type virtual_network_tags: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="[&#x27;Network ID to filter the list for a single virtual network.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="[&#x27;Network tag to filter the list for a single virtual network.&#x27;]",
        dictionaryType=None
    )
    virtual_network_ids = data_model.property(
        "virtualNetworkIDs", int,
        array=True, optional=True,
        documentation="[&#x27;Network IDs to include in the list.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tags = data_model.property(
        "virtualNetworkTags", int,
        array=True, optional=True,
        documentation="[&#x27;Network tag to include in the list.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSchedulesResult(data_model.DataObject):
    """ListSchedulesResult  

    :param schedules: [required] The list of schedules currently on the cluster. 
    :type schedules: Schedule

    """
    schedules = data_model.property(
        "schedules", Schedule,
        array=True, optional=False,
        documentation="[&#x27;The list of schedules currently on the cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNetworkConfigRequest(data_model.DataObject):
    """SetNetworkConfigRequest  
    The SetNetworkConfig API method enables you to set the network configuration for a node. To display the current network settings for a node, run the GetNetworkConfig API method. 
    Note: This method is available only through the per-node API endpoint 5.0 or later.
    Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.

    :param network: [required] An object containing node network settings to modify. 
    :type network: NetworkParams

    """
    network = data_model.property(
        "network", NetworkParams,
        array=False, optional=False,
        documentation="[&#x27;An object containing node network settings to modify.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeReadRequest(data_model.DataObject):
    """StartBulkVolumeReadRequest  
    StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes
    can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes
    of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node.
    Communications and server interaction information for external data access is passed by a script running on the storage system.
    At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a
    previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the
    read completes.
    Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param volume_id: [required] The ID of the volume to be read. 
    :type volume_id: int

    :param format: [required] The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 
    :type format: str

    :param snapshot_id:  The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 
    :type snapshot_id: int

    :param script:  The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 
    :type script: str

    :param script_parameters:  JSON parameters to pass to the script. 
    :type script_parameters: dict

    :param attributes:  JSON attributes for the bulk volume job. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume to be read.&#x27;]",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="[&#x27;The format of the volume data. It can be either of the following formats:&#x27;, &#x27;uncompressed: Every byte of the volume is returned without any compression.&#x27;, &#x27;native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk&#x27;, &#x27;volume write.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of a previously created snapshot used for bulk volume&#x27;, &#x27;reads. If no ID is entered, a snapshot of the current active&#x27;, &#x27;volume image is made.&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="[&#x27;The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key&#x27;, &#x27;and URL is returned to the script so the local web server&#x27;, &#x27;can be contacted.&#x27;]",
        dictionaryType=None
    )
    script_parameters = data_model.property(
        "scriptParameters", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON parameters to pass to the script.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;JSON attributes for the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddDrivesRequest(data_model.DataObject):
    """AddDrivesRequest  
    AddDrives enables you to add one or more available drives to the cluster, enabling the drives to host a portion of the cluster's data.
    When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be
    added via AddDrives before they can be utilized. Use the ListDrives method to display drives that are "available" to be added. When
    you add multiple drives, it is more efficient to add them in a single AddDrives method call rather than multiple individual methods
    with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.
    When you add a drive, the system automatically determines the "type" of drive it should be.
    The method is asynchronous and returns immediately. However, it can take some time for the data in the cluster to be rebalanced
    using the newly added drives. As the new drives are syncing on the system, you can use the ListSyncJobs method to see how the
    drives are being rebalanced and the progress of adding the new drive. You can also use the GetAsyncResult method to query the
    method's returned asyncHandle.

    :param drives: [required] Returns information about each drive to be added to the cluster. Possible values are: driveID: The ID of the drive to add. (Integer) type: (Optional) The type of drive to add. Valid values are "slice" or "block". If omitted, the system assigns the correct type. (String) 
    :type drives: NewDrive

    :param force_during_upgrade:  Allows the user to force the addition of drives during an upgrade. 
    :type force_during_upgrade: bool

    """
    drives = data_model.property(
        "drives", NewDrive,
        array=True, optional=False,
        documentation="[&#x27;Returns information about each drive to be added to the&#x27;, &#x27;cluster. Possible values are:&#x27;, &#x27;driveID: The ID of the drive to&#x27;, &#x27;add. (Integer)&#x27;, &#x27;type: (Optional) The type of drive&#x27;, &#x27;to add. Valid values are &quot;slice&quot; or &quot;block&quot;. If&#x27;, &#x27;omitted, the system assigns the correct&#x27;, &#x27;type. (String)&#x27;]",
        dictionaryType=None
    )
    force_during_upgrade = data_model.property(
        "forceDuringUpgrade", bool,
        array=False, optional=True,
        documentation="[&#x27;Allows the user to force the addition of drives during an upgrade.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteVolumeRequest(data_model.DataObject):
    """DeleteVolumeRequest  
    DeleteVolume marks an active volume for deletion. When marked, the volume is purged (permanently deleted) after the cleanup
    interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume are immediately terminated
    and no further connections are allowed while the volume is in this state. A marked volume is not returned in target discovery
    requests.
    Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from
    the system.
    If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or
    write operation is stopped.
    If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred
    to it or from it while in a deleted state. The remote volume that the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resume. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable.

    :param volume_id: [required] The ID of the volume to be deleted. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume to be deleted.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateScheduleResult(data_model.DataObject):
    """CreateScheduleResult  

    :param schedule_id: [required]  
    :type schedule_id: int

    """
    schedule_id = data_model.property(
        "scheduleID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ShutdownRequest(data_model.DataObject):
    """ShutdownRequest  
    The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method,
    log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options.

    :param nodes: [required] List of NodeIDs for the nodes to be shutdown. 
    :type nodes: int

    :param option:  Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. 
    :type option: str

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="[&#x27;List of NodeIDs for the nodes to be shutdown.&#x27;]",
        dictionaryType=None
    )
    option = data_model.property(
        "option", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the action to take for the node shutdown. Possible values are:&#x27;, &#x27;restart: Restarts the node.&#x27;, &#x27;halt: Shuts down the node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAsyncResultRequest(data_model.DataObject):
    """GetAsyncResultRequest  
    You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and
    might not be finished when the system sends the initial response. To obtain the status or result of the method call, use
    GetAsyncResult to poll the asyncHandle value returned by the method.
    GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual
    data returned for the operation depends on the original method call and the return data is documented with each method.

    :param async_handle: [required] A value that was returned from the original asynchronous method call. 
    :type async_handle: int

    :param keep_result:  If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. 
    :type keep_result: bool

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;A value that was returned from the original&#x27;, &#x27;asynchronous method call.&#x27;]",
        dictionaryType=None
    )
    keep_result = data_model.property(
        "keepResult", bool,
        array=False, optional=True,
        documentation="[&#x27;If true, GetAsyncResult does not remove the&#x27;, &#x27;asynchronous result upon returning it, enabling future&#x27;, &#x27;queries to that asyncHandle.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeResult(data_model.DataObject):
    """CreateVolumeResult  

    :param volume:   
    :type volume: Volume

    :param volume_id: [required] VolumeID for the newly created volume. 
    :type volume_id: int

    :param curve: [required] The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. 
    :type curve: dict

    """
    volume = data_model.property(
        "volume", Volume,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID for the newly created volume.&#x27;]",
        dictionaryType=None
    )
    curve = data_model.property(
        "curve", dict,
        array=False, optional=False,
        documentation="[&#x27;The curve is a set of key-value pairs.&#x27;, &#x27;The keys are I/O sizes in bytes.&#x27;, &#x27;The values represent the cost performing an IOP at a specific I/O size.&#x27;, &#x27;The curve is calculated relative to a 4096 byte operation set at 100 IOPS.&#x27;]",
        dictionaryType=int
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountRequest(data_model.DataObject):
    """ModifyAccountRequest  
    ModifyAccount enables you to modify an existing account.
    When you lock an account, any existing connections from that account are immediately terminated. When you change an account's
    CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or
    reconnections.
    To clear an account's attributes, specify {} for the attributes parameter.

    :param account_id: [required] Specifies the AccountID for the account to be modified. 
    :type account_id: int

    :param username:  Specifies the username associated with the account. (Might be 1 to 64 characters in length). 
    :type username: str

    :param status:  Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. 
    :type status: str

    :param initiator_secret:  Specifies the CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. 
    :type initiator_secret: CHAPSecret

    :param target_secret:  Specifies the CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. 
    :type target_secret: CHAPSecret

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the AccountID for the account to be modified.&#x27;]",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the username associated with the&#x27;, &#x27;account. (Might be 1 to 64 characters in length).&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=True,
        documentation="[&#x27;Sets the status for the account. Possible values are:&#x27;, &#x27;active: The account is active and connections are allowed.&#x27;, &#x27;locked: The account is locked and connections are refused.&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;Specifies the CHAP secret to use for the initiator. This secret must&#x27;, &#x27;be 12-16 characters in length and should be&#x27;, &#x27;impenetrable. The initiator CHAP secret must be unique&#x27;, &#x27;and cannot be the same as the target CHAP secret.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", CHAPSecret,
        array=False, optional=True,
        documentation="[&#x27;Specifies the CHAP secret to use for the target (mutual CHAP&#x27;, &#x27;authentication). This secret must be 12-16 characters in&#x27;, &#x27;length and should be impenetrable. The target CHAP&#x27;, &#x27;secret must be unique and cannot be the same as the&#x27;, &#x27;initiator CHAP secret.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterAdmin(data_model.DataObject):
    """ClusterAdmin  

    :param auth_method: [required]  
    :type auth_method: str

    :param access: [required]  
    :type access: str

    :param cluster_admin_id: [required]  
    :type cluster_admin_id: int

    :param username: [required]  
    :type username: str

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    auth_method = data_model.property(
        "authMethod", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetCurrentClusterAdminResult(data_model.DataObject):
    """GetCurrentClusterAdminResult  

    :param cluster_admin: [required] Information about all cluster and LDAP administrators that exist for a cluster. 
    :type cluster_admin: ClusterAdmin

    """
    cluster_admin = data_model.property(
        "clusterAdmin", ClusterAdmin,
        array=False, optional=False,
        documentation="[&#x27;Information about all cluster and LDAP administrators that exist for a cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeRequest(data_model.DataObject):
    """ResetNodeRequest  
    The ResetNode API method enables you to reset a node to the factory settings. All data, packages (software upgrades, and so on),
    configurations, and log files are deleted from the node when you call this method. However, network settings for the node are
    preserved during this operation. Nodes that are participating in a cluster cannot be reset to the factory settings.
    The ResetNode API can only be used on nodes that are in an "Available" state. It cannot be used on nodes that are "Active" in a
    cluster, or in a "Pending" state.
    Caution: This method clears any data that is on the node. Exercise caution when using this method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param build: [required] Specifies the URL to a remote Element software image to which the node will be reset. 
    :type build: str

    :param force: [required] Required parameter to successfully reset the node. 
    :type force: bool

    :param options:  Specifications for running the reset operation. 
    :type options: str

    :param reboot:  Should it be rebooted? 
    :type reboot: bool

    """
    build = data_model.property(
        "build", str,
        array=False, optional=False,
        documentation="[&#x27;Specifies the URL to a remote Element software image to which the node will&#x27;, &#x27;be reset.&#x27;]",
        dictionaryType=None
    )
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;Required parameter to successfully reset the node.&#x27;]",
        dictionaryType=None
    )
    options = data_model.property(
        "options", str,
        array=False, optional=True,
        documentation="[&#x27;Specifications for running the reset operation.&#x27;]",
        dictionaryType=None
    )
    reboot = data_model.property(
        "reboot", bool,
        array=False, optional=True,
        documentation="[&#x27;Should it be rebooted?&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoRequest(data_model.DataObject):
    """SetLoginSessionInfoRequest  
    You can use SetLoginSessionInfo to set the period of time that a session's login authentication is valid. After the log in period elapses without activity on the system, the authentication expires. New login credentials are required for continued access to the cluster after the timeout period has elapsed.

    :param timeout: [required] Cluster authentication expiration period. Formatted in HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can be used to equal a 90 minute timeout period. The default value is 30 minutes. 
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="[&#x27;Cluster authentication expiration period. Formatted in&#x27;, &#x27;HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can&#x27;, &#x27;be used to equal a 90 minute timeout period. The default value is 30 minutes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSnapshotResult(data_model.DataObject):
    """CreateSnapshotResult  

    :param snapshot: [required]  
    :type snapshot: Snapshot

    :param snapshot_id: [required] ID of the newly-created snapshot. 
    :type snapshot_id: int

    :param checksum: [required] A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;ID of the newly-created snapshot.&#x27;]",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=False,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortInfo(data_model.DataObject):
    """FibreChannelPortInfo  
    Fibre Channel Node Port Info object returns information about all Fibre Channel ports on a node, or for one node in the cluster. The same information is returned for all ports or port information for one node. This information is returned with the API method ListNodeFibreChannelPortInfo (in the SolidFire API Guide).

    :param firmware: [required] The version of the firmware installed on the Fibre Channel port. 
    :type firmware: str

    :param hba_port: [required] The ID of the individual HBA port. 
    :type hba_port: int

    :param model: [required] Model of the HBA on the port. 
    :type model: str

    :param n_port_id: [required] Unique SolidFire port node ID. 
    :type n_port_id: str

    :param pci_slot: [required] Slot in which the pci card resides on the Fibre Channel node hardware. 
    :type pci_slot: int

    :param serial: [required] Serial number on the Fibre Channel port. 
    :type serial: str

    :param speed: [required] Speed of the HBA on the port. 
    :type speed: str

    :param state: [required] Possible values:  <strong>UnknownNotPresentOnlineOfflineBlockedBypassedDiagnosticsLinkdownErrorLoopbackDeleted</strong> 
    :type state: str

    :param switch_wwn: [required] The World Wide Name of the Fibre Channel switch port. 
    :type switch_wwn: str

    :param wwnn: [required] World Wide Node Name of the HBA node. 
    :type wwnn: str

    :param wwpn: [required] World Wide Port Name assigned to the physical port of the HBA. 
    :type wwpn: str

    """
    firmware = data_model.property(
        "firmware", str,
        array=False, optional=False,
        documentation="[&#x27;The version of the firmware installed on the Fibre Channel port.&#x27;]",
        dictionaryType=None
    )
    hba_port = data_model.property(
        "hbaPort", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the individual HBA port.&#x27;]",
        dictionaryType=None
    )
    model = data_model.property(
        "model", str,
        array=False, optional=False,
        documentation="[&#x27;Model of the HBA on the port.&#x27;]",
        dictionaryType=None
    )
    n_port_id = data_model.property(
        "nPortID", str,
        array=False, optional=False,
        documentation="[&#x27;Unique SolidFire port node ID.&#x27;]",
        dictionaryType=None
    )
    pci_slot = data_model.property(
        "pciSlot", int,
        array=False, optional=False,
        documentation="[&#x27;Slot in which the pci card resides on the Fibre Channel node hardware.&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[&#x27;Serial number on the Fibre Channel port.&#x27;]",
        dictionaryType=None
    )
    speed = data_model.property(
        "speed", str,
        array=False, optional=False,
        documentation="[&#x27;Speed of the HBA on the port.&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="[&#x27;Possible values:&#x27;, u&#x27;&#x27;, &#x27;&lt;strong&gt;UnknownNotPresentOnlineOfflineBlockedBypassedDiagnosticsLinkdownErrorLoopbackDeleted&lt;/strong&gt;&#x27;]",
        dictionaryType=None
    )
    switch_wwn = data_model.property(
        "switchWwn", str,
        array=False, optional=False,
        documentation="[&#x27;The World Wide Name of the Fibre Channel switch port.&#x27;]",
        dictionaryType=None
    )
    wwnn = data_model.property(
        "wwnn", str,
        array=False, optional=False,
        documentation="[&#x27;World Wide Node Name of the HBA node.&#x27;]",
        dictionaryType=None
    )
    wwpn = data_model.property(
        "wwpn", str,
        array=False, optional=False,
        documentation="[&#x27;World Wide Port Name assigned to the physical port of the HBA.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortList(data_model.DataObject):
    """FibreChannelPortList  
    List of all Fibre Channel ports.

    :param fibre_channel_ports: [required] List of all physical Fibre Channel ports. 
    :type fibre_channel_ports: FibreChannelPortInfo

    """
    fibre_channel_ports = data_model.property(
        "fibreChannelPorts", FibreChannelPortInfo,
        array=True, optional=False,
        documentation="[&#x27;List of all physical Fibre Channel ports.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelPortInfoResult(data_model.DataObject):
    """FibreChannelPortInfoResult  
    Used to return information about the Fibre Channel ports.

    :param result: [required] Used to return information about the Fibre Channel ports. 
    :type result: FibreChannelPortList

    """
    result = data_model.property(
        "result", FibreChannelPortList,
        array=False, optional=False,
        documentation="[&#x27;Used to return information about the Fibre Channel ports.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListFibreChannelPortInfoResult(data_model.DataObject):
    """ListFibreChannelPortInfoResult  
    ListFibreChannelPortInfoResult is used to return information about the Fibre Channel ports.

    :param fibre_channel_port_info: [required] Used to return information about the Fibre Channel ports. 
    :type fibre_channel_port_info: dict

    """
    fibre_channel_port_info = data_model.property(
        "fibreChannelPortInfo", dict,
        array=False, optional=False,
        documentation="[&#x27;Used to return information about the Fibre Channel ports.&#x27;]",
        dictionaryType=FibreChannelPortInfoResult
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationResult(data_model.DataObject):
    """EnableLdapAuthenticationResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeResult(data_model.DataObject):
    """RestoreDeletedVolumeResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDeletedVolumesResult(data_model.DataObject):
    """ListDeletedVolumesResult  

    :param volumes: [required] List of deleted volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;List of deleted volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsRequest(data_model.DataObject):
    """ListSnapshotsRequest  
    ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster.

    :param volume_id:  Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. 
    :type volume_id: int

    :param snapshot_id:  Retrieves information for a specific snapshot ID. 
    :type snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="[&#x27;Retrieves snapshots for a volume. If volumeID is not provided,&#x27;, &#x27;all snapshots for all volumes are returned.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;Retrieves information for a specific snapshot ID.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveVolumesResult(data_model.DataObject):
    """ListActiveVolumesResult  

    :param volumes: [required] List of active volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;List of active volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNtpInfoResult(data_model.DataObject):
    """GetNtpInfoResult  

    :param broadcastclient: [required] Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values: true false 
    :type broadcastclient: bool

    :param servers: [required] List of NTP servers. 
    :type servers: str

    """
    broadcastclient = data_model.property(
        "broadcastclient", bool,
        array=False, optional=False,
        documentation="[&#x27;Indicates whether or not the nodes in the cluster are listening for broadcast NTP messages. Possible values:&#x27;, &#x27;true&#x27;, &#x27;false&#x27;]",
        dictionaryType=None
    )
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="[&#x27;List of NTP servers.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAsyncResultsRequest(data_model.DataObject):
    """ListAsyncResultsRequest  
    You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system.
    Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult
    to query any of the asyncHandles returned by ListAsyncResults.

    :param async_result_types:  An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster 
    :type async_result_types: str

    """
    async_result_types = data_model.property(
        "asyncResultTypes", str,
        array=True, optional=True,
        documentation="[&#x27;An optional list of types of results. You can use this list to restrict the&#x27;, &#x27;results to only these types of operations. Possible values are:&#x27;, &#x27;BulkVolume: Copy operations between volumes, such as backups or&#x27;, &#x27;restores.&#x27;, &#x27;Clone: Volume cloning operations.&#x27;, &#x27;DriveRemoval: Operations involving the system copying data from a&#x27;, &#x27;drive in preparation to remove it from the cluster.&#x27;, &#x27;RtfiPendingNode: Operations involving the system installing&#x27;, &#x27;compatible software on a node before adding it to the cluster&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyAccountResult(data_model.DataObject):
    """ModifyAccountResult  

    :param account: [required]  
    :type account: Account

    """
    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVirtualVolumeCountResult(data_model.DataObject):
    """GetVirtualVolumeCountResult  

    :param count: [required] The number of virtual volumes currently in the system. 
    :type count: int

    """
    count = data_model.property(
        "count", int,
        array=False, optional=False,
        documentation="[&#x27;The number of virtual volumes currently in the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListUtilitiesResult(data_model.DataObject):
    """ListUtilitiesResult  

    :param utilities: [required] List of utilities currently available to run on the node. 
    :type utilities: str

    """
    utilities = data_model.property(
        "utilities", str,
        array=False, optional=False,
        documentation="[&#x27;List of utilities currently available to run on the node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveInitiatorsFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveInitiatorsFromVolumeAccessGroupRequest  
    RemoveInitiatorsFromVolumeAccessGroup enables
    you to remove initiators from a specified volume access
    group.

    :param volume_access_group_id: [required] The ID of the volume access group from which the initiators are removed. 
    :type volume_access_group_id: int

    :param initiators: [required] The list of initiators to remove from the volume access group. 
    :type initiators: str

    :param delete_orphan_initiators:  true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 
    :type delete_orphan_initiators: bool

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group&#x27;, &#x27;from which the initiators are removed.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="[&#x27;The list of initiators to remove from the volume&#x27;, &#x27;access group.&#x27;]",
        dictionaryType=None
    )
    delete_orphan_initiators = data_model.property(
        "deleteOrphanInitiators", bool,
        array=False, optional=True,
        documentation="[&#x27;true: Delete initiator objects after they are removed from a volume access group.&#x27;, &#x27;false: Do not delete initiator objects after they are removed from a volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetDefaultQoSRequest(data_model.DataObject):
    """SetDefaultQoSRequest  
    SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or
    IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide.

    :param min_iops:  The minimum number of sustained IOPS provided by the cluster to a volume. 
    :type min_iops: int

    :param max_iops:  The maximum number of sustained IOPS provided by the cluster to a volume. 
    :type max_iops: int

    :param burst_iops:  The maximum number of IOPS allowed in a short burst scenario. 
    :type burst_iops: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;The minimum number of sustained IOPS provided by the cluster to a&#x27;, &#x27;volume.&#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of sustained IOPS provided by the cluster to a&#x27;, &#x27;volume.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of IOPS allowed in a short burst scenario.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpTrapInfoResult(data_model.DataObject):
    """SetSnmpTrapInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainersRequest(data_model.DataObject):
    """DeleteStorageContainersRequest  
    DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time.
    The storage containers you remove must not contain any VVols.

    :param storage_container_ids: [required] A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=False,
        documentation="[&#x27;A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VolumeAccessGroup(data_model.DataObject):
    """VolumeAccessGroup  
    A volume access group is a useful way of grouping volumes and initiators together for ease of management.
    
    Volume Access Group Limits:
    
    - A volume access group can contain up to sixty-four initiator IQNs.
    - An initiator can only beinteger to only one volume access group.
    - A volume access group can contain up to two thousand volumes.
    - Each volume access group can beinteger to a maximum of four other volume access groups.

    :param deleted_volumes: [required] A list of deleted volumes that have yet to be purged from the VAG. 
    :type deleted_volumes: int

    :param volume_access_group_id: [required] Unique ID for this volume access group. 
    :type volume_access_group_id: int

    :param name: [required] Name of the volume access group. 
    :type name: str

    :param initiator_ids: [required] A list of IDs of initiators that are mapped to the VAG. 
    :type initiator_ids: int

    :param initiators: [required] List of unique initiator names beintegering to the volume access group. 
    :type initiators: str

    :param volumes: [required] List of volumes beintegering to the volume access group. 
    :type volumes: int

    :param attributes: [required] List of name/value pairs 
    :type attributes: dict

    """
    deleted_volumes = data_model.property(
        "deletedVolumes", int,
        array=True, optional=False,
        documentation="[&#x27;A list of deleted volumes that have yet to be purged from the VAG.&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID for this volume access group.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the volume access group.&#x27;]",
        dictionaryType=None
    )
    initiator_ids = data_model.property(
        "initiatorIDs", int,
        array=True, optional=False,
        documentation="[&#x27;A list of IDs of initiators that are mapped to the VAG.&#x27;]",
        dictionaryType=None
    )
    initiators = data_model.property(
        "initiators", str,
        array=True, optional=False,
        documentation="[&#x27;List of unique initiator names beintegering to the volume access group.&#x27;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;List of volumes beintegering to the volume access group.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of name/value pairs&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeAccessGroupResult(data_model.DataObject):
    """CreateVolumeAccessGroupResult  

    :param volume_access_group_id: [required] The ID for the newly-created volume access group. 
    :type volume_access_group_id: int

    :param volume_access_group:   
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID for the newly-created volume access group.&#x27;]",
        dictionaryType=None
    )
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerRequest(data_model.DataObject):
    """CreateStorageContainerRequest  
    CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature.

    :param name: [required] The name of the storage container. Follows SolidFire account naming restrictions. 
    :type name: str

    :param initiator_secret:  The secret for CHAP authentication for the initiator. 
    :type initiator_secret: str

    :param target_secret:  The secret for CHAP authentication for the target. 
    :type target_secret: str

    :param account_id:  Non-storage container account that will become a storage container. 
    :type account_id: int

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the storage container. Follows SolidFire account&#x27;, &#x27;naming restrictions.&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="[&#x27;The secret for CHAP authentication for the initiator.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="[&#x27;The secret for CHAP authentication for the target.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="[&#x27;Non-storage container account that will become a&#x27;, &#x27;storage container.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddVirtualNetworkResult(data_model.DataObject):
    """AddVirtualNetworkResult  

    :param virtual_network_id:  The virtual network ID of the new virtual network. 
    :type virtual_network_id: int

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="[&#x27;The virtual network ID of the new virtual network.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddNodesRequest(data_model.DataObject):
    """AddNodesRequest  
    AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster. 
    Note: It might take several seconds after adding a new node for it to start up and register its drives as available.

    :param pending_nodes: [required]  List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. 
    :type pending_nodes: int

    :param auto_install:  Whether these nodes should be autoinstalled 
    :type auto_install: bool

    """
    pending_nodes = data_model.property(
        "pendingNodes", int,
        array=True, optional=False,
        documentation="[&#x27; List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method.&#x27;]",
        dictionaryType=None
    )
    auto_install = data_model.property(
        "autoInstall", bool,
        array=False, optional=True,
        documentation="[&#x27;Whether these nodes should be autoinstalled&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RtfiInfo(data_model.DataObject):
    """RtfiInfo  

    :param mipi:   
    :type mipi: str

    :param generation: [required]  
    :type generation: str

    :param status_url_logfile:   
    :type status_url_logfile: str

    :param build: [required]  
    :type build: str

    :param status_url_all: [required]  
    :type status_url_all: str

    :param generation_next:   
    :type generation_next: int

    :param mip:   
    :type mip: str

    :param status_url_current: [required]  
    :type status_url_current: str

    :param options:   
    :type options: dict

    """
    mipi = data_model.property(
        "mipi", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    generation = data_model.property(
        "generation", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status_url_logfile = data_model.property(
        "statusUrlLogfile", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    build = data_model.property(
        "build", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status_url_all = data_model.property(
        "statusUrlAll", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    generation_next = data_model.property(
        "generationNext", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mip = data_model.property(
        "mip", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status_url_current = data_model.property(
        "statusUrlCurrent", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    options = data_model.property(
        "options", dict,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeDetails(data_model.DataObject):
    """ResetNodeDetails  

    :param rtfi_info: [required]  
    :type rtfi_info: RtfiInfo

    """
    rtfi_info = data_model.property(
        "rtfiInfo", RtfiInfo,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetNodeResult(data_model.DataObject):
    """ResetNodeResult  

    :param details:   
    :type details: ResetNodeDetails

    :param duration:   
    :type duration: str

    :param result:   
    :type result: str

    :param rtfi_info:   
    :type rtfi_info: RtfiInfo

    """
    details = data_model.property(
        "details", ResetNodeDetails,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    rtfi_info = data_model.property(
        "rtfiInfo", RtfiInfo,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableLdapAuthenticationRequest(data_model.DataObject):
    """EnableLdapAuthenticationRequest  
    The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials.

    :param auth_type:  Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind 
    :type auth_type: str

    :param group_search_base_dn:  The base DN of the tree to start the group search (will do a subtree search from here). 
    :type group_search_base_dn: str

    :param group_search_custom_filter:  For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 
    :type group_search_custom_filter: str

    :param group_search_type:  Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). 
    :type group_search_type: str

    :param search_bind_dn:  A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 
    :type search_bind_dn: str

    :param search_bind_password:  The password for the searchBindDN account used for searching. 
    :type search_bind_password: str

    :param server_uris: [required] A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 
    :type server_uris: str

    :param user_dntemplate:  A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. 
    :type user_dntemplate: str

    :param user_search_base_dn:  The base DN of the tree to start the search (will do a subtree search from here). 
    :type user_search_base_dn: str

    :param user_search_filter:  The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. 
    :type user_search_filter: str

    """
    auth_type = data_model.property(
        "authType", str,
        array=False, optional=True,
        documentation="[&#x27;Identifies which user authentication method to use. Must be one of the following:&#x27;, &#x27;DirectBind&#x27;, &#x27;SearchAndBind&#x27;]",
        dictionaryType=None
    )
    group_search_base_dn = data_model.property(
        "groupSearchBaseDN", str,
        array=False, optional=True,
        documentation="[&#x27;The base DN of the tree to start the group search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    group_search_custom_filter = data_model.property(
        "groupSearchCustomFilter", str,
        array=False, optional=True,
        documentation="[&#x27;For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.&#x27;]",
        dictionaryType=None
    )
    group_search_type = data_model.property(
        "groupSearchType", str,
        array=False, optional=True,
        documentation="[&#x27;Controls the default group search filter used, and must be one of the following:&#x27;, &#x27;NoGroups: No group support.&#x27;, &#x27;ActiveDirectory: Nested membership of all of a users AD groups.&#x27;, &#x27;MemberDN: MemberDN style groups (single level).&#x27;]",
        dictionaryType=None
    )
    search_bind_dn = data_model.property(
        "searchBindDN", str,
        array=False, optional=True,
        documentation="[&#x27;A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).&#x27;]",
        dictionaryType=None
    )
    search_bind_password = data_model.property(
        "searchBindPassword", str,
        array=False, optional=True,
        documentation="[&#x27;The password for the searchBindDN account used for searching.&#x27;]",
        dictionaryType=None
    )
    server_uris = data_model.property(
        "serverURIs", str,
        array=True, optional=False,
        documentation="[&#x27;A comma-separated list of LDAP server URIs (examples: &quot;ldap://1.2.3.4&quot; and ldaps://1.2.3.4:123&quot;)&#x27;]",
        dictionaryType=None
    )
    user_dntemplate = data_model.property(
        "userDNTemplate", str,
        array=False, optional=True,
        documentation="[&#x27;A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user.&#x27;]",
        dictionaryType=None
    )
    user_search_base_dn = data_model.property(
        "userSearchBaseDN", str,
        array=False, optional=True,
        documentation="[&#x27;The base DN of the tree to start the search (will do a subtree search from here).&#x27;]",
        dictionaryType=None
    )
    user_search_filter = data_model.property(
        "userSearchFilter", str,
        array=False, optional=True,
        documentation="[&#x27;The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&amp;(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStateInfo(data_model.DataObject):
    """NodeStateInfo  

    :param cluster: [required] Name of the cluster. 
    :type cluster: str

    :param state: [required] <strong>Available:</strong> Node has not been configured with a cluster name.<br><strong>Pending:</strong> Node is pending for a specific named cluster and can be added.<br><strong>Active:</strong> Node is active and a member of a cluster and may not be added to another cluster. 
    :type state: str

    """
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=False,
        documentation="[&#x27;Name of the cluster.&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=False,
        documentation="[&#x27;&lt;strong&gt;Available:&lt;/strong&gt; Node has not been configured with a cluster name.&lt;br&gt;&lt;strong&gt;Pending:&lt;/strong&gt; Node is pending for a specific named cluster and can be added.&lt;br&gt;&lt;strong&gt;Active:&lt;/strong&gt; Node is active and a member of a cluster and may not be added to another cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeStateResult(data_model.DataObject):
    """NodeStateResult  

    :param node_id: [required] ID of the node. 
    :type node_id: int

    :param result:  NodeStateInfo object. 
    :type result: NodeStateInfo

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;ID of the node.&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", NodeStateInfo,
        array=False, optional=True,
        documentation="[&#x27;NodeStateInfo object.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateResult(data_model.DataObject):
    """GetClusterStateResult  

    :param nodes:  Array of NodeStateResult objects for each node in the cluster. 
    :type nodes: NodeStateResult

    :param cluster:   
    :type cluster: str

    :param state:   
    :type state: str

    """
    nodes = data_model.property(
        "nodes", NodeStateResult,
        array=True, optional=True,
        documentation="[&#x27;Array of NodeStateResult objects for each node in the cluster.&#x27;]",
        dictionaryType=None
    )
    cluster = data_model.property(
        "cluster", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    state = data_model.property(
        "state", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableEncryptionAtRestResult(data_model.DataObject):
    """EnableEncryptionAtRestResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyBackupTargetResult(data_model.DataObject):
    """ModifyBackupTargetResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelCloneRequest(data_model.DataObject):
    """CancelCloneRequest  
    CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the
    system completes and removes the operation's associated asyncHandle.

    :param clone_id: [required] The cloneID for the ongoing clone process. 
    :type clone_id: int

    """
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="[&#x27;The cloneID for the ongoing clone process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountResult(data_model.DataObject):
    """GetAccountResult  

    :param account: [required] Account details. 
    :type account: Account

    """
    account = data_model.property(
        "account", Account,
        array=False, optional=False,
        documentation="[&#x27;Account details.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetAccountByIDRequest(data_model.DataObject):
    """GetAccountByIDRequest  
    GetAccountByID enables you to return details about a specific account, given its accountID.

    :param account_id: [required] Specifies the account for which details are gathered. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the account for which details are gathered.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleRequest(data_model.DataObject):
    """TestConnectEnsembleRequest  
    The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param ensemble:  Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. 
    :type ensemble: str

    """
    ensemble = data_model.property(
        "ensemble", str,
        array=False, optional=True,
        documentation="[&#x27;Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToSnapshotResult(data_model.DataObject):
    """RollbackToSnapshotResult  

    :param snapshot:   
    :type snapshot: Snapshot

    :param snapshot_id:  ID of the newly-created snapshot. 
    :type snapshot_id: int

    :param checksum:  A string that represents the correct digits in the stored snapshot. This checksum can be used later to compare other snapshots to detect errors in the data. 
    :type checksum: str

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the newly-created snapshot.&#x27;]",
        dictionaryType=None
    )
    checksum = data_model.property(
        "checksum", str,
        array=False, optional=True,
        documentation="[&#x27;A string that represents the correct digits in the stored snapshot.&#x27;, &#x27;This checksum can be used later to compare other snapshots to detect errors in the data.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSystemStatusResult(data_model.DataObject):
    """GetSystemStatusResult  

    :param reboot_required: [required]  
    :type reboot_required: bool

    """
    reboot_required = data_model.property(
        "rebootRequired", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoRequest(data_model.DataObject):
    """GetClusterHardwareInfoRequest  
    You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI
    nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware
    identification information.

    :param type:  Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. 
    :type type: str

    """
    type = data_model.property(
        "type", str,
        array=False, optional=True,
        documentation="[&#x27;Includes only a certain type of hardware information in&#x27;, &#x27;the response. Possible values are:&#x27;, &#x27;drives: List only drive information in the response.&#x27;, &#x27;nodes: List only node information in the response.&#x27;, &#x27;all: Include both drive and node information in the&#x27;, &#x27;response.&#x27;, &#x27;If this parameter is omitted, a type of &quot;all&quot; is assumed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetRequest(data_model.DataObject):
    """RemoveBackupTargetRequest  
    RemoveBackupTarget allows you to delete backup targets.

    :param backup_target_id: [required] The unique target ID of the target to remove. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique target ID of the target to remove.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateVolumeRequest(data_model.DataObject):
    """CreateVolumeRequest  
    CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is
    available for connection via iSCSI.

    :param name: [required] The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. 
    :type name: str

    :param account_id: [required] AccountID for the owner of this volume. 
    :type account_id: int

    :param total_size: [required] Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
    :type total_size: int

    :param enable512e: [required] Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. 
    :type enable512e: bool

    :param qos:  Initial quality of service settings for this volume. Default values are used if none are specified. Valid settings are: minIOPS maxIOPS burstIOPS You can get the default values for a volume by using the GetDefaultQoS method. 
    :type qos: QoS

    :param attributes:  The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the volume access group (might be user specified).&#x27;, &#x27;Not required to be unique, but recommended.&#x27;, &#x27;Might be 1 to 64 characters in length.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;AccountID for the owner of this volume.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=False,
        documentation="[&#x27;Total size of the volume, in bytes. Size is rounded up to&#x27;, &#x27;the nearest 1MB size.&#x27;]",
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=False,
        documentation="[&#x27;Specifies whether 512e emulation is enabled or not. Possible values are:&#x27;, &#x27;true: The volume provides 512-byte sector emulation.&#x27;, &#x27;false: 512e emulation is not enabled.&#x27;]",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="[&#x27;Initial quality of service settings for this volume. Default&#x27;, &#x27;values are used if none are specified. Valid settings are:&#x27;, &#x27;minIOPS&#x27;, &#x27;maxIOPS&#x27;, &#x27;burstIOPS&#x27;, &#x27;You can get the default values for a volume by using the GetDefaultQoS method.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;The list of name-value pairs in JSON object format.&#x27;, &#x27;Total attribute size must be less than 1000B, or 1KB,&#x27;, &#x27;including JSON formatting characters.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterResult(data_model.DataObject):
    """CreateClusterResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetConfigRequest(data_model.DataObject):
    """SetConfigRequest  
    The SetConfig API method enables you to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method. 
    Note: This method is available only through the per-node API endpoint 5.0 or later.
    Caution: Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Exercise caution when using this method.

    :param config: [required] Objects that you want changed for the cluster interface settings. 
    :type config: Config

    """
    config = data_model.property(
        "config", Config,
        array=False, optional=False,
        documentation="[&#x27;Objects that you want changed for the cluster interface settings.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesRequest(data_model.DataObject):
    """ModifyVolumesRequest  
    ModifyVolumes allows you to configure up to 500 existing volumes at one time. Changes take place immediately. If ModifyVolumes fails to modify any of the specified volumes, none of the specified volumes are changed.If you do not specify QoS values when you modify volumes, the QoS values for each volume remain unchanged. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method.When you need to increase the size of volumes that are being replicated, do so in the following order to prevent replication errors:Increase the size of the "Replication Target" volume.Increase the size of the source or "Read / Write" volume. recommends that both the target and source volumes be the same size.NOTE: If you change access status to locked or replicationTarget all existing iSCSI connections are terminated.

    :param volume_ids: [required] A list of volumeIDs for the volumes to be modified. 
    :type volume_ids: int

    :param account_id:  AccountID to which the volume is reassigned. If none is specified, the previous account name is used. 
    :type account_id: int

    :param access:  Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change.  
    :type access: str

    :param qos:  New quality of service settings for this volume.If not specified, the QoS settings are not changed. 
    :type qos: QoS

    :param total_size:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume. 
    :type total_size: int

    :param attributes:  List of name/value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=False,
        documentation="[&#x27;A list of volumeIDs for the volumes to be modified.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="[&#x27;AccountID to which the volume is reassigned. If none is specified, the previous account name is used.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change. &#x27;]",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="[&#x27;New quality of service settings for this volume.If not specified, the QoS settings are not changed.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name/value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingNodesResult(data_model.DataObject):
    """ListPendingNodesResult  

    :param pending_nodes: [required]  
    :type pending_nodes: PendingNode

    """
    pending_nodes = data_model.property(
        "pendingNodes", PendingNode,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CancelGroupCloneResult(data_model.DataObject):
    """CancelGroupCloneResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActivePairedVolumesResult(data_model.DataObject):
    """ListActivePairedVolumesResult  

    :param volumes: [required] Volume information for the paired volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;Volume information for the paired volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestoreDeletedVolumeRequest(data_model.DataObject):
    """RestoreDeletedVolumeRequest  
    RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection.

    :param volume_id: [required] VolumeID of the deleted volume to be restored. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID of the deleted volume to be restored.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoRequest(data_model.DataObject):
    """SetNtpInfoRequest  
    SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients.
    Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults.

    :param servers: [required] List of NTP servers to add to each nodes NTP configuration. 
    :type servers: str

    :param broadcastclient:  Enables every node in the cluster as a broadcast client. 
    :type broadcastclient: bool

    """
    servers = data_model.property(
        "servers", str,
        array=True, optional=False,
        documentation="[&#x27;List of NTP servers to add to each nodes NTP configuration.&#x27;]",
        dictionaryType=None
    )
    broadcastclient = data_model.property(
        "broadcastclient", bool,
        array=False, optional=True,
        documentation="[&#x27;Enables every node in the cluster as a broadcast client.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartClusterPairingResult(data_model.DataObject):
    """StartClusterPairingResult  

    :param cluster_pairing_key: [required] A string of characters that is used by the "CompleteClusterPairing" API method. 
    :type cluster_pairing_key: str

    :param cluster_pair_id: [required] Unique identifier for the cluster pair. 
    :type cluster_pair_id: int

    """
    cluster_pairing_key = data_model.property(
        "clusterPairingKey", str,
        array=False, optional=False,
        documentation="[&#x27;A string of characters that is used by the &quot;CompleteClusterPairing&quot; API method.&#x27;]",
        dictionaryType=None
    )
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier for the cluster pair.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairResult(data_model.DataObject):
    """RemoveVolumePairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveAccountRequest(data_model.DataObject):
    """RemoveAccountRequest  
    RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account
    using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use
    RemoveAccount to remove the account.

    :param account_id: [required] Specifies the AccountID for the account to be removed. 
    :type account_id: int

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the AccountID for the account to be removed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateStorageContainerResult(data_model.DataObject):
    """CreateStorageContainerResult  

    :param storage_container: [required]  
    :type storage_container: StorageContainer

    """
    storage_container = data_model.property(
        "storageContainer", StorageContainer,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotResult(data_model.DataObject):
    """DeleteGroupSnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsResult(data_model.DataObject):
    """ListGroupSnapshotsResult  

    :param group_snapshots: [required] List of Group Snapshots. 
    :type group_snapshots: GroupSnapshot

    """
    group_snapshots = data_model.property(
        "groupSnapshots", GroupSnapshot,
        array=True, optional=False,
        documentation="[&#x27;List of Group Snapshots.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNvramInfoRequest(data_model.DataObject):
    """GetNvramInfoRequest  
    GetNvramInfo enables you to retrieve information from each node about the NVRAM card.

    :param force:  Required parameter to successfully run on all nodes in the cluster. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=True,
        documentation="[&#x27;Required parameter to successfully run on all&#x27;, &#x27;nodes in the cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyResult(data_model.DataObject):
    """GetVolumeEfficiencyResult  

    :param compression:  The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. 
    :type compression: float

    :param deduplication: [required] The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. 
    :type deduplication: float

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. 
    :type missing_volumes: int

    :param thin_provisioning: [required] The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. 
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). 
    :type timestamp: str

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=True,
        documentation="[&#x27;The amount of space being saved by compressing data on a single volume.&#x27;, &#x27;Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.&#x27;]",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="[&#x27;The amount of space being saved on a single volume by not duplicating data.&#x27;, &#x27;Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="[&#x27;The volumes that could not be queried for efficiency data.&#x27;, &#x27;Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.&#x27;]",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="[&#x27;The ratio of space used to the amount of space allocated for storing data.&#x27;, &#x27;Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;The last time efficiency data was collected after Garbage Collection (GC).&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PendingOperation(data_model.DataObject):
    """PendingOperation  

    :param pending: [required] true: operation is still in progress. false: operation is no integerer in progress. 
    :type pending: bool

    :param operation: [required] Name of operation that is in progress or has completed. 
    :type operation: str

    """
    pending = data_model.property(
        "pending", bool,
        array=False, optional=False,
        documentation="[&#x27;true: operation is still in progress.&#x27;, &#x27;false: operation is no integerer in progress.&#x27;]",
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation="[&#x27;Name of operation that is in progress or has completed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetPendingOperationResult(data_model.DataObject):
    """GetPendingOperationResult  

    :param pending_operation: [required]  
    :type pending_operation: PendingOperation

    """
    pending_operation = data_model.property(
        "pendingOperation", PendingOperation,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumeParams(data_model.DataObject):
    """CloneMultipleVolumeParams  

    :param volume_id: [required] Required parameter for "volumes" array: volumeID. 
    :type volume_id: int

    :param access:  Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 
    :type access: str

    :param name:  New name for the clone. 
    :type name: str

    :param new_account_id:  Account ID for the new volume. 
    :type new_account_id: int

    :param new_size:  New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 
    :type new_size: int

    :param attributes:  List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Required parameter for &quot;volumes&quot; array: volumeID.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Access settings for the new volume.&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.&#x27;, u&#x27;&#x27;, &#x27;If unspecified, the access settings of the clone will be the same as the source.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;New name for the clone.&#x27;]",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;Account ID for the new volume.&#x27;]",
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetNtpInfoResult(data_model.DataObject):
    """SetNtpInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeAccessGroupEfficiencyRequest(data_model.DataObject):
    """GetVolumeAccessGroupEfficiencyRequest  
    GetVolumeAccessGroupEfficiency enables you to
    retrieve efficiency information about a volume access
    group. Only the volume access group you provide as the
    parameter in this API method is used to compute the
    capacity.

    :param volume_access_group_id: [required] The volume access group for which capacity is computed. 
    :type volume_access_group_id: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The volume access group for which&#x27;, &#x27;capacity is computed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairResult(data_model.DataObject):
    """ModifyVolumePairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiator(data_model.DataObject):
    """CreateInitiator  
    Object containing characteristics of each new initiator.

    :param name: [required] (Required) The name of the initiator (IQN or WWPN) to create. (String) 
    :type name: str

    :param alias:  (Optional) The friendly name to assign to this initiator. (String) 
    :type alias: str

    :param volume_access_group_id:  (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 
    :type volume_access_group_id: int

    :param attributes:  (Optional) A set of JSON attributes assigned to this initiator. (JSON Object) 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;(Required) The name of the initiator (IQN or WWPN) to create. (String)&#x27;]",
        dictionaryType=None
    )
    alias = data_model.property(
        "alias", str,
        array=False, optional=True,
        documentation="[&#x27;(Optional) The friendly name to assign to this initiator. (String)&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="[&#x27;(Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer)&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;(Optional) A set of JSON attributes assigned to this initiator. (JSON Object)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsRequest(data_model.DataObject):
    """CreateInitiatorsRequest  
    CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them
    aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
    If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create
    any initiators (no partial completion is possible).

    :param initiators: [required] A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 
    :type initiators: CreateInitiator

    """
    initiators = data_model.property(
        "initiators", CreateInitiator,
        array=True, optional=False,
        documentation="[&#x27;A list of objects containing characteristics of each new initiator. Values are:&#x27;, &#x27;name: (Required) The name of the initiator (IQN or WWPN) to create.&#x27;, &#x27;(String)&#x27;, &#x27;alias: (Optional) The friendly name to assign to this initiator. (String)&#x27;, &#x27;attributes: (Optional) A set of JSON attributes to assign to this initiator.&#x27;, &#x27;(JSON Object)&#x27;, &#x27;volumeAccessGroupID: (Optional) The ID of the volume access group&#x27;, &#x27;into to which this newly created initiator will be added. (Integer)&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterFullThresholdResult(data_model.DataObject):
    """GetClusterFullThresholdResult  

    :param block_fullness: [required] Current computed level of block fullness of the cluster. Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended. 
    :type block_fullness: str

    :param fullness: [required] Reflects the highest level of fullness between "blockFullness" and "metadataFullness". 
    :type fullness: str

    :param max_metadata_over_provision_factor: [required] A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. 
    :type max_metadata_over_provision_factor: int

    :param metadata_fullness: [required] Current computed level of metadata fullness of the cluster. 
    :type metadata_fullness: str

    :param slice_reserve_used_threshold_pct: [required] Error condition; message sent to "Alerts" if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned. 
    :type slice_reserve_used_threshold_pct: int

    :param stage2_aware_threshold: [required] Awareness condition: Value that is set for "Stage 2" cluster threshold level. 
    :type stage2_aware_threshold: int

    :param stage2_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage2 condition will exist. 
    :type stage2_block_threshold_bytes: int

    :param stage3_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage3 condition will exist. 
    :type stage3_block_threshold_bytes: int

    :param stage3_block_threshold_percent: [required] The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log. 
    :type stage3_block_threshold_percent: int

    :param stage3_low_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is getting low. 
    :type stage3_low_threshold: int

    :param stage4_critical_threshold: [required] Error condition; message sent to "Alerts" that capacity on a cluster is critically low. 
    :type stage4_critical_threshold: int

    :param stage4_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage4 condition will exist. 
    :type stage4_block_threshold_bytes: int

    :param stage5_block_threshold_bytes: [required] Number of bytes being used by the cluster at which a stage5 condition will exist. 
    :type stage5_block_threshold_bytes: int

    :param sum_total_cluster_bytes: [required] Physical capacity of the cluster measured in bytes. 
    :type sum_total_cluster_bytes: int

    :param sum_total_metadata_cluster_bytes: [required] Total amount of space that can be used to store metadata. 
    :type sum_total_metadata_cluster_bytes: int

    :param sum_used_cluster_bytes: [required] Number of bytes used on the cluster. 
    :type sum_used_cluster_bytes: int

    :param sum_used_metadata_cluster_bytes: [required] Amount of space used on volume drives to store metadata. 
    :type sum_used_metadata_cluster_bytes: int

    """
    block_fullness = data_model.property(
        "blockFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of block fullness of the cluster.&#x27;, &#x27;Possible values: stage1Happy: No alerts or error conditions. stage2Aware: 3 nodes of capacity available. stage3Low: 2 nodes of capacity available. stage4Critical: 1 node of capacity available. No new volumes or clones can be created. stage5CompletelyConsumed: Completely consumed. Cluster is read-only, iSCSI connection is maintained but all writes are suspended.&#x27;]",
        dictionaryType=None
    )
    fullness = data_model.property(
        "fullness", str,
        array=False, optional=False,
        documentation="[&#x27;Reflects the highest level of fullness between &quot;blockFullness&quot; and &quot;metadataFullness&quot;.&#x27;]",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=False,
        documentation="[&#x27;A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.&#x27;]",
        dictionaryType=None
    )
    metadata_fullness = data_model.property(
        "metadataFullness", str,
        array=False, optional=False,
        documentation="[&#x27;Current computed level of metadata fullness of the cluster.&#x27;]",
        dictionaryType=None
    )
    slice_reserve_used_threshold_pct = data_model.property(
        "sliceReserveUsedThresholdPct", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; if the reserved slice utilization is greater than the sliceReserveUsedThresholdPct value returned.&#x27;]",
        dictionaryType=None
    )
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Awareness condition: Value that is set for &quot;Stage 2&quot; cluster threshold level.&#x27;]",
        dictionaryType=None
    )
    stage2_block_threshold_bytes = data_model.property(
        "stage2BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage2 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage3_block_threshold_bytes = data_model.property(
        "stage3BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage3 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=False,
        documentation="[&#x27;The percent value set for stage3. At this percent full, a warning will be posted in the Alerts log.&#x27;]",
        dictionaryType=None
    )
    stage3_low_threshold = data_model.property(
        "stage3LowThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is getting low.&#x27;]",
        dictionaryType=None
    )
    stage4_critical_threshold = data_model.property(
        "stage4CriticalThreshold", int,
        array=False, optional=False,
        documentation="[&#x27;Error condition; message sent to &quot;Alerts&quot; that capacity on a cluster is critically low.&#x27;]",
        dictionaryType=None
    )
    stage4_block_threshold_bytes = data_model.property(
        "stage4BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage4 condition will exist.&#x27;]",
        dictionaryType=None
    )
    stage5_block_threshold_bytes = data_model.property(
        "stage5BlockThresholdBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes being used by the cluster at which a stage5 condition will exist.&#x27;]",
        dictionaryType=None
    )
    sum_total_cluster_bytes = data_model.property(
        "sumTotalClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Physical capacity of the cluster measured in bytes.&#x27;]",
        dictionaryType=None
    )
    sum_total_metadata_cluster_bytes = data_model.property(
        "sumTotalMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Total amount of space that can be used to store metadata.&#x27;]",
        dictionaryType=None
    )
    sum_used_cluster_bytes = data_model.property(
        "sumUsedClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Number of bytes used on the cluster.&#x27;]",
        dictionaryType=None
    )
    sum_used_metadata_cluster_bytes = data_model.property(
        "sumUsedMetadataClusterBytes", int,
        array=False, optional=False,
        documentation="[&#x27;Amount of space used on volume drives to store metadata.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountRequest(data_model.DataObject):
    """ListVolumesForAccountRequest  
    ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account.

    :param account_id: [required] Returns all volumes owned by this AccountID. 
    :type account_id: int

    :param start_volume_id:  The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 
    :type start_volume_id: int

    :param limit:  The maximum number of volumes to return from the API. 
    :type limit: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=False,
        documentation="[&#x27;Returns all volumes owned by this AccountID.&#x27;]",
        dictionaryType=None
    )
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of the first volume to list.&#x27;, &#x27;This can be useful for paging results.&#x27;, &#x27;By default, this starts at the lowest VolumeID.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of volumes to return from the API.&#x27;]",
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableEncryptionAtRestResult(data_model.DataObject):
    """DisableEncryptionAtRestResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeEfficiencyRequest(data_model.DataObject):
    """GetVolumeEfficiencyRequest  
    GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity.

    :param volume_id: [required] Specifies the volume for which capacity is computed. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the volume for which capacity is computed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVirtualNetworkRequest(data_model.DataObject):
    """ModifyVirtualNetworkRequest  
    You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove
    address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or
    disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network.
    Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
    Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the
    "namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the
    "namespace" parameter only during a scheduled maintenance window.

    :param virtual_network_id:  The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
    :type virtual_network_id: int

    :param virtual_network_tag:  The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 
    :type virtual_network_tag: int

    :param name:  The new name for the virtual network. 
    :type name: str

    :param address_blocks:  The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 
    :type address_blocks: AddressBlock

    :param netmask:  New network mask for this virtual network. 
    :type netmask: str

    :param svip:  The storage virtual IP address for this virtual network. The svip for a virtual network cannot be changed. You must create a new virtual network to use a different svip address. 
    :type svip: str

    :param gateway:  The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 
    :type gateway: str

    :param namespace:  When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network. 
    :type namespace: bool

    :param attributes:  A new list of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    virtual_network_id = data_model.property(
        "virtualNetworkID", int,
        array=False, optional=True,
        documentation="[&#x27;The unique identifier of the virtual network to modify. This is the virtual&#x27;, &#x27;network ID assigned by the cluster. &#x27;, &#x27;Note: This parameter is optional&#x27;, &#x27;but either virtualNetworkID or virtualNetworkTag must be specified&#x27;, &#x27;with this API method.&#x27;]",
        dictionaryType=None
    )
    virtual_network_tag = data_model.property(
        "virtualNetworkTag", int,
        array=False, optional=True,
        documentation="[&#x27;The network tag that identifies the virtual network to modify.&#x27;, &#x27;Note: This parameter is optional&#x27;, &#x27;but either virtualNetworkID or virtualNetworkTag must be specified&#x27;, &#x27;with this API method.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;The new name for the virtual network.&#x27;]",
        dictionaryType=None
    )
    address_blocks = data_model.property(
        "addressBlocks", AddressBlock,
        array=True, optional=True,
        documentation="[&#x27;The new addressBlock to set for this virtual network. This might contain&#x27;, &#x27;new address blocks to add to the existing object or omit&#x27;, &#x27;unused address blocks that need to be removed. Alternatively, you&#x27;, &#x27;can extend or reduce the size of existing address blocks. You can only&#x27;, &#x27;increase the size of the starting addressBlocks for a virtual network&#x27;, &#x27;object; you can never decrease it.&#x27;, &#x27;Attributes for this parameter are:&#x27;, &#x27;start: The start of the IP address range. (String)&#x27;, &#x27;size: The number of IP addresses to include in the block. (Integer)&#x27;]",
        dictionaryType=None
    )
    netmask = data_model.property(
        "netmask", str,
        array=False, optional=True,
        documentation="[&#x27;New network mask for this virtual network.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=True,
        documentation="[&#x27;The storage virtual IP address for this virtual network. The svip for a&#x27;, &#x27;virtual network cannot be changed. You must create a new virtual&#x27;, &#x27;network to use a different svip address.&#x27;]",
        dictionaryType=None
    )
    gateway = data_model.property(
        "gateway", str,
        array=False, optional=True,
        documentation="[&#x27;The IP address of a gateway of the virtual network. This parameter is only valid if the &quot;namespace&quot; parameter is set to true.&#x27;]",
        dictionaryType=None
    )
    namespace = data_model.property(
        "namespace", bool,
        array=False, optional=True,
        documentation="[&#x27;When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;A new list of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVirtualVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVirtualVolumeResult  

    :param virtual_volume_stats: [required]  
    :type virtual_volume_stats: VolumeStats

    """
    virtual_volume_stats = data_model.property(
        "VirtualVolumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesForAccountResult(data_model.DataObject):
    """ListVolumesForAccountResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;List of volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoRequest(data_model.DataObject):
    """GetNodeHardwareInfoRequest  
    GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about
    manufacturers, vendors, versions, and other associated hardware identification information.

    :param node_id: [required] The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. 
    :type node_id: int

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the node for which hardware information is being requested. Information&#x27;, &#x27;about a Fibre Channel node is returned if a Fibre Channel node is specified.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SecureEraseDrivesRequest(data_model.DataObject):
    """SecureEraseDrivesRequest  
    SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation.
    You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase.

    :param drives: [required] List of driveIDs to be secure erased. 
    :type drives: int

    """
    drives = data_model.property(
        "drives", int,
        array=True, optional=False,
        documentation="[&#x27;List of driveIDs to be secure erased.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveInfo(data_model.DataObject):
    """DriveInfo  

    :param capacity: [required] Total capacity of the drive, in bytes. 
    :type capacity: int

    :param drive_id: [required] DriveID for this drive. 
    :type drive_id: int

    :param node_id: [required] NodeID where this drive is located. 
    :type node_id: int

    :param serial: [required] Drive serial number. 
    :type serial: str

    :param slot: [required] Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive. 
    :type slot: int

    :param status: [required]  
    :type status: str

    :param type: [required]  
    :type type: str

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="[&#x27;Total capacity of the drive, in bytes.&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;DriveID for this drive.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;NodeID where this drive is located.&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[&#x27;Drive serial number.&#x27;]",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="[&#x27;Slot number in the server chassis where this drive is located, or -1 if SATADimm used for internal metadata drive.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDrivesResult(data_model.DataObject):
    """ListDrivesResult  

    :param drives: [required] Information for the drives that are connected to the cluster. 
    :type drives: DriveInfo

    """
    drives = data_model.property(
        "drives", DriveInfo,
        array=True, optional=False,
        documentation="[&#x27;Information for the drives that are connected to the cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeBinding(data_model.DataObject):
    """VirtualVolumeBinding  

    :param protocol_endpoint_id: [required] The unique ID of the protocol endpoint. 
    :type protocol_endpoint_id: UUID

    :param protocol_endpoint_in_band_id: [required] The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint. 
    :type protocol_endpoint_in_band_id: str

    :param protocol_endpoint_type: [required] The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type. 
    :type protocol_endpoint_type: str

    :param virtual_volume_binding_id: [required] The unique ID of the virtual volume binding object. 
    :type virtual_volume_binding_id: int

    :param virtual_volume_host_id: [required] The unique ID of the virtual volume host. 
    :type virtual_volume_host_id: UUID

    :param virtual_volume_id: [required] The unique ID of the virtual volume. 
    :type virtual_volume_id: UUID

    :param virtual_volume_secondary_id: [required] The secondary ID of the virtual volume. 
    :type virtual_volume_secondary_id: str

    """
    protocol_endpoint_id = data_model.property(
        "protocolEndpointID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The unique ID of the protocol endpoint.&#x27;]",
        dictionaryType=None
    )
    protocol_endpoint_in_band_id = data_model.property(
        "protocolEndpointInBandID", str,
        array=False, optional=False,
        documentation="[&#x27;The scsiNAADeviceID of the protocol endpoint. For more information, see protocolEndpoint.&#x27;]",
        dictionaryType=None
    )
    protocol_endpoint_type = data_model.property(
        "protocolEndpointType", str,
        array=False, optional=False,
        documentation="[&#x27;The type of protocol endpoint. SCSI is the only value returned for the protocol endpoint type.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_binding_id = data_model.property(
        "virtualVolumeBindingID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique ID of the virtual volume binding object.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The unique ID of the virtual volume host.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_id = data_model.property(
        "virtualVolumeID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The unique ID of the virtual volume.&#x27;]",
        dictionaryType=None
    )
    virtual_volume_secondary_id = data_model.property(
        "virtualVolumeSecondaryID", str,
        array=False, optional=False,
        documentation="[&#x27;The secondary ID of the virtual volume.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsResult(data_model.DataObject):
    """ListVirtualVolumeBindingsResult  

    :param bindings: [required] Describes the VVol <-> Host binding. 
    :type bindings: VirtualVolumeBinding

    """
    bindings = data_model.property(
        "bindings", VirtualVolumeBinding,
        array=True, optional=False,
        documentation="[&#x27;Describes the VVol &lt;-&gt; Host binding.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminResult(data_model.DataObject):
    """ModifyClusterAdminResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToSnapshotRequest(data_model.DataObject):
    """RollbackToSnapshotRequest  
    RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot
    from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it.
    The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true.
    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is
    at stage 4 or 5.

    :param volume_id: [required] VolumeID for the volume. 
    :type volume_id: int

    :param snapshot_id: [required] The ID of a previously created snapshot on the given volume. 
    :type snapshot_id: int

    :param save_current_state: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID for the volume.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of a previously created snapshot on the given volume.&#x27;]",
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="[&#x27;Specifies whether to save an active volume image or delete it. Values are:&#x27;, &#x27;true: The previous active volume image is kept.&#x27;, &#x27;false: (default) The previous active volume image is deleted.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&#x27;Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with &quot;- copy&quot; appended to the end of the name.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeRequest(data_model.DataObject):
    """ListVolumeStatsByVolumeRequest  
    ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the
    creation of the volume.

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterFaultInfo(data_model.DataObject):
    """ClusterFaultInfo  

    :param drive_ids:   
    :type drive_ids: int

    :param network_interface:   
    :type network_interface: str

    :param severity: [required]  
    :type severity: str

    :param type: [required]  
    :type type: str

    :param code: [required]  
    :type code: str

    :param details: [required]  
    :type details: str

    :param node_hardware_fault_id: [required]  
    :type node_hardware_fault_id: int

    :param node_id: [required]  
    :type node_id: int

    :param service_id: [required]  
    :type service_id: int

    :param drive_id: [required]  
    :type drive_id: int

    :param resolved: [required]  
    :type resolved: bool

    :param cluster_fault_id: [required]  
    :type cluster_fault_id: int

    :param date: [required]  
    :type date: str

    :param resolved_date: [required]  
    :type resolved_date: str

    :param data:   
    :type data: dict

    """
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    network_interface = data_model.property(
        "networkInterface", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    severity = data_model.property(
        "severity", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    code = data_model.property(
        "code", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    details = data_model.property(
        "details", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_hardware_fault_id = data_model.property(
        "nodeHardwareFaultID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    resolved = data_model.property(
        "resolved", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_fault_id = data_model.property(
        "clusterFaultID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    date = data_model.property(
        "date", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    resolved_date = data_model.property(
        "resolvedDate", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    data = data_model.property(
        "data", dict,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterFaultsResult(data_model.DataObject):
    """ListClusterFaultsResult  

    :param faults: [required] The list of Cluster Fault objects. 
    :type faults: ClusterFaultInfo

    """
    faults = data_model.property(
        "faults", ClusterFaultInfo,
        array=True, optional=False,
        documentation="[&#x27;The list of Cluster Fault objects.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddLdapClusterAdminRequest(data_model.DataObject):
    """AddLdapClusterAdminRequest  
    AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the
    cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant
    accounts.
    You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group.

    :param username: [required] The distinguished user name for the new LDAP cluster admin. 
    :type username: str

    :param access: [required] Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 
    :type access: str

    :param accept_eula:  Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. 
    :type accept_eula: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;The distinguished user name for the new LDAP cluster admin.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="[&#x27;Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference.&#x27;]",
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="[&#x27;Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumePairRequest(data_model.DataObject):
    """ModifyVolumePairRequest  
    ModifyVolumePair enables you to pause or restart replication between a pair of volumes.

    :param volume_id: [required] The ID of the volume to be modified. 
    :type volume_id: int

    :param paused_manual:  Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication 
    :type paused_manual: bool

    :param mode:  Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. 
    :type mode: str

    :param pause_limit:  Internal use only. 
    :type pause_limit: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume to be modified.&#x27;]",
        dictionaryType=None
    )
    paused_manual = data_model.property(
        "pausedManual", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies whether to pause or restart volume replication process. Valid values are: &#x27;, &#x27;true: Pauses volume replication&#x27;, &#x27;false: Restarts volume replication&#x27;]",
        dictionaryType=None
    )
    mode = data_model.property(
        "mode", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the volume replication mode. Possible values are:&#x27;, &#x27;Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.&#x27;, &#x27;Sync: The source acknowledges the write when the data is stored locally and on the remote cluster.&#x27;, &#x27;SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated.&#x27;]",
        dictionaryType=None
    )
    pause_limit = data_model.property(
        "pauseLimit", int,
        array=False, optional=True,
        documentation="[&#x27;Internal use only.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumesRequest(data_model.DataObject):
    """CloneMultipleVolumesRequest  
    CloneMultipleVolumes enables you to create a clone of a group of specified volumes. You can assign a consistent set of characteristics
    to a group of multiple volumes when they are cloned together.
    Before using groupSnapshotID to clone the volumes in a group snapshot, you must create the group snapshot by using the
    CreateGroupSnapshot API method or the Element OS Web UI. Using groupSnapshotID is optional when cloning multiple volumes.
    Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is
    at stage 4 or 5.

    :param volumes: [required] Unique ID for each volume to include in the clone. If optional parameters are not specified, the values are inherited from the source volumes. Required parameter for "volumes" array: volumeID Optional parameters for "volumes" array: access: Can be one of readOnly, readWrite, locked, or replicationTarget attributes: List of name-value pairs in JSON object format. name: New name for the clone. newAccountID: Account ID for the new volumes. newSize: New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB. 
    :type volumes: CloneMultipleVolumeParams

    :param access:  New default access method for the new volumes if not overridden by information passed in the volume's array. 
    :type access: str

    :param group_snapshot_id:  ID of the group snapshot to use as a basis for the clone. 
    :type group_snapshot_id: int

    :param new_account_id:  New account ID for the volumes if not overridden by information passed in the volumes array. 
    :type new_account_id: int

    """
    volumes = data_model.property(
        "volumes", CloneMultipleVolumeParams,
        array=True, optional=False,
        documentation="[&#x27;Unique ID for each volume to include in the clone. If&#x27;, &#x27;optional parameters are not specified, the values are inherited from the source volumes.&#x27;, &#x27;Required parameter for &quot;volumes&quot; array:&#x27;, &#x27;volumeID&#x27;, &#x27;Optional parameters for &quot;volumes&quot; array:&#x27;, &#x27;access: Can be one of readOnly, readWrite,&#x27;, &#x27;locked, or replicationTarget&#x27;, &#x27;attributes: List of name-value pairs in JSON object&#x27;, &#x27;format.&#x27;, &#x27;name: New name for the clone.&#x27;, &#x27;newAccountID: Account ID for the new volumes.&#x27;, &#x27;newSize: New size Total size of the volume, in bytes.&#x27;, &#x27;Size is rounded up to the nearest 1MB.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;New default access method for the new volumes if not&#x27;, &quot;overridden by information passed in the volume&#x27;s array.&quot;]",
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the group snapshot to use as a basis for the clone.&#x27;]",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;New account ID for the volumes if not overridden by&#x27;, &#x27;information passed in the volumes array.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsRequest(data_model.DataObject):
    """ListVolumeAccessGroupsRequest  
    ListVolumeAccessGroups enables you to return
    information about the volume access groups that are
    currently in the system.

    :param start_volume_access_group_id:  The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). 
    :type start_volume_access_group_id: int

    :param limit:  The maximum number of results to return. This can be useful for paging. 
    :type limit: int

    """
    start_volume_access_group_id = data_model.property(
        "startVolumeAccessGroupID", int,
        array=False, optional=True,
        documentation="[&#x27;The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0).&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;The maximum number of results to return. This can be&#x27;, &#x27;useful for paging.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ProtocolEndpoint(data_model.DataObject):
    """ProtocolEndpoint  

    :param protocol_endpoint_id: [required]  
    :type protocol_endpoint_id: UUID

    :param protocol_endpoint_state: [required]  
    :type protocol_endpoint_state: str

    :param provider_type: [required]  
    :type provider_type: str

    :param primary_provider_id: [required]  
    :type primary_provider_id: int

    :param secondary_provider_id: [required]  
    :type secondary_provider_id: int

    :param scsi_naadevice_id: [required]  
    :type scsi_naadevice_id: str

    """
    protocol_endpoint_id = data_model.property(
        "protocolEndpointID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    protocol_endpoint_state = data_model.property(
        "protocolEndpointState", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    provider_type = data_model.property(
        "providerType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    primary_provider_id = data_model.property(
        "primaryProviderID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    secondary_provider_id = data_model.property(
        "secondaryProviderID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_naadevice_id = data_model.property(
        "scsiNAADeviceID", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsResult(data_model.DataObject):
    """ListProtocolEndpointsResult  

    :param protocol_endpoints: [required]  
    :type protocol_endpoints: ProtocolEndpoint

    """
    protocol_endpoints = data_model.property(
        "protocolEndpoints", ProtocolEndpoint,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLResult(data_model.DataObject):
    """SetSnmpACLResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListGroupSnapshotsRequest(data_model.DataObject):
    """ListGroupSnapshotsRequest  
    ListGroupSnapshots enables you to get information about all group snapshots that have been created.

    :param volume_id:  An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. 
    :type volume_id: int

    :param group_snapshot_id:  Retrieves information for a specific group snapshot ID. 
    :type group_snapshot_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=True,
        documentation="[&#x27;An array of unique volume IDs to query. If you do not&#x27;, &#x27;specify this parameter, all group snapshots on the cluster&#x27;, &#x27;are included.&#x27;]",
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;Retrieves information for a specific group snapshot ID.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureRequest(data_model.DataObject):
    """EnableFeatureRequest  
    You can use EnableFeature to enable cluster features that are disabled by default.

    :param feature: [required] Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. 
    :type feature: str

    """
    feature = data_model.property(
        "feature", str,
        array=False, optional=False,
        documentation="[&#x27;Indicates which feature to enable. Valid value is:&#x27;, &#x27;vvols: Enable the NetApp SolidFire VVols cluster feature.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpNetwork(data_model.DataObject):
    """SnmpNetwork  
    The SNMP network object contains information about SNMP configuration for the cluster nodes. SNMP v3 is supported on SolidFire clusters.

    :param access: [required] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. 
    :type access: str

    :param cidr: [required] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. 
    :type cidr: int

    :param community: [required] SNMP community string. 
    :type community: str

    :param network: [required] This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. 
    :type network: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;ro: read-only access.*&#x27;, &#x27;rw: for read-write access.&#x27;, &#x27;rosys: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all networks other than the default &quot;localhost&quot; be set to &quot;ro&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
        dictionaryType=None
    )
    cidr = data_model.property(
        "cidr", int,
        array=False, optional=False,
        documentation="[&#x27;A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31.&#x27;]",
        dictionaryType=None
    )
    community = data_model.property(
        "community", str,
        array=False, optional=False,
        documentation="[&#x27;SNMP community string.&#x27;]",
        dictionaryType=None
    )
    network = data_model.property(
        "network", str,
        array=False, optional=False,
        documentation="[&#x27;This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of &quot;default&quot; is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveNodesRequest(data_model.DataObject):
    """RemoveNodesRequest  
    You can use RemoveNodes to remove one or more nodes that should no longer participate in the cluster. Before removing a node, you must remove all drives the node contains using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated away from the node.
    After you remove a node, it registers itself as a pending node. You can add the node again or shut it down (shutting the node down removes it from the Pending Node list).

    :param nodes: [required] List of NodeIDs for the nodes to be removed. 
    :type nodes: int

    """
    nodes = data_model.property(
        "nodes", int,
        array=True, optional=False,
        documentation="[&#x27;List of NodeIDs for the nodes to be removed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteGroupSnapshotRequest(data_model.DataObject):
    """DeleteGroupSnapshotRequest  
    DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed.

    :param group_snapshot_id: [required] Specifies the unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_members: [required] Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. 
    :type save_members: bool

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the unique ID of the group snapshot.&#x27;]",
        dictionaryType=None
    )
    save_members = data_model.property(
        "saveMembers", bool,
        array=False, optional=False,
        documentation="[&#x27;Specifies whether to preserve snapshots or delete them. Valid values are:&#x27;, &#x27;true: Snapshots are preserved, but group association is removed.&#x27;, &#x27;false: The group and snapshots are deleted.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifySnapshotResult(data_model.DataObject):
    """ModifySnapshotResult  

    :param snapshot:   
    :type snapshot: Snapshot

    """
    snapshot = data_model.property(
        "snapshot", Snapshot,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumesFromVolumeAccessGroupRequest(data_model.DataObject):
    """RemoveVolumesFromVolumeAccessGroupRequest  
    The RemoveVolumeFromVolumeAccessGroup method enables you to remove volumes from a volume access group.

    :param volume_access_group_id: [required] The ID of the volume access group to remove volumes from. 
    :type volume_access_group_id: int

    :param volumes: [required] The ID of the volume access group to remove volumes from. 
    :type volumes: int

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group to remove volumes from.&#x27;]",
        dictionaryType=None
    )
    volumes = data_model.property(
        "volumes", int,
        array=True, optional=False,
        documentation="[&#x27;The ID of the volume access group to remove volumes from.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyStorageContainerRequest(data_model.DataObject):
    """ModifyStorageContainerRequest  
    ModifyStorageContainer enables you to make changes to an existing virtual volume storage container.

    :param storage_container_id: [required] The unique ID of the virtual volume storage container to modify. 
    :type storage_container_id: UUID

    :param initiator_secret:  The new secret for CHAP authentication for the initiator. 
    :type initiator_secret: str

    :param target_secret:  The new secret for CHAP authentication for the target. 
    :type target_secret: str

    """
    storage_container_id = data_model.property(
        "storageContainerID", UUID,
        array=False, optional=False,
        documentation="[&#x27;The unique ID of the virtual volume storage container to modify.&#x27;]",
        dictionaryType=None
    )
    initiator_secret = data_model.property(
        "initiatorSecret", str,
        array=False, optional=True,
        documentation="[&#x27;The new secret for CHAP authentication for the initiator.&#x27;]",
        dictionaryType=None
    )
    target_secret = data_model.property(
        "targetSecret", str,
        array=False, optional=True,
        documentation="[&#x27;The new secret for CHAP authentication for the target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipDetails(data_model.DataObject):
    """TestConnectMvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: dict

    :param mvip: [required] The MVIP tested against. 
    :type mvip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", dict,
        array=False, optional=False,
        documentation="[&#x27;Details of the ping tests with 56 Bytes and 1500 Bytes.&#x27;]",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="[&#x27;The MVIP tested against.&#x27;]",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="[&#x27;Whether the test could connect to the MVIP.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipResult(data_model.DataObject):
    """TestConnectMvipResult  

    :param details: [required] Information about the test operation 
    :type details: TestConnectMvipDetails

    :param duration: [required] The length of time required to run the test. 
    :type duration: str

    :param result: [required] The results of the entire test 
    :type result: str

    """
    details = data_model.property(
        "details", TestConnectMvipDetails,
        array=False, optional=False,
        documentation="[&#x27;Information about the test operation&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The length of time required to run the test.&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;The results of the entire test&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClearClusterFaultsResult(data_model.DataObject):
    """ClearClusterFaultsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipDetails(data_model.DataObject):
    """TestConnectSvipDetails  

    :param ping_bytes: [required] Details of the ping tests with 56 Bytes and 1500 Bytes. 
    :type ping_bytes: dict

    :param svip: [required] The SVIP tested against. 
    :type svip: str

    :param connected: [required] Whether the test could connect to the MVIP. 
    :type connected: bool

    """
    ping_bytes = data_model.property(
        "pingBytes", dict,
        array=False, optional=False,
        documentation="[&#x27;Details of the ping tests with 56 Bytes and 1500 Bytes.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;The SVIP tested against.&#x27;]",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="[&#x27;Whether the test could connect to the MVIP.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectSvipResult(data_model.DataObject):
    """TestConnectSvipResult  

    :param details: [required] Information about the test operation 
    :type details: TestConnectSvipDetails

    :param duration: [required] The length of time required to run the test. 
    :type duration: str

    :param result: [required] The results of the entire test 
    :type result: str

    """
    details = data_model.property(
        "details", TestConnectSvipDetails,
        array=False, optional=False,
        documentation="[&#x27;Information about the test operation&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The length of time required to run the test.&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;The results of the entire test&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeResult(data_model.DataObject):
    """ListVolumeStatsByVolumeResult  

    :param volume_stats: [required] List of account activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=True, optional=False,
        documentation="[&#x27;List of account activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpV3UsmUser(data_model.DataObject):
    """SnmpV3UsmUser  
    The SNMP v3 usmUser object is used with the API method SetSnmpInfo to configure SNMP on the cluster.

    :param access: [required] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. 
    :type access: str

    :param name: [required] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. 
    :type name: str

    :param password: [required] The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." 
    :type password: str

    :param passphrase: [required] The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." 
    :type passphrase: str

    :param sec_level: [required] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. 
    :type sec_level: str

    """
    access = data_model.property(
        "access", str,
        array=False, optional=False,
        documentation="[&#x27;rouser: read-only access.*&#x27;, &#x27;rwuser: for read-write access.&#x27;, &#x27;rosys: for read-only access to a restricted set of system information&#x27;, &#x27;*SolidFire recommends that all USM users be set to &quot;rouser&quot; access, because all SolidFire MIB objects are read-only.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="[&#x27;The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;auth&quot; or &quot;priv.&quot;&#x27;]",
        dictionaryType=None
    )
    passphrase = data_model.property(
        "passphrase", str,
        array=False, optional=False,
        documentation="[&#x27;The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if &quot;secLevel&quot; is &quot;priv.&quot;&#x27;]",
        dictionaryType=None
    )
    sec_level = data_model.property(
        "secLevel", str,
        array=False, optional=False,
        documentation="[&#x27;noauth: No password or passphrase is required.&#x27;, &#x27;auth: A password is required for user access.&#x27;, &#x27;priv: A password and passphrase is required for user access.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpInfoResult(data_model.DataObject):
    """GetSnmpInfoResult  

    :param networks:  List of networks and access types enabled for SNMP.  Note: "networks" will only be present if SNMP V3 is disabled. 
    :type networks: SnmpNetwork

    :param enabled: [required] If the nodes in the cluster are configured for SNMP. 
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the nodes in the cluster are configured for SNMP v3. 
    :type snmp_v3_enabled: bool

    :param usm_users:  If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the "networks" parameter. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="[&#x27;List of networks and access types enabled for SNMP.&#x27;, u&#x27;&#x27;, &#x27;Note: &quot;networks&quot; will only be present if SNMP V3 is disabled.&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the nodes in the cluster are configured for SNMP.&#x27;]",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the nodes in the cluster are configured for SNMP v3.&#x27;]",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="[&#x27;If SNMP v3 is enabled, the values returned is a list of user access parameters for SNMP information from the cluster. This will be returned instead of the &quot;networks&quot; parameter.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumesResult(data_model.DataObject):
    """ModifyVolumesResult  

    :param volumes: [required]  
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RestartNetworkingRequest(data_model.DataObject):
    """RestartNetworkingRequest  
    The RestartNetworking API method enables you to restart the networking services on a node.
    Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity.
    Exercise caution when using this method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param force: [required] Required parameter to successfully reset the node. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;Required parameter to successfully reset the node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListNodeFibreChannelPortInfoResult(data_model.DataObject):
    """ListNodeFibreChannelPortInfoResult  
    List of fibre channel port info results grouped by node.

    :param fibre_channel_ports: [required] List of all physical Fibre Channel ports. 
    :type fibre_channel_ports: FibreChannelPortInfo

    """
    fibre_channel_ports = data_model.property(
        "fibreChannelPorts", FibreChannelPortInfo,
        array=True, optional=False,
        documentation="[&#x27;List of all physical Fibre Channel ports.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSupportBundleRequest(data_model.DataObject):
    """CreateSupportBundleRequest  
    CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file.

    :param bundle_name:  The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. 
    :type bundle_name: str

    :param extra_args:  Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. 
    :type extra_args: str

    :param timeout_sec:  The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. 
    :type timeout_sec: int

    """
    bundle_name = data_model.property(
        "bundleName", str,
        array=False, optional=True,
        documentation="[&#x27;The unique name for the support bundle. If no name is provided, &quot;supportbundle&quot; and the node name are used as the filename.&#x27;]",
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=True,
        documentation="[&#x27;Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support.&#x27;]",
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=True,
        documentation="[&#x27;The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveStats(data_model.DataObject):
    """DriveStats  

    :param active_sessions:   
    :type active_sessions: int

    :param drive_id:   
    :type drive_id: int

    :param failed_die_count: [required]  
    :type failed_die_count: int

    :param life_remaining_percent: [required]  
    :type life_remaining_percent: int

    :param lifetime_read_bytes: [required]  
    :type lifetime_read_bytes: int

    :param lifetime_write_bytes: [required]  
    :type lifetime_write_bytes: int

    :param power_on_hours: [required]  
    :type power_on_hours: int

    :param read_bytes: [required]  
    :type read_bytes: int

    :param read_ops: [required]  
    :type read_ops: int

    :param reallocated_sectors: [required]  
    :type reallocated_sectors: int

    :param reserve_capacity_percent: [required]  
    :type reserve_capacity_percent: int

    :param timestamp: [required]  
    :type timestamp: str

    :param total_capacity: [required]  
    :type total_capacity: int

    :param used_capacity:   
    :type used_capacity: int

    :param used_memory: [required]  
    :type used_memory: int

    :param write_bytes: [required]  
    :type write_bytes: int

    :param write_ops: [required]  
    :type write_ops: int

    """
    active_sessions = data_model.property(
        "activeSessions", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    failed_die_count = data_model.property(
        "failedDieCount", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_bytes = data_model.property(
        "readBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    read_ops = data_model.property(
        "readOps", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    total_capacity = data_model.property(
        "totalCapacity", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    used_capacity = data_model.property(
        "usedCapacity", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    used_memory = data_model.property(
        "usedMemory", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    write_bytes = data_model.property(
        "writeBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    write_ops = data_model.property(
        "writeOps", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetDriveStatsResult(data_model.DataObject):
    """GetDriveStatsResult  

    :param drive_stats: [required]  
    :type drive_stats: DriveStats

    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsRequest(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsRequest  
    The ModifyVolumeAccessGroupLunAssignments
    method enables you to define custom LUN assignments
    for specific volumes. This method changes only LUN
    values set on the lunAssignments parameter in the
    volume access group. All other LUN assignments remain
    unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups. 
    Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception. 
    Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments.

    :param volume_access_group_id: [required] The ID of the volume access group for which the LUN assignments will be modified. 
    :type volume_access_group_id: int

    :param lun_assignments: [required] The volume IDs with new assigned LUN values. 
    :type lun_assignments: LunAssignment

    """
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume access group for which the LUN assignments will be modified.&#x27;]",
        dictionaryType=None
    )
    lun_assignments = data_model.property(
        "lunAssignments", LunAssignment,
        array=True, optional=False,
        documentation="[&#x27;The volume IDs with new assigned LUN values.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeReadResult(data_model.DataObject):
    """StartBulkVolumeReadResult  

    :param async_handle: [required] ID of the async process to be checked for completion. 
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session. 
    :type key: str

    :param url: [required] URL to access the node's web server 
    :type url: str

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;ID of the async process to be checked for completion.&#x27;]",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="[&#x27;Opaque key uniquely identifying the session.&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="[&quot;URL to access the node&#x27;s web server&quot;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNetworkConfigResult(data_model.DataObject):
    """GetNetworkConfigResult  

    :param network: [required]  
    :type network: Network

    """
    network = data_model.property(
        "network", Network,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByVolumeAccessGroupRequest(data_model.DataObject):
    """ListVolumeStatsByVolumeAccessGroupRequest  
    ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the
    specified volume access group(s).

    :param volume_access_groups:  An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. 
    :type volume_access_groups: int

    :param include_virtual_volumes:  Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", int,
        array=True, optional=True,
        documentation="[&#x27;An array of VolumeAccessGroupIDs for which volume&#x27;, &#x27;activity is returned. If omitted, statistics for all volume&#x27;, &#x27;access groups are returned.&#x27;]",
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Specifies that virtual volumes are included in the response by default.&#x27;, &#x27;To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class UpdateBulkVolumeStatusResult(data_model.DataObject):
    """UpdateBulkVolumeStatusResult  

    :param status: [required] Status of the session requested. Returned status: preparing active done failed 
    :type status: str

    :param url: [required] The URL to access the node's web server provided only if the session is still active. 
    :type url: str

    :param attributes: [required] Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not. 
    :type attributes: dict

    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Status of the session requested. Returned status:&#x27;, &#x27;preparing&#x27;, &#x27;active&#x27;, &#x27;done&#x27;, &#x27;failed&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="[&quot;The URL to access the node&#x27;s web server provided only if the session is still active.&quot;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;Returns attributes that were specified in the BulkVolumeStatusUpdate method. Values are returned if they have changed or not.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpResult(data_model.DataObject):
    """EnableSnmpResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class FibreChannelSession(data_model.DataObject):
    """FibreChannelSession  
    FibreChannelSession contains information about each Fibre Channel session that is visible to the cluster and what target ports it is visible on.

    :param initiator_wwpn: [required] The WWPN of the initiator which is logged into the target port. 
    :type initiator_wwpn: str

    :param node_id: [required] The node owning the Fibre Channel session. 
    :type node_id: int

    :param service_id: [required] The service ID of the FService owning this Fibre Channel session 
    :type service_id: int

    :param target_wwpn: [required] The WWPN of the target port involved in this session. 
    :type target_wwpn: str

    :param volume_access_group_id:  The ID of the volume access group to which the initiatorWWPN beintegers. If not in a volume access group, the value will be null. 
    :type volume_access_group_id: int

    """
    initiator_wwpn = data_model.property(
        "initiatorWWPN", str,
        array=False, optional=False,
        documentation="[&#x27;The WWPN of the initiator which is logged into the target port.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The node owning the Fibre Channel session.&#x27;]",
        dictionaryType=None
    )
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="[&#x27;The service ID of the FService owning this Fibre Channel session&#x27;]",
        dictionaryType=None
    )
    target_wwpn = data_model.property(
        "targetWWPN", str,
        array=False, optional=False,
        documentation="[&#x27;The WWPN of the target port involved in this session.&#x27;]",
        dictionaryType=None
    )
    volume_access_group_id = data_model.property(
        "volumeAccessGroupID", int,
        array=False, optional=True,
        documentation="[&#x27;The ID of the volume access group to which the initiatorWWPN beintegers. If not in a volume access group, the value will be null.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListFibreChannelSessionsResult(data_model.DataObject):
    """ListFibreChannelSessionsResult  
    Used to return information about the Fibre Channel sessions.

    :param sessions: [required] A list of FibreChannelSession objects with information about the Fibre Channel session. 
    :type sessions: FibreChannelSession

    """
    sessions = data_model.property(
        "sessions", FibreChannelSession,
        array=True, optional=False,
        documentation="[&#x27;A list of FibreChannelSession objects with information about the Fibre Channel session.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class VirtualVolumeTask(data_model.DataObject):
    """VirtualVolumeTask  

    :param virtual_volume_task_id: [required]  
    :type virtual_volume_task_id: UUID

    :param virtualvolume_id: [required]  
    :type virtualvolume_id: UUID

    :param clone_virtual_volume_id: [required]  
    :type clone_virtual_volume_id: UUID

    :param status: [required]  
    :type status: str

    :param operation: [required]  
    :type operation: str

    :param virtual_volume_host_id: [required]  
    :type virtual_volume_host_id: UUID

    :param parent_metadata: [required]  
    :type parent_metadata: dict

    :param parent_total_size: [required]  
    :type parent_total_size: int

    :param parent_used_size: [required]  
    :type parent_used_size: int

    :param cancelled: [required]  
    :type cancelled: bool

    """
    virtual_volume_task_id = data_model.property(
        "virtualVolumeTaskID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtualvolume_id = data_model.property(
        "virtualvolumeID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    clone_virtual_volume_id = data_model.property(
        "cloneVirtualVolumeID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    operation = data_model.property(
        "operation", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volume_host_id = data_model.property(
        "virtualVolumeHostID", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    parent_metadata = data_model.property(
        "parentMetadata", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    parent_total_size = data_model.property(
        "parentTotalSize", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    parent_used_size = data_model.property(
        "parentUsedSize", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cancelled = data_model.property(
        "cancelled", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksResult(data_model.DataObject):
    """ListVirtualVolumeTasksResult  

    :param tasks: [required] List of VVol Async Tasks. 
    :type tasks: VirtualVolumeTask

    """
    tasks = data_model.property(
        "tasks", VirtualVolumeTask,
        array=True, optional=False,
        documentation="[&#x27;List of VVol Async Tasks.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesRequest(data_model.DataObject):
    """PurgeDeletedVolumesRequest  
    PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted; you can use this method to purge up to 500 volumes at one time. You must delete volumes using DeleteVolumes before they can be purged. Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required.

    :param volume_ids:  A list of volumeIDs of volumes to be purged from the system. 
    :type volume_ids: int

    :param account_ids:  A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system. 
    :type account_ids: int

    :param volume_access_group_ids:  A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system. 
    :type volume_access_group_ids: int

    """
    volume_ids = data_model.property(
        "volumeIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volumeIDs of volumes to be purged from the system.&#x27;]",
        dictionaryType=None
    )
    account_ids = data_model.property(
        "accountIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system.&#x27;]",
        dictionaryType=None
    )
    volume_access_group_ids = data_model.property(
        "volumeAccessGroupIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterConfigResult(data_model.DataObject):
    """GetClusterConfigResult  

    :param cluster: [required] Cluster configuration information the node uses to communicate with the cluster. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="[&#x27;Cluster configuration information the node uses to communicate with the cluster.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetVolumeStatsResult(data_model.DataObject):
    """GetVolumeStatsResult  

    :param volume_stats: [required] Volume activity information. 
    :type volume_stats: VolumeStats

    """
    volume_stats = data_model.property(
        "volumeStats", VolumeStats,
        array=False, optional=False,
        documentation="[&#x27;Volume activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterHardwareInfo(data_model.DataObject):
    """ClusterHardwareInfo  

    :param drives: [required]  
    :type drives: dict

    :param nodes: [required]  
    :type nodes: dict

    """
    drives = data_model.property(
        "drives", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=DriveHardwareInfo
    )
    nodes = data_model.property(
        "nodes", dict,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=dict
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterHardwareInfoResult(data_model.DataObject):
    """GetClusterHardwareInfoResult  

    :param cluster_hardware_info: [required] Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node. 
    :type cluster_hardware_info: ClusterHardwareInfo

    """
    cluster_hardware_info = data_model.property(
        "clusterHardwareInfo", ClusterHardwareInfo,
        array=False, optional=False,
        documentation="[&#x27;Hardware information for all nodes and drives in the cluster. Each object in this output is labeled with the nodeID of the given node.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SupportBundleDetails(data_model.DataObject):
    """SupportBundleDetails  

    :param bundle_name: [required] The name specified in the 'CreateSupportBundle API method. If no name was specified, 'supportbundle' will be used. 
    :type bundle_name: str

    :param extra_args: [required] The arguments passed with this method. 
    :type extra_args: str

    :param files: [required] A list of the support bundle files that were created. 
    :type files: str

    :param url: [required] The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list. 
    :type url: str

    :param output: [required] The commands that were run and their output, with newlines replaced by HTML <br> elements. 
    :type output: str

    :param timeout_sec: [required] The timeout specified for the support bundle creation process. 
    :type timeout_sec: int

    """
    bundle_name = data_model.property(
        "bundleName", str,
        array=False, optional=False,
        documentation="[&quot;The name specified in the &#x27;CreateSupportBundle API method. If no name was specified, &#x27;supportbundle&#x27; will be used.&quot;]",
        dictionaryType=None
    )
    extra_args = data_model.property(
        "extraArgs", str,
        array=False, optional=False,
        documentation="[&#x27;The arguments passed with this method.&#x27;]",
        dictionaryType=None
    )
    files = data_model.property(
        "files", str,
        array=True, optional=False,
        documentation="[&#x27;A list of the support bundle files that were created.&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=True, optional=False,
        documentation="[&#x27;The URL that you can use to download the bundle file(s). Should correspond 1:1 with files list.&#x27;]",
        dictionaryType=None
    )
    output = data_model.property(
        "output", str,
        array=False, optional=False,
        documentation="[&#x27;The commands that were run and their output, with newlines replaced by HTML &lt;br&gt; elements.&#x27;]",
        dictionaryType=None
    )
    timeout_sec = data_model.property(
        "timeoutSec", int,
        array=False, optional=False,
        documentation="[&#x27;The timeout specified for the support bundle creation process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateSupportBundleResult(data_model.DataObject):
    """CreateSupportBundleResult  

    :param details: [required] The details of the support bundle.  
    :type details: SupportBundleDetails

    :param duration: [required] The amount of time required to create the support bundle in the format HH:MM:SS.ssssss 
    :type duration: str

    :param result: [required] Whether the support bundle creation passed of failed. 
    :type result: str

    """
    details = data_model.property(
        "details", SupportBundleDetails,
        array=False, optional=False,
        documentation="[&#x27;The details of the support bundle. &#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The amount of time required to create the support bundle in the format HH:MM:SS.ssssss&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;Whether the support bundle creation passed of failed.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetDefaultQoSResult(data_model.DataObject):
    """SetDefaultQoSResult  

    :param min_iops: [required] The minimum number of sustained IOPS that are provided by the cluster to a volume.  
    :type min_iops: int

    :param max_iops: [required] The maximum number of sustained IOPS that are provided by the cluster to a volume. 
    :type max_iops: int

    :param burst_iops: [required] The maximum number of IOPS allowed in a short burst scenario. 
    :type burst_iops: int

    """
    min_iops = data_model.property(
        "minIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;The minimum number of sustained IOPS that are provided by the cluster to a volume. &#x27;]",
        dictionaryType=None
    )
    max_iops = data_model.property(
        "maxIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;The maximum number of sustained IOPS that are provided by the cluster to a volume.&#x27;]",
        dictionaryType=None
    )
    burst_iops = data_model.property(
        "burstIOPS", int,
        array=False, optional=False,
        documentation="[&#x27;The maximum number of IOPS allowed in a short burst scenario.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoRequest(data_model.DataObject):
    """SetSnmpInfoRequest  
    SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to
    all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
    Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead.

    :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2. 
    :type networks: SnmpNetwork

    :param enabled:  If set to true, SNMP is enabled on each node in the cluster. 
    :type enabled: bool

    :param snmp_v3_enabled:  If set to true, SNMP v3 is enabled on each node in the cluster. 
    :type snmp_v3_enabled: bool

    :param usm_users:  If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="[&#x27;List of networks and what type of access they have to the&#x27;, &#x27;SNMP servers running on the cluster nodes. See the SNMP&#x27;, &#x27;Network Object for possible &quot;networks&quot; values. This parameter is required only for SNMP v2.&#x27;]",
        dictionaryType=None
    )
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=True,
        documentation="[&#x27;If set to true, SNMP is enabled on each node in the cluster.&#x27;]",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=True,
        documentation="[&#x27;If set to true, SNMP v3 is enabled on each node in the cluster.&#x27;]",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="[&#x27;If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListStorageContainersRequest(data_model.DataObject):
    """ListStorageContainersRequest  
    ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system.

    :param storage_container_ids:  A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. 
    :type storage_container_ids: UUID

    """
    storage_container_ids = data_model.property(
        "storageContainerIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetHardwareInfoResult(data_model.DataObject):
    """GetHardwareInfoResult  

    :param hardware_info: [required] Hardware information for this node.  
    :type hardware_info: dict

    """
    hardware_info = data_model.property(
        "hardwareInfo", dict,
        array=False, optional=False,
        documentation="[&#x27;Hardware information for this node. &#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveStatsResult(data_model.DataObject):
    """ListDriveStatsResult  

    :param drive_stats: [required] List of drive activity information for each drive. 
    :type drive_stats: DriveStats

    :param errors: [required] If there are errors retrieving information about a drive, this list contains the driveID and associated error message. Always present, and empty if there are no errors. 
    :type errors: dict

    """
    drive_stats = data_model.property(
        "driveStats", DriveStats,
        array=True, optional=False,
        documentation="[&#x27;List of drive activity information for each drive.&#x27;]",
        dictionaryType=None
    )
    errors = data_model.property(
        "errors", dict,
        array=True, optional=False,
        documentation="[&#x27;If there are errors retrieving information about a drive, this list contains the driveID and associated error message. Always present, and empty if there are no errors.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupResult(data_model.DataObject):
    """ModifyVolumeAccessGroupResult  

    :param volume_access_group: [required] An object containing information about the newly modified volume access group. 
    :type volume_access_group: VolumeAccessGroup

    """
    volume_access_group = data_model.property(
        "volumeAccessGroup", VolumeAccessGroup,
        array=False, optional=False,
        documentation="[&#x27;An object containing information about the newly modified volume access group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class LoginSessionInfo(data_model.DataObject):
    """LoginSessionInfo  

    :param timeout: [required]  
    :type timeout: str

    """
    timeout = data_model.property(
        "timeout", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLoginSessionInfoResult(data_model.DataObject):
    """GetLoginSessionInfoResult  

    :param login_session_info: [required] The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered. Objects returned are: timeout - The time, in minutes, when this session will timeout and expire. 
    :type login_session_info: LoginSessionInfo

    """
    login_session_info = data_model.property(
        "loginSessionInfo", LoginSessionInfo,
        array=False, optional=False,
        documentation="[&#x27;The authentication expiration period. Formatted in H:mm:ss. For example: 1:30:00, 20:00, 5:00. All leading zeros and colons are removed regardless of the format the timeout was entered.&#x27;, &#x27;Objects returned are:&#x27;, &#x27;timeout - The time, in minutes, when this session will timeout and expire.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListClusterAdminsResult(data_model.DataObject):
    """ListClusterAdminsResult  

    :param cluster_admins: [required] Information about the cluster admin. 
    :type cluster_admins: ClusterAdmin

    """
    cluster_admins = data_model.property(
        "clusterAdmins", ClusterAdmin,
        array=True, optional=False,
        documentation="[&#x27;Information about the cluster admin.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeStatsResult(data_model.DataObject):
    """GetNodeStatsResult  

    :param node_stats: [required] Node activity information. 
    :type node_stats: NodeStatsInfo

    """
    node_stats = data_model.property(
        "nodeStats", NodeStatsInfo,
        array=False, optional=False,
        documentation="[&#x27;Node activity information.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateInitiatorsResult(data_model.DataObject):
    """CreateInitiatorsResult  

    :param initiators: [required] List of objects containing details about the newly created initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="[&#x27;List of objects containing details about the newly created initiators&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetRemoteLoggingHostsResult(data_model.DataObject):
    """GetRemoteLoggingHostsResult  

    :param remote_hosts: [required] List of hosts to forward logging information to. 
    :type remote_hosts: LoggingServer

    """
    remote_hosts = data_model.property(
        "remoteHosts", LoggingServer,
        array=True, optional=False,
        documentation="[&#x27;List of hosts to forward logging information to.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairResult(data_model.DataObject):
    """RemoveClusterPairResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumesResult(data_model.DataObject):
    """ListVolumesResult  

    :param volumes: [required] List of volumes. 
    :type volumes: Volume

    """
    volumes = data_model.property(
        "volumes", Volume,
        array=True, optional=False,
        documentation="[&#x27;List of volumes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetEfficiencyResult(data_model.DataObject):
    """GetEfficiencyResult  

    :param compression:  The amount of space being saved by compressing data on a single volume. Stated as a ratio where "1" means data has been stored without being compressed. 
    :type compression: float

    :param deduplication:  The amount of space being saved on a single volume by not duplicating data. Stated as a ratio. 
    :type deduplication: float

    :param thin_provisioning:  The ratio of space used to the amount of space allocated for storing data. Stated as a ratio. 
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string. 
    :type timestamp: str

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle. 
    :type missing_volumes: int

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=True,
        documentation="[&#x27;The amount of space being saved by compressing data on a single volume. Stated as a ratio where &quot;1&quot; means data has been stored without being compressed.&#x27;]",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=True,
        documentation="[&#x27;The amount of space being saved on a single volume by not duplicating data. Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=True,
        documentation="[&#x27;The ratio of space used to the amount of space allocated for storing data. Stated as a ratio.&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;The last time efficiency data was collected after Garbage Collection (GC). ISO 8601 data string.&#x27;]",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="[&#x27;The volumes that could not be queried for efficiency data. Missing volumes can be caused by GC being less than hour old, temporary network loss or restarted services since the GC cycle.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetLimitsResult(data_model.DataObject):
    """GetLimitsResult  
    Limits for the cluster

    :param account_count_max: [required]  
    :type account_count_max: int

    :param account_name_length_max: [required]  
    :type account_name_length_max: int

    :param account_name_length_min: [required]  
    :type account_name_length_min: int

    :param bulk_volume_jobs_per_node_max: [required]  
    :type bulk_volume_jobs_per_node_max: int

    :param bulk_volume_jobs_per_volume_max: [required]  
    :type bulk_volume_jobs_per_volume_max: int

    :param clone_jobs_per_volume_max: [required]  
    :type clone_jobs_per_volume_max: int

    :param cluster_pairs_count_max: [required]  
    :type cluster_pairs_count_max: int

    :param initiator_name_length_max: [required]  
    :type initiator_name_length_max: int

    :param initiator_count_max: [required]  
    :type initiator_count_max: int

    :param initiators_per_volume_access_group_count_max: [required]  
    :type initiators_per_volume_access_group_count_max: int

    :param iscsi_sessions_from_fibre_channel_nodes_max: [required]  
    :type iscsi_sessions_from_fibre_channel_nodes_max: int

    :param secret_length_max: [required]  
    :type secret_length_max: int

    :param secret_length_min: [required]  
    :type secret_length_min: int

    :param snapshot_name_length_max: [required]  
    :type snapshot_name_length_max: int

    :param snapshots_per_volume_max: [required]  
    :type snapshots_per_volume_max: int

    :param volume_access_group_count_max: [required]  
    :type volume_access_group_count_max: int

    :param volume_access_group_lun_max: [required]  
    :type volume_access_group_lun_max: int

    :param volume_access_group_name_length_max: [required]  
    :type volume_access_group_name_length_max: int

    :param volume_access_group_name_length_min: [required]  
    :type volume_access_group_name_length_min: int

    :param volume_access_groups_per_initiator_count_max: [required]  
    :type volume_access_groups_per_initiator_count_max: int

    :param volume_access_groups_per_volume_count_max: [required]  
    :type volume_access_groups_per_volume_count_max: int

    :param initiator_alias_length_max: [required]  
    :type initiator_alias_length_max: int

    :param volume_burst_iopsmax: [required]  
    :type volume_burst_iopsmax: int

    :param volume_burst_iopsmin: [required]  
    :type volume_burst_iopsmin: int

    :param volume_count_max: [required]  
    :type volume_count_max: int

    :param volume_max_iopsmax: [required]  
    :type volume_max_iopsmax: int

    :param volume_max_iopsmin: [required]  
    :type volume_max_iopsmin: int

    :param volume_min_iopsmax: [required]  
    :type volume_min_iopsmax: int

    :param volume_min_iopsmin: [required]  
    :type volume_min_iopsmin: int

    :param volume_name_length_max: [required]  
    :type volume_name_length_max: int

    :param volume_name_length_min: [required]  
    :type volume_name_length_min: int

    :param volume_size_max: [required]  
    :type volume_size_max: int

    :param volume_size_min: [required]  
    :type volume_size_min: int

    :param volumes_per_account_count_max: [required]  
    :type volumes_per_account_count_max: int

    :param volumes_per_group_snapshot_max: [required]  
    :type volumes_per_group_snapshot_max: int

    :param volumes_per_volume_access_group_count_max: [required]  
    :type volumes_per_volume_access_group_count_max: int

    :param cluster_admin_account_max:   
    :type cluster_admin_account_max: int

    :param fibre_channel_volume_access_max:   
    :type fibre_channel_volume_access_max: int

    :param virtual_volumes_per_account_count_max:   
    :type virtual_volumes_per_account_count_max: int

    :param virtual_volume_count_max:   
    :type virtual_volume_count_max: int

    """
    account_count_max = data_model.property(
        "accountCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    account_name_length_max = data_model.property(
        "accountNameLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    account_name_length_min = data_model.property(
        "accountNameLengthMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bulk_volume_jobs_per_node_max = data_model.property(
        "bulkVolumeJobsPerNodeMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    bulk_volume_jobs_per_volume_max = data_model.property(
        "bulkVolumeJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    clone_jobs_per_volume_max = data_model.property(
        "cloneJobsPerVolumeMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_pairs_count_max = data_model.property(
        "clusterPairsCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_name_length_max = data_model.property(
        "initiatorNameLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_count_max = data_model.property(
        "initiatorCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiators_per_volume_access_group_count_max = data_model.property(
        "initiatorsPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    iscsi_sessions_from_fibre_channel_nodes_max = data_model.property(
        "iscsiSessionsFromFibreChannelNodesMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    secret_length_max = data_model.property(
        "secretLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    secret_length_min = data_model.property(
        "secretLengthMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_name_length_max = data_model.property(
        "snapshotNameLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshots_per_volume_max = data_model.property(
        "snapshotsPerVolumeMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_group_count_max = data_model.property(
        "volumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_group_lun_max = data_model.property(
        "volumeAccessGroupLunMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_group_name_length_max = data_model.property(
        "volumeAccessGroupNameLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_group_name_length_min = data_model.property(
        "volumeAccessGroupNameLengthMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_groups_per_initiator_count_max = data_model.property(
        "volumeAccessGroupsPerInitiatorCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_access_groups_per_volume_count_max = data_model.property(
        "volumeAccessGroupsPerVolumeCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    initiator_alias_length_max = data_model.property(
        "initiatorAliasLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_burst_iopsmax = data_model.property(
        "volumeBurstIOPSMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_burst_iopsmin = data_model.property(
        "volumeBurstIOPSMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_count_max = data_model.property(
        "volumeCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_max_iopsmax = data_model.property(
        "volumeMaxIOPSMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_max_iopsmin = data_model.property(
        "volumeMaxIOPSMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_min_iopsmax = data_model.property(
        "volumeMinIOPSMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_min_iopsmin = data_model.property(
        "volumeMinIOPSMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_name_length_max = data_model.property(
        "volumeNameLengthMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_name_length_min = data_model.property(
        "volumeNameLengthMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_size_max = data_model.property(
        "volumeSizeMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volume_size_min = data_model.property(
        "volumeSizeMin", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volumes_per_account_count_max = data_model.property(
        "volumesPerAccountCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volumes_per_group_snapshot_max = data_model.property(
        "volumesPerGroupSnapshotMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    volumes_per_volume_access_group_count_max = data_model.property(
        "volumesPerVolumeAccessGroupCountMax", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    cluster_admin_account_max = data_model.property(
        "clusterAdminAccountMax", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    fibre_channel_volume_access_max = data_model.property(
        "fibreChannelVolumeAccessMax", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volumes_per_account_count_max = data_model.property(
        "virtualVolumesPerAccountCountMax", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    virtual_volume_count_max = data_model.property(
        "virtualVolumeCountMax", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToGroupSnapshotRequest(data_model.DataObject):
    """RollbackToGroupSnapshotRequest  
    RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot.
    Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot.
    Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.

    :param group_snapshot_id: [required] Specifies the unique ID of the group snapshot. 
    :type group_snapshot_id: int

    :param save_current_state: [required] Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 
    :type save_current_state: bool

    :param name:  Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Specifies the unique ID of the group snapshot.&#x27;]",
        dictionaryType=None
    )
    save_current_state = data_model.property(
        "saveCurrentState", bool,
        array=False, optional=False,
        documentation="[&#x27;Specifies whether to save an active volume image or delete it. Values are:&#x27;, &#x27;true: The previous active volume image is kept.&#x27;, &#x27;false: (default) The previous active volume image is deleted.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=True,
        documentation="[&quot;Name for the group snapshot of the volume&#x27;s&quot;, &#x27;current state that is created if &quot;saveCurrentState&quot; is&#x27;, &#x27;set to true. If you do not give a name, the&#x27;, &#x27;name of the snapshots (group and individual&#x27;, &#x27;volume) are set to a timestamp of the time that&#x27;, &#x27;the rollback occurred.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetBackupTargetRequest(data_model.DataObject):
    """GetBackupTargetRequest  
    GetBackupTarget enables you to return information about a specific backup target that you have created.

    :param backup_target_id: [required] The unique identifier assigned to the backup target. 
    :type backup_target_id: int

    """
    backup_target_id = data_model.property(
        "backupTargetID", int,
        array=False, optional=False,
        documentation="[&#x27;The unique identifier assigned to the backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RollbackToGroupSnapshotResult(data_model.DataObject):
    """RollbackToGroupSnapshotResult  

    :param group_snapshot:   
    :type group_snapshot: GroupSnapshot

    :param group_snapshot_id:  Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param members:  List of checksum, volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;Unique ID of the new group snapshot.&#x27;]",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=True,
        documentation="[&#x27;List of checksum, volumeIDs and snapshotIDs for each member of the group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteSnapshotResult(data_model.DataObject):
    """DeleteSnapshotResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class IpmiInfo(data_model.DataObject):
    """IpmiInfo  

    :param sensors: [required]  
    :type sensors: dict

    """
    sensors = data_model.property(
        "sensors", dict,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoNodesResultObject(data_model.DataObject):
    """GetIpmiInfoNodesResultObject  

    :param ipmi_info: [required]  
    :type ipmi_info: IpmiInfo

    """
    ipmi_info = data_model.property(
        "ipmiInfo", IpmiInfo,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoNodesResult(data_model.DataObject):
    """GetIpmiInfoNodesResult  

    :param node_id: [required]  
    :type node_id: int

    :param result: [required]  
    :type result: GetIpmiInfoNodesResultObject

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetIpmiInfoNodesResultObject,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetIpmiInfoResult(data_model.DataObject):
    """GetIpmiInfoResult  

    :param nodes: [required] Detailed information from each sensor within a node.  
    :type nodes: GetIpmiInfoNodesResult

    """
    nodes = data_model.property(
        "nodes", GetIpmiInfoNodesResult,
        array=True, optional=False,
        documentation="[&#x27;Detailed information from each sensor within a node. &#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DeleteStorageContainerResult(data_model.DataObject):
    """DeleteStorageContainerResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeTasksRequest(data_model.DataObject):
    """ListVirtualVolumeTasksRequest  
    ListVirtualVolumeTasks returns a list of virtual volume tasks in the system.

    :param virtual_volume_task_ids:  A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. 
    :type virtual_volume_task_ids: UUID

    """
    virtual_volume_task_ids = data_model.property(
        "virtualVolumeTaskIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestDrivesRequest(data_model.DataObject):
    """TestDrivesRequest  
    You can use the TestDrives API method to run a hardware validation on all drives on the node. This method detects hardware
    failures on the drives (if present) and reports them in the results of the validation tests.
    You can only use the TestDrives method on nodes that are not "active" in a cluster.
    Note: This test takes approximately 10 minutes.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param minutes:  Specifies the number of minutes to run the test. 
    :type minutes: int

    """
    minutes = data_model.property(
        "minutes", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the number of minutes to run the test.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeAccessGroupLunAssignmentsResult(data_model.DataObject):
    """ModifyVolumeAccessGroupLunAssignmentsResult  

    :param volume_access_group_lun_assignments: [required]  
    :type volume_access_group_lun_assignments: VolumeAccessGroupLunAssignments

    """
    volume_access_group_lun_assignments = data_model.property(
        "volumeAccessGroupLunAssignments", VolumeAccessGroupLunAssignments,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Signature(data_model.DataObject):
    """Signature  

    :param data: [required]  
    :type data: str

    :param pubkey: [required]  
    :type pubkey: str

    :param version: [required]  
    :type version: int

    """
    data = data_model.property(
        "data", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    pubkey = data_model.property(
        "pubkey", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Origin(data_model.DataObject):
    """Origin  

    :param signature: [required]  
    :type signature: Signature

    :param contract_date: [required]  
    :type contract_date: str

    :param contract_name: [required]  
    :type contract_name: str

    :param contract_quantity: [required]  
    :type contract_quantity: int

    :param contract_type: [required]  
    :type contract_type: str

    :param integrator: [required]  
    :type integrator: str

    :param location: [required]  
    :type location: str

    :param organization: [required]  
    :type organization: str

    :param type: [required]  
    :type type: str

    """
    signature = data_model.property(
        "<signature>", Signature,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    contract_date = data_model.property(
        "contract-date", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    contract_name = data_model.property(
        "contract-name", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    contract_quantity = data_model.property(
        "contract-quantity", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    contract_type = data_model.property(
        "contract-type", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    integrator = data_model.property(
        "integrator", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    location = data_model.property(
        "location", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    organization = data_model.property(
        "organization", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginNodeResult(data_model.DataObject):
    """GetOriginNodeResult  

    :param origin:   
    :type origin: Origin

    """
    origin = data_model.property(
        "origin", Origin,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginNode(data_model.DataObject):
    """GetOriginNode  

    :param node_id: [required]  
    :type node_id: int

    :param result: [required]  
    :type result: GetOriginNodeResult

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", GetOriginNodeResult,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetOriginResult(data_model.DataObject):
    """GetOriginResult  

    :param nodes: [required]  
    :type nodes: GetOriginNode

    """
    nodes = data_model.property(
        "nodes", GetOriginNode,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ClusterInfo(data_model.DataObject):
    """ClusterInfo  
    Cluster Info object returns information the node uses to communicate with the cluster.

    :param mvip_interface:   
    :type mvip_interface: str

    :param mvip_vlan_tag:   
    :type mvip_vlan_tag: str

    :param svip_interface:   
    :type svip_interface: str

    :param svip_vlan_tag:   
    :type svip_vlan_tag: str

    :param encryption_at_rest_state: [required] Encryption at rest state. 
    :type encryption_at_rest_state: str

    :param ensemble: [required] Array of Node IP addresses that are participating in the cluster. 
    :type ensemble: str

    :param mvip: [required] Management network interface. 
    :type mvip: str

    :param mvip_node_id: [required] Node holding the master MVIP address 
    :type mvip_node_id: int

    :param name: [required] Unique cluster name. 
    :type name: str

    :param rep_count: [required] Number of replicas of each piece of data to store in the cluster. Valid value is 2 
    :type rep_count: int

    :param svip: [required] Storage virtual IP 
    :type svip: str

    :param svip_node_id: [required] Node holding the master SVIP address. 
    :type svip_node_id: int

    :param unique_id: [required] Unique ID for the cluster. 
    :type unique_id: str

    :param uuid: [required]  
    :type uuid: UUID

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    mvip_interface = data_model.property(
        "mvipInterface", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    mvip_vlan_tag = data_model.property(
        "mvipVlanTag", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    svip_interface = data_model.property(
        "svipInterface", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    svip_vlan_tag = data_model.property(
        "svipVlanTag", str,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    encryption_at_rest_state = data_model.property(
        "encryptionAtRestState", str,
        array=False, optional=False,
        documentation="[&#x27;Encryption at rest state.&#x27;]",
        dictionaryType=None
    )
    ensemble = data_model.property(
        "ensemble", str,
        array=True, optional=False,
        documentation="[&#x27;Array of Node IP addresses that are participating in the cluster.&#x27;]",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="[&#x27;Management network interface.&#x27;]",
        dictionaryType=None
    )
    mvip_node_id = data_model.property(
        "mvipNodeID", int,
        array=False, optional=False,
        documentation="[&#x27;Node holding the master MVIP address&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;Unique cluster name.&#x27;]",
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="[&#x27;Number of replicas of each piece of data to store in the cluster.&#x27;, &#x27;Valid value is 2&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Storage virtual IP&#x27;]",
        dictionaryType=None
    )
    svip_node_id = data_model.property(
        "svipNodeID", int,
        array=False, optional=False,
        documentation="[&#x27;Node holding the master SVIP address.&#x27;]",
        dictionaryType=None
    )
    unique_id = data_model.property(
        "uniqueID", str,
        array=False, optional=False,
        documentation="[&#x27;Unique ID for the cluster.&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterInfoResult(data_model.DataObject):
    """GetClusterInfoResult  

    :param cluster_info: [required]  
    :type cluster_info: ClusterInfo

    """
    cluster_info = data_model.property(
        "clusterInfo", ClusterInfo,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActivePairedVolumesRequest(data_model.DataObject):
    """ListActivePairedVolumesRequest  
    ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings.

    :param start_volume_id:  The beginning of the range of active paired volumes to return. 
    :type start_volume_id: int

    :param limit:  Maximum number of active paired volumes to return. 
    :type limit: int

    """
    start_volume_id = data_model.property(
        "startVolumeID", int,
        array=False, optional=True,
        documentation="[&#x27;The beginning of the range of active paired volumes to return.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;Maximum number of active paired volumes to return.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class StartBulkVolumeWriteResult(data_model.DataObject):
    """StartBulkVolumeWriteResult  

    :param async_handle: [required] ID of the async process to be checked for completion. 
    :type async_handle: int

    :param key: [required] Opaque key uniquely identifying the session. 
    :type key: str

    :param url: [required] URL to access the node's web server 
    :type url: str

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;ID of the async process to be checked for completion.&#x27;]",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="[&#x27;Opaque key uniquely identifying the session.&#x27;]",
        dictionaryType=None
    )
    url = data_model.property(
        "url", str,
        array=False, optional=False,
        documentation="[&quot;URL to access the node&#x27;s web server&quot;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Service(data_model.DataObject):
    """Service  

    :param service_id: [required] Unique identifier for this service. 
    :type service_id: int

    :param service_type: [required]  
    :type service_type: str

    :param node_id: [required] The node this service resides on. 
    :type node_id: int

    :param associated_bv:  This service's associated bulk volume service. This will only be set if the service type is a slice service. 
    :type associated_bv: int

    :param associated_ts:  This service's associated transport service. This will only be set if the service type is a slice service. 
    :type associated_ts: int

    :param associated_vs:  This service's associated volume service. This will only be set if the service type is a slice service. 
    :type associated_vs: int

    :param async_result_ids: [required] The list of asynchronous jobs currently running for this service. 
    :type async_result_ids: int

    :param drive_id:  If this service resides on a drive, the ID of that drive. 
    :type drive_id: int

    :param first_time_startup: [required] Has this service started successfully? When a new drive is added to the system, the created service will initially have a value of false here. After the service has started, this value will be set to true. This can be used to check if the service has ever started. 
    :type first_time_startup: bool

    :param ipc_port: [required] The port used for intra-cluster communication. This will be in the 4000-4100 range. 
    :type ipc_port: int

    :param iscsi_port: [required] The port used for iSCSI traffic. This will only be set if the service type is a transport service. 
    :type iscsi_port: int

    :param status: [required]  
    :type status: str

    :param started_drive_ids: [required]  
    :type started_drive_ids: int

    :param drive_ids: [required]  
    :type drive_ids: int

    """
    service_id = data_model.property(
        "serviceID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier for this service.&#x27;]",
        dictionaryType=None
    )
    service_type = data_model.property(
        "serviceType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The node this service resides on.&#x27;]",
        dictionaryType=None
    )
    associated_bv = data_model.property(
        "associatedBV", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated bulk volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    associated_ts = data_model.property(
        "associatedTS", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated transport service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    associated_vs = data_model.property(
        "associatedVS", int,
        array=False, optional=True,
        documentation="[&quot;This service&#x27;s associated volume service.&quot;, &#x27;This will only be set if the service type is a slice service.&#x27;]",
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="[&#x27;The list of asynchronous jobs currently running for this service.&#x27;]",
        dictionaryType=None
    )
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=True,
        documentation="[&#x27;If this service resides on a drive, the ID of that drive.&#x27;]",
        dictionaryType=None
    )
    first_time_startup = data_model.property(
        "firstTimeStartup", bool,
        array=False, optional=False,
        documentation="[&#x27;Has this service started successfully?&#x27;, &#x27;When a new drive is added to the system, the created service will initially have a value of false here.&#x27;, &#x27;After the service has started, this value will be set to true.&#x27;, &#x27;This can be used to check if the service has ever started.&#x27;]",
        dictionaryType=None
    )
    ipc_port = data_model.property(
        "ipcPort", int,
        array=False, optional=False,
        documentation="[&#x27;The port used for intra-cluster communication.&#x27;, &#x27;This will be in the 4000-4100 range.&#x27;]",
        dictionaryType=None
    )
    iscsi_port = data_model.property(
        "iscsiPort", int,
        array=False, optional=False,
        documentation="[&#x27;The port used for iSCSI traffic.&#x27;, &#x27;This will only be set if the service type is a transport service.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    started_drive_ids = data_model.property(
        "startedDriveIDs", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_ids = data_model.property(
        "driveIDs", int,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class Drive(data_model.DataObject):
    """Drive  

    :param drive_id: [required] A unique identifier for this drive. 
    :type drive_id: int

    :param node_id: [required] The node this drive is located. If the drive has been physically removed from the node, this is where it was last seen. 
    :type node_id: int

    :param assigned_service:  If this drive is hosting a service, the identifier for that service. 
    :type assigned_service: int

    :param async_result_ids: [required] The list of asynchronous jobs currently running on the drive (for example: a secure erase job). 
    :type async_result_ids: int

    :param capacity: [required] The raw capacity of this drive in bytes. 
    :type capacity: int

    :param serial: [required] The manufacturer's serial number for this drive. 
    :type serial: str

    :param slot:  Slot number in the server chassis where this drive is located. If the drive has been physically removed from the node, this will not have a value. 
    :type slot: int

    :param drive_status: [required] The current status of this drive. 
    :type drive_status: str

    :param drive_type: [required] The type of this drive. 
    :type drive_type: str

    :param reserved_slice_file_capacity:   
    :type reserved_slice_file_capacity: int

    :param customer_slice_file_capacity:   
    :type customer_slice_file_capacity: int

    :param attributes: [required] List of Name/Value pairs in JSON object format. 
    :type attributes: dict

    """
    drive_id = data_model.property(
        "driveID", int,
        array=False, optional=False,
        documentation="[&#x27;A unique identifier for this drive.&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[&#x27;The node this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this is where it was last seen.&#x27;]",
        dictionaryType=None
    )
    assigned_service = data_model.property(
        "assignedService", int,
        array=False, optional=True,
        documentation="[&#x27;If this drive is hosting a service, the identifier for that service.&#x27;]",
        dictionaryType=None
    )
    async_result_ids = data_model.property(
        "asyncResultIDs", int,
        array=True, optional=False,
        documentation="[&#x27;The list of asynchronous jobs currently running on the drive (for example: a secure erase job).&#x27;]",
        dictionaryType=None
    )
    capacity = data_model.property(
        "capacity", int,
        array=False, optional=False,
        documentation="[&#x27;The raw capacity of this drive in bytes.&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[&quot;The manufacturer&#x27;s serial number for this drive.&quot;]",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=True,
        documentation="[&#x27;Slot number in the server chassis where this drive is located.&#x27;, &#x27;If the drive has been physically removed from the node, this will not have a value.&#x27;]",
        dictionaryType=None
    )
    drive_status = data_model.property(
        "driveStatus", str,
        array=False, optional=False,
        documentation="[&#x27;The current status of this drive.&#x27;]",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="[&#x27;The type of this drive.&#x27;]",
        dictionaryType=None
    )
    reserved_slice_file_capacity = data_model.property(
        "reservedSliceFileCapacity", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    customer_slice_file_capacity = data_model.property(
        "customerSliceFileCapacity", int,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;List of Name/Value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DetailedService(data_model.DataObject):
    """DetailedService  

    :param service: [required]  
    :type service: Service

    :param node: [required]  
    :type node: Node

    :param drive:   
    :type drive: Drive

    :param drives: [required]  
    :type drives: Drive

    """
    service = data_model.property(
        "service", Service,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node = data_model.property(
        "node", Node,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive = data_model.property(
        "drive", Drive,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drives = data_model.property(
        "drives", Drive,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListServicesResult(data_model.DataObject):
    """ListServicesResult  

    :param services: [required]  
    :type services: DetailedService

    """
    services = data_model.property(
        "services", DetailedService,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListActiveNodesResult(data_model.DataObject):
    """ListActiveNodesResult  

    :param nodes: [required]  
    :type nodes: Node

    """
    nodes = data_model.property(
        "nodes", Node,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListBackupTargetsResult(data_model.DataObject):
    """ListBackupTargetsResult  

    :param backup_targets: [required] Objects returned for each backup target. 
    :type backup_targets: BackupTarget

    """
    backup_targets = data_model.property(
        "backupTargets", BackupTarget,
        array=True, optional=False,
        documentation="[&#x27;Objects returned for each backup target.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SnmpSendTestTrapsResult(data_model.DataObject):
    """SnmpSendTestTrapsResult  

    :param status: [required]  
    :type status: str

    """
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVirtualVolumeBindingsRequest(data_model.DataObject):
    """ListVirtualVolumeBindingsRequest  
    ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints.

    :param virtual_volume_binding_ids:  A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. 
    :type virtual_volume_binding_ids: int

    """
    virtual_volume_binding_ids = data_model.property(
        "virtualVolumeBindingIDs", int,
        array=True, optional=True,
        documentation="[&#x27;A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeStatsByAccountRequest(data_model.DataObject):
    """ListVolumeStatsByAccountRequest  
    ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account.

    :param accounts:  One or more account ids by which to filter the result. 
    :type accounts: int

    :param include_virtual_volumes:  Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. 
    :type include_virtual_volumes: bool

    """
    accounts = data_model.property(
        "accounts", int,
        array=True, optional=True,
        documentation="[&#x27;One or more account ids by which to filter the result.&#x27;]",
        dictionaryType=None
    )
    include_virtual_volumes = data_model.property(
        "includeVirtualVolumes", bool,
        array=False, optional=True,
        documentation="[&#x27;Includes virtual volumes in the response by default. To exclude virtual volumes, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpACLResult(data_model.DataObject):
    """GetSnmpACLResult  

    :param networks:  List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled. 
    :type networks: SnmpNetwork

    :param usm_users:  List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=True,
        documentation="[&#x27;List of networks and what type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is disabled.&#x27;]",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=True,
        documentation="[&#x27;List of users and the type of access they have to the SNMP servers running on the cluster nodes. Present if SNMP v3 is enabled.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVirtualNetworkResult(data_model.DataObject):
    """RemoveVirtualNetworkResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableSnmpRequest(data_model.DataObject):
    """EnableSnmpRequest  
    EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and
    the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.

    :param snmp_v3_enabled: [required] If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. 
    :type snmp_v3_enabled: bool

    """
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If set to &quot;true&quot;, then SNMP v3 is enabled on each node in the&#x27;, &#x27;cluster. If set to &quot;false&quot;, then SNMP v2 is enabled.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpInfoResult(data_model.DataObject):
    """SetSnmpInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DisableLdapAuthenticationResult(data_model.DataObject):
    """DisableLdapAuthenticationResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSnapshotsResult(data_model.DataObject):
    """ListSnapshotsResult  

    :param snapshots: [required] Information about each snapshot for each volume. If volumeID is not provided, all snapshots for all volumes is returned. Snapshots that are in a group will be returned with a "groupID". Snapshots that are enabled for replication. 
    :type snapshots: Snapshot

    """
    snapshots = data_model.property(
        "snapshots", Snapshot,
        array=True, optional=False,
        documentation="[&#x27;Information about each snapshot for each volume.&#x27;, &#x27;If volumeID is not provided, all snapshots for all volumes is returned.&#x27;, &#x27;Snapshots that are in a group will be returned with a &quot;groupID&quot;.&#x27;, &#x27;Snapshots that are enabled for replication.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyInitiatorsResult(data_model.DataObject):
    """ModifyInitiatorsResult  

    :param initiators: [required] List of objects containing details about the modified initiators 
    :type initiators: Initiator

    """
    initiators = data_model.property(
        "initiators", Initiator,
        array=True, optional=False,
        documentation="[&#x27;List of objects containing details about the modified initiators&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateClusterRequest(data_model.DataObject):
    """CreateClusterRequest  
    The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized.
    Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the
    cluster. Then, run the CreateCluster method.

    :param accept_eula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param mvip: [required] Floating (virtual) IP address for the cluster on the management network. 
    :type mvip: str

    :param svip: [required] Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 
    :type svip: str

    :param rep_count: [required] Number of replicas of each piece of data to store in the cluster. Valid value is "2". 
    :type rep_count: int

    :param username: [required] Username for the cluster admin. 
    :type username: str

    :param password: [required] Initial password for the cluster admin account. 
    :type password: str

    :param nodes: [required] CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 
    :type nodes: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="[&#x27;Required to indicate your acceptance of the End User License&#x27;, &#x27;Agreement when creating this cluster. To accept the EULA,&#x27;, &#x27;set this parameter to true.&#x27;]",
        dictionaryType=None
    )
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=False,
        documentation="[&#x27;Floating (virtual) IP address for the cluster on the management network.&#x27;]",
        dictionaryType=None
    )
    svip = data_model.property(
        "svip", str,
        array=False, optional=False,
        documentation="[&#x27;Floating (virtual) IP address for the cluster on the storage (iSCSI) network.&#x27;]",
        dictionaryType=None
    )
    rep_count = data_model.property(
        "repCount", int,
        array=False, optional=False,
        documentation="[&#x27;Number of replicas of each piece of data to store in the cluster. Valid value is &quot;2&quot;.&#x27;]",
        dictionaryType=None
    )
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;Username for the cluster admin.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="[&#x27;Initial password for the cluster admin account.&#x27;]",
        dictionaryType=None
    )
    nodes = data_model.property(
        "nodes", str,
        array=True, optional=False,
        documentation="[&quot;CIP/SIP addresses of the initial set of nodes making up the cluster. This node&#x27;s IP must be in the list.&quot;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListEventsRequest(data_model.DataObject):
    """ListEventsRequest  
    ListEvents returns events detected on the cluster, sorted from oldest to newest.

    :param max_events:  Specifies the maximum number of events to return. 
    :type max_events: int

    :param start_event_id:  Identifies the beginning of a range of events to return. 
    :type start_event_id: int

    :param end_event_id:  Identifies the end of a range of events to return. 
    :type end_event_id: int

    """
    max_events = data_model.property(
        "maxEvents", int,
        array=False, optional=True,
        documentation="[&#x27;Specifies the maximum number of events to return.&#x27;]",
        dictionaryType=None
    )
    start_event_id = data_model.property(
        "startEventID", int,
        array=False, optional=True,
        documentation="[&#x27;Identifies the beginning of a range of events to return.&#x27;]",
        dictionaryType=None
    )
    end_event_id = data_model.property(
        "endEventID", int,
        array=False, optional=True,
        documentation="[&#x27;Identifies the end of a range of events to return.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumesResult(data_model.DataObject):
    """PurgeDeletedVolumesResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListProtocolEndpointsRequest(data_model.DataObject):
    """ListProtocolEndpointsRequest  
    ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern
    access to their associated virtual volume storage containers.

    :param protocol_endpoint_ids:  A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. 
    :type protocol_endpoint_ids: UUID

    """
    protocol_endpoint_ids = data_model.property(
        "protocolEndpointIDs", UUID,
        array=True, optional=True,
        documentation="[&#x27;A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListVolumeAccessGroupsResult(data_model.DataObject):
    """ListVolumeAccessGroupsResult  

    :param volume_access_groups: [required] A list of objects describing each volume access group. 
    :type volume_access_groups: VolumeAccessGroup

    :param volume_access_groups_not_found:  A list of volume access groups not found by the system. Present if you used the "volumeAccessGroups" parameter and the system was unable to find one or more volume access groups that you specified. 
    :type volume_access_groups_not_found: int

    """
    volume_access_groups = data_model.property(
        "volumeAccessGroups", VolumeAccessGroup,
        array=True, optional=False,
        documentation="[&#x27;A list of objects describing each volume access group.&#x27;]",
        dictionaryType=None
    )
    volume_access_groups_not_found = data_model.property(
        "volumeAccessGroupsNotFound", int,
        array=True, optional=True,
        documentation="[&#x27;A list of volume access groups not found by the system. Present if you used the &quot;volumeAccessGroups&quot; parameter and the system was unable to find one or more volume access groups that you specified.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestLdapAuthenticationResult(data_model.DataObject):
    """TestLdapAuthenticationResult  

    :param groups: [required] List of LDAP groups that the tested user is a member of. 
    :type groups: str

    :param user_dn: [required] The tested user's full LDAP distinguished name. 
    :type user_dn: str

    """
    groups = data_model.property(
        "groups", str,
        array=True, optional=False,
        documentation="[&#x27;List of LDAP groups that the tested user is a member of.&#x27;]",
        dictionaryType=None
    )
    user_dn = data_model.property(
        "userDN", str,
        array=False, optional=False,
        documentation="[&quot;The tested user&#x27;s full LDAP distinguished name.&quot;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsResult(data_model.DataObject):
    """ListAccountsResult  

    :param accounts: [required] List of accounts. 
    :type accounts: Account

    """
    accounts = data_model.property(
        "accounts", Account,
        array=True, optional=False,
        documentation="[&#x27;List of accounts.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetSnmpACLRequest(data_model.DataObject):
    """SetSnmpACLRequest  
    SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all
    nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note
    that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo.

    :param networks: [required] List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled. 
    :type networks: SnmpNetwork

    :param usm_users: [required] List of users and the type of access they have to the SNMP servers running on the cluster nodes. 
    :type usm_users: SnmpV3UsmUser

    """
    networks = data_model.property(
        "networks", SnmpNetwork,
        array=True, optional=False,
        documentation="[&#x27;List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP&#x27;, &#x27;Network Object for possible &quot;networks&quot; values. This parameter is required if SNMP v3 is disabled.&#x27;]",
        dictionaryType=None
    )
    usm_users = data_model.property(
        "usmUsers", SnmpV3UsmUser,
        array=True, optional=False,
        documentation="[&#x27;List of users and the type of access they have to the SNMP servers running on the cluster nodes.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GroupCloneVolumeMember(data_model.DataObject):
    """GroupCloneVolumeMember  
    Represents the relationship between the source Volume and cloned Volume IDs.

    :param volume_id: [required] The VolumeID of the cloned volume. 
    :type volume_id: int

    :param src_volume_id: [required] The VolumeID of the source volume. 
    :type src_volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The VolumeID of the cloned volume.&#x27;]",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The VolumeID of the source volume.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneMultipleVolumesResult(data_model.DataObject):
    """CloneMultipleVolumesResult  

    :param async_handle: [required] A value returned from an asynchronous method call. 
    :type async_handle: int

    :param group_clone_id: [required] Unique ID of the new group clone. 
    :type group_clone_id: int

    :param members: [required] List of volumeIDs for the source and destination volume pairs. 
    :type members: GroupCloneVolumeMember

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[&#x27;A value returned from an asynchronous method call.&#x27;]",
        dictionaryType=None
    )
    group_clone_id = data_model.property(
        "groupCloneID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of the new group clone.&#x27;]",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupCloneVolumeMember,
        array=True, optional=False,
        documentation="[&#x27;List of volumeIDs for the source and destination volume pairs.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveVolumePairRequest(data_model.DataObject):
    """RemoveVolumePairRequest  
    RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume.

    :param volume_id: [required] The ID of the volume on which to stop the replication process. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume on which to stop the replication process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetStorageContainerEfficiencyResult(data_model.DataObject):
    """GetStorageContainerEfficiencyResult  

    :param compression: [required]  
    :type compression: float

    :param deduplication: [required]  
    :type deduplication: float

    :param missing_volumes: [required] The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle. 
    :type missing_volumes: int

    :param thin_provisioning: [required]  
    :type thin_provisioning: float

    :param timestamp: [required] The last time efficiency data was collected after Garbage Collection (GC). 
    :type timestamp: str

    """
    compression = data_model.property(
        "compression", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    deduplication = data_model.property(
        "deduplication", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    missing_volumes = data_model.property(
        "missingVolumes", int,
        array=True, optional=False,
        documentation="[&#x27;The volumes that could not be queried for efficiency data. Missing volumes can be caused by the Garbage Collection (GC) cycle being less than an hour old, temporary loss of network connectivity, or restarted services since the GC cycle.&#x27;]",
        dictionaryType=None
    )
    thin_provisioning = data_model.property(
        "thinProvisioning", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    timestamp = data_model.property(
        "timestamp", str,
        array=False, optional=False,
        documentation="[&#x27;The last time efficiency data was collected after Garbage Collection (GC).&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetLoginSessionInfoResult(data_model.DataObject):
    """SetLoginSessionInfoResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AsyncHandleResult(data_model.DataObject):
    """AsyncHandleResult  

    :param async_handle: [required]  
    :type async_handle: int

    """
    async_handle = data_model.property(
        "asyncHandle", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class PurgeDeletedVolumeRequest(data_model.DataObject):
    """PurgeDeletedVolumeRequest  
    PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using
    DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not
    typically required.

    :param volume_id: [required] The ID of the volume to be purged. 
    :type volume_id: int

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume to be purged.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SyncJob(data_model.DataObject):
    """SyncJob  

    :param bytes_per_second: [required]  
    :type bytes_per_second: float

    :param current_bytes: [required]  
    :type current_bytes: int

    :param dst_service_id: [required]  
    :type dst_service_id: int

    :param elapsed_time: [required]  
    :type elapsed_time: float

    :param percent_complete: [required]  
    :type percent_complete: float

    :param remaining_time: [required]  
    :type remaining_time: float

    :param slice_id: [required]  
    :type slice_id: int

    :param src_service_id: [required]  
    :type src_service_id: int

    :param total_bytes: [required]  
    :type total_bytes: int

    :param type: [required]  
    :type type: str

    :param clone_id: [required]  
    :type clone_id: int

    :param dst_volume_id: [required]  
    :type dst_volume_id: int

    :param node_id: [required]  
    :type node_id: int

    :param snapshot_id: [required]  
    :type snapshot_id: int

    :param src_volume_id: [required]  
    :type src_volume_id: int

    :param blocks_per_second: [required]  
    :type blocks_per_second: float

    :param stage: [required]  
    :type stage: str

    """
    bytes_per_second = data_model.property(
        "bytesPerSecond", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    current_bytes = data_model.property(
        "currentBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dst_service_id = data_model.property(
        "dstServiceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    slice_id = data_model.property(
        "sliceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    src_service_id = data_model.property(
        "srcServiceID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    total_bytes = data_model.property(
        "totalBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    clone_id = data_model.property(
        "cloneID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dst_volume_id = data_model.property(
        "dstVolumeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    blocks_per_second = data_model.property(
        "blocksPerSecond", float,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    stage = data_model.property(
        "stage", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListSyncJobsResult(data_model.DataObject):
    """ListSyncJobsResult  

    :param sync_jobs: [required]  
    :type sync_jobs: SyncJob

    """
    sync_jobs = data_model.property(
        "syncJobs", SyncJob,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class BulkVolumeJob(data_model.DataObject):
    """BulkVolumeJob  

    :param bulk_volume_id: [required] The internal bulk volume job ID. 
    :type bulk_volume_id: int

    :param create_time: [required] Timestamp created for the bulk volume job. 
    :type create_time: str

    :param elapsed_time: [required] The number of seconds since the job began. 
    :type elapsed_time: int

    :param format: [required] Format is either "compressed" or "native". 
    :type format: str

    :param key: [required] The unique key created by the bulk volume session. 
    :type key: str

    :param percent_complete: [required] The completed percentage reported by the operation. 
    :type percent_complete: int

    :param remaining_time: [required] The estimated time remaining in seconds. 
    :type remaining_time: int

    :param src_volume_id: [required] The source volume ID. 
    :type src_volume_id: int

    :param status: [required] Can be one of the following: preparing active done failed 
    :type status: str

    :param script:  The name of the script if one is provided. 
    :type script: str

    :param snapshot_id:  ID of the snapshot if a snapshot is in the source of the bulk volume job. 
    :type snapshot_id: int

    :param type: [required] Can be one of the following: read write 
    :type type: str

    :param attributes: [required] JSON attributes on the bulk volume job. 
    :type attributes: dict

    """
    bulk_volume_id = data_model.property(
        "bulkVolumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The internal bulk volume job ID.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=False,
        documentation="[&#x27;Timestamp created for the bulk volume job.&#x27;]",
        dictionaryType=None
    )
    elapsed_time = data_model.property(
        "elapsedTime", int,
        array=False, optional=False,
        documentation="[&#x27;The number of seconds since the job began.&#x27;]",
        dictionaryType=None
    )
    format = data_model.property(
        "format", str,
        array=False, optional=False,
        documentation="[&#x27;Format is either &quot;compressed&quot; or &quot;native&quot;.&#x27;]",
        dictionaryType=None
    )
    key = data_model.property(
        "key", str,
        array=False, optional=False,
        documentation="[&#x27;The unique key created by the bulk volume session.&#x27;]",
        dictionaryType=None
    )
    percent_complete = data_model.property(
        "percentComplete", int,
        array=False, optional=False,
        documentation="[&#x27;The completed percentage reported by the operation.&#x27;]",
        dictionaryType=None
    )
    remaining_time = data_model.property(
        "remainingTime", int,
        array=False, optional=False,
        documentation="[&#x27;The estimated time remaining in seconds.&#x27;]",
        dictionaryType=None
    )
    src_volume_id = data_model.property(
        "srcVolumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The source volume ID.&#x27;]",
        dictionaryType=None
    )
    status = data_model.property(
        "status", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;preparing&#x27;, &#x27;active&#x27;, &#x27;done&#x27;, &#x27;failed&#x27;]",
        dictionaryType=None
    )
    script = data_model.property(
        "script", str,
        array=False, optional=True,
        documentation="[&#x27;The name of the script if one is provided.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the snapshot if a snapshot is in the source of the bulk volume job.&#x27;]",
        dictionaryType=None
    )
    type = data_model.property(
        "type", str,
        array=False, optional=False,
        documentation="[&#x27;Can be one of the following:&#x27;, &#x27;read&#x27;, &#x27;write&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=False,
        documentation="[&#x27;JSON attributes on the bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListBulkVolumeJobsResult(data_model.DataObject):
    """ListBulkVolumeJobsResult  

    :param bulk_volume_jobs: [required] An array of information for each bulk volume job. 
    :type bulk_volume_jobs: BulkVolumeJob

    """
    bulk_volume_jobs = data_model.property(
        "bulkVolumeJobs", BulkVolumeJob,
        array=True, optional=False,
        documentation="[&#x27;An array of information for each bulk volume job.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectMvipRequest(data_model.DataObject):
    """TestConnectMvipRequest  
    The TestConnectMvip API method enables you to test the
    management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param mvip:  If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 
    :type mvip: str

    """
    mvip = data_model.property(
        "mvip", str,
        array=False, optional=True,
        documentation="[&#x27;If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpStateResult(data_model.DataObject):
    """GetSnmpStateResult  

    :param enabled: [required] If the nodes in the cluster are configured for SNMP. 
    :type enabled: bool

    :param snmp_v3_enabled: [required] If the node in the cluster is configured for SNMP v3. 
    :type snmp_v3_enabled: bool

    """
    enabled = data_model.property(
        "enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the nodes in the cluster are configured for SNMP.&#x27;]",
        dictionaryType=None
    )
    snmp_v3_enabled = data_model.property(
        "snmpV3Enabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If the node in the cluster is configured for SNMP v3.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListPendingActiveNodesResult(data_model.DataObject):
    """ListPendingActiveNodesResult  

    :param pending_active_nodes: [required] List of objects detailing information about all PendingActive nodes in the system. 
    :type pending_active_nodes: PendingActiveNode

    """
    pending_active_nodes = data_model.property(
        "pendingActiveNodes", PendingActiveNode,
        array=True, optional=False,
        documentation="[&#x27;List of objects detailing information about all PendingActive nodes in the system.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteVolumePairingRequest(data_model.DataObject):
    """CompleteVolumePairingRequest  
    You can use the CompleteVolumePairing method to complete the pairing of two volumes.

    :param volume_pairing_key: [required] The key returned from the StartVolumePairing method. 
    :type volume_pairing_key: str

    :param volume_id: [required] The ID of the volume on which to complete the pairing process. 
    :type volume_id: int

    """
    volume_pairing_key = data_model.property(
        "volumePairingKey", str,
        array=False, optional=False,
        documentation="[&#x27;The key returned from the StartVolumePairing method.&#x27;]",
        dictionaryType=None
    )
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;The ID of the volume on which to complete the pairing process.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetClusterStateRequest(data_model.DataObject):
    """GetClusterStateRequest  
    The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are:
    Available: Node has not been configured with a cluster name.
    Pending: Node is pending for a specific named cluster and can be added.
    Active: Node is an active member of a cluster and may not be added to another
    cluster.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param force: [required] To run this command, the force parameter must be set to true. 
    :type force: bool

    """
    force = data_model.property(
        "force", bool,
        array=False, optional=False,
        documentation="[&#x27;To run this command, the force parameter must be set to true.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DriveHardware(data_model.DataObject):
    """DriveHardware  

    :param canonical_name: [required]  
    :type canonical_name: str

    :param connected: [required]  
    :type connected: bool

    :param dev: [required]  
    :type dev: int

    :param dev_path: [required]  
    :type dev_path: str

    :param drive_type: [required]  
    :type drive_type: str

    :param life_remaining_percent: [required]  
    :type life_remaining_percent: int

    :param lifetime_read_bytes: [required]  
    :type lifetime_read_bytes: int

    :param lifetime_write_bytes: [required]  
    :type lifetime_write_bytes: int

    :param name: [required]  
    :type name: str

    :param path: [required]  
    :type path: str

    :param path_link: [required]  
    :type path_link: str

    :param power_on_hours: [required]  
    :type power_on_hours: int

    :param product: [required]  
    :type product: str

    :param reallocated_sectors: [required]  
    :type reallocated_sectors: int

    :param reserve_capacity_percent: [required]  
    :type reserve_capacity_percent: int

    :param scsi_compat_id: [required]  
    :type scsi_compat_id: str

    :param scsi_state: [required]  
    :type scsi_state: str

    :param security_at_maximum: [required]  
    :type security_at_maximum: bool

    :param security_enabled: [required]  
    :type security_enabled: bool

    :param security_frozen: [required]  
    :type security_frozen: bool

    :param security_locked: [required]  
    :type security_locked: bool

    :param security_supported: [required]  
    :type security_supported: bool

    :param serial: [required]  
    :type serial: str

    :param size: [required]  
    :type size: int

    :param slot: [required]  
    :type slot: int

    :param smart_ssd_write_capable:   
    :type smart_ssd_write_capable: bool

    :param uuid: [required]  
    :type uuid: UUID

    :param vendor: [required]  
    :type vendor: str

    :param version: [required]  
    :type version: str

    """
    canonical_name = data_model.property(
        "canonicalName", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    connected = data_model.property(
        "connected", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dev = data_model.property(
        "dev", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    dev_path = data_model.property(
        "devPath", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    drive_type = data_model.property(
        "driveType", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    life_remaining_percent = data_model.property(
        "lifeRemainingPercent", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lifetime_read_bytes = data_model.property(
        "lifetimeReadBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    lifetime_write_bytes = data_model.property(
        "lifetimeWriteBytes", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    path = data_model.property(
        "path", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    path_link = data_model.property(
        "pathLink", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    power_on_hours = data_model.property(
        "powerOnHours", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    product = data_model.property(
        "product", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    reallocated_sectors = data_model.property(
        "reallocatedSectors", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    reserve_capacity_percent = data_model.property(
        "reserveCapacityPercent", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_compat_id = data_model.property(
        "scsiCompatId", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    scsi_state = data_model.property(
        "scsiState", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_at_maximum = data_model.property(
        "securityAtMaximum", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_enabled = data_model.property(
        "securityEnabled", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_frozen = data_model.property(
        "securityFrozen", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_locked = data_model.property(
        "securityLocked", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    security_supported = data_model.property(
        "securitySupported", bool,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    serial = data_model.property(
        "serial", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    size = data_model.property(
        "size", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    slot = data_model.property(
        "slot", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    smart_ssd_write_capable = data_model.property(
        "smartSsdWriteCapable", bool,
        array=False, optional=True,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    uuid = data_model.property(
        "uuid", UUID,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    vendor = data_model.property(
        "vendor", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    version = data_model.property(
        "version", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class DrivesHardware(data_model.DataObject):
    """DrivesHardware  

    :param drive_hardware: [required]  
    :type drive_hardware: DriveHardware

    """
    drive_hardware = data_model.property(
        "driveHardware", DriveHardware,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class NodeDriveHardware(data_model.DataObject):
    """NodeDriveHardware  

    :param node_id: [required]  
    :type node_id: int

    :param result: [required]  
    :type result: DrivesHardware

    """
    node_id = data_model.property(
        "nodeID", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", DrivesHardware,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListDriveHardwareResult(data_model.DataObject):
    """ListDriveHardwareResult  

    :param nodes: [required]  
    :type nodes: NodeDriveHardware

    """
    nodes = data_model.property(
        "nodes", NodeDriveHardware,
        array=True, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetNodeHardwareInfoResult(data_model.DataObject):
    """GetNodeHardwareInfoResult  

    :param node_hardware_info: [required] Hardware information for the specified nodeID. 
    :type node_hardware_info: dict

    """
    node_hardware_info = data_model.property(
        "nodeHardwareInfo", dict,
        array=False, optional=False,
        documentation="[&#x27;Hardware information for the specified nodeID.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class GetSnmpTrapInfoResult(data_model.DataObject):
    """GetSnmpTrapInfoResult  

    :param trap_recipients: [required] List of hosts that are to receive the traps generated by the cluster. 
    :type trap_recipients: SnmpTrapRecipient

    :param cluster_fault_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_traps_enabled: bool

    :param cluster_fault_resolved_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. 
    :type cluster_fault_resolved_traps_enabled: bool

    :param cluster_event_traps_enabled: [required] If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. 
    :type cluster_event_traps_enabled: bool

    """
    trap_recipients = data_model.property(
        "trapRecipients", SnmpTrapRecipient,
        array=True, optional=False,
        documentation="[&#x27;List of hosts that are to receive the traps generated by the cluster.&#x27;]",
        dictionaryType=None
    )
    cluster_fault_traps_enabled = data_model.property(
        "clusterFaultTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.&#x27;]",
        dictionaryType=None
    )
    cluster_fault_resolved_traps_enabled = data_model.property(
        "clusterFaultResolvedTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.&#x27;]",
        dictionaryType=None
    )
    cluster_event_traps_enabled = data_model.property(
        "clusterEventTrapsEnabled", bool,
        array=False, optional=False,
        documentation="[&#x27;If &quot;true&quot;, when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetRemoteLoggingHostsResult(data_model.DataObject):
    """SetRemoteLoggingHostsResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class SetClusterConfigRequest(data_model.DataObject):
    """SetClusterConfigRequest  
    The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster
    interface settings for a node, run the GetClusterConfig API method.
    Note: This method is available only through the per-node API endpoint 5.0 or later.

    :param cluster: [required] Objects that are changed for the cluster interface settings. 
    :type cluster: ClusterConfig

    """
    cluster = data_model.property(
        "cluster", ClusterConfig,
        array=False, optional=False,
        documentation="[&#x27;Objects that are changed for the cluster interface settings.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDriveDetails(data_model.DataObject):
    """ResetDriveDetails  

    :param drive: [required] Drive name 
    :type drive: str

    :param return_code: [required]  
    :type return_code: int

    :param stderr: [required]  
    :type stderr: str

    :param stdout: [required]  
    :type stdout: str

    """
    drive = data_model.property(
        "drive", str,
        array=False, optional=False,
        documentation="[&#x27;Drive name&#x27;]",
        dictionaryType=None
    )
    return_code = data_model.property(
        "returnCode", int,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    stderr = data_model.property(
        "stderr", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    stdout = data_model.property(
        "stdout", str,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesDetails(data_model.DataObject):
    """ResetDrivesDetails  

    :param drives: [required] Details of a single drive that is being reset. 
    :type drives: ResetDriveDetails

    """
    drives = data_model.property(
        "drives", ResetDriveDetails,
        array=True, optional=False,
        documentation="[&#x27;Details of a single drive that is being reset.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ResetDrivesResult(data_model.DataObject):
    """ResetDrivesResult  

    :param details: [required] Details of drives that are being reset. 
    :type details: ResetDrivesDetails

    """
    details = data_model.property(
        "details", ResetDrivesDetails,
        array=False, optional=False,
        documentation="[&#x27;Details of drives that are being reset.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ListAccountsRequest(data_model.DataObject):
    """ListAccountsRequest  
    ListAccounts returns the entire list of accounts, with optional paging support.

    :param start_account_id:  Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. 
    :type start_account_id: int

    :param limit:  Maximum number of AccountInfo objects to return. 
    :type limit: int

    :param include_storage_containers:  Includes storage containers in the response by default. To exclude storage containers, set to false. 
    :type include_storage_containers: bool

    """
    start_account_id = data_model.property(
        "startAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;Starting AccountID to return. If no account exists with this&#x27;, &#x27;AccountID, the next account by AccountID order is used as&#x27;, &#x27;the start of the list. To page through the list, pass the&#x27;, &#x27;AccountID of the last account in the previous response +&#x27;, &#x27;1.&#x27;]",
        dictionaryType=None
    )
    limit = data_model.property(
        "limit", int,
        array=False, optional=True,
        documentation="[&#x27;Maximum number of AccountInfo objects to return.&#x27;]",
        dictionaryType=None
    )
    include_storage_containers = data_model.property(
        "includeStorageContainers", bool,
        array=False, optional=True,
        documentation="[&#x27;Includes storage containers in the response by&#x27;, &#x27;default. To exclude storage containers, set to false.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterFullThresholdRequest(data_model.DataObject):
    """ModifyClusterFullThresholdRequest  
    You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold setting to indicate the acceptable amount of utilized block storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console.

    :param stage2_aware_threshold:  The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. 
    :type stage2_aware_threshold: int

    :param stage3_block_threshold_percent:  The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. 
    :type stage3_block_threshold_percent: int

    :param max_metadata_over_provision_factor:  A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. 
    :type max_metadata_over_provision_factor: int

    """
    stage2_aware_threshold = data_model.property(
        "stage2AwareThreshold", int,
        array=False, optional=True,
        documentation="[&#x27;The number of nodes of capacity remaining in the cluster before the system triggers a&#x27;, &#x27;capacity notification.&#x27;]",
        dictionaryType=None
    )
    stage3_block_threshold_percent = data_model.property(
        "stage3BlockThresholdPercent", int,
        array=False, optional=True,
        documentation="[&#x27;The percentage of block storage utilization below the &quot;Error&quot; threshold that causes the&#x27;, &#x27;system to trigger a cluster &quot;Warning&quot; alert.&#x27;]",
        dictionaryType=None
    )
    max_metadata_over_provision_factor = data_model.property(
        "maxMetadataOverProvisionFactor", int,
        array=False, optional=True,
        documentation="[&#x27;A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class AddClusterAdminRequest(data_model.DataObject):
    """AddClusterAdminRequest  
    You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts.
    Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise.
    You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system.

    :param username: [required] Unique username for this cluster admin. Must be between 1 and 1024 characters in length. 
    :type username: str

    :param password: [required] Password used to authenticate this cluster admin. 
    :type password: str

    :param access: [required] Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. 
    :type access: str

    :param accept_eula:  Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 
    :type accept_eula: bool

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    username = data_model.property(
        "username", str,
        array=False, optional=False,
        documentation="[&#x27;Unique username for this cluster admin. Must be between 1 and 1024 characters in length.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=False,
        documentation="[&#x27;Password used to authenticate this cluster admin.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=False,
        documentation="[&#x27;Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide.&#x27;]",
        dictionaryType=None
    )
    accept_eula = data_model.property(
        "acceptEula", bool,
        array=False, optional=True,
        documentation="[&#x27;Required to indicate your acceptance of the End User License&#x27;, &#x27;Agreement when creating this cluster. To accept the EULA,&#x27;, &#x27;set this parameter to true.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class EnableFeatureResult(data_model.DataObject):
    """EnableFeatureResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveBackupTargetResult(data_model.DataObject):
    """RemoveBackupTargetResult  

    """

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CloneVolumeRequest(data_model.DataObject):
    """CloneVolumeRequest  
    CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone.
    Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume.
    Note: Cloned volumes do not inherit volume access group memberships from the source volume.

    :param volume_id: [required] VolumeID for the volume to be cloned. 
    :type volume_id: int

    :param name: [required] The name of the new cloned volume. Might be 1 to 64 characters in length. 
    :type name: str

    :param new_account_id:  AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. 
    :type new_account_id: int

    :param new_size:  New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. 
    :type new_size: int

    :param access:  Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
    :type access: str

    :param snapshot_id:  ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 
    :type snapshot_id: int

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    :param enable512e:  Should the volume provide 512-byte sector emulation? 
    :type enable512e: bool

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID for the volume to be cloned.&#x27;]",
        dictionaryType=None
    )
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the new cloned volume. Might be 1 to 64 characters in length.&#x27;]",
        dictionaryType=None
    )
    new_account_id = data_model.property(
        "newAccountID", int,
        array=False, optional=True,
        documentation="[&#x27;AccountID for the owner of the new volume. If unspecified, the&#x27;, &#x27;accountID of the owner of the volume being cloned is used.&#x27;]",
        dictionaryType=None
    )
    new_size = data_model.property(
        "newSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size of the volume, in bytes. Might be greater or less than the size of&#x27;, &#x27;the volume being cloned. If unspecified, the volume size is not&#x27;, &#x27;changed. Size is rounded to the nearest 1MB.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the level of access allowed for the new volume. Possible values are:&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume for a&#x27;, &#x27;paired set of volumes. If the volume is not paired, the access status is&#x27;, &#x27;locked.&#x27;, &#x27;If a value is not specified, the access value does not change.&#x27;]",
        dictionaryType=None
    )
    snapshot_id = data_model.property(
        "snapshotID", int,
        array=False, optional=True,
        documentation="[&#x27;ID of the snapshot that is used as the source of the clone. If no ID is&#x27;, &#x27;provided, the current active volume is used.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )
    enable512e = data_model.property(
        "enable512e", bool,
        array=False, optional=True,
        documentation="[&#x27;Should the volume provide 512-byte sector emulation?&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateBackupTargetRequest(data_model.DataObject):
    """CreateBackupTargetRequest  
    CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created.

    :param name: [required] The name of the backup target. 
    :type name: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    name = data_model.property(
        "name", str,
        array=False, optional=False,
        documentation="[&#x27;The name of the backup target.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyVolumeRequest(data_model.DataObject):
    """ModifyVolumeRequest  
    ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and
    changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve
    default QoS values for a newly created volume by running the GetDefaultQoS method.
    When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors:
    1. Increase the size of the "Replication Target" volume.
    2. Increase the size of the source or "Read / Write" volume.
    NetApp recommends that both the target and source volumes are the same size.
    Note: If you change the "access" status to locked or target, all existing iSCSI connections are terminated.

    :param volume_id: [required] VolumeID for the volume to be modified. 
    :type volume_id: int

    :param account_id:  AccountID to which the volume is reassigned. If unspecified, the previous account name is used. 
    :type account_id: int

    :param access:  Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 
    :type access: str

    :param qos:  New QoS settings for this volume. If not specified, the QoS settings are not changed. 
    :type qos: QoS

    :param total_size:  New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. 
    :type total_size: int

    :param set_create_time:  If set to true, changes the recorded date of volume creation. 
    :type set_create_time: bool

    :param create_time:  An ISO 8601 date string to set as the new volume creation date. Required if "setCreateTime" is set to true. 
    :type create_time: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    volume_id = data_model.property(
        "volumeID", int,
        array=False, optional=False,
        documentation="[&#x27;VolumeID for the volume to be modified.&#x27;]",
        dictionaryType=None
    )
    account_id = data_model.property(
        "accountID", int,
        array=False, optional=True,
        documentation="[&#x27;AccountID to which the volume is reassigned. If unspecified, the previous account name is used.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=False, optional=True,
        documentation="[&#x27;Specifies the access allowed for the volume. Possible values are:&#x27;, &#x27;readOnly: Only read operations are allowed.&#x27;, &#x27;readWrite: Reads and writes are allowed.&#x27;, &#x27;locked: No reads or writes are allowed.&#x27;, &#x27;If not specified, the access value does not change.&#x27;, &#x27;replicationTarget: Identify a volume as the target volume&#x27;, &#x27;for a paired set of volumes. If the volume is not paired, the&#x27;, &#x27;access status is locked.&#x27;, &#x27;If a value is not specified, the access value does not change.&#x27;]",
        dictionaryType=None
    )
    qos = data_model.property(
        "qos", QoS,
        array=False, optional=True,
        documentation="[&#x27;New QoS settings for this volume. If not specified,&#x27;, &#x27;the QoS settings are not changed.&#x27;]",
        dictionaryType=None
    )
    total_size = data_model.property(
        "totalSize", int,
        array=False, optional=True,
        documentation="[&#x27;New size of the volume in bytes. 1000000000 is equal to 1GB.&#x27;, &#x27;Size is rounded up to the nearest 1MB. This parameter&#x27;, &#x27;can only be used to increase the size of a volume.&#x27;]",
        dictionaryType=None
    )
    set_create_time = data_model.property(
        "setCreateTime", bool,
        array=False, optional=True,
        documentation="[&#x27;If set to true, changes the recorded date of volume creation.&#x27;]",
        dictionaryType=None
    )
    create_time = data_model.property(
        "createTime", str,
        array=False, optional=True,
        documentation="[&#x27;An ISO 8601 date string to set as the new volume creation date.&#x27;, &#x27;Required if &quot;setCreateTime&quot; is set to true.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CreateGroupSnapshotResult(data_model.DataObject):
    """CreateGroupSnapshotResult  

    :param group_snapshot: [required]  
    :type group_snapshot: GroupSnapshot

    :param group_snapshot_id: [required] Unique ID of the new group snapshot. 
    :type group_snapshot_id: int

    :param members: [required] List of checksum, volumeIDs and snapshotIDs for each member of the group. 
    :type members: GroupSnapshotMembers

    """
    group_snapshot = data_model.property(
        "groupSnapshot", GroupSnapshot,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    group_snapshot_id = data_model.property(
        "groupSnapshotID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique ID of the new group snapshot.&#x27;]",
        dictionaryType=None
    )
    members = data_model.property(
        "members", GroupSnapshotMembers,
        array=True, optional=False,
        documentation="[&#x27;List of checksum, volumeIDs and snapshotIDs for each member of the group.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class ModifyClusterAdminRequest(data_model.DataObject):
    """ModifyClusterAdminRequest  
    You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account.

    :param cluster_admin_id: [required] ClusterAdminID for the cluster admin or LDAP cluster admin to modify. 
    :type cluster_admin_id: int

    :param password:  Password used to authenticate this cluster admin. 
    :type password: str

    :param access:  Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. 
    :type access: str

    :param attributes:  List of name-value pairs in JSON object format. 
    :type attributes: dict

    """
    cluster_admin_id = data_model.property(
        "clusterAdminID", int,
        array=False, optional=False,
        documentation="[&#x27;ClusterAdminID for the cluster admin or LDAP cluster admin to modify.&#x27;]",
        dictionaryType=None
    )
    password = data_model.property(
        "password", str,
        array=False, optional=True,
        documentation="[&#x27;Password used to authenticate this cluster admin.&#x27;]",
        dictionaryType=None
    )
    access = data_model.property(
        "access", str,
        array=True, optional=True,
        documentation="[&#x27;Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide.&#x27;]",
        dictionaryType=None
    )
    attributes = data_model.property(
        "attributes", dict,
        array=False, optional=True,
        documentation="[&#x27;List of name-value pairs in JSON object format.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class RemoveClusterPairRequest(data_model.DataObject):
    """RemoveClusterPairRequest  
    You can use the RemoveClusterPair method to close the open connections between two paired clusters.
    Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method.

    :param cluster_pair_id: [required] Unique identifier used to pair two clusters. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier used to pair two clusters.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class CompleteClusterPairingResult(data_model.DataObject):
    """CompleteClusterPairingResult  

    :param cluster_pair_id: [required] Unique identifier for the cluster pair. 
    :type cluster_pair_id: int

    """
    cluster_pair_id = data_model.property(
        "clusterPairID", int,
        array=False, optional=False,
        documentation="[&#x27;Unique identifier for the cluster pair.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleDetails(data_model.DataObject):
    """TestConnectEnsembleDetails  

    :param nodes: [required] A list of each ensemble node in the test and the results of the tests. 
    :type nodes: dict

    """
    nodes = data_model.property(
        "nodes", dict,
        array=False, optional=False,
        documentation="[&#x27;A list of each ensemble node in the test and the results of the tests.&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

class TestConnectEnsembleResult(data_model.DataObject):
    """TestConnectEnsembleResult  

    :param details: [required]  
    :type details: TestConnectEnsembleDetails

    :param duration: [required] The length of time required to run the test. 
    :type duration: str

    :param result: [required] The results of the entire test 
    :type result: str

    """
    details = data_model.property(
        "details", TestConnectEnsembleDetails,
        array=False, optional=False,
        documentation="[u&#x27;&#x27;]",
        dictionaryType=None
    )
    duration = data_model.property(
        "duration", str,
        array=False, optional=False,
        documentation="[&#x27;The length of time required to run the test.&#x27;]",
        dictionaryType=None
    )
    result = data_model.property(
        "result", str,
        array=False, optional=False,
        documentation="[&#x27;The results of the entire test&#x27;]",
        dictionaryType=None
    )

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)