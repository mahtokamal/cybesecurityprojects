# Automation of Multi-Clouds with Terraform & Checkov Security Integration
**What is IaC (Infrastructure of Code) ?** <br>
Infrastructure as Code (IaC) is a method for managing and provisioning IT infrastructure with code, allowing teams to automate and standardize deployments across environments instead of performing manual configurations. This brings speed, reliability, and efficiency to cloud operations and security tasks.<br>

IaC uses machine-readable files—typically written in languages like YAML, JSON, or HCL (HashiCorp Configuration Language) —to define infrastructure resources such as servers, databases, networks, and storage. These code files are stored in version control systems, track changes, and can be reused or rolled back for consistent deployments. <br>

**NOTE:** Infrastructure as Code makes cloud and security operations faster, more reliable, and more secure, forming a backbone for modern DevOps and cloud-native strategies. <br>

**Benefits of IaC** <br>
- Automation: Reduces manual labor and human error.
- Repeatability: Enables identical infrastructure setups across different environments.
- Scalability: Infrastructure resources can be scaled up/down rapidly.
- Cost Efficiency: Resources can be created or destroyed on demand, saving costs.
- Documentation: IaC scripts serve as living documentation.
- Security: Policies and controls can be embedded directly in code, increasing compliance.

**Popular IaC tools** <br>
|Tools|Features|Cloud Platforms|
|---|---|---|
|Terraform|Declarative configs, cloud-agnostic|Multiple clouds|
|AWS CloudFormation|AWS-focused declarative templates|AWS only|
|Azure Resource Manager|Microsoft Azure infrastructure|Azure only|
|Pulumi|Code in general-purpose languages|Multiple clouds|
|Ansible|Agentless automation|	Multi-cloud|
|Chef|	Ruby-based configs|Multi-cloud|
|Puppet|Declarative state enforcement|Multi-cloud|
|Google Cloud Deployment Manager|Google Cloud templates|GCP only|
|SaltStack, Crossplane|Kubernetes integration/support|Multi-cloud|
|Vagrant|Local VM environments|	Local/multi-cloud|
|Spacelift, Checkov, Infracost, env0|Cost, policy, and governance tools|Usually multi-cloud |
## 1. Create a AWS account
**Sign-up for Amazon Web Services free accounts** <br>
- Visit https://aws.amazon.com/ click on "Create an AWS account"
- Sign up for AWS, enter your email address, AWS account name and verify email address , create root user Password and click on continue
  NOTE: This will create a root user account that will have highest level of privilege to control AWS account.
- In the Contact Information page, select "Personal - for your own projects", Enter your name, mobile number and address details then click "Agree and Continue"
- In billing information, select payment methods such as credit or debit cards,  add the card holder details, billing address, choose "Verify and continue"
- Now, Verfiy your phone number with verification codes and click "Send SMS"
- Next, select "Basic Support - Free"  as a support plan then "Complete Sign Up"
- A congratulations! message shows for signing up AWS account 
- you can now access AWS Console page for various AWS services.
  
![Screenshot (461)](https://github.com/user-attachments/assets/375b9644-4be0-4331-aaa6-ecfdf767708b)

![Screenshot (463)](https://github.com/user-attachments/assets/57eefead-493a-4700-bd17-7c97c6f0ec88)

![Screenshot (464)](https://github.com/user-attachments/assets/ea701bcf-10ab-452c-8fb8-c7e8c868b0aa)

![Screenshot (465)](https://github.com/user-attachments/assets/e9215e33-f2c9-4d85-a3e5-6fd972a83d9d)

![Screenshot (466)](https://github.com/user-attachments/assets/4cbfa968-27e5-4d7b-b910-e9e8f2076c3e)

![Screenshot (467)](https://github.com/user-attachments/assets/a3edae05-33d2-4989-8cee-0619c159e6d8)

![Screenshot (468)](https://github.com/user-attachments/assets/f13b886a-d47b-48fb-b67e-89560aab3c81)

![Screenshot (469)](https://github.com/user-attachments/assets/0939bbee-4686-4af4-afae-5902be92c7f8)

![Screenshot (470)](https://github.com/user-attachments/assets/76d0f10a-a260-4b1e-b185-0202dedda5bb)

![Screenshot (471)](https://github.com/user-attachments/assets/7d4ab44b-7c50-4167-9bd4-a07cd2d67cc6)

![Screenshot (472)](https://github.com/user-attachments/assets/beccf543-ef7d-4baa-a973-8c17d6517f7f)

![Screenshot (473)](https://github.com/user-attachments/assets/88d5a348-17cd-4f21-8f6e-c5c191498b50)

![Screenshot (474)](https://github.com/user-attachments/assets/fd86962a-208a-4538-bb64-ee45ad1ac064)

![Screenshot (475)](https://github.com/user-attachments/assets/cc752c62-b713-4f73-aecb-99c8c9ca35b5)

![Screenshot (476)](https://github.com/user-attachments/assets/218f071c-ef04-4f00-8940-b3e01aa12fc2)

![Screenshot (478)](https://github.com/user-attachments/assets/74364f5f-6660-49f2-bd5b-cdaa8c232abe)

## 2. Create Azure account
**Let's First create Microsoft Azure account** <br>

First Visit, [Microsoft Azure portal](https://azure.microsoft.com/en-us/get-started/azure-portal)and sign up for an account if you didn’t have. Once done, You will get $200 free credits added to your account and this will be enough for this project.

![image](https://github.com/user-attachments/assets/48404e67-04be-4d77-9f41-00f83fd2d66f)

![image](https://github.com/user-attachments/assets/8c75f2d6-56ac-43da-91b8-d0a12473cf05)

![image](https://github.com/user-attachments/assets/0433a323-d99d-4e63-84d8-6360154e0720)

![image](https://github.com/user-attachments/assets/fc08c1fb-0a77-42dd-b564-7265be1bef8b)

Once your account creation is done, just follows the following steps: <br>

![image](https://github.com/user-attachments/assets/31b38bb6-296f-4841-87d4-60e9c8d5e2e7)

After logging into azure portal, now you have to add payment method to become eligible for Azure's Free trial "$200 free credit" with a period of 30 days. Click on Start button and follows each step carefully: <br>

![Screenshot (329)](https://github.com/user-attachments/assets/4b5d42ba-7b60-47d1-ae24-d8fbea7636fc)

![Screenshot (331)](https://github.com/user-attachments/assets/d1846502-484a-4a62-be6f-84ccb64407fe)

![Screenshot (334)](https://github.com/user-attachments/assets/58055ce2-5358-48f8-a841-ab42172a41ee)

![Screenshot (335)](https://github.com/user-attachments/assets/d98787c7-65bd-4b6f-8f31-69a91b8fc99f)

![Screenshot (337)](https://github.com/user-attachments/assets/394e6835-cb04-4d94-8c97-5b4fd2f09b7b)

![Screenshot (341)](https://github.com/user-attachments/assets/4edafae7-5229-4042-be46-468c680609b8)

![Screenshot (342)](https://github.com/user-attachments/assets/e93c12f3-2fee-49ae-a73a-3d7abbc7457f)

![Screenshot (344)](https://github.com/user-attachments/assets/ad8a9364-86d1-47d3-8343-ac0915aef3ed)

Next, Click on "Go to Azure Portal" and it will direct to the Microsoft Azure platfrom, where you can start using services for 30 days. <br>

![Screenshot (345)](https://github.com/user-attachments/assets/a135b696-f336-4bb6-b7cb-85edb0dceb64)

![image](https://github.com/user-attachments/assets/76309c1d-1e09-4875-8a49-1e8f408b77f9)


## 3. Install Terraform GUI on Windows OS <br>

NOTE: you can install Terraform through powershell too, for convenience of the project and easy installations I utilized GUI.

- Goto https://developer.hashicorp.com/terraform/install and select OS "Windows" download and extract the files. <br> or else you can type "terraform windows download" in Google.
- In extracted file, select "terraform" application file and copy it, make folder "Terraform",  paste it(Terraform application file) on any desired drive (for e.g C:)
- copy the file path and goto "system environment variable" and paste the terraform file path there.
- open powershell and run the command "terraform" to test if it's working or not.
  
![Screenshot (553)](https://github.com/user-attachments/assets/a373357b-9f37-4954-a531-4c02f9d8afaa)

![Screenshot (554)](https://github.com/user-attachments/assets/c81743a6-667f-4918-aa9e-f29bfed48c13)

![Screenshot (555)](https://github.com/user-attachments/assets/33bbd7c2-0cd3-4bfb-829f-eaf8281e994b)

![Screenshot (556)](https://github.com/user-attachments/assets/330fb696-2b07-4218-bbeb-d2a69030b9ab)

![Screenshot (557)](https://github.com/user-attachments/assets/73708383-c0c3-4455-bbdf-cc389c615f12)

![Screenshot (558)](https://github.com/user-attachments/assets/367f6cf9-afe3-4486-bf3e-1d868dfbb9b8)

![Screenshot (559)](https://github.com/user-attachments/assets/1c48f782-79a4-4e11-a34e-a64120cae5c1)

![Screenshot (560)](https://github.com/user-attachments/assets/a1e53f5e-5c19-47c7-962c-b9937124abca)

![Screenshot (561)](https://github.com/user-attachments/assets/bfc2b55d-94ce-4af1-9f14-15d44ae9232d)

![Screenshot (562)](https://github.com/user-attachments/assets/05aabd2e-6b0b-4a95-981b-133806ef4017)

![Screenshot (563)](https://github.com/user-attachments/assets/082cd4ac-fe20-46a3-b021-9d5a6c887636)

![Screenshot (564)](https://github.com/user-attachments/assets/f554d946-3a1a-4541-b4ca-e86e20781ab7)

![Screenshot (565)](https://github.com/user-attachments/assets/f9b3e5dc-5bd4-4c73-b1f1-5459f7174c65)

![Screenshot (566)](https://github.com/user-attachments/assets/b85506f3-b14d-4b8c-8e3d-f9c9ab57cab3)

![Screenshot (567)](https://github.com/user-attachments/assets/fc267409-4453-418f-9f5a-cd288faec6ee)

![Screenshot (568)](https://github.com/user-attachments/assets/e765ba48-d62d-4f26-966f-18086560532d)

![Screenshot (569)](https://github.com/user-attachments/assets/957d271a-9876-4307-8eee-892542c977d5)

![Screenshot (570)](https://github.com/user-attachments/assets/c46ff4ea-5121-4ab8-8fa3-803e172a1253)

![Screenshot (571)](https://github.com/user-attachments/assets/422e61c1-cfe4-43c9-8efe-9e650c621c10)

![Screenshot (572)](https://github.com/user-attachments/assets/60114e64-9d96-4f56-a3a8-ed11c78f8576)

![Screenshot (573)](https://github.com/user-attachments/assets/1143f71a-bb65-401d-87f0-25a81cfb731f)

![Screenshot (574)](https://github.com/user-attachments/assets/4af37175-bd33-492e-bec0-5a8d85622b03)

![Screenshot (575)](https://github.com/user-attachments/assets/6743efa5-7264-4b05-9861-485a12f38e7b)

![Screenshot (576)](https://github.com/user-attachments/assets/19b33225-8eea-4f6a-ae95-272c7b114579)

## 4. Hands-on with Terraform Azure and CLI Installations 
 
- Type "install azure cli windows" on Google Search
- click on install the azure cli on windows
- then, Microsoft installer (MSI) and download latest MSI based on System architecture (32-bit or 64-bit)
- Now, azure cli installer file to install, accept terms & conditions, click install and finally finish.
- To verify azure cli installation, open powershell and type command az or az version.

![Screenshot (577)](https://github.com/user-attachments/assets/4969b7bf-c032-4178-bcb3-1e0e2cd05b73)

![Screenshot (578)](https://github.com/user-attachments/assets/c4cad774-497b-4de6-854d-0b998814c56c)

![Screenshot (579)](https://github.com/user-attachments/assets/75f7a3db-575d-487a-bef5-92b464ba4297)

![Screenshot (580)](https://github.com/user-attachments/assets/1d2a0039-ee19-47de-a3f3-e7307f235ad5)

![Screenshot (581)](https://github.com/user-attachments/assets/2982bfd9-1a82-4ca1-880e-77e665722867)

![Screenshot (582)](https://github.com/user-attachments/assets/8345b020-892e-459f-a8d0-ec6f5f0eb911)

![Screenshot (584)](https://github.com/user-attachments/assets/f0a4f391-0743-438f-bb53-3cf6bccce629)
![Screenshot (585)](https://github.com/user-attachments/assets/64df5390-1cf6-4ba5-bab3-cfe1fd3a466e)
![Screenshot (586)](https://github.com/user-attachments/assets/d6cf43b2-5aa2-44ed-b9b8-51da7e62c42d)

**Verifying azure CLI installation** <br>

![Screenshot (587)](https://github.com/user-attachments/assets/16c75a62-d5af-4a37-bbb6-bb248083a3eb)

![Screenshot (588)](https://github.com/user-attachments/assets/45a0f35f-fce9-4975-afe8-c5e2f4c09119)

### 4.1. Hands-On with Terraform Microsoft Azure <br>
**Let's understand Terraform loop first**

- Init: Initialize the (local) Terraform environment. Usually executed only once per session.
- Plan: Compare the Terraform state with the as-is state in the cloud, build and display an execution plan. This does not change the deployment (read-only).
- Apply: Apply the plan from the plan phase. This potentially changes the deployment (read and write).
- Destroy all resources that are governed by this specific terraform environment.

- Now, Open powershell and type az login (a GUI prompt appears that let you log into Microsoft Azure, enter you azure user account and password) and proceed to continue
- After logged in, subscription name, tenant and Subscription ID will show and enter "1" for selected Subscription ID
- Then, az account show (In the output in the terminal, find the ID of the subscription that you want to use:)
- {
- "environmentName": "AzureCloud",
- "homeTenantId": "0envbwi39-home-Tenant-Id",
- "id": "35akss-subscription-id",
- "isDefault": true,
- "managedByTenants": [],
- "name": "Subscription-Name",
- "state": "Enabled",
- "tenantDefaultDomain": ""
- "tenantDisplayName": "Default Directory"
- "tenantId": "0envbwi39-TenantId",
- "user": {
- "name": "your-username@domain.com",
- "type": "user"
- }
![Screenshot (529)](https://github.com/user-attachments/assets/705faa7d-ddc0-448e-928f-db5340d3ed8a)

![Screenshot (530)](https://github.com/user-attachments/assets/d1997b34-7590-4143-9dc8-7bf7318379a6)

![Screenshot (531)](https://github.com/user-attachments/assets/127db038-d18a-4c96-8379-87ba99370c09)

![Screenshot (532)](https://github.com/user-attachments/assets/24aa2e99-1e24-4c05-a64f-1b108196e661)

Once you have chosen the account subscription ID, set the account with the Azure CLI.
- az account set --subscription "your-subscription-ID"
![Screenshot (533)](https://github.com/user-attachments/assets/cdc02d03-0ce8-414a-b89e-f67e166d2803)

Next, we create a Service Principal. A Service Principal is an application within Azure Active Directory with the authentication tokens Terraform needs to perform actions on your behalf. Update the <SUBSCRIPTION_ID> with the subscription ID you specified in the previous step.
- az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/<YOUR_SUBSCRIPTION_ID>"

The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see the assignment details


- {
- "appId": "xxxxxx-xxx-xxxx-xxxx-xxxxxxxxxx",
- "displayName": "azure-cli-2022-xxxx",
- "password": "xxxxxx~xxxxxx~xxxxx",
- "tenant": "xxxxx-xxxx-xxxxx-xxxx-xxxxx"
- }


![Screenshot (534)](https://github.com/user-attachments/assets/f185c508-f1d0-4184-92ac-093cc3fc5fe1)

Environment Variables <br>
In your Powershell terminal, set the following environment variables. Be sure to update the variable values with the values Azure returned in the previous command.

 $env:ARM_CLIENT_ID="<APPID_VALUE>"
 $env:ARM_SUBSCRIPTION_ID="<SUBSCRIPTION_ID>"
 $env:ARM_TENANT_ID="<TENANT_VALUE>"
 $env:ARM_CLIENT_SECRET="<PASSWORD_VALUE>"

- type gci env:ARM_* (shows all environment variables that you set)

![Screenshot (535)](https://github.com/user-attachments/assets/45ac22fd-e22a-4d02-a12d-6f37bab019c0)

Now, verify the environment variables <br>
Install Visual Studio Code and Setup Environment <br>
- https://code.visualstudio.com/download
create a directory that contains our terraform configuration file (.tf) format <br>
- mkdir \terraform
- cd \terraform
- code main.tf (configurartion autmatically opens into Visual Studio)

![Screenshot (536)](https://github.com/user-attachments/assets/03d9164f-683d-4006-a662-479b076fc4b2)

![Screenshot (537)](https://github.com/user-attachments/assets/b4a57e47-2ee3-477a-8b7a-7a04246c80cd)

![Screenshot (538)](https://github.com/user-attachments/assets/246fa1f0-ef37-419e-8511-e12b78e1fa93)

Now we need to write configuration to create a new resource group.

#Configure the Azure provider <br>
terraform { <br>
required_providers { <br>
azurerm = { <br>
source = "hashicorp/azurerm" <br>
version = "~> 3.0.2" <br>
} <br>
} <br>
required_version = ">= 1.1.0" <br>
} <br>
provider "azurerm" { <br>
features {} <br>
} <br>

resource "azurerm_resource_group" "rg" { <br>
name = "myTFResourceGroup" <br>
location = "westus2" <br>
} <br>

Note:The location of your resource group is hardcoded in this example. If you do not have access to the resource group location westus2, update the main.tf file with your Azure region. This is a complete configuration that Terraform can apply. In the following sections we will review each block of the configuration in more detail.

![Screenshot (539)](https://github.com/user-attachments/assets/5cae4a8e-286e-4985-af8f-e29cd3a7c404)

### 4.2.Terraform Block
The terraform {} block contains Terraform settings, including the required providers Terraform will use to provision your infrastructure. For each provider, the source attribute defines an optional hostname, a namespace, and the provider type. Terraform installs providers from the Terraform Registry by default. In this example configuration, the azurerm provider's source is defined as hashicorp/azurerm, which is shorthand for registry.terraform.io/hashicorp/azurerm.


You can also define a version constraint for each provider in the required_providers block. The version attribute is optional, but we recommend using it to enforce the provider version. Without it, Terraform will always use the latest version of the provider, which may introduce breaking changes.

### 1. Providers
The provider block configures the specified provider, in this case azurerm. A provider is a plugin that Terraform uses to create and manage your resources. You can define multiple provider blocks in a Terraform configuration to manage resources from different providers.


### 2. Resource
Use resource blocks to define components of your infrastructure. A resource might be a physical component such as a server, or it can be a logical resource such as a Heroku application.


Resource blocks have two strings before the block: the resource type and the resource name. In this example, the resource type is azurerm_resource_group and the name is rg. The prefix of the type maps to the name of the provider. In the example configuration, Terraform manages the azurerm_resource_group resource with the azurerm provider. Together, the resource type and resource name form a unique ID for the resource. For example, the ID for your network is azurerm_resource_group.rg.


Resource blocks contain arguments which you use to configure the resource. The Azure provider documentation documents supported resources and their configuration options, including azurerm_resource_group and its supported arguments.

### 3. Initialize your Terraform configuration
Initialize your learn-terraform-azure directory in your terminal. The terraform commands will work with any operating system. Your output should look similar to the one in the assignment text.

- terraform init (to initialize)

Initializing the backend... <br>
Initializing provider plugins... <br>

- Finding hashicorp/azurerm versions matching "~> 3.0.2"...
- Installing hashicorp/azurerm v3.0.2...
- Installed hashicorp/azurerm v3.0.2 (signed by HashiCorp)

Terraform has been successfully initialized! <br>

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands should now work. <br>


If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.


![Screenshot (540)](https://github.com/user-attachments/assets/92ff820b-2a42-4706-803c-dca6047ee646)


### 4. Format and validate the configuration
We recommend using consistent formatting in all of your configuration files. The terraform fmt command automatically updates configurations in the current directory for readability and consistency.

Format your configuration. Terraform will print out the names of the files it modified, if any. In this case, your configuration file was already formatted correctly, so Terraform won't return any file names.

 - terraform fmt

You can also make sure your configuration is syntactically valid and internally consistent by using the terraform validate command. The example configuration provided above is valid, so Terraform will return a success message.

![Screenshot (541)](https://github.com/user-attachments/assets/a4fdb827-8084-4c21-ad84-005583d7e85b)

- terraform validate (shows Success! message if it is valid configuration file)

![Screenshot (542)](https://github.com/user-attachments/assets/a6a89f26-ccd0-4ce2-b75a-98c7f27a4e3c)

### 5. Apply your Terraform Configuration
Run the terraform apply command to apply your configuration. This output shows the execution plan and will prompt you for approval before proceeding. If anything in the plan seems incorrect or dangerous, it is safe to abort here with no changes made to your infrastructure. Type yes at the confirmation prompt to proceed.


- terraform apply

An execution plan has been generated and is shown below. Resource actions are indicated with the following symbols: <br>

+ create

Terraform will perform the action of creating a resource group: <br>

azurerm_resource_group.rg will be created <br>
+ resource "azurerm_resource_group" "rg" { <br>
+ id = (known after apply) <br>
+ location = "westus2" <br>
+ name = "myTFResourceGroup" <br>
} <br>

 

Plan: 1 to add, 0 to change, 0 to destroy. <br>

Do you want to perform these actions? <br>

Terraform will perform the actions described above. <br>
Only 'yes' will be accepted to approve. <br>


- Enter a value: yes

azurerm_resource_group.rg: Creating... <br>
azurerm_resource_group.rg: Creation complete after 1s [id=/subscriptions/c9ed8610-47a3-4107-a2b2-a322114dfb29/resourceGroups/myTFResourceGroup] <br>

Apply complete! Resources: 1 added, 0 changed, 0 destroyed. <br>

Navigate to the Azure portal in your web browser to check to make sure the resource group was created.

![Screenshot (543)](https://github.com/user-attachments/assets/472e5dac-785a-49f4-9cae-5a7698197e54)

![Screenshot (544)](https://github.com/user-attachments/assets/713778b0-6ca3-4354-bd0f-1eebb926879d)

(navigate to the azure portal to verfiy if resource group is created or not) <br>

![Screenshot (545)](https://github.com/user-attachments/assets/a42b6399-d06d-4f0f-84ba-753705672e61)

![Screenshot (546)](https://github.com/user-attachments/assets/0a86dd55-ae76-4bd2-a39d-623ac9246c62)

### 6. Inspect your state
When you apply your configuration, Terraform writes data into a file called terraform.tfstate. This file contains the IDs and properties of the resources Terraform created so that it can manage or destroy those resources going forward. Your state file contains all of the data in your configuration and could also contain sensitive values in plaintext, so do not share it or check it in to source control. <br>

For teams or larger projects, consider storing your state remotely. Remote stage storage enables collaboration using Terraform but is beyond the scope of this exercise. <br>

Inspect the current state using terraform show.

- terraform show
azurerm_resource_group.rg: <br>
resource "azurerm_resource_group" "rg" {

id = "/subscriptions/c9ed8610-47a3-4107-a2b2-a322114dfb29/resourceGroups/myTFResourceGroup" <br>
location = "westus2" <br>
name = "myTFResourceGroup" <br>
} <br>

When Terraform created this resource group, it also gathered the resource's properties and meta-data. These values can be referenced to configure other resources or outputs. <br>

To review the information in your state file, use the state command. If you have a long state file, you can see a list of the resources you created with Terraform by using the list subcommand. <br>

- terraform state list

If you run terraform state, you will see a full list of available commands to view and manipulate the configuration's state.

- terraform state

This command has subcommands for advanced state management. <br>

These subcommands can be used to slice and dice the Terraform state. This is sometimes necessary in advanced cases. For your safety, all
state management commands that modify the state create a timestamped backup of the state prior to making modifications. <br>


The structure and output of the commands is specifically tailored to work well with the common Unix utilities such as grep, awk, etc. We recommend using those tools to perform more advanced state tasks. <br>

![Screenshot (547)](https://github.com/user-attachments/assets/4a979106-a0b7-4c10-a818-2cdd3cc416ab)
![Screenshot (548)](https://github.com/user-attachments/assets/8cda327d-03d3-4f77-90fb-bda3e201d79e)
![Screenshot (549)](https://github.com/user-attachments/assets/ade11a40-92f3-4675-a129-4218606ddeb6)

### 7. Terraform Destroy

Lastly, issue the terraform destroy command to complete the lifecycle and undo the changes that you made. Terraform keeps a state of the changes you made in the terraform state file so it knows exactly which ones to undo.


- terraform destroy

Terraform will perform the following actions: <br>

#azurerm_resource_group.rg will be destroyed
resource "azurerm_resource_group" "rg" { <br>

id = "/subscriptions/b7b18fdb-6e24-4934-a25e-2957c9e62d05/resourceGroups/myTFResourceGroup" -> null <br>
location = "westus2" -> null <br>
name = "myTFResourceGroup" -> null <br>
tags = {} -> null <br>
}

Plan: 0 to add, 0 to change, 1 to destroy. <br>
Do you really want to destroy all resources?
- yes

![Screenshot (550)](https://github.com/user-attachments/assets/7965ce24-b6dc-42f1-bcd8-89e0f430c850)


![Screenshot (551)](https://github.com/user-attachments/assets/6dc9823c-30d1-4f10-8d57-a15cb09ae177)

- you can verify the deletion of resource group from Azure portal
![Screenshot (545)](https://github.com/user-attachments/assets/a42b6399-d06d-4f0f-84ba-753705672e61)
![Screenshot (552)](https://github.com/user-attachments/assets/f9371d9a-bda6-4499-99ac-df811b9eb44f)

## 5. Hands-on with Terraform AWS and CLI installations
### 5.1. In this lab , you will provision an EC2 instance on Amazon Web Services. EC2 instances are virtual machines running on AWS, and a common component of many infrastructure projects.
The first thing we are going to do is install the AWS CLI. Follow the steps below to download it. <br>
- visit google search "aws cli installation on windows" to download it
- click on first hyperlink appears on Google, "install/update", choose "Windows"
- Download and run the AWS CLI MSI installer for windows based on system architecture
- save it on system, run the installer and follow the installation wizards and accept Terms & Conditions and lastly click "finish"
- open powershell and run aws and aws --version (to verify the aws cli installations)
  
![Screenshot (589)](https://github.com/user-attachments/assets/dd171f20-c943-42f5-9de4-ce660f80a9e0)

![Screenshot (590)](https://github.com/user-attachments/assets/cd34c31a-9a13-46b2-87ad-5528d7be9855)

![Screenshot (591)](https://github.com/user-attachments/assets/f21b54ce-4bb3-4bee-b81a-a766df24769f)

![Screenshot (592)](https://github.com/user-attachments/assets/6e0915ce-21d7-4451-9c19-84e992985a42)

![Screenshot (593)](https://github.com/user-attachments/assets/fdcc2c3a-4119-494a-953d-b12c5898c65e)

![Screenshot (594)](https://github.com/user-attachments/assets/aca3581b-3c2f-42b6-a68c-55c48ff50ba0)

![Screenshot (595)](https://github.com/user-attachments/assets/04987634-0999-43f9-8d0f-de11ab5bb236)

![Screenshot (596)](https://github.com/user-attachments/assets/b4620319-3ec6-4db9-b81c-c3a3301da86b)

![Screenshot (597)](https://github.com/user-attachments/assets/445873e9-6e12-4a81-a047-2cf73b19b0c3)

![Screenshot (598)](https://github.com/user-attachments/assets/637b4dc8-c306-447c-b8a0-85398ceb06a4)

![Screenshot (599)](https://github.com/user-attachments/assets/728d76ae-d00b-46e8-89d1-2d03d442c7df)

![Screenshot (600)](https://github.com/user-attachments/assets/78339f32-9977-491d-a4f2-0be9c506e40f)

![Screenshot (601)](https://github.com/user-attachments/assets/c89ed59a-e4da-4bf5-9832-fd8834ad96b4)


### 5.2. Recommended not to use root user account to sign into AWS console(instead, use IAM user) to complete this project
**How to Create AWS IAM user ?** <br>
- first login using root user account into AWS console
- search tab "IAM" and click (will open IAM dashboard)
- Under Access Management tab, Select "Users", "Create User"
- Enter "user name" and check on "Provide user access to the AWS Management Console"
- choose "I want to create an IAM user", console password "custom password", "user must creat a password at next sign-in", "Next"
- Permission options "Attach policies directly"
- Permission policies, search tab "IAM", under policy name "IAMFullAccess", "AmazonEC2FullAccess", "AWSLambda_FullAccess" then Next.
- Review and Create and just click on "Create User", message "User Created Successfully"
- In Retrieve Password, shows console sign-in details, click on "Email sign-in instructions" (to receive by email about sign URL and details), "Return to users list"
- Refresh the IAM dashboard to see the newly created IAM user "kamal"
- Now, you can use the IAM user and password to logged in as an IAM user account
- after logged in, you can see the IAM users have restricted access to the AWS management console
![Screenshot (603)](https://github.com/user-attachments/assets/10e3506f-fdd1-4030-9334-b1bbae0c9124)

![Screenshot (604)](https://github.com/user-attachments/assets/1e3e3fe2-3076-40ca-b5fe-ea40b36dbe7d)

![Screenshot (605)](https://github.com/user-attachments/assets/9817512a-50b3-4479-887b-a0f29a9753f3)

![Screenshot (606)](https://github.com/user-attachments/assets/855e19a8-e7d1-4fd9-94fa-224bda1d80a1)

![Screenshot (608)](https://github.com/user-attachments/assets/17c0d2d4-1731-4c06-8ffe-70fa3fdf4a93)

![Screenshot (622)](https://github.com/user-attachments/assets/d9bcd72c-a315-4846-9c6a-f5ebd158811f)

![Screenshot (623)](https://github.com/user-attachments/assets/df030ce8-76ab-4e64-ac5e-3f4587aa8a3c)

![Screenshot (624)](https://github.com/user-attachments/assets/3159b737-561f-470b-bfe2-11be51f61106)

![Screenshot (625)](https://github.com/user-attachments/assets/285936cf-5a56-4568-8fd5-078118f9ed29)

![Screenshot (626)](https://github.com/user-attachments/assets/23514f59-e5b8-4ada-a2b7-e920aa9160a0)

![Screenshot (627)](https://github.com/user-attachments/assets/b52a5a76-53da-432d-9a4c-33e1cc138a28)

![Screenshot (631)](https://github.com/user-attachments/assets/1e20d8ea-81ad-4eca-8f72-28e76d289443)

![Screenshot (632)](https://github.com/user-attachments/assets/0613d220-ec54-44ed-beaa-fc6ece29c5fd)

![Screenshot (633)](https://github.com/user-attachments/assets/d4704896-bf76-4403-ad0c-8908514fd184)

![Screenshot (634)](https://github.com/user-attachments/assets/4f8057bc-98d5-4092-8739-32964017de61)

![Screenshot (635)](https://github.com/user-attachments/assets/6b8382bf-0604-4a9a-ae9c-54f5a844f242)

![Screenshot (636)](https://github.com/user-attachments/assets/1a88cdc0-1deb-4ea9-b467-515d9784fbff)

![Screenshot (637)](https://github.com/user-attachments/assets/5963809f-fb26-4c49-97e0-d139dea787c4)

![Screenshot (638)](https://github.com/user-attachments/assets/6eff1ad0-6958-4e18-b806-a254ae21d899)

![Screenshot (639)](https://github.com/user-attachments/assets/7936dcda-1329-42a5-9083-53e2cd169837)

![Screenshot (641)](https://github.com/user-attachments/assets/2b459b10-1b28-48d7-8e55-8f89ebe1bc1d)

![Screenshot (642)](https://github.com/user-attachments/assets/7cdf025a-49c6-4638-9a42-c08af529c67e)

![Screenshot (643)](https://github.com/user-attachments/assets/69165e7d-077a-48b0-bcfc-d262160f9945)

![Screenshot (645)](https://github.com/user-attachments/assets/7a41b378-1fdf-4444-b910-b1f1719ff9aa)

![Screenshot (646)](https://github.com/user-attachments/assets/f0a6e374-1b22-4d26-82e7-5fcac6fd6bfd)

![Screenshot (647)](https://github.com/user-attachments/assets/d37f4904-76a5-4805-95f5-ebcc2a13f119)

![Screenshot (648)](https://github.com/user-attachments/assets/45503170-aea6-473b-a210-4963661d0471)


Now, the next thing we need to do is create access keys so that the AWS CLI can access your AWS account. For this let’s switch to a web browser and go to your AWS console. I recommend not using your AWS root user but if you don’t use AWS for anything yet, it might be OK. In my case I have created a separate user for this lab and I will login directly to my console with this user. After we get there it should look similar to yours. <br>

- click on user profile top right corner of AWS console, then "Security Credentials"
- Scroll down to access keys and click the button to create an access key.
- Select the Command Line Interface option, check on confirmation and click next.
- Click create access key. (Successful Message "Access Key Created") and click done.

Now this is the only time you’ll be able to view the access key secret. If you need it again you’ll have to create a new key. Store it in your password manager or the safest way you have at your disposal. <br>

![Screenshot (649)](https://github.com/user-attachments/assets/2eb53814-99f9-46ff-b77a-5a5ec7f14984)

![Screenshot (650)](https://github.com/user-attachments/assets/5026e4bc-fb34-4a99-b16f-f3df82a87425)

![Screenshot (651)](https://github.com/user-attachments/assets/6d36745d-1dbe-404b-b5a1-49922ad064c1)

![Screenshot (652)](https://github.com/user-attachments/assets/aedff595-cbab-4ac3-afa6-a553f074872e)

![Screenshot (653)](https://github.com/user-attachments/assets/e4d3c6ca-7bcb-4c94-a12c-af1a7fa794b1)

![Screenshot (654)](https://github.com/user-attachments/assets/5df92c76-3158-4e37-af23-79afd42ddd45)

![Screenshot (655)](https://github.com/user-attachments/assets/1d2e98e6-18cf-4c38-910d-2a84d07de005)

![Screenshot (656)](https://github.com/user-attachments/assets/0cb791f6-a41a-463c-bfc0-7ba9f34d4fa5)

![Screenshot (658)](https://github.com/user-attachments/assets/906dc26a-52c9-4904-b031-52915fa0acca)


Now lets go back to the terminal. To use your IAM credentials to authenticate the Terraform AWS provider, set the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables to the key values we just got. <br>

- $Env: AWS_ACCESS_KEY_ID= ""
- $Env: AWS_SECRET_ACCESS_KEY= ""

Now we’re all set up to use AWS with Terraform! <br>

Let’s write the configuration. Each Terraform configuration must be in its own working directory. Create a directory for your configuration.<br>
- mkdir learn-terraform-aws-instance
- cd C:\learn-terraform-aws-instance\



![Screenshot (659)](https://github.com/user-attachments/assets/6ed5f0d0-a79c-4d66-a7f7-f80d20da9036)

![Screenshot (660)](https://github.com/user-attachments/assets/4545ce03-ed77-42f4-9884-9216385636ae)

![Screenshot (661)](https://github.com/user-attachments/assets/72256534-f13b-4c3f-93b2-8e7e4785e2a9)

Open main.tf in visual studio code. <br>
- code main.tf

Paste in the configuration (below).  Save the file.<br>

terraform { <br>
required_providers {  <br>
aws = { <br>
source = "hashicorp/aws" <br>
version = "~> 4.16" <br>
} <br>
} <br>
 
required_version = ">= 1.2.0" <br>
} <br>
 
provider "aws" { <br>
region = "us-west-2" <br>
} <br>
 
resource "aws_instance" "app_server" { <br>
ami = "ami-830c94e3" <br>
instance_type = "t2.micro" <br>
 
tags = { <br>
Name = "ExampleAppServerInstance" <br>
} <br>
} <br>

![Screenshot (662)](https://github.com/user-attachments/assets/4320ab52-c8a6-4309-8f46-23ef44acafc1)

![Screenshot (663)](https://github.com/user-attachments/assets/0df1e1a4-88a3-4732-a6c2-e1c7e6f7d5da)

### 5.3. This is a complete configuration that you can deploy with Terraform. The following sections review each block of this configuration in more detail. <br>
### 5.3.1 Terraform Block
The terraform {} block contains Terraform settings, including the required providers Terraform will use to provision your infrastructure. For each provider, the source attribute defines an optional hostname, a namespace, and the provider type. Terraform installs providers from the Terraform Registry by default. In this example configuration, the aws provider's source is defined as hashicorp/aws, which is shorthand for registry.terraform.io/hashicorp/aws.

You can also set a version constraint for each provider defined in the required_providers block. The version attribute is optional, but we recommend using it to constrain the provider version so that Terraform does not install a version of the provider that does not work with your configuration. If you do not specify a provider version, Terraform will automatically download the most recent version during initialization.


### 1. Providers
The provider block configures the specified provider, in this case aws. A provider is a plugin that Terraform uses to create and manage your resources.

You can use multiple provider blocks in your Terraform configuration to manage resources from different providers. You can even use different providers together. For example, you could pass the IP address of your AWS EC2 instance to a monitoring resource from DataDog.


### 2. Resources
Use resource blocks to define components of your infrastructure. A resource might be a physical or virtual component such as an EC2 instance, or it can be a logical resource such as a Heroku application.


Resource blocks have two strings before the block: the resource type and the resource name. In this example, the resource type is aws_instance and the name is app_server. The prefix of the type maps to the name of the provider. In the example configuration, Terraform manages the aws_instance resource with the aws provider. Together, the resource type and resource name form a unique ID for the resource. For example, the ID for your EC2 instance is aws_instance.app_server.


Resource blocks contain arguments which you use to configure the resource. Arguments can include things like machine sizes, disk image names, or VPC IDs.  For your EC2 instance, the example configuration sets the AMI ID to an Ubuntu image, and the instance type to t2.micro, which qualifies for AWS' free tier. It also sets a tag to give the instance a name.

### 3. Initialize the directory
When you create a new configuration — or check out an existing configuration from version control — you need to initialize the directory with terraform init.

Initializing a configuration directory downloads and installs the providers defined in the configuration, which in this case is the aws provider.

Initialize the directory.<br>
- terraform init

Terraform downloads the aws provider and installs it in a hidden subdirectory of your current working directory, named .terraform. The terraform init command prints out which version of the provider was installed. Terraform also creates a lock file named .terraform.lock.hcl which specifies the exact provider versions used, so that you can control when you want to update the providers used for your project. <br>


![Screenshot (664)](https://github.com/user-attachments/assets/0e6cd8a3-c944-4499-8727-2b8c3ecb7183)

### 4. Format and validate the configuration
We recommend using consistent formatting in all of your configuration files. The terraform fmt command automatically updates configurations in the current directory for readability and consistency.

Format your configuration. Terraform will print out the names of the files it modified, if any.

- terraform fmt

You can also make sure your configuration is syntactically valid and internally consistent by using the terraform validate command. <br>

Validate your configuration. The example configuration is valid, so Terraform will return a success message. <br>
- terraform validate
![Screenshot (665)](https://github.com/user-attachments/assets/2f60d0c1-2568-46e4-a1af-7885eaf002f4)

![Screenshot (666)](https://github.com/user-attachments/assets/0301231e-fd14-4a09-afc5-8d97feb589b9)

### 5. Create infrastructure
Apply the configuration now with the terraform apply command.

- terraform apply

Before it applies any changes, Terraform prints out the execution plan which describes the actions Terraform will take in order to change your infrastructure to match the configuration. <br>


The output format is similar to the diff format generated by tools such as Git. The output has a + next to aws_instance.app_server, meaning that Terraform will create this resource. Beneath that, it shows the attributes that will be set. When the value displayed is known after apply, it means that the value will not be known until the resource is created. For example, AWS assigns Amazon Resource Names (ARNs) to instances upon creation, so Terraform cannot know the value of the arn attribute until you apply the change and the AWS provider returns that value from the AWS API. <br>

Terraform will now pause and wait for your approval before proceeding. If anything in the plan seems incorrect or dangerous, it is safe to abort here before Terraform modifies your infrastructure. <br>

In this case the plan is acceptable, so type yes at the confirmation prompt to proceed. Executing the plan will take a few minutes since Terraform waits for the EC2 instance to become available. <br>

- yes

You have now created infrastructure using Terraform! Visit the EC2 console and find your new EC2 instance. Make sure you are in the right region to see your EC2 instance, in this case it is US-WEST-2. <br>


![Screenshot (667)](https://github.com/user-attachments/assets/89ea7ee6-4278-41a9-9c53-bb08645e97c3)

![Screenshot (668)](https://github.com/user-attachments/assets/7a67f9ef-af85-4410-8525-8cc4398caae7)

![Screenshot (669)](https://github.com/user-attachments/assets/d9e3eabe-55ac-4fc4-9792-e533d5683766)

![Screenshot (670)](https://github.com/user-attachments/assets/1b88ba8e-4d4b-4eee-9962-0dc732f0c9ca)

Now, you can verify through  IAM user AWS management console that you just created EC2 instance <br>

![Screenshot (671)](https://github.com/user-attachments/assets/b69dd171-66b4-490b-9a9d-852efe449647)

![Screenshot (672)](https://github.com/user-attachments/assets/28e81f47-f9d9-4ba7-bc54-361f04ceea6a)

### 6. Terraform Destroy
Lastly, the Terraform Destroy command will destroy all resources created. It reads the .tfstate file created in your working directory to know which resources were created thus which need to be destroyed. Issue the Terraform Destroy command now. <br>

- terraform destroy
- Enter a value: yes (to destroy everything)

And that completes the lifecycle of initializing, planning, applying and destroying AWS infrastructure with Terraform. If you would like to continue your learning with Terraform, I’d highly recommend the Udemy course Terraform for Absolute Beginners with Labs. This innovative course from KodeKloud walks you through creating a Terraform file from scratch with lectures and by using their proprietary lab platform KodeKloud. The only reason I recommend it is because I took it myself and thought it was a fantastic course. As of now, you understand how the Terraform lifecycle works and have configured both Azure and AWS with Terraform so that you can continue your learning. <br>
![Screenshot (673)](https://github.com/user-attachments/assets/4516dd36-cd4a-43a4-8d78-0d8c3bbc8602)
![Screenshot (674)](https://github.com/user-attachments/assets/90cb2ac3-e8cf-4f18-a05b-7f6e187d2e78)
![Screenshot (675)](https://github.com/user-attachments/assets/b26cc547-eea8-44f5-b1c4-a348bd18f267)

## 6. IAC- Scanning for Misconfigurations
**Checking for Misconfigurations with Checkov** <br>
Checkov is a static code analysis tool for scanning infrastructure as code (IaC) files for misconfigurations that may lead to security or compliance problems. Checkov includes more than 750 predefined policies to check for common misconfiguration issues.  Checkov also supports the creation and contribution of custom policies. 


Supported IaC types
Checkov scans these IaC file types:


- Terraform (for AWS, GCP, Azure and OCI)
- CloudFormation (including AWS SAM)
- Azure Resource Manager (ARM)
- Serverless framework
- Helm charts
- Kubernetes
- Docker


This lab shows how to install Checkov, run a scan, and analyze the results.


### Install Pip3 and Python
pip3 is the official package manager and pip command for Python 3. It enables the installation and management of third party software packages with features and functionality not found in the Python standard library. Pip3 installs packages from PyPI (Python Package Index).

You can get it by installing the latest version of python here (official website).

### Install Checkov From PyPI Using Pip

- pip3 install checkov

### Make Terraform Directory and Move There

- mkdir ~/checkov-example
- cd ~/checkov-example

**Create main.tf file with VS Code** <br>

- code main.tf

### Paste Code into File, Save, then Exit

Make sure there are no copy and paste extra characters in your code.

resource "aws_s3_bucket" "foo-bucket" { <br>
#same resource configuration as previous example, but acl set for public access. <br>
acl = "public-read" <br>
} <br>
data "aws_caller_identity" "current" {} <br>

### Format the file

- terraform fmt

### Execute Checkov

Make sure you're in the directory that your Terraform is in.

- checkov -f main.tf

### Results

<img width="1819" height="380" alt="Screenshot (686)" src="https://github.com/user-attachments/assets/0c513f18-6324-46e1-86fe-72d4d6d411c5" />

It's that simple.  As you can see Checkov runs and it notes that versioning was not enabled for that resource.  Checkov checks for all common configuration and security errors in your Terraform code BEFORE deploying it.  Anytime you download a Terraform script to execute in your environment, you will want to run Checkov to make sure that it meets your standards for configuration. <br>

Now, output the Checkov report to a file and save this file to attach to the form when submitting for a grade at the end of the course. <br>
