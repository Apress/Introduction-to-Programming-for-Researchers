# final pipelines

zcat datafile/hygdata_v41.zip | tail -n +2 | sed -e 's/""//g' | gawk -F',' '$7{print}' |  egrep Ori | gawk -F',' '{ if ($14 < 2.5) print $7}'

zcat datafile/hygdata_v41.zip | tail -n +2 | sed -e 's/""//g' | gawk -F',' '$7{printf("%5s\t%s %s\t%s\n", $14, $28, $30, $7)}' |  egrep Ori | sort -n
