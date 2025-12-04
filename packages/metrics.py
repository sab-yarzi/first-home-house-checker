import os
from datadog import initialize, api

def report_metrics(count:int, duration:float, status_code:int):
    dd_api_key = os.environ.get('DD_API_KEY')
    dd_app_key = os.environ.get('DD_APP_KEY')

    if not dd_api_key or not dd_app_key:
        raise ValueError("DD_API_KEY and DD_APP_KEY environment variables must be set.")

    initialize(dd_api_key, dd_app_key)

    try:
        api.Metric.send([
            {
                'metric': 'stb.properties.available',
                'points': count,
                'type': 'gauge',
                'tags': ['env:dev']
            },
            {
                'metric': 'stb.request.duration',
                'points': duration,
                'type': 'gauge',
                'tags': ['env:dev']
            },
            {
                'metric': 'stb.response.status_code',
                'points': status_code,
                'type': 'gauge',
                'tags': ['env:dev']
            }
        ])
        print(f"DataDog metrics reported: properties_available={count}, request_duration={duration}, response_status_code={status_code}")
    except Exception as e:
        print("Failed to report DataDog metrics:", e)