sudo -H pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo -H pip3 install -U
sudo -H pip2 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo -H pip2 install -U
