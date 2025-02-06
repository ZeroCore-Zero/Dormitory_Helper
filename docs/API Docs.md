# API Docs

API list for this project.

## Overview

For all api requests, their root path are `http://dormitory.lingzc.com/api`

For all success response body (return 200), their structure are as below:

```json
{
	"key": "value",
	"hint": "datas put here"
}
```
For all fail response body, (return 4xx), the response body is empty or as below:

```json
{
	"code": 123456,
	"msg": "message",
	"data": {}
}
```

## Interfaces

Please use [Apifox](https://dormitory-helper.apifox.cn).
