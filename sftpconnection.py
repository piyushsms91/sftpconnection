import os
import paramiko
myHostname = "server.ssh.prod.acquia-sites.com"
myUsername = "server.dev"
myPassword = "server@123"
localpath = "/Users/piyush/Documents/piyush_project/digipy/sftpcommand/test.txt"
remotepath = "/mnt/gfs/server/manualbackups/test.txt"

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect('server.ssh.prod.acquia-sites.com', username=myUsername, password=myPassword)
sftp = ssh.open_sftp()
print ("Connection succesfully stablished ... ")
sftp.put(localpath, remotepath,callback=None, confirm=True)
sftp.close()
ssh.close()
