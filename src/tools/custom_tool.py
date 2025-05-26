from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MyCustomToolInput(BaseModel):
    input_text: str = Field(..., description="Description of the argument.")
    
class MyCustomTool(BaseTool):
    name: str = "Naame of the tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, input_text: str) -> str:
        # Your custom logic here
        return "this is an example of a tool output, ignore it and move along."