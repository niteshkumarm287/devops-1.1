from google.cloud.logging_v2.services.config_service_v2 import ConfigServiceV2Client
from google.cloud.logging_v2.types import GetSinkRequest

def get_sink_filters(project_id, sink_name):
    # Initialize the client
    client = ConfigServiceV2Client()

    # Create the sink path
    sink_path = f"projects/{project_id}/sinks/{sink_name}"

    # Create the request with the correct field
    request = GetSinkRequest(sink_name=sink_path)

    # Fetch the sink details
    sink = client.get_sink(request=request)
    print("Inclusion Filter:", sink.filter)

    # Check for exclusion filters
    if sink.exclusions:
        for exclusion in sink.exclusions:
            print("Exclusion Name:", exclusion.name)
            print("Exclusion Filter:", exclusion.filter)
    else:
        print("No Exclusion Filters")

# Replace with your project ID and sink name
get_sink_filters("nitesh-gcp-444718", "_Required")
