<template>
  <el-icon>
    <UserFilled style="width: 30px;height: 30px"/>
  </el-icon>
  <el-button type="primary" @click="inHome">
    <!-- <RouterLink to="/main"> -->
      点击进入主页
    <!-- </RouterLink> -->
  </el-button>
  <br>
  <RouterView/>
</template>

<script lang="ts" setup>
import {ElButton} from 'element-plus';
import {UserFilled} from "@element-plus/icons-vue";
import {useRouter} from "vue-router";

const router = useRouter();
const inHome = () => {
  router.push("/main");
}

</script>
