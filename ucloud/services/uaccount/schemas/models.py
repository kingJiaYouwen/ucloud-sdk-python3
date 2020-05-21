""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class ProjectListInfoSchema(schema.ResponseSchema):
    """ ProjectListInfo - 项目信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "MemberCount": fields.Int(required=True, load_from="MemberCount"),
        "ParentId": fields.Str(required=True, load_from="ParentId"),
        "ParentName": fields.Str(required=True, load_from="ParentName"),
        "ProjectId": fields.Str(required=True, load_from="ProjectId"),
        "ProjectName": fields.Str(required=True, load_from="ProjectName"),
        "ResourceCount": fields.Int(required=True, load_from="ResourceCount"),
    }


class RegionInfoSchema(schema.ResponseSchema):
    """ RegionInfo - 数据中心信息
    """

    fields = {
        "BitMaps": fields.Str(required=True, load_from="BitMaps"),
        "IsDefault": fields.Bool(required=True, load_from="IsDefault"),
        "Region": fields.Str(required=True, load_from="Region"),
        "RegionId": fields.Int(required=True, load_from="RegionId"),
        "RegionName": fields.Str(required=True, load_from="RegionName"),
        "Zone": fields.Str(required=True, load_from="Zone"),
    }


class UserInfoSchema(schema.ResponseSchema):
    """ UserInfo - 用户信息
    """

    fields = {
        "Admin": fields.Int(required=True, load_from="Admin"),
        "Administrator": fields.Str(required=True, load_from="Administrator"),
        "AuthState": fields.Str(required=True, load_from="AuthState"),
        "City": fields.Str(required=True, load_from="City"),
        "CompanyName": fields.Str(required=True, load_from="CompanyName"),
        "Finance": fields.Int(required=True, load_from="Finance"),
        "IndustryType": fields.Int(required=True, load_from="IndustryType"),
        "PhonePrefix": fields.Str(required=True, load_from="PhonePrefix"),
        "Province": fields.Str(required=True, load_from="Province"),
        "UserAddress": fields.Str(required=True, load_from="UserAddress"),
        "UserEmail": fields.Str(required=True, load_from="UserEmail"),
        "UserId": fields.Int(required=True, load_from="UserId"),
        "UserName": fields.Str(required=True, load_from="UserName"),
        "UserPhone": fields.Str(required=True, load_from="UserPhone"),
        "UserType": fields.Int(required=True, load_from="UserType"),
        "UserVersion": fields.Int(required=True, load_from="UserVersion"),
    }