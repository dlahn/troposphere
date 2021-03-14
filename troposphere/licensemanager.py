# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import integer


class Grant(AWSObject):
    resource_type = "AWS::LicenseManager::Grant"

    props = {
        'AllowedOperations': ([basestring], False),
        'GrantName': (basestring, False),
        'HomeRegion': (basestring, False),
        'LicenseArn': (basestring, False),
        'Principals': ([basestring], False),
        'Status': (basestring, False),
    }


class BorrowConfiguration(AWSProperty):
    props = {
        'AllowEarlyCheckIn': (boolean, True),
        'MaxTimeToLiveInMinutes': (integer, True),
    }


class ProvisionalConfiguration(AWSProperty):
    props = {
        'MaxTimeToLiveInMinutes': (integer, True),
    }


class ConsumptionConfiguration(AWSProperty):
    props = {
        'BorrowConfiguration': (BorrowConfiguration, False),
        'ProvisionalConfiguration': (ProvisionalConfiguration, False),
        'RenewType': (basestring, False),
    }


class Entitlement(AWSProperty):
    props = {
        'AllowCheckIn': (boolean, False),
        'MaxCount': (integer, False),
        'Name': (basestring, True),
        'Overage': (boolean, False),
        'Unit': (basestring, True),
        'Value': (basestring, False),
    }


class IssuerData(AWSProperty):
    props = {
        'Name': (basestring, True),
        'SignKey': (basestring, False),
    }


class Metadata(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class ValidityDateFormat(AWSProperty):
    props = {
        'Begin': (basestring, True),
        'End': (basestring, True),
    }


class License(AWSObject):
    resource_type = "AWS::LicenseManager::License"

    props = {
        'Beneficiary': (basestring, False),
        'ConsumptionConfiguration': (ConsumptionConfiguration, True),
        'Entitlements': ([Entitlement], True),
        'HomeRegion': (basestring, True),
        'Issuer': (IssuerData, True),
        'LicenseMetadata': ([Metadata], False),
        'LicenseName': (basestring, True),
        'ProductName': (basestring, True),
        'ProductSKU': (basestring, False),
        'Status': (basestring, False),
        'Validity': (ValidityDateFormat, True),
    }