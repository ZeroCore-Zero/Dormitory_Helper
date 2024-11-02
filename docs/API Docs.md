# API Docs

API list for this project.

## Overview

For all api requests, their root path are `http://dormitory.lingzc.com/api`

For all response body, their structure are as below:

```json
	{
		"code": 100000,
		"msg": "This is a message.",
		"data": {
			"key": "value",
			"hint": "datas put here"
		}
	}
```

- `code` field indicates the status of response, for more details, see [Code List](./code.md)
- `msg` field is a short description for this code
- `data` field is the data need to pass

> ![NOTE]
> Below documents will not introduce `code` and `msg` fields, their content are the content in `data` field directly.

## Interfaces

### /login

#### request

1. `login_opt`: Login option, select one from 'default' and 'bupt_net_login', which decide what the next `username` parameter means.
2. `username`: For different `login_opt`, this parameter represent different means as below:
	- default: email address bind to user account
	- bupt_net_login: BUPTID of user
3. `password`: Password of user

#### response

1. `success`: Whether login is success. If false, please retry, otherwise a `login` will be set by server in cookies for identification.