workd=/media/user1/3f01b061-6b30-485c-8565-c41ef5a79485/8tb/trek2/trek2brohawn-alignment/new-trek2brohawn-mutatetrek1/trek2down/compel/prod/hlrndone
scripts=/media/user1/3f01b061-6b30-485c-8565-c41ef5a79485/8tb/homeofficeall/ramascripts
ion=( 2e 4e )

for name in ${ion[@]}
do
	for i in {1..5}
	do
		cd $workd/$name/$i
		mkdir rama
		cd rama
		cp $scripts/* .
		bash ramaall.sh
	done
done
