from google.adk.agents import Agent
from google.adk.integrations.gcs import GCSToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool
from typing import Optional

TARGET_BUCKET = "qwiklabs-gcp-02-637032565994-bucket"

def pin_bucket_callback(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext,
) -> Optional[dict]:
    args["bucket_name"] = TARGET_BUCKET
    return None

gcs_toolset = GCSToolset()

root_agent = Agent(
    model="gemini-2.5-flash",
    name="gcs_pdf_search_agent",
    instruction=f"""You are a document assistant. All files live in bucket "{TARGET_BUCKET}".
Use list_objects to list files. Use get_object_data only for relevant text files or PDFs.
Answer questions based on retrieved documents and cite the file used.
Never claim a file's contents unless you successfully retrieved them.""",
    tools=[gcs_toolset],
    before_tool_callback=pin_bucket_callback,
)
