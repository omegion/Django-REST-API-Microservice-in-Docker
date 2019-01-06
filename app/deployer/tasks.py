from celery.decorators import task
from celery.utils.log import get_task_logger
from deployer.models import Deployer

import time

logger = get_task_logger(__name__)


@task(name="test_task")
def test_task(num):
    """sends an email when feedback form is filled successfully"""
    deployer = Deployer.objects.filter(id=1).first()
    holder = int(deployer.queue_id)+1
    deployer.queue_id = str(holder)
    deployer.save()
    logger.info("Sent feedback email")

    print(num)
    return num