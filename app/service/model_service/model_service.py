# -*- coding: utf-8 -*-
import traceback
from app import app
from app.liberary.model_worker import model_factory


def start_model(model_name):
    app.logger.info(f'🟢 Start model :{model_name}')
    try:
        model_instance = model_factory(model_name)
        if isinstance(model_instance, str):
            return f'{model_name} is not available'
        model = model_instance.lunch_model()
        app.logger.info(f'🟢 Start model :{model_name} success.')
        return model
        # process = Process(
        #     target=model_instance.lunch_model(),
        #     name=f'model_worker_{model_name}',
        #     # kwargs=,
        #     daemon=True,
        # )
        # process.start()
        # app.redis.hset(app.seed, f'{model_name}_worker_process', process)
        # app.redis.hset('AI Service', f'{model_name}_worker_instance_{app.seed}', model)

    except BaseException as e:
        app.logger.error(f'🔴 Start model :{model_name} failed.')
        app.logger.error(traceback.format_exc())
        app.logger.error(e)


def get_model_by_name(model_name):
    model = app.redis.hget('AI Service', f'{model_name}_worker_instance_{app.seed}')
    return model


def list_llm_models():
    app.redis.hget('AI Service')


