#!/bin/bash
#URL FOR file signatures https://www.garykessler.net/library/file_sigs.html

#Repeatedly decompresses or decodes the output of its previous version 500 times
# to get the flag

FNAME=flag
TRUE=1
C=0
ZERO="000"

while [[ $TRUE -lt 502 ]]; do
	if [[ $C -lt 10 ]]; then
		ZERO="000"
	elif [[ $C -lt 100 ]]; then
		ZERO="00"
	elif [[ $C -lt 1000 ]]; then
		ZERO="0"
	else
		ZERO=""
	fi

	##Grab filesignature
	FHEAD=$(hd "$FNAME" | head -n1 | awk -F" " '{print $2$3$4}')

	echo -n "$FHEAD		$FNAME		"

	if [[ $FHEAD == "1f8b08" ]]; then
		#GZ
		gzip --decompress "$FNAME" --stdout > "flag_$ZERO$C"
		echo "gzip"
	elif [[ $FHEAD == "425a68" ]]; then
		#BZ2
		bzip2 --decompress "$FNAME" --stdout > "flag_$ZERO$C"
		echo "bz2"
	elif [[ $FHEAD == "504b03" ]]; then
		#ZIP 
		gunzip -c "$FNAME" > "flag_$ZERO$C"
		echo "ZIP"
	else
		#base64
		cat "$FNAME" | base64 --decode > "flag_$ZERO$C"
		echo "b64"
	fi
	
	FNAME="flag_$ZERO$C"
	
	((C=$C+1))
	((TRUE=$TRUE+1))
done

