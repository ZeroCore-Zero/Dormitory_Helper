<template>
    <el-container>

        <el-header>
            <div>
                <img src="../../photo/logo.png" width="56" height="56">
                <!-- 这里是校徽图片，网页中的header的width为56.6 -->
                <span>电商后台管理系统</span>
            </div>
        </el-header>

        <el-main>
            <el-tabs tab-position="left" model-value="name1">
                <el-tab-pane label="AA统计" name="name1">
                    <Bill />
                </el-tab-pane>
                <el-tab-pane label="电费监测" name="name2">正在开发</el-tab-pane>
            </el-tabs>
        </el-main>

    </el-container>
</template>

<script setup>
    import {ElTabs, ElTabPane, ElContainer, ElHeader, ElMain} from 'element-plus';
    import Bill from '../components/Bill.vue';
</script>

<style>
.el-tab-pane {
    word-break: break-all;
    word-wrap: break-word;
}

/* 以下均为对于导航栏的修饰，使用了div的嵌套 */
.el-header{
background-color: #c8e8f5;
display: flex;
color: #1860e6;
font-size: 25px;
padding-left: 0;

div{
display: flex;
align-items: center;
span
{
  margin-left: 15px;
}
}

}

</style>