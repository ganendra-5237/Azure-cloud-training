from flask import Flask
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Connect to Azure Blob Storage
connection_string = """<connection_string>"""
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


@app.route("/")
def list_all_files():
    # Get a reference to the container
    container_name = "ganendramlcontainer"  # Replace with your container name
    container_client = blob_service_client.get_container_client(container_name)

    # List all files in the container
    files = []
    for blob in container_client.list_blobs():
        files.append(blob.name)

    # Return the list of files as a response
    return "\n".join(files)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
