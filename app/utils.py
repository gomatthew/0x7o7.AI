import datetime
from typing import Literal
from langchain_community.chat_models import ChatOpenAI


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

