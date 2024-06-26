import datetime
from typing import Literal, Union, Dict
from langchain_community.chat_models import ChatOpenAI


import asyncio
from typing import Literal, Union, Dict, List, Callable, Awaitable
from app import app


# def get_ChatOpenAI(
#         model_name: str,
#         temperature: float,
#         max_tokens: int = None,
#         stream: bool = True,
#         callbacks=List[Callable],
#         verbose: bool = True
# ) -> ChatOpenAI:
#     model_instance = model_factory(model_name)
#     llm = model_instance.get_llm()
#     ChatOpenAI()

def get_model_config(model_name) -> Union[str, Dict]:
    llm_model_config = app.config.get('MODEL_CONFIG')
    if model_name not in llm_model_config.keys():
        return f'{model_name} is not available, you need add model instance in project'
    return llm_model_config.get(model_name)


def detect_device() -> Literal["cuda", "mps", "cpu"]:
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        if torch.backends.mps.is_available():
            return "mps"
    except:
        pass
    return "cpu"


async def wrap_done(fn: Awaitable, event: asyncio.Event):
    """Wrap an awaitable with a event to signal when it's done or an exception is raised."""
    try:
        await fn
    except Exception as e:
        print(e)
        msg = f"Caught exception: {e}"
        print(f'{e.__class__.__name__}: {msg}')
    finally:
        # Signal the aiter to stop.
        event.set()


#
# def get_ChatOpenAI(
#         model_name: str,
#         temperature: float,
#         max_tokens: int = None,
#         streaming: bool = True,
#         callbacks: List[Callable] = [],
#         verbose: bool = True,
#         **kwargs: Any,
# ) -> ChatOpenAI:
#     config = get_model_worker_config(model_name)
#     if model_name == "openai-api":
#         model_name = config.get("model_name")
#     ChatOpenAI._get_encoding_model = MinxChatOpenAI.get_encoding_model
#     model = ChatOpenAI(
#         streaming=streaming,
#         verbose=verbose,
#         callbacks=callbacks,
#         openai_api_key=config.get("api_key", "EMPTY"),
#         openai_api_base=config.get("api_base_url", fschat_openai_api_address()),
#         model_name=model_name,
#         temperature=temperature,
#         max_tokens=max_tokens,
#         openai_proxy=config.get("openai_proxy"),
#         **kwargs
#     )
#     return model


class DateTimeLib(object):
    @property
    def now(self):
        return datetime.datetime.now()


dt = DateTimeLib()
