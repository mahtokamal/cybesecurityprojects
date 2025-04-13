# Security Analysis Methodology using SPLUNK

## What is SOC Analyst Methods?
The SOC Analyst method consists of 5-step security analysis method. Being a SOC Analyst, you have the responsibility to determine whether a security event is a malicious or not.

Despite in the prevalence age of AI and automation tools, the manual security analysis method plays a key role in security event because manual method adds depth to threat comprehension and response strategies.

**Following are the Steps for security Analysis:** <br>

![image](https://github.com/user-attachments/assets/23f75fb5-aba3-4d87-ae01-1230b3c3f9f6)

**Step 1: Reason** <br>
Find reason and signature why this alert triggered.

**Step 2: Supporting Evidence** <br>
Document everything that supports the collected evidence for security analysis. Try to collect and gather as much as information from the security logs. This step is very important as these evidences are required in the analysis phase.

Nowadays, the SOAR (Security Orchestration and Automation Response) automaton tools are being widely used for this step and it eases the security analysis efforts. However, manual automation still plays a key role and adds depth to the security analysis methodologies.

**Step 3: Analysis** <br>
At this stage, first we need to do analysis and reputation check on source IP.

You can't trust on just 1 reputation check on source IP because some of the information may not be available on publicly available platform and different online platforms have different kinds of data available for respective IP and they don't share with each other. Therefore, it is always required to cross-check on source IP.

**Step 4: Conclusion** <br>
Write a short summary of what happened and the immediate actions that you can take. But the practice is to keep it short simple and precise that will be easily readable and measures for further actions.

**Step 5: Next Steps** <br>
write the actions that you cannot take and might be forwarded to senior concerned authority for further actions.

## Importance of Security Event Gateways
Security Event Gateways are indispensable for allocation of times that are required for each step. Some of the events may demand more or less amount of time in specific steps.

Following are the general guidelines that suggest the proportion of time shared for each step:

![image](https://github.com/user-attachments/assets/cdc8d9b7-a4cf-4b6b-ba56-894dd15d7a9c)

-	5% is for identifying and understanding what caused the alarm to trigger.
-	40% is for gathering and documenting all evidence pertaining to the alarm.
-	40% is for studying the evidence, checking the reputation of the indicators, looking for historical correlations, and otherwise determining if this is malicious behavior.
-	10% is for crafting a conclusion that is the result of your security analysis, and taking any necessary immediate actions.
-	5% is for determining the next steps, if any.

## Project Ideas:
As a part of SOC Analyst NOW! Course, which already included Splunk Cyber Range. It is a Splunk instance that actualize the enterprise-level settings that contains live attack data from honeypot infrastructure across the World.

To access and want to do Security Analysis project, you have to become Black Badge Member to take advantages of Lifetime premium memberships.

First visit the website cybernoweducation and after loading, click on Log in.

![image](https://github.com/user-attachments/assets/c8ddc850-042b-4192-a38b-3e98da40320d)

Now, use your credentials to log in.

![image](https://github.com/user-attachments/assets/b6708344-bb36-42c0-b178-5e882e54b235)

Now you can see the homepage of the website. Next, click on profile icon and a drop-down list menu would pop up.

![image](https://github.com/user-attachments/assets/0bcaae70-7a3b-4452-b848-ab90bb47bf5e)

Just click on My Programs.

![image](https://github.com/user-attachments/assets/2cdd086c-cc1c-4c15-be5a-ffb94cc2a21a)

And wait for few seconds to load your enrolled course or program, where you can see two tabs i.e. active or completed tab.

![image](https://github.com/user-attachments/assets/bd704ed3-7068-4bfd-a214-21e7127eae94)

Now, scrolled down and select SOC Analyst NOW! And click view Program to open it and see your progress.

![image](https://github.com/user-attachments/assets/897fe3b5-51e7-4fe4-a211-0768bad73438)

Now, from left side of tab scrolled it and select “The SOC Analyst Method” section and expand it.

![image](https://github.com/user-attachments/assets/65452db8-a69f-4c0e-abe3-523128e6ef19)

Then, click on Submit Your Analysis.

![image](https://github.com/user-attachments/assets/68fe43ec-79ad-4696-b3f7-8f7a5823d8f7)

Now, follow the mentioned instructions and click on given link to access the Splunk instance.

![image](https://github.com/user-attachments/assets/70696a03-4e49-4301-abcb-a7ce884dcabb)

Now, click on Search & Reporting

![image](https://github.com/user-attachments/assets/72a2ec67-dfdf-4feb-a73b-c42453b308c1)

Now, use filters options and select last 30 days (we’ll be using last 30 days of security logs).

![image](https://github.com/user-attachments/assets/a75dc19d-ec57-4949-b49c-21aed70654d6)

Now click on Search field and type “md5=*” and click on search icon. (Here, we are targeting the logs that contain md5 fields).

MD5 (message-digest) is a hashing algorithm that are used to verify the integrity of files.

![image](https://github.com/user-attachments/assets/38cf3010-7820-4843-86b1-5d9aff1ade80)

**Let’s follow each steps carefully:** <br>
**SOC Analyst Methods or steps to follow:** <br>
**1.	Reason** <br>
Now, we have the list of logs available that we will use from one of the logs. For this project, just select and expand (‘>’ icon) of the first log that appears first.

![image](https://github.com/user-attachments/assets/5585c01c-0e1c-4e8f-91b7-ceae1a5bb772)

Now, we can see the details of our selected logs.

![image](https://github.com/user-attachments/assets/5eabbe0c-f7c6-446a-b6b3-09df637b80e7)

Now, go to signature field and copy its value “Connection to Honeypot”. 

![image](https://github.com/user-attachments/assets/d314ab63-db9a-4af9-b02d-0870520a4a26)

Now, Select Severity and copy its level “high”.

![image](https://github.com/user-attachments/assets/212e594c-d50d-4cba-b4a6-ede1d3277a73)

**Key findings for first phase:** <br>
Signature: Connection to Honeypot
Severity: High


**2. Supporting Evidence** <br>

For this part, First select the Event time and copy it.

![image](https://github.com/user-attachments/assets/88bdcd99-505b-40b6-8581-a1d39ed85b41)

Next, pick source ip(src), source port(src_port), protocol (tcp).

![image](https://github.com/user-attachments/assets/a3825f13-db73-402b-bd48-fa7c4dc47b4b)

Again, Choose destination ip (dest), destination port (dest_port), destination hostname (sensor), destination type(Vendor_product).

![image](https://github.com/user-attachments/assets/b394854f-e1f6-4ad7-9449-a0dd97288ad7)

For hash part select md5 and sha512 and copy it.

![image](https://github.com/user-attachments/assets/315d687c-79b3-4e10-95c9-1b770790a874)

**Key findings for phase 2:** <br>

Time: 2025-03-18T12:39:12.575698 <br>

Source IP: 170.244.70.10 <br>
Source Port: 50721 <br>
Protocol: TCP <br>

Destination IP (targeted): 172.172.168.52 <br>
Destination Hostname (sensor): 634851ba-c550-11ef-8089-000d3a556b22 <br>
Destination Port: 445 <br>
Destination Type (Vendor Product): Dionaea Honeypot <br>

MD5 hash: ae12bb54af31227017feffd9598a6f5e <br>
sha 512: a80b1cc70cafff3b8edb2e732fa2360436cc7556ba91977ab1fa505ad7c6e184c465839d1584f827be17ccb751240432348debe69eed4e006321d9af4334621b <br>

**3. Analysis** <br>

In this stage, we’ll use publicly available tools that helps us to do analysis whether a source IP is considered to be verdict as a malicious or not.
To do analysis on collected evidence, first select the source IP go to https://whois.domaintools.com/

![image](https://github.com/user-attachments/assets/a13e7198-65e8-4458-bf85-de880203755a)

Paste the source IP (170.244.70.10) and click on search.

![image](https://github.com/user-attachments/assets/539b66ef-827e-4507-b58f-b06f9b983d5b)

![image](https://github.com/user-attachments/assets/fb7710ec-0515-41db-b7d1-6b18384cf96c)

Now, we can see the details available related to our source IP such as location, domain name, registrant information and many more.

![image](https://github.com/user-attachments/assets/cede9b0b-4bde-4a1d-af9d-ffc03a3974ec)

Now, you can copy the first part or the important details that are related to source IP.

![image](https://github.com/user-attachments/assets/2c4af341-e1f5-40fb-bafa-9d48dab7a266)

Now, go to the virus total website and click on search tab.

![image](https://github.com/user-attachments/assets/a14e9f5a-38d7-454f-85b2-aec6433c4749)

Now, paste the source IP (170.244.70.10) and enter to see the results available into the database.

![image](https://github.com/user-attachments/assets/effc3ecc-0014-4bfd-b37e-1ee373ad2a15)

![image](https://github.com/user-attachments/assets/a993a4b4-9f7e-48ed-8908-c331bc724909)

Now we have the result on the source IP and as per virus total reports it flagged 0 out of 94 times.

![image](https://github.com/user-attachments/assets/3aa0e4d1-5286-47da-a619-5f1560db9305)

To know more details about it, you can click on details, relations and community tab to get more information.

![image](https://github.com/user-attachments/assets/fdb99093-44c9-4418-9db8-6d2895da1c11)

![image](https://github.com/user-attachments/assets/bcd4cfd3-26ff-4dea-bc1a-ee5fdfe49f62)

To cross-check on source IP visit ipvoid.com

![image](https://github.com/user-attachments/assets/294a8270-68ba-4207-90f8-b6edefe221f9)

Scrolled down and click on IP blacklist check.

![image](https://github.com/user-attachments/assets/94619213-d4e3-4599-b269-af4df945fb1a)

Now paste the source IP (170.244.70.10) and click on check IP address

![image](https://github.com/user-attachments/assets/faa4cfc8-585f-4da0-b121-9d08be64ea4a)

Next, scrolled down the cursor and you’ll see the value of detection count i.e. how many times ipvoid flagged the source IP (170.244.70.10).

![image](https://github.com/user-attachments/assets/d712e064-9392-4543-ba7f-5a6e40a0a421)

Staying on IP void and scrolled down again to see the IP blocklist reports. 
Now, click on IPSpamList under Engine field to get more information about the IP.

![image](https://github.com/user-attachments/assets/eb7216d0-74c4-4260-a2b1-80b9c4a21ee4)

Again, paste the source IP (170.244.70.10) in the ipspamlist.com website.

![image](https://github.com/user-attachments/assets/93f44765-f436-44c0-bb2d-2ef48faf9c4f)

After results have been generated from the ipspamlist, just scroll down, you can see many details, however just focused on category field (“MS-DS Attack”).

![image](https://github.com/user-attachments/assets/f8442dd5-5eb4-4371-b489-66da649129f3)

To know what is MS-DS attack, just copy it and paste it on google search engine to get the idea about the attack type.

![image](https://github.com/user-attachments/assets/a42000a8-43dd-431f-9a2f-3ead0d5af252)

Now, click on 3-4 relevant source that are related to MS-DS attack. 

![image](https://github.com/user-attachments/assets/7847397b-d227-40c0-8d52-79df484e28a8)

In our case, we found Microsoft DS vulnerability that explain about the MS-DS attack, open it and just review it, what it is?

![image](https://github.com/user-attachments/assets/f37a9935-d1ae-4812-9561-cb4f74c352c3)

![image](https://github.com/user-attachments/assets/b8ab5662-632a-4d3a-9333-d2d7e4276df8)

Now, it is evident that it targeted SMB port 445 which resembles to our collected logs data about the targeted destination port (445).

![image](https://github.com/user-attachments/assets/000b1a77-9921-48e7-a8c7-14a74a397625)

Now, use google search to know detail about source IP.

![image](https://github.com/user-attachments/assets/ad4e3c30-b272-4a16-84c5-f6ed599b8e89)

![image](https://github.com/user-attachments/assets/0fe52169-6687-4fd7-9023-5e91fc6ee7ac)

Paste source IP (170.244.70.10) on google search bar and click search button.

![image](https://github.com/user-attachments/assets/e1a25c1c-eb26-4c07-985f-8a78d48ba10a)

Just try to open 2-3 links that provides some important insights on given IP.

![image](https://github.com/user-attachments/assets/17bfff93-7d01-4cd3-8f45-57b9481c8da0)

As in our case we have got the coordinates details about source IP after opening ipinfo.io link.

![image](https://github.com/user-attachments/assets/67d12b11-7a80-4651-baf5-1e090c73d3fa)

![image](https://github.com/user-attachments/assets/a7349e66-1fd7-457a-afc3-2f62b2f67696)

![image](https://github.com/user-attachments/assets/f0777eec-c954-4453-9f42-65199f61890d)

![image](https://github.com/user-attachments/assets/549cfe82-bf3b-4ee5-9305-ba26c7b52428)

or else, we can visit abuseipdb website to get the more information about the source ip.

![image](https://github.com/user-attachments/assets/d2929cd8-dcbd-4d18-a204-effa4cbcf89b)

Now, enter the source IP(170.244.70.10) on search field then click check.

![image](https://github.com/user-attachments/assets/eaf3ed4b-8fcd-4112-b01f-833dbbc131e2)

Now, we can see that the source IP (170.244.70.10) was reported 29 times with confidence of abuse is 73%, which is more than enough to report it as a malicious.

![image](https://github.com/user-attachments/assets/ebb012be-d53a-4b1f-8f3d-d96240d77c95)

![image](https://github.com/user-attachments/assets/9122fa96-353f-411d-89e0-7c68510edd5e)

We can get in-depth details on source IP from abuseipdb that tells us about the threat category.

![image](https://github.com/user-attachments/assets/b06beaa6-c14e-4eed-91f0-07f08c7fb32d)

Once reputation check on IP is done, we’ll focus on file hash. For that, just visit virustotal and click on search tab.

![image](https://github.com/user-attachments/assets/d0231bd4-c583-4c96-81ba-3d816b98c8b7)

Paste the md5 (ae12bb54af31227017feffd9598a6f5e) hash on search field and hit enter.

![image](https://github.com/user-attachments/assets/dc15c0b3-7553-4919-a76e-fb5662eada58)

Now, we have results in our hand, the given hash file is flagged 66 out of 70 times and here, we have more information on hash file such as threat labels, categories and the families of threat it belongs to. Therefore, it will save our time in conclusion stage.

![image](https://github.com/user-attachments/assets/2c645738-0ede-4650-ada1-d64f2c41f0ba)

![image](https://github.com/user-attachments/assets/fd9286c5-b5af-4321-8196-d171fff69347)

Now, google the hash files and click on some of the results from 2-3 popular sandbox environments.

In our case, just click on hybrid analysis link.

![image](https://github.com/user-attachments/assets/9ab85755-dd7e-412c-a467-2767bb8801f6)

Now, we can clearly see the hash file is verdicted as a malicious.

![image](https://github.com/user-attachments/assets/4e00da4f-35bb-4c6b-a472-7e990c456bad)

![image](https://github.com/user-attachments/assets/ae8912de-2bbc-42a4-91d9-925242456cb1)

If you want to see the result with threat score in hybrid analysis just search on google and open it.

![image](https://github.com/user-attachments/assets/73b8804b-6dc4-4c47-8281-3e92f0d28574)

Then, click on Report Search

![image](https://github.com/user-attachments/assets/3738ecae-c48e-4b61-b233-83113826a837)

Paste the hash of file on search field and click Search.

![image](https://github.com/user-attachments/assets/88b61160-aad1-44ed-a724-0ad7b4bfccfa)

![image](https://github.com/user-attachments/assets/335905b8-e1d5-4bee-9467-22ae03d37dba)

We can see the results with threat scores or you can click one of the links available based on Timestamp.

![image](https://github.com/user-attachments/assets/4c0d60f4-659f-4522-afb5-482e59e25784)

Click on latest timestamp and open it.

![image](https://github.com/user-attachments/assets/fcd3d23c-fd46-4590-a579-b88eeae6a710)

Now, we have threat score details which is 100 out of 100 available for the given hash file, which is again important to report it as a malicious activity.

![image](https://github.com/user-attachments/assets/a281252c-ea17-426a-ad35-546b3709ab7b)

**Key Findings for phase 3:**

inetnum:     170.244.68.0/22 <br>
aut-num:     AS266517 <br>
abuse-c:     MAWBA21 <br>
owner:       New Life Telecom Eireli EPP <br>
ownerid:     13.064.983/0001-71 <br>
responsible: New Life Telecom Eireli EPP <br>
country:     BR <br>
owner-c:     MAWBA21 <br>
tech-c:      RALSC23 <br>
created:     20170119 <br>
changed:     20250307 <br>

**Result of reputation checks on IP** <br>

Virus Total: 0/94 <br>
Ipvoid: 1/93 <br>
IPspamlist: reports port 445 Network traffic as a MS-DS Attack similar to what we saw in the destination port (targeted port). <br>
AbuseIPDB: listed 29 times for abusive activities engagement and the Confidence of Abuse is 73%. <br>


Hash: <br>
Virus Total: 66/70 (WannaCry Ransomware) <br>
Hybrid analysis (Sandbox report): verdict malicious with threat score 100/100<br>


**4. Conclusion** <br>

After a thorough analysis on Source IP address (170.244.70.10), it is confirmed to be as a malicious and rogue for sending port 445 Network traffic, which targeted Microsoft SMB (Server Message Block) commonly used for communication protocol to share computing resources and the indicator of the hash file found is also known to be malicious and of a WannaCry Ransomware variant from multiple sources. Therefore, I conclude, this is a malicious behaviour.

**5. Next Steps** <br>

As per my conclusion, please, block the mentioned source IP address at the Firewall level and marked this to be blacked with respective hash on all the endpoint devices which could be exploited by attacker. I Escalated this to Incident Response team for further and immediate actions.


























































