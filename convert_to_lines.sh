DIR=$1
LINEDIR=line_svgs
NEWDIR=$LINEDIR/$(basename $1)
echo $DIR
mkdir -p $NEWDIR
cp html_header.txt $NEWDIR.html
for f in `ls $DIR/`;
do
  python svgsimplify.py $DIR/$f $NEWDIR/$f
  echo "<img src='$NEWDIR/$f' />" >> $NEWDIR.html
done
