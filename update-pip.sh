sudo -H pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo -H pip3 install -U
