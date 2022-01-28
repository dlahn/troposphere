# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.secretsmanager import (
    policytypes,
    validate_tags_or_list,
    validate_target_types,
)


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html>`__
    """

    resource_type = "AWS::SecretsManager::ResourcePolicy"

    props: PropsDictType = {
        "BlockPublicPolicy": (boolean, False),
        "ResourcePolicy": (policytypes, True),
        "SecretId": (str, True),
    }


class HostedRotationLambda(AWSProperty):
    """
    `HostedRotationLambda <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html>`__
    """

    props: PropsDictType = {
        "KmsKeyArn": (str, False),
        "MasterSecretArn": (str, False),
        "MasterSecretKmsKeyArn": (str, False),
        "RotationLambdaName": (str, False),
        "RotationType": (str, True),
        "SuperuserSecretArn": (str, False),
        "SuperuserSecretKmsKeyArn": (str, False),
        "VpcSecurityGroupIds": (str, False),
        "VpcSubnetIds": (str, False),
    }


class RotationRules(AWSProperty):
    """
    `RotationRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html>`__
    """

    props: PropsDictType = {
        "AutomaticallyAfterDays": (integer, False),
        "Duration": (str, False),
        "ScheduleExpression": (str, False),
    }


class RotationSchedule(AWSObject):
    """
    `RotationSchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html>`__
    """

    resource_type = "AWS::SecretsManager::RotationSchedule"

    props: PropsDictType = {
        "HostedRotationLambda": (HostedRotationLambda, False),
        "RotateImmediatelyOnUpdate": (boolean, False),
        "RotationLambdaARN": (str, False),
        "RotationRules": (RotationRules, False),
        "SecretId": (str, True),
    }


class GenerateSecretString(AWSProperty):
    """
    `GenerateSecretString <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html>`__
    """

    props: PropsDictType = {
        "ExcludeCharacters": (str, False),
        "ExcludeLowercase": (boolean, False),
        "ExcludeNumbers": (boolean, False),
        "ExcludePunctuation": (boolean, False),
        "ExcludeUppercase": (boolean, False),
        "GenerateStringKey": (str, False),
        "IncludeSpace": (boolean, False),
        "PasswordLength": (integer, False),
        "RequireEachIncludedType": (boolean, False),
        "SecretStringTemplate": (str, False),
    }


class ReplicaRegion(AWSProperty):
    """
    `ReplicaRegion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-replicaregion.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "Region": (str, True),
    }


class Secret(AWSObject):
    """
    `Secret <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html>`__
    """

    resource_type = "AWS::SecretsManager::Secret"

    props: PropsDictType = {
        "Description": (str, False),
        "GenerateSecretString": (GenerateSecretString, False),
        "KmsKeyId": (str, False),
        "Name": (str, False),
        "ReplicaRegions": ([ReplicaRegion], False),
        "SecretString": (str, False),
        "Tags": (validate_tags_or_list, False),
    }


class SecretTargetAttachment(AWSObject):
    """
    `SecretTargetAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html>`__
    """

    resource_type = "AWS::SecretsManager::SecretTargetAttachment"

    props: PropsDictType = {
        "SecretId": (str, True),
        "TargetId": (str, True),
        "TargetType": (validate_target_types, True),
    }
