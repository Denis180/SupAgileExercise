path=$(pwd)

bin_path=${path}/bin
django_path=${path}/www

if [ -d $bin_path/$a ]; then

echo "A virtualenv is present"

else

virtualenv --no-site-packages --python=python2.6 --distribute ${path}/
${bin_path}/pip install -r ${path}/requirement-dev.txt

fi
