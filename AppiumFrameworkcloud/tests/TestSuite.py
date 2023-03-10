# 1. Import the files
import  unittest
from AppiumFrameworkcloud.tests.LoginTest import LoginTest
from AppiumFrameworkcloud.tests.ContactUsFormTest import ContactforTest



# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactforTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,gt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

