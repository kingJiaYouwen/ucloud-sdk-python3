""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class UnetEIPAddrSetSchema(schema.ResponseSchema):
    """ UnetEIPAddrSet - DescribeEIP
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class UnetAllocateEIPSetSchema(schema.ResponseSchema):
    """ UnetAllocateEIPSet - AllocateEIP
    """

    fields = {
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class VIPSetSchema(schema.ResponseSchema):
    """ VIPSet - VIPSet
    """

    fields = {
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class EIPAddrSetSchema(schema.ResponseSchema):
    """ EIPAddrSet - DescribeShareBandwidth
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
    }


class UnetBandwidthPackageSetSchema(schema.ResponseSchema):
    """ UnetBandwidthPackageSet - DescribeBandwidthPackage
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthPackageId": fields.Str(
            required=False, load_from="BandwidthPackageId"
        ),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DisableTime": fields.Int(required=False, load_from="DisableTime"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EnableTime": fields.Int(required=False, load_from="EnableTime"),
    }


class UnetBandwidthUsageEIPSetSchema(schema.ResponseSchema):
    """ UnetBandwidthUsageEIPSet - DescribeBandwidthUsage
    """

    fields = {
        "CurBandwidth": fields.Float(required=False, load_from="CurBandwidth"),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class ShareBandwidthSetSchema(schema.ResponseSchema):
    """ ShareBandwidthSet - DescribeEIP
    """

    fields = {
        "ShareBandwidth": fields.Int(
            required=False, load_from="ShareBandwidth"
        ),
        "ShareBandwidthId": fields.Str(
            required=False, load_from="ShareBandwidthId"
        ),
        "ShareBandwidthName": fields.Str(
            required=False, load_from="ShareBandwidthName"
        ),
    }


class UnetEIPResourceSetSchema(schema.ResponseSchema):
    """ UnetEIPResourceSet - DescribeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceName": fields.Str(required=False, load_from="ResourceName"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
    }


class UnetEIPSetSchema(schema.ResponseSchema):
    """ UnetEIPSet - DescribeEIP
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "BandwidthType": fields.Int(required=False, load_from="BandwidthType"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EIPAddr": fields.List(UnetEIPAddrSetSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "Expire": fields.Bool(required=False, load_from="Expire"),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PayMode": fields.Str(required=False, load_from="PayMode"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "Resource": UnetEIPResourceSetSchema(),
        "ShareBandwidthSet": ShareBandwidthSetSchema(),
        "Status": fields.Str(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Weight": fields.Int(required=False, load_from="Weight"),
    }


class FirewallRuleSetSchema(schema.ResponseSchema):
    """ FirewallRuleSet - DescribeFirewall
    """

    fields = {
        "DstPort": fields.Str(required=False, load_from="DstPort"),
        "Priority": fields.Str(required=False, load_from="Priority"),
        "ProtocolType": fields.Str(required=False, load_from="ProtocolType"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RuleAction": fields.Str(required=False, load_from="RuleAction"),
        "SrcIP": fields.Str(required=False, load_from="SrcIP"),
    }


class FirewallDataSetSchema(schema.ResponseSchema):
    """ FirewallDataSet - DescribeFirewall
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "FWId": fields.Str(required=True, load_from="FWId"),
        "GroupId": fields.Str(required=True, load_from="GroupId"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceCount": fields.Int(required=False, load_from="ResourceCount"),
        "Rule": fields.List(FirewallRuleSetSchema()),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class ResourceSetSchema(schema.ResponseSchema):
    """ ResourceSet - 资源信息
    """

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "PrivateIP": fields.Str(required=False, load_from="PrivateIP"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "ResourceID": fields.Str(required=False, load_from="ResourceID"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "Status": fields.Int(required=False, load_from="Status"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "Zone": fields.Int(required=False, load_from="Zone"),
    }


class EIPSetDataSchema(schema.ResponseSchema):
    """ EIPSetData - describeShareBandwidth
    """

    fields = {
        "Bandwidth": fields.Int(required=False, load_from="Bandwidth"),
        "EIPAddr": fields.List(EIPAddrSetSchema()),
        "EIPId": fields.Str(required=False, load_from="EIPId"),
    }


class UnetShareBandwidthSetSchema(schema.ResponseSchema):
    """ UnetShareBandwidthSet - DescribeShareBandwidth
    """

    fields = {
        "BandwidthGuarantee": fields.Int(
            required=False, load_from="BandwidthGuarantee"
        ),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "EIPSet": fields.List(EIPSetDataSchema()),
        "ExpireTime": fields.Int(required=False, load_from="ExpireTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "PostPayStartTime": fields.Int(
            required=False, load_from="PostPayStartTime"
        ),
        "ShareBandwidth": fields.Int(
            required=False, load_from="ShareBandwidth"
        ),
        "ShareBandwidthId": fields.Str(
            required=False, load_from="ShareBandwidthId"
        ),
    }


class VIPDetailSetSchema(schema.ResponseSchema):
    """ VIPDetailSet - VIPDetailSet
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "RealIp": fields.Str(required=False, load_from="RealIp"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "VIP": fields.Str(required=False, load_from="VIP"),
        "VIPId": fields.Str(required=False, load_from="VIPId"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class EIPPayModeSetSchema(schema.ResponseSchema):
    """ EIPPayModeSet - GetEIPPayModeEIP
    """

    fields = {
        "EIPId": fields.Str(required=False, load_from="EIPId"),
        "EIPPayMode": fields.Str(required=False, load_from="EIPPayMode"),
    }


class EIPPriceDetailSetSchema(schema.ResponseSchema):
    """ EIPPriceDetailSet - GetEIPPrice
    """

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Float(required=False, load_from="Price"),
        "PurchaseValue": fields.Int(required=False, load_from="PurchaseValue"),
    }