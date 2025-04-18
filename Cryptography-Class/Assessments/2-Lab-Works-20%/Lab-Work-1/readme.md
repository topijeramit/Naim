# 🛡️ Network Protocol Vulnerability Lab – Walkthrough

## 📌 Objective  
Simulate brute-force attacks on common network services (**FTP**, **TELNET**, **SSH**, **HTTP**), assess their security posture, capture and analyze network traffic, and recommend mitigations.

---

## 🖥️ Lab Environment

| Component     | Details                               |
|---------------|---------------------------------------|
| **Attacker VM** | Kali Linux 2024.4                     |
| **Target VM**   | Metasploitable2 / Custom Vulnerable Linux |
| **Tools Used**  | Hydra, Burp Suite, Wireshark          |

---

# 🧾 Task 1: Enumeration of Target

### 🎯 Goal  
Discover valid usernames and running services on the target system.

---

### 🔍 Step 1.1 – Perform Nmap Scan

**Command Used:**
```bash
nmap -p20,21,22,23,80 <target-ip>
```
![Screenshot 2025-04-17 214346](https://github.com/user-attachments/assets/1cd0a0a5-c008-4874-ab17-3a670d8e2cc9)

---

## 1.2 🧰 Enum4linux Enumeration

Since common ports such as **FTP (21)**, **TELNET (23)**, **SSH (22)**, and **HTTP (80)** are open on the target, we used `enum4linux` to perform enumeration and attempt to extract valid usernames and other valuable SMB-related information.

### 🔧 Command Used:
```bash
enum4linux -a <target-ip>
```
![Screenshot 2025-04-17 214452](https://github.com/user-attachments/assets/15e1e011-11cd-4606-abe0-fdfd75ec00da)
---

# 🔐 Task 2: Brute Force Attacks

## ✅ Preparation

Before initiating brute-force attacks, prepare the required wordlists:

- `userlist.txt` – A list of potential usernames
- `passlist.txt` – A list of potential passwords

### 🗂️ Wordlist Options

You can choose to:

- Use built-in wordlists provided by Kali Linux (e.g., `/usr/share/wordlists/rockyou.txt`)
- Or create simple custom wordlists for testing:

```bash
# Create a username list
echo -e "admin\nmsfadmin\nanonymous\nuser\ntest" > userlist.txt

# Create a password list
echo -e "1234\nmsfadmin\nftp123\nadmin\npassword" > passlist.txt
```

## 🔹 2.1 FTP Brute Force with Hydra

We used **Hydra** to perform a brute-force attack on the FTP service running on the target.

### 🔧 Command Used:
```bash
hydra -L userlist.txt -P passlist.txt ftp://<TARGET_IP> -V
```
![Screenshot 2025-04-17 213621](https://github.com/user-attachments/assets/a09f7343-70f4-4e46-9bfd-eb8651ab1879)
---

## 🔹 2.2 Telnet Brute Force with Hydra
Command to attack Telnet:
```bash
hydra -L userlist.txt -P passlist.txt telnet://<TARGET_IP> -V
```
![Screenshot 2025-04-17 213857](https://github.com/user-attachments/assets/45a06840-0981-4764-a5f7-b0749953d013)
---

## 🔹 2.3 SSH Brute Force with NetExec
Command to attack SSH:
```bash
nxc ssh <TARGET_IP> -u userlist.txt -p passlist.txt
```
![Screenshot 2025-04-17 214121](https://github.com/user-attachments/assets/aa80c2d9-b489-479f-a9d1-299c67f7108a)

---

## 🔹 2.4 HTTP Login Brute Force Using Burp Suite Intruder

### Step 1: Launch Burp’s Embedded Browser
- Open **Burp Suite**.
- Navigate to `Proxy > Intercept`.
- Ensure **Intercept is ON**.
- Click **Open Browser** to launch Burp’s embedded browser.

  ![Screenshot 2025-04-18 004649](https://github.com/user-attachments/assets/434ec4d1-14e1-4aec-b619-7d3880a91a40)


### Step 2: Access the Target (Metasploitable2)
- Open a Firefox browser (or use Burp's browser).
- Enter the target IP address (e.g., `http://<TARGET_IP>`).
- Navigate to the **DVWA** section.
- Login using:
  - **Username:** `admin`
  - **Password:** `password`
- In the left panel, click on **Brute Force**.
- Enter any sample values into the username and password fields (e.g., `aaa` for both), then click **Login**.
![Screenshot 2025-04-18 005800](https://github.com/user-attachments/assets/00278747-c090-4268-b837-82f50c3bb4f1)
![Screenshot 2025-04-18 005901](https://github.com/user-attachments/assets/f484dd59-6303-4784-8649-32a2694ba08d)



### Step 3: Forward the Request
- In Burp’s `Proxy > Intercept` tab, Everytime the intercept get request keep click **Forward** to send the intercepted request.
- If multiple requests are caught, continue forwarding until the page loads.
- Go to `Proxy > HTTP history` tab, and find `http://192.168.65.54/dvwa/vulnerabilities/brute/?username=aaa&password=aaa&Login=Login` then right click and choose **Send to Intruder**.

![Screenshot 2025-04-18 011547](https://github.com/user-attachments/assets/42fbdebc-4e9a-4e73-8174-7f7206d40f4d)

---

### Step 4: Disable Intercept
- Switch **Intercept is OFF** so that future browser requests are not paused.
![Screenshot 2025-04-18 011645](https://github.com/user-attachments/assets/ffb34692-3f80-49d4-98aa-dfede894f190)
---

### Step 5: Configure the Intruder Attack
- In **Intruder** tab:
  - Set **Attack Type** to **Cluster Bomb**.
  - Highlight and mark the username and password fields as **payload positions**.
  - On the **Payload position**, Load with the file in the with the **Username list** (`userlist.txt`) and **Password list** (`passlist.txt`). (`Example:/usr/share/wordlists`)

    ![Screenshot 2025-04-18 012509](https://github.com/user-attachments/assets/a02ce97c-fd4a-4911-942d-d872dfca82c2)
---

### Step 6: Launch the Attack
- Click **Start Attack**.
- Monitor the results by checking the **Response** and **Length** columns.
- Look for responses that differ in length or content.
- You can also click **Render** to view the visual output of each response.
- A successful login might return a message like:  
  **"Welcome to the password protected area admin"**
- Failed attempts usually return:  
  **"Username and/or password incorrect"**

![Screenshot 2025-04-18 013242](https://github.com/user-attachments/assets/baeea78f-9554-4245-90f4-757bb7dbf0e0)
![Screenshot 2025-04-18 013424](https://github.com/user-attachments/assets/6e000750-4cde-43a9-a6dd-8d495b61045a)
![Screenshot 2025-04-18 024126](https://github.com/user-attachments/assets/822b18c3-3da2-469f-81fc-7fef8e9474fa)

---

## 3. Sniffing and Traffic Analysis

**🎯 Goal:** Analyze how user credentials are transmitted over various network protocols using Wireshark, highlighting the difference between plaintext and encrypted traffic.

**🛠 Tool Used:** Wireshark  
**🎯 Target IP:** `192.168.188.117`

---

In this task, we capture and inspect traffic from login attempts using different protocols (FTP, Telnet, SSH) to identify whether the transmitted credentials are visible or encrypted.

## 🔹 Steps
1. Open Wireshark.
> **Command:** 
```bash
wireshark
```
  - Choose `eth0` for sniffing traffic.

![Screenshot 2025-04-18 085454](https://github.com/user-attachments/assets/bf6c38b7-90e3-4937-8bbf-7e8946b9131f)
---
2. Start capture on the network interface connected to the target for the FTP.
   - (1) FTP command:
```bash
ftp <target-ip> 
```
   - Enter the `Username = msfadmin` and `Password = msfadmin` as we got exploit from brute force attack before.

![Screenshot 2025-04-18 085400](https://github.com/user-attachments/assets/649e7e78-83d3-4fe8-a91a-6082d4afa384)
![Screenshot 2025-04-18 085342](https://github.com/user-attachments/assets/d67d6d56-e7ab-4834-aa1b-c6ab525ca947)
---

4. Apply filter on Wireshark:
```bash
ftp || tcp.port == 21
```

3. Get the FTP packet for FTP.
   - Choose the first one packet that have `FTP` and right click.
   - Go to `Follow` and click `TCP Stream`.

![Screenshot 2025-04-18 025804](https://github.com/user-attachments/assets/b5f02b2e-119f-421e-b5e7-d52bdc4ee86f)
---
![Screenshot 2025-04-18 085311](https://github.com/user-attachments/assets/5d7e3996-9b37-4c14-833d-63d807b71f05)
---
### 3.2 Capturing TELNET Credentials

1. On the attacker's terminal, connect to the TELNET service adn enter a command:

```bash
telnet 192.168.43.137
```
- Username: `msfadmin`

- Password: `msfadmin`

![image](https://github.com/user-attachments/assets/ee1ddec3-43ac-4586-b5e0-e203927bb35e)

![image](https://github.com/user-attachments/assets/f09e689c-a26d-41a7-a4d1-2ca258d93981)

2. While typing the credentials, each keystroke is transmitted and captured in plaintext.

3. In Wireshark, apply the filter:
```bash
telnet || tcp.port == 23
```

![image](https://github.com/user-attachments/assets/4725d2e9-1aff-4765-addd-7d79221f817e)

- Look through the packet list for TELNET traffic.

- Right-click → Follow → TCP Stream

![image](https://github.com/user-attachments/assets/de8e502e-9986-47eb-9935-597530f40635)

![image](https://github.com/user-attachments/assets/dae81cb3-3fed-455c-84bd-a114f212e7fe)

### 3.3 SSH Traffic

1.  **Start an SSH session** from your terminal:

    `ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa msfadmin@192.168.43.137`

    -   **Username**: `msfadmin`

    -   **Password**: `msfadmin`

    > 🛑 If you see this error:\
    > `Unable to negotiate with 192.168.43.137 port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss`\
    > Use the command above to force use of `ssh-rsa` which is supported by Metasploitable2.

![image](https://github.com/user-attachments/assets/f1ce378f-eaa1-4ae1-8f19-6d59ecbfce6d)

2.  **Open Wireshark** on your attacker machine.

3.  **Apply the filter** to display only SSH traffic:

```
ssh || tcp.port == 22
```

![image](https://github.com/user-attachments/assets/c03738f3-09db-47ee-aa80-3f0a02aa85dd)

4.  **In Wireshark**:

    -   Observe the captured SSH packets.

    -   Note that the contents are **fully encrypted**.

    -   No credentials or commands can be read in the packet data.

5.  **Optional**: Right-click on any SSH packet → `Follow` → `TCP Stream`.

    -   The stream will display **garbled** or **binary** data, confirming encryption.

![image](https://github.com/user-attachments/assets/29cabe20-b802-4330-9ad2-4ac6c7438b86)

## C. Analyze Problems Encounter

#### Issues Faced During Brute Force Attacks

- **Enumeration**: On Metasploitable 2, there were too many usernames, so it was important to carefully check valid usernames.
- **BurpSuite Bruteforce**: Had to be very careful with payload positions in Burp Intruder. A mistake in setting the payload position led to incorrect attack attempts.
- **Metasploitable2 uses an older SSH server version** that may not be compatible with newer OpenSSH clients.  
  To connect successfully, you may need to use the following command:
  
  ```bash
  ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa username@ip
  ```
  This forces the SSH client to accept the older `ssh-rsa` algorithm, which is deprecated in recent OpenSSH versions.  

* * * * *

## D. Mitigation Strategies
----------------------------

## Mitigation Strategies

| **Problem**                                    | **How to Fix It (Mitigation)**                                                                 |
|------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Brute Force Attacks**                        | Stop users from trying too many wrong passwords. Lock the account or add a delay after several failed tries. Use CAPTCHA. |
| **Plaintext Protocols (FTP, TELNET)**          | Don’t use FTP or TELNET because they send data without protection. Use **SFTP** or **SSH** instead, which are encrypted and safe. |
| **Weak Login Pages (like DVWA HTTP)**          | Use **HTTPS** so data is protected while moving on the internet. |
| **Username is Easy to Find (Enumeration)**     | Don’t show error messages that say if a username is correct or not. Use a general message like “Invalid login” for all failed logins.




