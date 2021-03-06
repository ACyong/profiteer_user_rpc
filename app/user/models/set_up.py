# -*- coding: utf-8 -*-
from app.user.models.user import User
from utils.logger import logger


MODEL_2_TAIL = [User]


def set_up_models():
    logger.debug("Model start init")
    for index in range(100):
        for model_class in MODEL_2_TAIL:
            model_class.model(index)
    logger.debug("Model finished")
