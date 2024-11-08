<template>
  <el-icon>
    <UserFilled style="width: 30px;height: 30px"/>
  </el-icon>
  <el-button type="success" style="width: 120px;height: 40px">
    <RouterLink to="/main">
      点击进入主页
    </RouterLink>
  </el-button>
  <br>
  <RouterView/>
</template>

<script lang="ts" setup>
import {ElButton} from 'element-plus';
import {UserFilled} from "@element-plus/icons-vue";
</script>
<!--<style>-->

<!--.el-table .warning-row {-->
<!--  &#45;&#45;el-table-tr-bg-color: var(&#45;&#45;el-color-warning-light-9);-->
<!--}-->

<!--.el-table .success-row {-->
<!--  &#45;&#45;el-table-tr-bg-color: var(&#45;&#45;el-color-success-light-9);-->
<!--}-->

<!--</style>-->