LLAMA_MODELS = [
    "ChemPlusX/llama2-chat-ft-NER",
    "ChemPlusX/llama2-base-ft-NER",
    "meta-llama/Llama-2-7b-chat-hf",
]
LLAMA_MODEL_MAP = {
    "llama2-chat-ft": "ChemPlusX/llama2-chat-ft-NER",
    "llama2-base-ft": "ChemPlusX/llama2-base-ft-NER",
    "llama2-chat": "meta-llama/Llama-2-7b-chat-hf",
}
LLAMA_CHAT_MODELS = [
    "ChemPlusX/llama-chat-ft-NER",
    "meta-llama/Llama-2-7b-chat-hf",
]
HF_MODEL_ACCESS = "https://huggingface.co/meta-llama/Llama-2-7b"
AUTH_TOKEN_REQUIREMENT_ERROR = f"HuggingFace Auth token is required to authenticate the use of LLaMA2 models. Access to LLaMA models can be requested here <{HF_MODEL_ACCESS}>"
