# Code List

This is a list contains all of the value of `code` field in response.

## Overview

A simple method to distinguish the status is the code structure.

|Code Structure|Explanation|
|---|---|
|`1xyyzz`|Client need to do some changes and resend the request|
|`2xyyzz`|Success operation|
|`3xyyzz`|*Not Define*|
|`4xyyzz`|Operation is not allowed|
|`5xyyzz`|Server error|

## Detail

### 200000

> msg: `success`

Generic code, no any other information.

### 400000

> msg: `not login`

User not login, or cookie is expire.