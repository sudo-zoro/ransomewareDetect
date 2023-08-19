# Encrypt Ransomeware

The project is based on detection of encryption ransomware. Using the python and its GUI packages.

## :cookie: Requirments 
- Python3
- PyQt5

***Open Source tool***
- yara 


## :orange_book: Application Functionality 
**MONITOR**

``The path to the directory is set and monitor button initiates the detection module and all the activity will be shown in File operations and Detection modules.``

**DELETE**

``Once the malicious file is detected in the directory, seting the path of that file and with the press of delete button the malicious file will be deleted``


## :art: Output
**Attack Simulation**

![01](https://github.com/sudo-zoro/ransomewareDetect/assets/85948202/6362f6d4-3c75-4bd9-b532-9fd165b3f890)

***Here the malicious code is executed and can be seen the content inside the files are all encrypted in the output of cat command***

![02](https://github.com/sudo-zoro/ransomewareDetect/assets/85948202/b1fa7372-57ea-4eba-afbe-2fd76fdc5efb)

***Just show casing the with proper key the decryption of all the files***


**Detection**

![03](https://github.com/sudo-zoro/ransomewareDetect/assets/85948202/a9831dce-c829-4da8-becc-a97ef1ccdf93)

![04](https://github.com/sudo-zoro/ransomewareDetect/assets/85948202/59c54cb6-0033-4c63-aa07-9bc7f8f84d77)

![05](https://github.com/sudo-zoro/ransomewareDetect/assets/85948202/3ecdf494-2de2-4c43-a37f-6fbb45d9e222)

***The above output shows the detection of the ransomware file and its path with the possible key it is using to encrypt the files***

**Project can be imporved by adding more possible rules to yara and regexp match to find the key**




