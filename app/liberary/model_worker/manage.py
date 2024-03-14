# -*- coding: utf-8 -*-
def do_run_model(**kwargs):
    from fastchat.serve.model_worker import app, GptqConfig, AWQConfig, ModelWorker, worker_id

    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args([])
    for k, v in kwargs.items():
        setattr(args, k, v)

    gptq_config = GptqConfig(
        ckpt=args.gptq_ckpt or args.model_path,
        wbits=args.gptq_wbits,
        groupsize=args.gptq_groupsize,
        act_order=args.gptq_act_order,
    )
    awq_config = AWQConfig(
        ckpt=args.awq_ckpt or args.model_path,
        wbits=args.awq_wbits,
        groupsize=args.awq_groupsize, )
    worker = ModelWorker(controller_addr=args.controller_address,
                         worker_addr=args.worker_address,
                         worker_id=worker_id,
                         model_path=args.model_path,
                         model_names=args.model_names,
                         limit_worker_concurrency=args.limit_worker_concurrency,
                         no_register=args.no_register,
                         device=args.device,
                         num_gpus=args.num_gpus,
                         max_gpu_memory=args.max_gpu_memory,
                         load_8bit=args.load_8bit,
                         cpu_offloading=args.cpu_offloading,
                         gptq_config=gptq_config,
                         awq_config=awq_config,
                         stream_interval=args.stream_interval,
                         conv_template=args.conv_template,
                         embed_in_truncate=args.embed_in_truncate, )
    app._worker = worker
    return app
