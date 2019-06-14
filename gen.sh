#!/usr/bin/env bash

ucloud-model sdk apis --lang python3 --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/clients.tpl --output ./ucloud/client.py
ucloud-model sdk apis --lang python3 --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/docs.tpl --output ./docs/services.rst


mkdir -p ./ucloud/services/uaccount/schemas
touch ./ucloud/services/uaccount/__init__.py
touch ./ucloud/services/uaccount/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UAccount --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/uaccount/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UAccount --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/uaccount/schemas/models.py
ucloud-model sdk apis --lang python3 --product UAccount --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/uaccount/client.py
black ucloud/services/uaccount
python -m ucloud.services.uaccount.client

mkdir -p ./ucloud/services/udpn/schemas
touch ./ucloud/services/udpn/__init__.py
touch ./ucloud/services/udpn/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UDPN --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/udpn/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UDPN --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/udpn/schemas/models.py
ucloud-model sdk apis --lang python3 --product UDPN --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/udpn/client.py
black ucloud/services/udpn
python -m ucloud.services.udpn.client

mkdir -p ./ucloud/services/uphost/schemas
touch ./ucloud/services/uphost/__init__.py
touch ./ucloud/services/uphost/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UPHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/uphost/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UPHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/uphost/schemas/models.py
ucloud-model sdk apis --lang python3 --product UPHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/uphost/client.py
black ucloud/services/uphost
python -m ucloud.services.uphost.client

mkdir -p ./ucloud/services/ulb/schemas
touch ./ucloud/services/ulb/__init__.py
touch ./ucloud/services/ulb/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product ULB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/ulb/schemas/apis.py
ucloud-model sdk apis --lang python3 --product ULB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/ulb/schemas/models.py
ucloud-model sdk apis --lang python3 --product ULB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/ulb/client.py
black ucloud/services/ulb
python -m ucloud.services.ulb.client

mkdir -p ./ucloud/services/udb/schemas
touch ./ucloud/services/udb/__init__.py
touch ./ucloud/services/udb/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UDB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/udb/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UDB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/udb/schemas/models.py
ucloud-model sdk apis --lang python3 --product UDB --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/udb/client.py
black ucloud/services/udb
python -m ucloud.services.udb.client

mkdir -p ./ucloud/services/umem/schemas
touch ./ucloud/services/umem/__init__.py
touch ./ucloud/services/umem/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UMem --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/umem/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UMem --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/umem/schemas/models.py
ucloud-model sdk apis --lang python3 --product UMem --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/umem/client.py
black ucloud/services/umem
python -m ucloud.services.umem.client

mkdir -p ./ucloud/services/pathx/schemas
touch ./ucloud/services/pathx/__init__.py
touch ./ucloud/services/pathx/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product PathX --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/pathx/schemas/apis.py
ucloud-model sdk apis --lang python3 --product PathX --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/pathx/schemas/models.py
ucloud-model sdk apis --lang python3 --product PathX --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/pathx/client.py
black ucloud/services/pathx
python -m ucloud.services.pathx.client

mkdir -p ./ucloud/services/uhost/schemas
touch ./ucloud/services/uhost/__init__.py
touch ./ucloud/services/uhost/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/uhost/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/uhost/schemas/models.py
ucloud-model sdk apis --lang python3 --product UHost --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/uhost/client.py
black ucloud/services/uhost
python -m ucloud.services.uhost.client

mkdir -p ./ucloud/services/unet/schemas
touch ./ucloud/services/unet/__init__.py
touch ./ucloud/services/unet/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UNet --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/unet/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UNet --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/unet/schemas/models.py
ucloud-model sdk apis --lang python3 --product UNet --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/unet/client.py
black ucloud/services/unet
python -m ucloud.services.unet.client

mkdir -p ./ucloud/services/vpc/schemas
touch ./ucloud/services/vpc/__init__.py
touch ./ucloud/services/vpc/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product VPC --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/vpc/schemas/apis.py
ucloud-model sdk apis --lang python3 --product VPC --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/vpc/schemas/models.py
ucloud-model sdk apis --lang python3 --product VPC --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/vpc/client.py
black ucloud/services/vpc
python -m ucloud.services.vpc.client

mkdir -p ./ucloud/services/udisk/schemas
touch ./ucloud/services/udisk/__init__.py
touch ./ucloud/services/udisk/schemas/__init__.py
ucloud-model sdk apis --lang python3 --product UDisk --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/schema.tpl --output ./ucloud/services/udisk/schemas/apis.py
ucloud-model sdk apis --lang python3 --product UDisk --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/model.tpl --output ./ucloud/services/udisk/schemas/models.py
ucloud-model sdk apis --lang python3 --product UDisk --type public --template ../ucloud-api-model-v2/apisdk/lang/python/templates/client.tpl --output ./ucloud/services/udisk/client.py
black ucloud/services/udisk
python -m ucloud.services.udisk.client

