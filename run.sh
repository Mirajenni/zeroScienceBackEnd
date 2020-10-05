local_dir="$(dirname $0)"
run=$local_dir/flaskProject/main.py
PYTHON_PATH=$local_dir/ FLASK_APP=$run $local_dir/venv/bin/python $run
