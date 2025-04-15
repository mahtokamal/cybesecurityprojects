# Deployment of T-Pot (Honey Pot) Project on Microsoft Azure Environment

## Creating a Virtual Machine
First Visit, [Microsoft Azure portal](https://azure.microsoft.com/en-us/get-started/azure-portal)and sign up for an account if you didn’t have. Once done, You will get $200 free credits added to your account and this will be enough for this project.

![image](https://github.com/user-attachments/assets/48404e67-04be-4d77-9f41-00f83fd2d66f)

![image](https://github.com/user-attachments/assets/8c75f2d6-56ac-43da-91b8-d0a12473cf05)

![image](https://github.com/user-attachments/assets/0433a323-d99d-4e63-84d8-6360154e0720)

![image](https://github.com/user-attachments/assets/fc08c1fb-0a77-42dd-b564-7265be1bef8b)

## Creating a Azure Virtual Machine
Once your account creation is done, just follows the following steps:
![image](https://github.com/user-attachments/assets/31b38bb6-296f-4841-87d4-60e9c8d5e2e7)

![image](https://github.com/user-attachments/assets/76309c1d-1e09-4875-8a49-1e8f408b77f9)

At the top search icon bar 🔎 , type "Virtual Machine" and select it. Scrolled down.

![image](https://github.com/user-attachments/assets/c9f7836a-80e1-4187-9cef-aa66891648d7)

![image](https://github.com/user-attachments/assets/5f63c727-501e-450a-92d2-6d6ed3795be4)

When you see "Create" button just click on it to create a new virtual Machine.

![image](https://github.com/user-attachments/assets/f6d9c685-f8a0-430f-ac23-e2fc0f5aff50)

Choose the option "Azure Virtual Machine hosted by Azure".

![image](https://github.com/user-attachments/assets/0a240240-e9ea-4d1d-ad9d-524648ef4880)

Then We will create a new resource group and name it “tpot-rg” as shown in the figure below:

> [!IMPORTANT]
> A Resource group is basically a container that holds related resources for an Azure solution.
> Azure Resource Group includes VMs, storage accounts, virtual networks, web apps, databases and database servers.

This Project will be having some of the resources such as Virtual Machine, Public IP address, Network Security Group,… etc that will be inside of this resource group.
When you finish with the Honey Pot(T-Pot) lab, all that you need to do is delete the resource group to delete this entire project.

![image](https://github.com/user-attachments/assets/9d03295c-653f-4847-b198-7f28eba458f0)

Click on "Create new" as shown in the Right under Resource group and named it as "tpot-rg" and hit "OK".

![image](https://github.com/user-attachments/assets/0efb5f0b-5ebd-47d4-8f11-30a0e658c0df)

![image](https://github.com/user-attachments/assets/181a00c2-52bb-44ae-8c41-0c2f899e1e57)

Now, select the following details carefully:

- Name the Virutal Machine name as, ""tpot-VM
- Set the region to be "East-US"
- Set No Infrastructure Redundancy Required or let it select automatically by Azure options for Availability options
- Click see all images and select “Ubuntu Server 24.04 LTS -x64 Gen1(free service eligible)”
- Security type,"Standard"
- 
![Screenshot (363)](https://github.com/user-attachments/assets/c6d3cd15-c05f-484f-b471-bdf25ee12d57)

![Screenshot (448)](https://github.com/user-attachments/assets/fa14b446-b9a9-46b6-b5c0-ceb46308c96d)

![Screenshot (364)](https://github.com/user-attachments/assets/6239793b-ad95-4f9b-b555-f50611b6bd3b)

Let it remain VM Achitecure by default

![Screenshot (365)](https://github.com/user-attachments/assets/2ea83c5c-a95c-4ffa-9017-6b71fcc7c1c4)

- Select size "Standard_D2s_v3 - 2 vcpus, 8 GiB memory"

![Screenshot (367)](https://github.com/user-attachments/assets/9986803b-b81c-4b58-b3e2-707d0625f924)

- Select authentication type "Password"
- Choose username ‘azureuser’ and type a password(your convenience for this project)
- Click “Next: Disks"

![Screenshot (368)](https://github.com/user-attachments/assets/dd693786-dc5e-4af8-9719-22d6e5ac38c3)

- On the "Disks" tab, Change the disk size to 128GiB
- Click Next

![Screenshot (369)](https://github.com/user-attachments/assets/b5592b2f-789f-43e8-8dea-b5317884117a)

![Screenshot (370)](https://github.com/user-attachments/assets/e58c1c15-525e-4ce6-9733-303ab471d569)

## Networking tab

- be sure to Check the box to "Delete public IP and NIC when VM is deleted"
- Click “Next: Management”
![Screenshot (373)](https://github.com/user-attachments/assets/cc376b57-1c61-4575-941f-a5117c98b547)

![Screenshot (374)](https://github.com/user-attachments/assets/027d556a-bb15-4255-8347-6cf45504ad82)

![Screenshot (376)](https://github.com/user-attachments/assets/263a2644-0913-4c44-9abe-cba05f8bf2ce)

## Management

- Click “Review + create” at the top
- Click “Create” to create your new VM (by reading Terms)
- Wait for your Virual Machine completely finish deployment process
![Screenshot (378)](https://github.com/user-attachments/assets/6bea8b28-7c95-49b8-a0f3-4b2548b7b32e)
![Screenshot (379)](https://github.com/user-attachments/assets/befd3a5a-4516-4d33-b297-fcb6c4048238)

![Screenshot (380)](https://github.com/user-attachments/assets/5e5e2eb7-0733-4a7c-8948-29de3d6ec7ba)
![Screenshot (381)](https://github.com/user-attachments/assets/f49bcd2d-0000-4843-8b7a-cfa159829008)

![Screenshot (383)](https://github.com/user-attachments/assets/ecacd06e-eb20-4070-b027-d04d774bf79d)
![Screenshot (384)](https://github.com/user-attachments/assets/844fc590-9ccd-4806-be5e-cbc55ea3c1c8)

# Open Traffic Flow
Now we need to open up the gates and create a rule to allow all communication in to the honeypot. This will allow the adversaries to be able to attack the honeypot so you can collect the data.

- At the top search bar, type in “tpot-vm-nsg” and select the network security group resource

![Screenshot (386)](https://github.com/user-attachments/assets/0443798b-e947-402b-816c-0a278fe51c5a)

- Select “Inbound security rules” on the left

![Screenshot (387)](https://github.com/user-attachments/assets/f37b09cb-6658-44df-a294-56a9d37f5d48)

![Screenshot (388)](https://github.com/user-attachments/assets/fc7e28bc-9c8a-4946-b8c7-19e72cc184ce)

- Click “Add”
- 
![Screenshot (389)](https://github.com/user-attachments/assets/ec836f95-4ee1-4c01-9c97-a4059bdebe10)

- Change Destination port ranges to start “*” (Note, in the screenshots you'll see 8080, but I made mistake be sure to select"*")
- Change Priority to “100”
- Change Name to “DANGER_ALLOW_ALL”
- Click “Add”

![Screenshot (390)](https://github.com/user-attachments/assets/08b28ca8-14b4-4d1c-b1a9-ff96d5455d2d)

![Screenshot (391)](https://github.com/user-attachments/assets/0fcc897e-6389-44aa-a507-cf51df7700d4)

![Screenshot (393)](https://github.com/user-attachments/assets/b3ca51ed-8865-4891-bb7d-1da8053357ae)


# Configuring the honeypot
Now we need to go grab the public IP address for the VM, as its time to log into the VM.
- Type in “tpot-vm” in the search bar at the top and select the resource

![Screenshot (394)](https://github.com/user-attachments/assets/ac9db121-43b2-4afe-8624-37d8a23c6761)

- Copy the Public IP address to the clipboard

![Screenshot (395)](https://github.com/user-attachments/assets/005be76b-cb10-401f-8a0c-8a3b61cfb2e3)

Windows has the ability to connect SSH from the command prompt in Win 10 and Win 11, Mac and Linux also allows SSH from the terminal. Go ahead and SSH into the host:
Use the formats (ssh azureuser@public ip address) <br>
Example - ssh azureuser@20.55.37.81 then enter your created password.

![Screenshot (397)](https://github.com/user-attachments/assets/55fef1bb-3bfd-43e9-86e4-ed08b5fb0046)

- Execute these commands <br>
env bash -c "$(curl -sL https://github.com/telekom-security/tpotce/raw/master/install.sh)" <br>
Select "Hive" install <br>
sudo reboot (when finished) <br>

![Screenshot (398)](https://github.com/user-attachments/assets/dac3787d-69d4-4149-9881-e4c00f3887c5)

![Screenshot (400)](https://github.com/user-attachments/assets/fab41a89-029c-4d93-9185-0255b70cf5e2)

![Screenshot (402)](https://github.com/user-attachments/assets/7abb668b-5099-48f3-8456-90202e6d11b6)

![Screenshot (404)](https://github.com/user-attachments/assets/8376c966-48de-4b0d-93e5-5915036aaa1e)

![Screenshot (405)](https://github.com/user-attachments/assets/dcaca239-6744-4103-aa6e-88bcb2e45a3c)

![Screenshot (406)](https://github.com/user-attachments/assets/a36b281b-9592-4932-8dd4-61affc1738e8)

![Screenshot (409)](https://github.com/user-attachments/assets/9d05062b-91da-41aa-aa58-2ff5e9f3605b)

> [!NOTE]
> Note: The installation script changes the port to SSH on, so if you want to connect ssh to it you have to use this syntax (ssh azureuser@public ip address -p 64295)

![Screenshot (416)](https://github.com/user-attachments/assets/cdb3b58b-ffda-4967-9557-4c33a9211f89)


- You can now login to the honeypot web interface via https://publicipaddress:64297
- Open web browser, paste the adrress into URL  https://20.55.37.81:64297
- click on advanced, then "proceed to 20.55.37.81:64297(unsafe)"
- Now, Sign in with username(azureuser) and password, you'll be directed to T-pot(Honey pot) website
- To know the attacker's source ip that attacked our deployed Honey pot, click on Kibana, scrolled down, you'll see attacker's source ip and alert signature.

![Screenshot (410)](https://github.com/user-attachments/assets/2a2dd736-00b8-49cb-ac48-63ba8d1397a0)

![Screenshot (411)](https://github.com/user-attachments/assets/e0abbdb0-ba90-434c-9e7f-4f229dd699b8)

![Screenshot (413)](https://github.com/user-attachments/assets/f46547ab-42a1-4deb-b241-0799cf378118)

![Screenshot (415)](https://github.com/user-attachments/assets/5d126cba-d714-4651-8631-888da475f851)

![Screenshot (418)](https://github.com/user-attachments/assets/dce07b8a-c5e1-421f-9766-950fb40df9f1)

![Screenshot (419)](https://github.com/user-attachments/assets/4fba3e16-e019-40f6-a391-9276aea0a69e)

![Screenshot (420)](https://github.com/user-attachments/assets/00097401-9b04-4293-9642-4cdf09d86500)

## Deleting Resource Group
- Be sure to delete the resource group when you're finished!
- To delete resource group, log into Azure portal
- Click on Resource, choose the resource group(tpot-rg), click on Delete resource group tab
- check on the box "Apply force delete for selected Virtual Machines and Virtual machine scale sets"
- Now, enter resource group name(tpot-rg) to confirm deletion, then confirm "Delete"
- Then, You'll get prompted a deletion message "Deleted resource group tpot-rg"
- Refresh it, you will not found your resource group and you'll get a Status code "404" that confirms resource deletion.

![Screenshot (432)](https://github.com/user-attachments/assets/3da28290-c343-4d19-bdd3-618d4a3c1612)

![Screenshot (433)](https://github.com/user-attachments/assets/3ea1cbf7-52c4-453d-8d2b-24da5f334d8d)

![Screenshot (435)](https://github.com/user-attachments/assets/9b93b20f-ff59-400d-8868-cbc8025724b9)

![Screenshot (436)](https://github.com/user-attachments/assets/c34df05d-f3b5-40f3-bb04-db56b4e997a4)

![Screenshot (440)](https://github.com/user-attachments/assets/7199aa63-fe32-4ecf-8079-679ba858d1e5)

![Screenshot (441)](https://github.com/user-attachments/assets/fd8f34a1-2559-4ff7-9d0a-ba36e81cc8d9)

![Screenshot (442)](https://github.com/user-attachments/assets/309afc44-b6a1-4400-932e-1084cf0facc8)

![Screenshot (443)](https://github.com/user-attachments/assets/fc4f446b-02d4-4c20-948a-047765528171)

![Screenshot (445)](https://github.com/user-attachments/assets/c71035b5-275a-46ab-a31c-8c030a0a1a97)

![Screenshot (447)](https://github.com/user-attachments/assets/ab1c3f4e-d248-423c-b3fd-f3d0a4fcfc6f)

