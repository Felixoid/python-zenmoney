## Python library for ZenMoney API
This library allows you to use [ZenMoney API](https://github.com/zenmoney/ZenPlugins/wiki/ZenMoney-API).

There is a simplest way to start:

```python
from zenmoney import *

oauth = OAuth2('consumer_key', 'consumer_secret', 'user_name', 'user_pass')
api = Request(oauth.token)
diff = api.diff(Diff(**{'serverTimestamp': 1}))
```
