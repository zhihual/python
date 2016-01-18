# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

import pandas
link = 'http://aws.amazon.com/ec2/pricing/' 
data = pandas.read_html(link)
print type(data)
print data[0]