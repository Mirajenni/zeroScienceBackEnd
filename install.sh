local_dir="$(dirname $0)"
virtualenv -p python3.6 $local_dir/venv
$local_dir/venv/bin/pip install -r $local_dir/requirements.txt
