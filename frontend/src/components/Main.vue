<script setup>
import {ElButton} from "element-plus";
</script>

<template>
  <div style="display: inline-block;width: 800px;height: 150px">
    <el-button type="primary" style="margin-left: 50px" class="component_of_Main">
      <RouterLink to="/create">创建账单</RouterLink>
    </el-button>
    <el-button type="warning" style="margin-left: 50px" class="component_of_Main">
      <RouterLink to="/check">审计账单</RouterLink>
    </el-button>
    <el-button type="success" style="margin-left: 50px" class="component_of_Main">
      <RouterLink to="/clear">分摊账单</RouterLink>
    </el-button>
  </div>
  <br>
  <RouterView style="margin-right: 50px"/>
</template>

<style scoped>
.component_of_Main {
  margin: 50px 50px 50px 100px;
  width: 150px;
  height: 50px;
}
</style>