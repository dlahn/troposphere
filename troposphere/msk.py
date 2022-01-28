# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer


class PublicAccess(AWSProperty):
    """
    `PublicAccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class ConnectivityInfo(AWSProperty):
    """
    `ConnectivityInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html>`__
    """

    props: PropsDictType = {
        "PublicAccess": (PublicAccess, False),
    }


class ProvisionedThroughput(AWSProperty):
    """
    `ProvisionedThroughput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "VolumeThroughput": (integer, False),
    }


class EBSStorageInfo(AWSProperty):
    """
    `EBSStorageInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html>`__
    """

    props: PropsDictType = {
        "ProvisionedThroughput": (ProvisionedThroughput, False),
        "VolumeSize": (integer, False),
    }


class StorageInfo(AWSProperty):
    """
    `StorageInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html>`__
    """

    props: PropsDictType = {
        "EBSStorageInfo": (EBSStorageInfo, False),
    }


class BrokerNodeGroupInfo(AWSProperty):
    """
    `BrokerNodeGroupInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html>`__
    """

    props: PropsDictType = {
        "BrokerAZDistribution": (str, False),
        "ClientSubnets": ([str], True),
        "ConnectivityInfo": (ConnectivityInfo, False),
        "InstanceType": (str, True),
        "SecurityGroups": ([str], False),
        "StorageInfo": (StorageInfo, False),
    }


class Iam(AWSProperty):
    """
    `Iam <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class Scram(AWSProperty):
    """
    `Scram <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class Sasl(AWSProperty):
    """
    `Sasl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html>`__
    """

    props: PropsDictType = {
        "Iam": (Iam, False),
        "Scram": (Scram, False),
    }


class Tls(AWSProperty):
    """
    `Tls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html>`__
    """

    props: PropsDictType = {
        "CertificateAuthorityArnList": ([str], False),
        "Enabled": (boolean, False),
    }


class Unauthenticated(AWSProperty):
    """
    `Unauthenticated <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class ClientAuthentication(AWSProperty):
    """
    `ClientAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html>`__
    """

    props: PropsDictType = {
        "Sasl": (Sasl, False),
        "Tls": (Tls, False),
        "Unauthenticated": (Unauthenticated, False),
    }


class ConfigurationInfo(AWSProperty):
    """
    `ConfigurationInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "Revision": (integer, True),
    }


class EncryptionAtRest(AWSProperty):
    """
    `EncryptionAtRest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html>`__
    """

    props: PropsDictType = {
        "DataVolumeKMSKeyId": (str, True),
    }


class EncryptionInTransit(AWSProperty):
    """
    `EncryptionInTransit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html>`__
    """

    props: PropsDictType = {
        "ClientBroker": (str, False),
        "InCluster": (boolean, False),
    }


class EncryptionInfo(AWSProperty):
    """
    `EncryptionInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html>`__
    """

    props: PropsDictType = {
        "EncryptionAtRest": (EncryptionAtRest, False),
        "EncryptionInTransit": (EncryptionInTransit, False),
    }


class CloudWatchLogs(AWSProperty):
    """
    `CloudWatchLogs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "LogGroup": (str, False),
    }


class Firehose(AWSProperty):
    """
    `Firehose <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html>`__
    """

    props: PropsDictType = {
        "DeliveryStream": (str, False),
        "Enabled": (boolean, True),
    }


class S3(AWSProperty):
    """
    `S3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, False),
        "Enabled": (boolean, True),
        "Prefix": (str, False),
    }


class BrokerLogs(AWSProperty):
    """
    `BrokerLogs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogs": (CloudWatchLogs, False),
        "Firehose": (Firehose, False),
        "S3": (S3, False),
    }


class LoggingInfo(AWSProperty):
    """
    `LoggingInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html>`__
    """

    props: PropsDictType = {
        "BrokerLogs": (BrokerLogs, True),
    }


class JmxExporter(AWSProperty):
    """
    `JmxExporter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html>`__
    """

    props: PropsDictType = {
        "EnabledInBroker": (boolean, True),
    }


class NodeExporter(AWSProperty):
    """
    `NodeExporter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html>`__
    """

    props: PropsDictType = {
        "EnabledInBroker": (boolean, True),
    }


class Prometheus(AWSProperty):
    """
    `Prometheus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html>`__
    """

    props: PropsDictType = {
        "JmxExporter": (JmxExporter, False),
        "NodeExporter": (NodeExporter, False),
    }


class OpenMonitoring(AWSProperty):
    """
    `OpenMonitoring <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html>`__
    """

    props: PropsDictType = {
        "Prometheus": (Prometheus, True),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html>`__
    """

    resource_type = "AWS::MSK::Cluster"

    props: PropsDictType = {
        "BrokerNodeGroupInfo": (BrokerNodeGroupInfo, True),
        "ClientAuthentication": (ClientAuthentication, False),
        "ClusterName": (str, True),
        "ConfigurationInfo": (ConfigurationInfo, False),
        "EncryptionInfo": (EncryptionInfo, False),
        "EnhancedMonitoring": (str, False),
        "KafkaVersion": (str, True),
        "LoggingInfo": (LoggingInfo, False),
        "NumberOfBrokerNodes": (integer, True),
        "OpenMonitoring": (OpenMonitoring, False),
        "Tags": (dict, False),
    }
