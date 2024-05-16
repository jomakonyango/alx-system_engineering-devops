UFW ussermanual
First, connect to your web-01 server via SSH. You can do this with the following command (replace ubuntu with your username and 52.91.126.247 with your server’s IP address):
ssh ubuntu@52.91.126.247

Once you’re connected to your server, you can install UFW with these commands:
sudo apt update
sudo apt install ufw

Deny all incoming traffic by default:
sudo ufw default deny incoming

Allow outgoing traffic by default:
sudo ufw default allow outgoing

Allow incoming traffic on the ports you specified (SSH, HTTPS, HTTP):
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp

Enable UFW:
sudo ufw enable

You can check the status of UFW and see the rules that are currently in effect at any time with this command:
sudo ufw status verbose
