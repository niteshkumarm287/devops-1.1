import json
from google.cloud.logging_v2.services.config_service_v2 import ConfigServiceV2Client

def get_all_sink_filters_json(project_id):
    """
    Retrieve inclusion and exclusion filters for all sinks in a project and output in JSON format.

    Args:
        project_id (str): The GCP project ID.
    """
    # Initialize the client
    client = ConfigServiceV2Client()

    # List all sinks in the project
    sinks = client.list_sinks(parent=f"projects/{project_id}")
    
    # Prepare data structure for JSON
    sinks_data = []

    for sink in sinks:
        sink_info = {
            "sink_name": sink.name,
            "inclusion_filter": sink.filter,
            "exclusions": []
        }

        # Add exclusion filters if present
        if sink.exclusions:
            for exclusion in sink.exclusions:
                sink_info["exclusions"].append({
                    "exclusion_name": exclusion.name,
                    "exclusion_filter": exclusion.filter
                })

        # Append sink info to the list
        sinks_data.append(sink_info)

    # Convert to JSON and print
    sinks_json = json.dumps(sinks_data, indent=4)
    print(sinks_json)

# Replace with your project ID
get_all_sink_filters_json("nitesh-gcp-444718")

# Add the JSON output to a file --> Next step
