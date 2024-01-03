from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

# Retrieve values from the 'influxdb' section
bucket = config['influxdb']['bucket']
org = config['influxdb']['org']
token = config['influxdb']['token']
url = config['influxdb']['url']

print(f"Bucket: {bucket}")
print(f"Org: {org}")
print(f"Token: {token}")
print(f"URL: {url}")

# Establish a client connection
client = InfluxDBClient(url=url, token=token, org=org)

# Create a write API using the client
write_api = client.write_api(write_options=SYNCHRONOUS)

# Create a new point (data point)
point = Point("measurement_name").tag("tag_key", "tag_value").field("field_key", 10)

# Write the point to your bucket
write_api.write(bucket=bucket, org=org, record=point)

# Close the client
client.close()

