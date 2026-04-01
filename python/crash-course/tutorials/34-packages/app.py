# Method 1
import ecommerce.shipping                           # SYNTAX: import package.module
ecommerce.shipping.calc_shipping()

# Method 2
from ecommerce.shipping import calc_shipping        # SYNTAX: from package.module import function
calc_shipping()

# Method 3
from ecommerce import shipping                      # SYNTAX: from package import module
shipping.calc_shipping()