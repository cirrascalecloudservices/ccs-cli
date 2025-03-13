# PREVIEW PREVIEW PREVIEW

Docs: https://github.com/cirrascalecloudservices/ccs-cli/wiki

# Install

## Mac

<pre>
brew install python3
pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY to ~/.zshenv

## Linux

<pre>
sudo apt-get install python3-pip -y
sudo pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY to /etc/environment

Note- for ubuntu 24.04+ may need to use --break-system-packages

Note- when editing /etc/environment, need to close and reopen terminal for changes to take effect

## Windows

1. Install git from https://git-scm.com/download/win
2. Install python
   1. [recommended] if installing python from https://www.python.org/downloads then be sure to check "Add python to path"
   1. [less recommended] if installing python from windows app store then be sure to add pip path to windows path using "advanced system settings" -> "environment variables"

<pre>
pip install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
</pre>

and then add CCS_KEY using "advanced system settings" -> "environment variables"
