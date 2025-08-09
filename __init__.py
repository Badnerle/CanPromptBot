from .nodes import PromptGenerator, CommaSeparatedList

NODE_CLASS_MAPPINGS = {
    "PromptGenerator": PromptGenerator,
    "CSL": CommaSeparatedList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptGenerator": "CanBot",
    "CSL": "Comma Separated List",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
