path=$(pwd)

bin_path=${path}/bin
django_path=${path}/www
sudo ln -s /usr/lib/*/libjpeg.so /usr/lib
sudo ln -s /usr/lib/*/libz.so /usr/lib
sudo ln -s /usr/lib/*/libfreetype.so /usr/lib

if [ -d $bin_path/$a ]; then

echo "A virtualenv is present"
${bin_path}/pip install -r ${path}/requirement-dev.txt

else

virtualenv --no-site-packages --python=python2.6 --distribute ${path}/
${bin_path}/pip install -r ${path}/requirement-dev.txt

fi
