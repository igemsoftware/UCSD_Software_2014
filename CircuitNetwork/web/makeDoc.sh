for pythonFile in $1/*py
do
	module=$(basename $pythonFile)
	module=${module%.py}
	echo "pydoc $module > $1/doc/$module.html"
	pydoc $module > $1/doc/$module.html
done
