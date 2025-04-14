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







