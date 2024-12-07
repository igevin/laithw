from openai import AzureOpenAI

# from openai.lib.azure import AzureOpenAI

def create_azure_client():
    # 需要在环境变量中配置以下四个变量，否则要作为参数传入：
    # export OPENAI_API_TYPE=azure
    # export OPENAI_API_VERSION=2023-12-01-preview
    # export AZURE_OPENAI_ENDPOINT=https://xxx.openai.azure.com/
    # export AZURE_OPENAI_API_KEY=xxx
    client = AzureOpenAI()
    return client


def create_azure_client_with_spec(api_version, api_key, endpoint):
    client = AzureOpenAI(
        api_version=api_version,
        api_key=api_key,
        azure_endpoint=endpoint
    )
    return client