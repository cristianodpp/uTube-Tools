import sys
import core
import prepare

print(60*"-")
print ('Welcome to uTube Manager Tool')
print(60*"-")

# Hide errors
sys.tracebacklimit = 0

# Prepare Sys
prepare.prepareClass().main()

# Call menu
core.coreClass().main()
