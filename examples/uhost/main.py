import os
import logging
import random

from ucloud.client import Client
from ucloud.helpers import wait, utils

logging.basicConfig()
logger = logging.getLogger(__name__)


def main():
    client = Client({
        "region": "cn-bj2",
        "project_id": os.getenv("UCLOUD_PROJECT_ID"),
        "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
        "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
    })

    logger.info("finding image, random choice one")
    images = client.uhost().describe_image().get('ImageSet', [])

    assert len(images) > 0

    logger.info("creating uhost instance ...")
    image = random.choice(images)

    resp = client.uhost().create_uhost_instance({
        'Name': 'sdk-python-example',
        'Zone': image["zone"],
        'ImageId': image["image_id"],
        'LoginMode': "Password",
        'Password': utils.b64encode(utils.gen_password(20)),
        'CPU': 1,
        'Memory': 1,
        'Disks': [{
            'Size': 10,
            'Type': 'CLOUD_SSD'
        }],
    })
    uhost_id = utils.first(resp["UHostIds"])
    logger.info("uhost instance is created")

    def refresh_state():
        uhost = utils.first(client.uhost().describe_uhost_instance({'UHostIds': [uhost_id]}).get('UHostSet', []))
        if uhost.get('State') in ['Running', 'Stopped']:
            return uhost['State'].lower()
        return 'pending'

    logger.info("wait uhost state is running ...")
    try:
        wait.wait_for_state(pending=['running'], target=['pending'], timeout=300, refresh=refresh_state)
    except wait.WaitTimeoutException as e:
        logger.error(e)
    logger.info("uhost instance is running")

    logger.info("stopping uhost for clean up resources ...")
    client.uhost().stop_uhost_instance({'UHostId': [uhost_id]})

    try:
        wait.wait_for_state(pending=['pending'], target=['stopped'], timeout=180, refresh=refresh_state)
    except wait.WaitTimeoutException as e:
        logger.error(e)
    else:
        logger.info("uhost instance is stopped")

    logger.info("remove uhost instance from cloud")
    client.uhost().terminate_uhost_instance({'UHostId': uhost_id})


if __name__ == '__main__':
    main()