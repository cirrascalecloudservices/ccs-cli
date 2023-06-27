# ccs-cli
cirrascale command line interface

# Mac

<pre>
brew install python3
pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY to ~/.zshenv

# Linux

<pre>
sudo apt install python3-pip
sudo pip install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY to /etc/environment

# Windows

1. Install git from https://git-scm.com/download/win
2. Install python
   1. if installing python from windows app store then be sure to add pip path to windows path using "advanced system settings".
   1. if installing python from https://www.python.org/downloads then be sure to check "Add python to path".

<pre>
pip install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY using "advanced system settings" -> "environment variables"
