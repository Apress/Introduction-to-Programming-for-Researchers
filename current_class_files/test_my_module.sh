echo ""
echo "testing is_nucl_str_clean()"
echo "1 garbage filter test."
echo "1 good input test."
python unittest_is_nucl_str_clean.py

echo ""
echo "testing euclid_gcd()"
echo "1 garbage filter test"
echo "1 good input test"
python unittest_euclid_gcd.py

echo ""
echo "testing per_gc_content()"
echo "2 garbage filter tests."
echo "1 good input test."
python unittest_per_gc_content.py


