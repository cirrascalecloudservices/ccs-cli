# PREVIEW PREVIEW PREVIEW

Docs: https://github.com/cirrascalecloudservices/ccs-cli/wiki

# Install

## Mac

<pre>
brew install python3
pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall --break-system-packages
</pre>

and then add CCS_KEY to ~/.zshenv

## Linux

20.04 focal and 22.04 jammy:
<pre>
sudo apt-get install python3-pip -y
sudo pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli
</pre>

24.04 noble and later:
<pre>
sudo apt-get install python3-pip -y
sudo pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --break-system-packages
</pre>

if u don't know the ubuntu release, e.g., in a generic cloud-init script, then do this:
<pre>
sudo apt-get install python3-pip -y
sudo pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --break-system-packages || sudo pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli
</pre>

and then add CCS_KEY to /etc/environment

(in other words, try the modern way first and fallback to the classic way)

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

# Format

`ccs` emits one json object per line. pipe it through `ccsfmt` to get a table:

<pre>
ccs compute/get | ccsfmt
--------------------------------------------------------------
 name     site   type             status  addresses
--------------------------------------------------------------
 GPUAB12  san01  4u-8xgpu-4028gr  active  ['123.45.67.89/24']
 GPUC3D4  san01  4u-8xgpu-4028gr  active  ['123.45.67.90/24']
--------------------------------------------------------------
</pre>

## SSH config

`ccsfmt --ssh` formats hosts as ssh config stanzas instead of a table:

<pre>
ccs compute/get | ccsfmt --ssh
Host GPUAB12 gpuab12
  HostName 123.45.67.89

Host GPUC3D4 gpuc3d4
  HostName 123.45.67.90
</pre>

each host gets a lowercase alias, so `ssh GPUAB12` and `ssh gpuab12` both work.

write it to its own file under `~/.ssh/config.d`:

<pre>
ccs compute/get | ccsfmt --ssh > ~/.ssh/config.d/ccs
</pre>

and make sure `~/.ssh/config` includes that dir:

<pre>
Include config.d/*
</pre>

hosts with no usable address are skipped and reported on stderr, so they don't end up in the file. this includes hosts whose ip is `-`, e.g., switches, nas, and not-yet-turned-over machines

# Uninstall

<pre>
sudo pip3 uninstall ccs-cli --break-system-packages || sudo pip3 uninstall ccs-cli
</pre>
