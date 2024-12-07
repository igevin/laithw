import os
from openai import OpenAI

def create_client() -> OpenAI:
    """
    创建并返回一个OpenAI客户端实例。

    此函数不接受任何参数。

    返回:
    OpenAI: 一个OpenAI客户端实例，用于与OpenAI API进行交互。
    """

    # 创建 client 时，原本需要传入 base_url 和 api_key 两个参数，如下面create_client_with_spec() 方法。
    # 不传入值时，使用默认值，或从环境变量里读取配置的值
    client = OpenAI()
    return client

def create_client_with_spec(base_url: str, api_key: str) -> OpenAI:
    """
    使用特定的base_url和api_key创建一个OpenAI客户端。

    参数:
    base_url (str): 用于连接API的基础URL，如果不传值，则从环境变量 `OPENAI_BASE_URL` 中取值，或使用默认值
    api_key (str): 用于认证的API密钥。如果不传值，则从环境变量 `OPENAI_API_KEY` 中取值

    返回:
    OpenAI: 一个初始化后的OpenAI客户端实例。
    """
    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )
    return client

def create_client_qwen() -> OpenAI:
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
    )

    return client