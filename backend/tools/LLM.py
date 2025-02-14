from enum import Enum

class MODELS(Enum):
    GPT4 = "gpt-4"
    GPT4o = "gpt-4o"
    GPT350125="gpt-35-turbo-0125"
    GPT351106 = "gpt-35-turbo-1106"
    O1 = "o1"
    O3 = "o3"
    R1 = "r1"
    UNKNOWN = "unknown"    

class API_VERSION(Enum):
    GPT4 = "2024-05-01-preview"
    GPT4o = "2024-05-01-preview"
    GPT350125 = "2024-05-01-preview"
    GPT351106 = "2024-05-01-preview"
    O1 = "need to fill in"
    O3 = "o3"
    R1 = "r1"
    UNKNOWN = "unknown"