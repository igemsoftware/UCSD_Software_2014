for image in $1/*png
do
	echo $image
	newName=$(basename $image)
	newName=${newName##sbol_operon}
	newName="operon_sbol$newName"
	mv $image $1/$newName
done
