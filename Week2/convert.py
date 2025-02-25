#Converting meters to miles,feet and inches.

METERS_TO_MILES = 1609.34
METERS_TO_FEET = 0.3048
METERS_TO_INCHES = 0.0254

meter = float(input("Enter any length meters that u want to Convert:"))

miles = meter/METERS_TO_MILES
feet = meter/METERS_TO_FEET
inches = meter/METERS_TO_INCHES

print("")
print(meter,"meters is %.2f miles." % miles)
print(meter,"meters is %.2f miles." % feet)
print(meter,"meters is %.2f miles." % inches)

