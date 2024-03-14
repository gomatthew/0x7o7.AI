import os.path
import uvicorn
from app import create_app
from app.dto.response_dto import BaseResponse
from app.liberary.model_worker.manage import do_run_model
from app.utils import detect_device

RUNTIME_ENV = 'dev'
debug = True if RUNTIME_ENV == 'dev' else False
app = create_app(RUNTIME_ENV)


def run_model(model_name):
    device = app.config.DEFAULT_DEVICE
    if model_name not in app.config.LLM_MODELS:
        return BaseResponse(status=404, message='wrong model name,check your model config.')
    if device == 'auto':
        device = detect_device()
    host = app.config.MODEL_WORKER.get('default').get('host')
    default_port = app.config.MODEL_WORKER.get('default').get('port')
    port = app.config.MODEL_WORKER.get(model_name).get('port') if app.config.MODEL_WORKER.get(model_name).get('port') else default_port

    model_path = os.path.join(app.config.MODEL_ROOT_PATH, model_name)
    gptq_config = dict(gptq_ckpt=app.config.MODEL_WORKER.get('gptq_ckpt'), model_path=model_path,
                       gptq_wbits=app.config.MODEL_WORKER.get('gptq_wbits'),
                       gptq_groupsize=app.config.MODEL_WORKER.get('gptq_groupsize'),
                       gptq_act_order=app.config.MODEL_WORKER.get('gptq_act_order'))
    awq_config = dict(awq_ckpt=app.config.MODEL_WORKER.get('awq_ckpt'), model_path=model_path,
                      awq_wbits=app.config.MODEL_WORKER.get('awq_wbits'),
                      awq_groupsize=app.config.MODEL_WORKER.get('awq_groupsize'))
    model_worker_config = dict(controller_addr='http://127.0.0.1:20000',
                               worker_address='http://127.0.0.1:20002',
                               model_path=model_path, model_names=model_name,
                               limit_worker_concurrency=app.config.MODEL_WORKER.get('limit_worker_concurrency'),
                               no_register=app.config.MODEL_WORKER.get('no_register'),
                               device=device,
                               num_gpus=app.config.MODEL_WORKER.get('num_gpus'),
                               max_gpu_memory=app.config.MODEL_WORKER.get('max_gpu_memory'),
                               load_8bit=app.config.MODEL_WORKER.get('load_8bit'),
                               cpu_offloading=app.config.MODEL_WORKER.get('cpu_offloading'),
                               gptq_config=app.config.MODEL_WORKER.get('gptq_config'),
                               awq_config=app.config.MODEL_WORKER.get('awq_config'),
                               stream_interval=app.config.MODEL_WORKER.get('stream_interval'),
                               conv_template=app.config.MODEL_WORKER.get('conv_template'),
                               embed_in_truncate=app.config.MODEL_WORKER.get('embed_in_truncate')
                               )
    _app = do_run_model(**gptq_config, **awq_config, **model_worker_config)
    uvicorn.run(_app, host=host, port=port, log_level=log_level.lower())


def main():
    if debug:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)
    else:
        uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=1)


if __name__ == '__main__':
    model_worker = run_model(model_path='')
