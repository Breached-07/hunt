# Hunt - IP to ISP Tracing Tool
         
         Hunt is a Python-based command-line tool that resolves the Internet Service Provider (ISP) associated with a given IP address.
## Requirements:
- Python 3.x
- ipwhois library (Install it via pip)
## Installation
          git clone https://github.com/Breached-07/hunt.git

## Downloading ip whois
           pip install pipwhois
            
## Post-Download Setup:
           After downloading the script,open terminal and follow these steps to set it up as a command-line tool:

## Rename the file:
   
         
         mv hunt.py hunt
         
## Make it executable:
         
          chmod +x hunt
         
## Move it to a directory in your system (to run it globally):
         
          sudo mv hunt /usr/local/bin
## Running the script: 
         
          hunt <IP_ADDRESS>  
## Check help page          
         hunt --help
## NOTE : 
If there is a issue is related to the line-ending characters (in UNIX SYSTEMS)
Run the following command: 
     
                          dos2unix hunt.py
             
          
          
                   
          
 
          
          
           
