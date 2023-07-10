# Azure-cloud-training


## Step 1: Create a resource group:

	Go to the Azure portal (portal.azure.com).
	Click on "Resource groups" in the left-hand menu.
	Click on the "Add" button to create a new resource group.
	Provide a name for the resource group (e.g., "cloud_training").
	Select the desired region (East US).
	Click on the "Review + Create" button, then click "Create" to create the resource group.
	
## Step 2: Create a storage account in the East US region and under the cloud_training resource group:
	In the Azure portal, go to your resource group (e.g., "cloud_training").
	Click on the "Add" button to create a new resource.
	Search for "Storage account" and select it from the results.
	Click on the "Create" button to start the creation process.
	Provide a name for the storage account.
	Select the desired region (East US).
	Choose the desired performance and redundancy options.
	Under the "Advanced" tab, select the resource group you created earlier (e.g., "cloud_training").
	Click on the "Review + Create" button, then click "Create" to create the storage account.
	
## Step 3: Create a container and 3 folders inside the container:
	Go to the Azure portal and navigate to your storage account.
	In the left-hand menu, under the "Blob service" section, click on "Containers."
	Click on the "+ Container" button to create a new container.
	Provide a name for the container.
	Click "OK" to create the container.
	To create folders inside the container, you'll need to create blobs with "/" in the name. For example, to create a folder named "folder1," create a blob with the name "folder1/". Repeat this step to create the other two folders.

## Step 4: Copy files to the created folders:

	To copy files to the folders, you can use Azure Storage Explorer, which is a graphical tool for managing Azure storage accounts.
	Download and install Azure Storage Explorer from the official Microsoft website: https://azure.microsoft.com/en-us/features/storage-explorer/
	Launch Azure Storage Explorer and sign in with your Azure account.
	Connect to your storage account by clicking on the "Connect" button and following the instructions.
	Once connected, navigate to your container and the respective folders.
	Right-click on each folder and select "Upload" to upload the desired files into the respective folders.
	
## Step 5: Create a Flask app to list the filenames based on the folder name:

	Create a Python Flask application on your local machine.
	Use the Azure SDK for Blob Storage to establish the client connection and list the files inside the folders.You can use app.py 
	Use the Flask framework to create a web server and expose an API endpoint that accepts the folder name as a parameter and calls the list_files function to retrieve the filenames.

## Step 6: Create a VNET with one subnet in the East US region and under the cloud_training resource group:

	In the Azure portal, go to your resource group (e.g., "cloud_training").
	Click on the "Add" button to create a new resource.
	Search for "Virtual network" and select it from the results.
	Click on the "Create" button to start the creation process.
	Provide a name for the virtual network.
	Select the desired region (East US).
	Choose the address space for the VNET (e.g., 10.0.0.0/16).
	Add a subnet to the VNET (e.g., 10.0.0.0/24).
	Click on the "Review + Create" button, then click "Create" to create the VNET.
	
## Step 7: Create a VM (Standard_A1_v1) with a public IP, 10GB disk, and place it in the cloud_training resource group, VNET, and subnet created above:
	In the Azure portal, go to your resource group (e.g., "cloud_training").
	Click on the "Add" button to create a new resource.
	Search for "Virtual machine" and select it from the results.
	Click on the "Create" button to start the creation process.
	Provide a name for the virtual machine.
	Select the desired region (East US).
	Choose the desired VM size (e.g., Standard_A1_v1).
	Configure the authentication method (password or SSH key) and provide the necessary details.
	Under the "Disks" section, add a new data disk with the desired size (e.g., 10GB).
	Configure the networking settings:
	Select the VNET and subnet you created earlier.
	Enable the option for a public IP address.
	Click on the "Review + Create" button, then click "Create" to create the VM.
	
## Step 8: Deploy the Flask app to the VM:
	Connect to the VM using SSH (using a tool like PuTTY if you're on Windows).
	Install the necessary dependencies, including Python and any required packages for your Flask app.
	Copy your Flask app code and any supporting files to the VM.
	Start the Flask app by running the appropriate command, such as python app.py, inside the VM's terminal.
	Remember to replace placeholders like <storage_account_name>, <container_name>, <folder_name>, and any other placeholders with your actual values as you follow the steps.






Regenerate response

