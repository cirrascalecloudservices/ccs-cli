# PREVIEW PREVIEW PREVIEW

Docs: https://github.com/cirrascalecloudservices/ccs-cli/wiki

# Install

## uv (any platform)

If u have [uv](https://docs.astral.sh/uv/), this works the same on mac, linux and windows, and
avoids the `--break-system-packages` stuff needed on newer ubuntu:

<pre>
uv tool install git+https://github.com/cirrascalecloudservices/ccs-cli --force
</pre>

and then add CCS_KEY to the environment as described in the per-platform sections below.

To upgrade or uninstall later:
<pre>
uv tool upgrade ccs-cli
uv tool uninstall ccs-cli
</pre>

If u don't have uv yet:
<pre>
curl -LsSf https://astral.sh/uv/install.sh | sh          # mac/linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # windows
</pre>

## No install at all (uv)

ccs.py declares its own dependencies inline, so uv can run it without installing anything.
Useful in cloud-init and other throwaway environments:

<pre>
curl -LsSf https://raw.githubusercontent.com/cirrascalecloudservices/ccs-cli/main/ccs.py -o ccs.py
uv run ./ccs.py compute/get
</pre>

uv fetches requests and tabulate into a cache on first run.

## Mac

<pre>
brew install python3
pip3 install git+https://github.com/cirrascalecloudservices/ccs-cli --force-reinstall
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

# Uninstall

if installed with uv:
<pre>
uv tool uninstall ccs-cli
</pre>

20.04 focal and 22.04 jammy:
<pre>
sudo pip3 uninstall ccs-cli
</pre>

24.04 noble and later:
<pre>
sudo pip3 uninstall ccs-cli --break-system-packages
</pre>

unknown, e.g., cloud-init:
<pre>
sudo pip3 uninstall ccs-cli --break-system-packages || sudo pip3 uninstall ccs-cli
</pre>
